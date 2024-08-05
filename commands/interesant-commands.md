# Try this commands

set userpasswd: Changes user passwords, allowing attackers to lock out legitimate users or escalate privileges.
ssh authentication-type: Configures SSH authentication methods, potentially allowing attackers to weaken security.
set ssh-hostkey: Alters SSH host keys, allowing man-in-the-middle attacks.
set timeout: Changes session timeouts, which could keep unauthorized sessions open longer.
telnet remote: Enables remote telnet access, which is insecure and can be exploited for remote control.
shell: Provides access to the underlying shell, giving attackers full control over the system.
restore backup: Restores configuration from a backup, potentially overriding secure settings.
restore manufactory: Resets device to factory settings, erasing all security configurations.
set portmirror: Enables port mirroring, which can be used to sniff network traffic.
set opticdata: Changes optical settings, potentially disrupting network communication.
set collect: Configures data collection, potentially exposing sensitive information.
display current-configuration: Shows the current configuration, revealing system details to attackers.
display device-cert info: Displays device certificates, potentially allowing attackers to spoof devices.
display connection all: Shows all connections, revealing active sessions and network details.
set cwmp debug: Configures CWMP (CPE WAN Management Protocol) debugging, potentially exposing management traffic.
clear rogue flag: Removes rogue device flags, potentially allowing unauthorized devices to connect.
set iaccess speed: Changes internet access speed, potentially affecting network performance.
set flashlock: Configures flash memory locking, potentially disabling security measures.
display memory detail: Shows detailed memory usage, potentially revealing sensitive data in memory.
set aptelnet: Configures telnet access, which is insecure and can be exploited for remote control.

# List of commands categorized and separated
set apssh
set aptelnet
set userpasswd
ifconfig
ip route
ip neigh
dhcp client
dhcp server pool config
display ip interface
display ip route
set lanport qbuf
set port isolate
set portmirror
set ethportmirror

#Firewall and Security Commands:

display firewall rule
set iaccess speed
ssh authentication-type
make ssh hostkey
set ssh
set cwmp debug
display access mode
set voiceportloop
set voip

#Debugging and Diagnostics Commands:

debug
ping
traceroute
collect debug info
display diagnose info
oamcmd debug
omcicmd debug
chipdebug

#Configuration and Backup Commands:

save data
save log
restore backup
restore manufactory
display current-configuration
display sysinfo

WiFi and Network Interface Commands:

set wifi
set wlan
display wlan config
display wifi
add wifi filter
del wifi filter
"""

# Writing the commands to a txt file
with open('/mnt/data/commands_list.txt', 'w') as file:
    file.write(commands)


