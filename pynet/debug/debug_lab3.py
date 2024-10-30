#!/usr/bin/env python3

# This method returns a list with the su commands available on the WAP
def su_help_commands():
    su_commands_path = "/home/grimaldi/Bash/Telnet/commands/su_commands.md"

    su_list = [b'su\r\n']
    with open(su_commands_path, 'r') as file:
        next(file)  # Skip first line
        for command in file:
            command = command.strip().encode('ascii') + b'\r\n'
            su_list.append(command)
    return su_list

# Loop the list
#su_list = su_help_commands()
#for command in su_list:
#    print(command)


# Method for getting all the commands using 'display'
def display_commands():
    display_path = "/home/grimaldi/Bash/Telnet/commands/display_direct.md"

    display_list = [b'su\r\n']
    with open(display_path, 'r') as file:
        next(file)  # Skip first line
        for command in file:
            command = command.strip().encode('ascii') + b'\r\n'
            display_list.append(command)
    return display_list


display_list = display_commands()
for command in display_list:
    print(command)
   



