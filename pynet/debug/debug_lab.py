#!/usr/bin/env python3

import sys
import time
from itertools import cycle


def debug_1():
    print("Write a buffer to represent in bytes. Press Ctrl+D for EOF:")
    command = sys.stdin.read().strip()
    print("\n-----------------------------------------------------------------")

    #command = bytes(command, 'latin1').decode('unicode_escape').encode('latin1')

    command1 = bytes(command, 'latin')
    print(f"\n\n[!] Command1:\t{command1}\n\n[*] Type:\t{type(command1)}")
    print("-----------------------------------------------------------------")

    command2 = bytes(command, 'latin').decode('unicode_escape')
    print(f"\n\n[!] Command2:\t{command2}\n\n[*] Type:\t{type(command2)}")
    print("-----------------------------------------------------------------")

    command3 = bytes(command, 'latin').decode('unicode_escape').encode('latin')
    print(f"\n\n[!] Command2:\t{command2}\n\n[*] Type:\t{type(command2)}")
    print("-----------------------------------------------------------------")

    command4 = bytes(command, 'ascii')
    print(f"\n\n[!] Command2:\t{command2}\n\n[*] Type:\t{type(command2)}")
    print("-----------------------------------------------------------------")


def debug_2():
    print("Write a buffer to represent in bytes. Press Ctrl+D for EOF:")
    command_original = sys.stdin.read().strip()
    print()
    print("\n-----------------------------------------------------------------")

    cont = 0
    while True:
        command = command_original
        #encoder = input("Select an encoder ('ascii', 'latin'): ").strip()

        #command = bytes(command, encoder)

        # Remove the \x notation
        command = command.replace('\\x', '')

        # Convert to bytes
        command = bytes.fromhex(command)

        #command = string_to_hex(command)
        #command = bytes(command)


        print(f"\n[!] Command [{cont}]:   {command}")
        print(f"\n[*] Type:   [{cont}]:   {type(command)}")
        print("-----------------------------------------------------------------")

        cont += 1


def debug_3():
    print("Write a buffer to represent in bytes. Press Ctrl+D for EOF:")
    command = sys.stdin.read().strip()
    print("\n-----------------------------------------------------------------")

    #original_bytes = "\xff\xfd\x01ls"
    original_bytes = command

    # Separate the fixed part and the string part
    fixed_part = original_bytes[:12]
    string_part = original_bytes[12:]

    print(f"{fixed_part}    \nType: {type(fixed_part)}")
    print(f"{string_part}   \nType: {type(string_part)}")
    print()
    print("\n-----------------------------------------------------------------")

    # Transform fixed part to bytes
    fixed_part = hex_to_bytes(fixed_part)

    # Encode the string part to bytes
    string_part = string_to_hex(string_part)
    string_part = hex_to_bytes(string_part)

    print(f"{fixed_part}    \nType: {type(fixed_part)}")
    print(f"{string_part}   \nType: {type(string_part)}")
    print()
    print("\n-----------------------------------------------------------------")


    # Concatenate the fixed part with the encoded string part
    result = fixed_part + string_part

    print(result)  # Output: b'\xff\xfd\x01\x6c\x73'


# Returns a list with commands from a file 
def list_help_commands():
    
    # Include hardcoded path for the commands
    commands_path = "/home/grimaldi/Bash/Telnet/commands/commands.md"

    # A list to store available commands
    available_commands = list()

    with open(commands_path, 'r') as commands_file:
        for command in commands_file:
            #print(command)
            command = command[:-1]
            available_commands.append(command)

    return available_commands

# Defines a global list
available_commands = list_help_commands()
del available_commands[0]
command_iterator = cycle(available_commands)


def debug_4():

    #command = available_commands.pop()
    command = next(command_iterator)

    try:
        
        # Convert the command string with escaped characters to bytes
        command_bytes = bytes(command, 'latin1').decode('unicode_escape').encode('latin1')
        
        # Append the necessary newline characters for Telnet
        buffer = command_bytes + b' ? \r\n'
        print(f"[==>] Sending this buffer instead:\n{buffer}\n")
        return buffer

    except Exception as e:
        print(f"Error: \n{e}")
        return buffer

def hex_to_bytes(command):
    # Remove the \x notation
    command = command.replace('\\x', '')
    # Convert to bytes
    command = bytes.fromhex(command)
    return command

#def ascii_to_hex(command):



def string_to_hex(data):
        
    # Convert each character to its ASCII hexadecimal representation
    hex_output = '\\x'
    hex_output += '\\x'.join(format(ord(char), '02x') for char in data)
    
    # Print the hexadecimal representation
    #print(f"[~] Hexadecimal representation:\t'{hex_output}'")

    return hex_output


if __name__ == "__main__":
    # Redirect flow to debuging scenario 1
    #debug_1()
    #debug_2()
    #debug_3()
    while True:
        debug_4()
        time.sleep(1)
