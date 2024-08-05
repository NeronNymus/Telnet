#!/usr/bin/env python3

import sys

# Creating the dictionary with byte representations
byte_dict = {i: bytes([i]) for i in range(256)}

# Printing all the byte number representations of ASCII characters
for i in range(256):
    character = byte_dict[i]
    
    char_display = repr(character)
    #print(f"[{i}]\t{char_display}")

#eof = b'\x04'
#int_eof = eof[0]
#print(int_eof)

def hex_to_decimal():
    print("[!] Press Enter to exit")
    while True:
        # Prompt the user for input
        byte_str = input("\n[!] Write the byte representation (in hex, e.g., ff): ")

        if byte_str == "exit":
            return
        
        # Break the loop if the input is empty
        if not byte_str:
            print("[ ] Exiting...")
            break

        try:
            # Ensure the input string is valid hex
            if len(byte_str) != 2 or not all(c in '0123456789abcdefABCDEF' for c in byte_str):
                raise ValueError("[x] Invalid byte representation. It should be exactly two hex digits.")
            
            # Convert the hex string to a byte object
            byte_obj = bytes.fromhex(byte_str)
            
            # Convert the byte object to its decimal representation
            decimal_value = int.from_bytes(byte_obj, byteorder='big')
            
            # Print the result
            print(f"[~] {byte_obj} = {decimal_value}")

        except ValueError as e:
            # Handle invalid input
            print(e)


def decimal_to_hex():
    while True:
        # Prompt the user for input
        decimal_str = input("\n[!] Write the decimal value (0-255) or press Enter to exit: ")

        try:
            # Ensure the input string is a valid decimal number
            decimal_value = int(decimal_str)
            if decimal_value < 0 or decimal_value > 255:
                raise ValueError("Invalid decimal value. It should be in the range 0-255.")
            
            # Get the byte representation from the dictionary
            byte_obj = byte_dict[decimal_value]
            
            # Convert the byte object to its hexadecimal representation
            #hex_value = byte_obj.hex()
            
            # Print the result
            print(f"[{decimal_value}]\t{byte_obj}")

        except ValueError as e:
            # Handle invalid input
            print(e)


def hex_to_string():
    pass


def string_to_hex():
    while True:
        # Prompt the user for input
        data = input("\n[!] Write a string to convert: ")
        
        # Convert each character to its ASCII hexadecimal representation
        hex_output = '\\x'
        hex_output += '\\x'.join(format(ord(char), '02x') for char in data)
        
        # Print the hexadecimal representation
        print(f"[~] Hexadecimal representation:\t'{hex_output}'")


def hex_to_bytes(command):
    # Remove the \x notation
    command = command.replace('\\x', '')

    # Convert to bytes
    command = bytes.fromhex(command)

    return command




# Options
def help_panel():
    print("[!] Options:\n")
    print("\t[help] Print this message.")
    print("\t[1] HEXADECIMAL ASCII to DECIMAL representation.")
    print("\t[2] DECIMAL integer to HEXADECIMAL")

    print("\t[3] HEX chain to STRING representation")
    print("\t[4] STRING chain to HEX")
    print("-----------------------------------------------------------------")

if __name__ == "__main__":

    help_panel()

    min_option = 1
    max_option = 4

    while True:
        option = input("[*] Select an option: ")

        if option == "help":
            help_panel()
            continue

        try:
            option = int(option)    # Tranform to integer
        except:
            continue

        if option < min_option or option > max_option:
            print("[#] Invalid option. Retry.\n")
            continue

        elif option == 1:
            hex_to_decimal()

        elif option == 2: 
            decimal_to_hex()

        elif option == 3:
            hex_to_string()

        elif option == 4:
            string_to_hex()
