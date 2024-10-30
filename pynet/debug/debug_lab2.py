#!/usr/bin/env python3

# Construct commands with load pack syntax from the WAP
def load_pack_format(protocol_list, ftp_filenames, ip_addr, username, password, port):

    telnet_commands = list()

    for protocol in protocol_list:
        for filename in ftp_filenames:
                            ## load pack by {https|sftp|ftp|tftp|http} svrip {ip addr} remotefile {file name} [user {user name}] [pwd {password}] [port {port}]
            command = f"load pack by {protocol} svrip {ip_addr} remotefile {filename} user {username} pwd {password} port {port} \r\n"
            command = command.encode('ascii')
            telnet_commands.append(command)

    return telnet_commands

# The lists begins with file names served in the ftpserver
## WAP Syntax:
protocol_list = ['ftp', 'tftp', 'sftp']
ftp_filenames = ['test1']
commands_seq7 = load_pack_format(protocol_list, ftp_filenames, "10.39.84.117", "ftpserver", "52a7cZdX", 23)


for command in commands_seq7:
    print(command)


def ls(wap_path, format=1):
    
    ls_command = "wap list format " + str(format) + " path "+ wap_path + "\r\n"
    ls_command = ls_command.encode('ascii')
    print(ls_command)

ls("/")
