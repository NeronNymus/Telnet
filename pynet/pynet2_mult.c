#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <time.h>

#define MAX_LINE_LENGTH 1024
#define MAX_SPLITS 10000

char *splitted_files[MAX_SPLITS];
int split_count = 0;
pid_t child_pids[MAX_SPLITS];
int child_count = 0;

// Function to handle SIGINT (Ctrl+C)
void handle_sigint(int sig) {
    printf("\n[!] Caught SIGINT. Terminating child processes...\n");
    for (int i = 0; i < child_count; i++) {
        kill(child_pids[i], SIGTERM);
    }
    exit(1);
}

// Function to split the input file into multiple files
void split_file(const char *input_path, int number) {
    FILE *file = fopen(input_path, "r");
    if (!file) {
        perror("fopen");
        exit(1);
    }

    char **ip_addresses = NULL;
    int total_lines = 0;
    char line[MAX_LINE_LENGTH];

    while (fgets(line, sizeof(line), file)) {
        ip_addresses = realloc(ip_addresses, sizeof(char*) * (total_lines + 1));
        ip_addresses[total_lines] = strdup(line);
        total_lines++;
    }
    fclose(file);

    // Seed random generator
    srand(time(NULL));

    // Fisher-Yates shuffle
    for (int i = total_lines - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        char *temp = ip_addresses[i];
        ip_addresses[i] = ip_addresses[j];
        ip_addresses[j] = temp;
    }

    int chunk_size = total_lines / number;
    int remainder = total_lines % number;
    int index = 0;

    for (int i = 0; i < number; i++) {
        int current_chunk_size = chunk_size + (i < remainder ? 1 : 0);
        char *out_path = malloc(strlen(input_path) + 15);
        sprintf(out_path, "%s.%d", input_path, i + 1);
        FILE *out_file = fopen(out_path, "w");
        if (!out_file) {
            perror("fopen");
            exit(1);
        }
        for (int j = 0; j < current_chunk_size; j++) {
            fputs(ip_addresses[index], out_file);
            free(ip_addresses[index]);
            index++;
        }
        fclose(out_file);
        splitted_files[split_count++] = out_path;
        printf("[!] Splitted: %s     %d\n", out_path, current_chunk_size);
    }
    free(ip_addresses);
}

// Function to call pynet2.py with appropriate arguments
void call_pynet(const char *ip_file, const char *port, const char *commands_list, const char *g_value, const char *d_value) {
    pid_t pid = fork();
    if (pid == 0) {
        // Child process

        // Print the command to be executed
        printf("Executing: run_pynet2.sh -iL %s -p %s -l -iC %s -g %s -d %s\n", ip_file, port, commands_list, g_value, d_value);
        fflush(stdout);

        // Redirect stdout and stderr to /dev/null
        int devnull = open("/dev/null", O_WRONLY);
        if (devnull != -1) {
            dup2(devnull, STDOUT_FILENO);
            dup2(devnull, STDERR_FILENO);
            close(devnull);
        }

        execlp("/media/Kali/home/grimaldi/Bash/Telnet/pynet/run_pynet2.sh",
               "run_pynet2.sh", "-iL", ip_file, "-p", port, "-l", "-iC", commands_list, "-g", g_value, "-d", d_value,
               (char *)NULL);

        // Only reached if execlp fails
        perror("execlp");
        exit(1);
    } else if (pid > 0) {
        // Parent process
        child_pids[child_count++] = pid;
    } else {
        // Fork failed
        perror("fork");
        exit(1);
    }
}

int main(int argc, char *argv[]) {
    if (argc < 13) {
        fprintf(stderr, "Usage: %s -iL <ip_list> -iC <commands_list> -n <processes> -g <group_size> -d <depth> [-p <port>]\n", argv[0]);
        exit(1);
    }

    char *ip_list = NULL;
    char *commands_list = NULL;
    char *processes = NULL;
    char *port = "23"; // Default port
    char *g_value = NULL;
    char *d_value = NULL;

    // Parse command-line arguments
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-iL") == 0 && i + 1 < argc) {
            ip_list = argv[++i];
        } else if (strcmp(argv[i], "-iC") == 0 && i + 1 < argc) {
            commands_list = argv[++i];
        } else if (strcmp(argv[i], "-n") == 0 && i + 1 < argc) {
            processes = argv[++i];
        } else if (strcmp(argv[i], "-g") == 0 && i + 1 < argc) {
            g_value = argv[++i];
        } else if (strcmp(argv[i], "-d") == 0 && i + 1 < argc) {
            d_value = argv[++i];
        } else if (strcmp(argv[i], "-p") == 0 && i + 1 < argc) {
            port = argv[++i];
        }
    }

    if (!ip_list || !commands_list || !processes || !g_value || !d_value) {
        fprintf(stderr, "Missing required arguments.\n");
        exit(1);
    }

    int num_processes = atoi(processes);
    if (num_processes <= 0 || num_processes > MAX_SPLITS) {
        fprintf(stderr, "Invalid number of processes. Must be between 1 and %d.\n", MAX_SPLITS);
        exit(1);
    }

    // Register SIGINT handler
    signal(SIGINT, handle_sigint);

    // Split the input file
    split_file(ip_list, num_processes);

    // Fork child processes to call pynet2.py
    for (int i = 0; i < split_count; i++) {
        call_pynet(splitted_files[i], port, commands_list, g_value, d_value);
    }

    // Wait for all child processes to finish
    for (int i = 0; i < child_count; i++) {
        waitpid(child_pids[i], NULL, 0);
    }

    // Free allocated memory
    for (int i = 0; i < split_count; i++) {
        free(splitted_files[i]);
    }

    return 0;
}
