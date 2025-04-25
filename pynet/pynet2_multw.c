#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <time.h>

#define MAX_LINE_LENGTH 1024
#define MAX_SPLITS 10000

char *splitted_files[MAX_SPLITS];
PROCESS_INFORMATION processes[MAX_SPLITS];
int split_count = 0;
int child_count = 0;

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
        ip_addresses[total_lines] = _strdup(line);
        total_lines++;
    }
    fclose(file);

    srand((unsigned int)time(NULL));

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

void call_pynet(const char *python_script_path, const char *ip_file, const char *port, const char *commands_list) {
    char cmd[1024];
    snprintf(cmd, sizeof(cmd),
             "python \"%s\" -iL \"%s\" -p \"%s\" -l -iC \"%s\"",
             python_script_path, ip_file, port, commands_list);

    STARTUPINFOA si = {0};
    PROCESS_INFORMATION pi = {0};
    si.cb = sizeof(si);

    if (!CreateProcessA(
            NULL, cmd, NULL, NULL, FALSE,
            CREATE_NEW_CONSOLE, NULL, NULL, &si, &pi)) {
        fprintf(stderr, "Failed to start process: %s\n", cmd);
        return;
    }

    processes[child_count++] = pi;
}

int main(int argc, char *argv[]) {
    if (argc < 8) {
        fprintf(stderr, "Usage: %s <pynet2.py> -iL <ip_list> -iC <commands_list> -n <processes> [-p <port>]\n", argv[0]);
        return 1;
    }

    char *pynet2_path = argv[1];
    char *ip_list = NULL;
    char *commands_list = NULL;
    char *processes_arg = NULL;
    char *port = "23";

    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "-iL") == 0) ip_list = argv[++i];
        else if (strcmp(argv[i], "-iC") == 0) commands_list = argv[++i];
        else if (strcmp(argv[i], "-n") == 0) processes_arg = argv[++i];
        else if (strcmp(argv[i], "-p") == 0) port = argv[++i];
    }

    if (!ip_list || !commands_list || !processes_arg) {
        fprintf(stderr, "Missing required arguments.\n");
        return 1;
    }

    int num_processes = atoi(processes_arg);
    if (num_processes <= 0 || num_processes > MAX_SPLITS) {
        fprintf(stderr, "Invalid number of processes.\n");
        return 1;
    }

    split_file(ip_list, num_processes);

    for (int i = 0; i < split_count; i++) {
        call_pynet(pynet2_path, splitted_files[i], port, commands_list);
    }

    for (int i = 0; i < child_count; i++) {
        WaitForSingleObject(processes[i].hProcess, INFINITE);
        CloseHandle(processes[i].hProcess);
        CloseHandle(processes[i].hThread);
    }

    for (int i = 0; i < split_count; i++) {
        free(splitted_files[i]);
    }

    return 0;
}
