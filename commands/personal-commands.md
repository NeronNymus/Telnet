# Some Mirai commands
/bin/busybox ps
/bin/busybox kill -9
/bin/busybox mkdir
/bin/busybox rm
/bin/busybox cp
/bin/busybox echo
/bin/busybox wget
/bin/busybox tftp
/bin/busybox 
/bin/busybox 
/bin/busybox 

# Agressive commands
su
component delete all
reset

# Personal Available commands

## This command directly prints the associate SSID to the router. This works
## very well for mapping the biyect function defined as f:(IP)=SSID
## Then it is possible to analyze if the IP's change over time.
SU_WAP>display wifi associate␇
Mac               SSID                             Time   TxRate  RxRate  Mode  Antenas  PowerSave DualBand  BF  11K 11V 11R 
############################################################## 2.4GHz ##############################################################
Number of associated STAs on 2.4GHz band: 3

48:90:2F:BC:34:71 Totalplay-6DAB                   42199  86M     39M     11bgn 1*1      on        0         0   1   1   0   
1E:12:9C:D3:68:F8 Totalplay-6DAB                   39184  86M     65M     11bgn 1*1      off       1         0   1   1   0   
A4:3E:A0:C2:F8:CA Totalplay-6DAB                   2537   14M     65M     11bgn 1*1      off       0         0   0   1   0   
##############################################################  5GHz  ##############################################################
Number of associated STAs on 5GHz band: 1

64:1C:AE:D1:2B:2E Totalplay-6DAB-5G                2445   243M    216M    11na  2*2      off       1         0   0   0   0   

success!

SU_WAP> display tr069 info
Enable :true
ACS URL :http://tr069.totalplay.com.mx/MyACS/Default.aspx
ACS Username :totalplay
ACS Password :**********
Periodic Inform :true
Periodic Inform Interval :96132 second(s)
Time To Send Next Inform :27976 second(s)
Connection Request Username :totalplay
Connection Request Password :**********
Connection Request Path :c5e1b022b6be771ddc2dfd6c93e7c5fe
Connection Request Port :7547
CPE OUI :00259E
CPE ProductClass :HG8145X6
CPE SerialNumber :48575443B1676DAB
CPE Manufacture :Huawei Technologies Co., Ltd
CPE ModelName :HG8145X6
Unsolicited Report Status :Succeeded



WAP>display sysinfo
*************** system infomation ***************
CpuUsed  = 6 Percent(s)
MemUsed  = 63 Percent(s)
CurTime  = 2024-08-02 19:07:41-06:00
*************************************************

success!

WAP>display deviceInfo
*************** device information ***************
Manufacturer     = Huawei Technologies Co., Ltd
ManufacturerOUI  = 00259E
ModelName        = HG8145V5
Description      = EchoLife HG8145V5 GPON Terminal (CLASS B+/PRODUCT ID:2150084771AGM6045387)
ManufactureInfo  = 2150084771AGM6045387.C412
ProductClass     = HG8145V5
SpecVersion      = 1.0
ProvisioningCode = 
UpTime           = 1 day(s) 19:16:41
ReleaseTime      = 2023-02-14_15:09:15 
UpPort mode      = 1
DeviceAlias      = 
TotalMemory      = 256 Mbytes
TotalFlash       = 128 Mbytes
HardwareInfo     = GPON 4*GE + 2.4G/5G Wi-Fi + 1POTS + 1USB
Manufacture Date = 
*************************************************

success!


WAP>display cpu info

processor	: 0
model name	: ARMv7 Processor rev 1 (v7l)
BogoMIPS	: 1594.16
Features	: half thumb fastmult edsp thumbee tls 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x4
CPU part	: 0xc09
CPU revision	: 1
CPU physical	: 0

processor	: 1
model name	: ARMv7 Processor rev 1 (v7l)
BogoMIPS	: 1594.16
Features	: half thumb fastmult edsp thumbee tls 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x4
CPU part	: 0xc09
CPU revision	: 1
CPU physical	: 1

Hardware	: Hisilicon A9
Revision	: 0000
Serial		: 0000000000000000



success!


WAP>display inner version
MainVersion      : V500R022C00SPC234B001
StandbyVersion   : V500R022C00SPC234B001
ComponentVersion : not exist
ResourceVersion  : not exist
PluginVersion    : V500R022C00SPC234A2310120253
VersionMask      : 1

WAP>display version
hardware version          = 15AD.A
main software version     = V5R022C00S234
standby software version  = V5R022C00S234
uboot version             = 2020.01

success!


success!

# Try combinations with this command
display file 

display waninfo all detail

display wanmac
display lanmac
display productmac

display iptables nat
display iptables filter
set portmirror
display flow
display dhcp server user all

# Get the SSID name of the wifi
display wifi information

# list files, equivalent to ls
# using this command, pseudo tree and find can be implemented
wap list format 1 path /
wap top

# Network commands
ping 
traceroute

## This logs the incoming ping requests
trafficdump protocol icmp 

# Flood attacks
ping -i 1 -s 65507 -t 64 <target_IP>

## Resolve mac address of internal hosts
arping -I br0 -f 192.168.100.1

# Analyze open ports
netstat -na

# Change the password!!
SU_WAP>set userpasswd root
old password:
new password:
reenter new password:
Password of root has been modified successfully!

success!


# SSH related commands
set apssh mac 68:E2:09:18:20:98 enable 1
set apssh mac 68:e2:09:18:20:98 enable 1

load ssh-pubkey by ftp svrip 192.168.100.233 remotefile id_ftp.pub user ftpserver pwd 52a7cZdX port 21
load ssh-pubkey by ftp svrip 10.39.84.122 remotefile id_ftp.pub user ftpserver pwd 52a7cZdX port 21

load ssh-pubkey by ftp svrip 10.39.84.117 remotefile id_ftp.pub user ftpserver pwd 52a7cZdX port 21

# ftp related commands
## syntax
load fem par by {tftp|sftp} [svrip {ip addr}] [par_name {file name}] [user {user name}] [pwd {password}] [port {port}]
load pack by {https|sftp|ftp|tftp|http} svrip {ip addr} remotefile {file name} [user {user name}] [pwd {password}] [port {port}]. Attention: Only some boards support ftp|tftp|http service

# examples
load fem par by sftp svrip 10.39.84.117 par_name id_ftp.pub user ftpserver pwd 52a7cZdX port 21
load fem par by sftp svrip 10.39.84.117 par_name R020.bin user ftpserver pwd 52a7cZdX port 21

# This already works
load pack by ftp svrip 10.39.84.117 remotefile basic_test user ftpserver pwd 52a7cZdX port 21
load pack by ftp svrip 10.39.84.117 remotefile test1 user ftpserver pwd 52a7cZdX port 21	
load pack by ftp svrip 10.39.84.117 remotefile id_ftp.pub user ftpserver pwd 52a7cZdX port 21	
load pack by ftp svrip 10.39.84.117 remotefile R020.bin user ftpserver pwd 52a7cZdX port 21
load pack by ftp svrip 10.39.84.117 remotefile R020.bin user ftpserver pwd 52a7cZdX port 21



# Delicate available telnet commands
set aptelnet
set cwmp debug

# Check paths
SU_WAP>wap list path /   
bin
boot
dev
etc
html
init
lib
libexec
linuxrc
mnt
proc
root
sbin
share
sys
tmp 
usr
var

# Checking security
SU_WAP>check security config 
check result:

WEB password | ABNORMAL | the web password of the user has not been changed
Telnet password | ABNORMAL | the telnet password has not been changed
SSH password | ABNORMAL | the SSH password has not been changed
FTP service | NORMAL | FTP service has been disabled
SFTP service | ABNORMAL | SFTP service has been enabled, which may cause security risks
WAN listening port 80 | ABNORMAL | wan side web server listening port
WAN listening port 23 | ABNORMAL | wan side telnet service listening port
WAN listening port 22 | ABNORMAL | wan side SSH service listening port
WAN listening port 8022 | ABNORMAL | wan side SFTP service listening port
WAN listening port 7547 | NORMAL | TR069 client wan side listening port
WAN listening port 53 | NORMAL | dnsmasq(tcp)
WAN listening port 53 | NORMAL | dnsmasq(udp)
WAN listening port 5060 | ABNORMAL | voice_h248sip(udp)
Listening port 0.0.0.0:67 | NORMAL | Exception process: dhcpd(udp)
Listening port 0.0.0.0:68 | NORMAL | Exception process: dhcpc(udp)
Listening port :::546 | NORMAL | Exception process: dhcp6c(udp)
Listening port :::547 | NORMAL | Exception process: dhcp6s(udp)
secure boot | ABNORMAL | secure boot is not supported
integrity protection | NORMAL | supports integrity protection


success!


# Su access
WAP>su
success!
SU_WAP>shell

BusyBox v1.32.1 () built-in shell (ash)
Enter 'help' for a list of built-in commands.


profile close core dump

# Ip route
# This command show where is redirected the public IP 187.251.158.90 and IPv6 too.
# Is it possible to fetch the ip routes of the router.

SU_WAP>ip route show
default via 10.126.0.1 dev ppp257 table 100 
187.251.158.90 via 10.126.0.1 dev ppp257 table 100 
192.168.100.0/24 dev br0 table 100 scope link  src 10.126.120.16 
default via 10.161.128.1 dev wan2 table 101 
192.168.100.0/24 dev br0 table 101 scope link  src 10.161.230.252 
default via 10.13.128.1 dev wan3 table 102 
192.168.100.0/24 dev br0 table 102 scope link  src 10.13.180.1 
blackhole default table 200  metric 150 
default via 10.161.128.1 dev wan2 table lan1  metric 100 
blackhole default table lan1  metric 150 
192.168.100.0/24 dev br0 table lan1 scope link 
default via 10.13.128.1 dev wan3 table lan2  metric 100 
blackhole default table lan2  metric 150 
192.168.100.0/24 dev br0 table lan2 scope link 
default via 10.126.0.1 dev ppp257 table lan3  metric 100 
blackhole default table lan3  metric 150 
192.168.100.0/24 dev br0 table lan3 scope link 
default dev ppp257 scope link  metric 10 
10.1.0.0/24 via 10.13.128.1 dev wan3  metric 10 
10.3.1.0/24 via 10.13.128.1 dev wan3  metric 10 
10.5.4.0/24 via 10.13.128.1 dev wan3  metric 10 
10.13.128.0/18 dev wan3 scope link  src 10.13.180.1 
10.126.0.1 dev ppp257 scope link  src 10.126.120.16 
10.161.128.0/17 dev wan2 scope link  src 10.161.230.252 
10.187.1.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.3.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.4.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.5.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.6.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.7.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.8.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.9.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.14.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.15.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.16.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.17.0/24 via 10.13.128.1 dev wan3  metric 10 
10.187.19.0/24 via 10.13.128.1 dev wan3  metric 10 
10.201.0.0/24 via 10.13.128.1 dev wan3  metric 10 
10.207.58.0/24 via 10.13.128.1 dev wan3  metric 10 
10.207.59.0/24 via 10.13.128.1 dev wan3  metric 10 
10.207.61.0/24 via 10.13.128.1 dev wan3  metric 10 
10.207.251.0/24 via 10.13.128.1 dev wan3  metric 10 
10.213.8.0/24 via 10.13.128.1 dev wan3  metric 10 
10.213.12.0/24 via 10.13.128.1 dev wan3  metric 10 
189.203.173.0/24 via 10.13.128.1 dev wan3  metric 10 
192.168.100.0/24 dev br0 scope link  src 192.168.100.1 
207.83.200.0/24 via 10.13.128.1 dev wan3  metric 10 
broadcast 10.13.128.0 dev wan3 table local scope link  src 10.13.180.1 
local 10.13.180.1 dev wan3 table local scope host  src 10.13.180.1 
broadcast 10.13.191.255 dev wan3 table local scope link  src 10.13.180.1 
local 10.126.120.16 dev ppp257 table local scope host  src 10.126.120.16 
broadcast 10.161.128.0 dev wan2 table local scope link  src 10.161.230.252 
local 10.161.230.252 dev wan2 table local scope host  src 10.161.230.252 
broadcast 10.161.255.255 dev wan2 table local scope link  src 10.161.230.252 
broadcast 127.0.0.0 dev lo table local scope link  src 127.0.0.1 
local 127.0.0.0/8 dev lo table local scope host  src 127.0.0.1 
local 127.0.0.1 dev lo table local scope host  src 127.0.0.1 
broadcast 127.255.255.255 dev lo table local scope link  src 127.0.0.1 
broadcast 169.254.254.0 dev lo table local scope link  src 169.254.254.185 
local 169.254.254.0/24 dev lo table local scope host  src 169.254.254.185 
local 169.254.254.185 dev lo table local scope host  src 169.254.254.185 
broadcast 169.254.254.255 dev lo table local scope link  src 169.254.254.185 
broadcast 192.168.100.0 dev br0 table local scope link  src 192.168.100.1 
local 192.168.100.1 dev br0 table local scope host  src 192.168.100.1 
broadcast 192.168.100.255 dev br0 table local scope link  src 192.168.100.1 
2806:2f0:7581:f137::/64 dev br0 table 100  metric 100 
blackhole 2806:2f0:7581:f137::/64 dev lo table 100  metric 1024 
default dev ppp257 table 100  metric 100 
2806:2f0:7581:f137::/64 dev br0 table 101  metric 100 
2806:2f0:7581:f137::/64 dev br0 table 102  metric 100 
2806:2f0:7581:f137::/64 dev br0 table 103  metric 100 
2806:2f0:7581:f137::/64 dev br0 table 107  metric 100 
default dev ppp257 table lan1  metric 100 
blackhole default dev lo table lan1  metric 101 
2806:2f0:7580:0:8e67:a8de:91aa:5c39 dev ppp257  metric 256 
2806:2f0:7581:f137::/64 dev br0  metric 10 
blackhole 2806:2f0:7581:f137::/64 dev lo  metric 1024 
fe80::20c6:db:f8df:1893 dev ppp257  metric 256 
fe80::f6a4:d6ff:fe99:4d6d dev ppp257  metric 256 
fe80::/64 dev br0  metric 256 
fe80::/64 dev veth0  metric 256 
fe80::/64 dev veth1  metric 256 
fe80::/64 dev vap0  metric 256 
fe80::/64 dev vap2  metric 256 
fe80::/64 dev vap3  metric 256 
fe80::/64 dev vap4  metric 256 
fe80::/64 dev vap6  metric 256 
fe80::/64 dev vap7  metric 256 
default dev ppp257  metric 1024 
local ::1 dev lo table local  metric 0 
local 2806:2f0:7580:0:8e67:a8de:91aa:5c39 dev ppp257 table local  metric 0 
anycast fe80:: dev br0 table local  metric 0 
local fe80::1 dev br0 table local  metric 0 
local fe80::44f:d2ff:fe0f:422b dev veth0 table local  metric 0 
local fe80::20c6:db:f8df:1893 dev ppp257 table local  metric 0 
local fe80::d0b2:f8ff:fe9e:1342 dev veth1 table local  metric 0 
local fe80::f23f:95ff:fec7:4b8f dev br0 table local  metric 0 
local fe80::f23f:95ff:fec7:4b98 dev vap0 table local  metric 0 
local fe80::f23f:95ff:fec7:4b9a dev vap2 table local  metric 0 
local fe80::f23f:95ff:fec7:4b9b dev vap3 table local  metric 0 
local fe80::f23f:95ff:fec7:4b9c dev vap4 table local  metric 0 
local fe80::f23f:95ff:fec7:4b9e dev vap6 table local  metric 0 
local fe80::f23f:95ff:fec7:4b9f dev vap7 table local  metric 0 
multicast ff00::/8 dev eth0 table local  metric 256 
multicast ff00::/8 dev br0 table local  metric 256 
multicast ff00::/8 dev ppp257 table local  metric 256 
multicast ff00::/8 dev veth0 table local  metric 256 
multicast ff00::/8 dev veth1 table local  metric 256 
multicast ff00::/8 dev vap0 table local  metric 256 
multicast ff00::/8 dev vap2 table local  metric 256 
multicast ff00::/8 dev vap3 table local  metric 256 
multicast ff00::/8 dev vap4 table local  metric 256 
multicast ff00::/8 dev vap6 table local  metric 256 
multicast ff00::/8 dev vap7 table local  metric 256

# ip neigh
SU_WAP>ip neigh
10.161.128.1 dev wan2 lladdr f4:a4:d6:99:4d:6d ref 1 used 1156/8/8 nud reachable timeout 158
192.168.100.70 dev br0 lladdr 98:42:65:40:96:6a ref 1 used 117967/9/117967 nud reachable timeout 319
192.168.100.234 dev br0 lladdr 10:59:32:d4:14:03 ref 1 used 2825/82/2825 nud reachable timeout 246
192.168.100.110 dev br0 lladdr 7a:32:af:c4:7a:f2 ref 1 used 2824/82/2824 nud reachable timeout 246
192.168.100.134 dev br0 lladdr b0:e4:5c:fd:59:72 ref 1 used 2824/82/2824 nud reachable timeout 246
192.168.100.125 dev br0 lladdr 82:4d:46:4d:9e:29 ref 1 used 2824/82/2824 nud reachable timeout 246
192.168.100.7 dev br0 lladdr 10:08:c1:b4:8c:9e ref 1 used 4899/82/2834 nud reachable timeout 246
192.168.100.174 dev br0 lladdr 46:2c:8a:1d:a7:f1 ref 1 used 3051/82/1770 nud reachable timeout 246
192.168.100.76 dev br0 lladdr 58:d9:d5:45:27:49 ref 1 used 2834/82/2833 nud reachable timeout 246
192.168.100.133 dev br0 lladdr 26:1d:92:43:5e:a2 ref 1 used 343/81/342 nud reachable timeout 247
192.168.100.101 dev br0 lladdr da:4d:20:29:48:3f ref 1 used 721/81/742 nud reachable timeout 247
192.168.100.253 dev br0 lladdr 4e:56:c9:4c:ee:00 ref 1 used 2046/269/2056 nud reachable timeout 59
192.168.100.250 dev br0 lladdr fa:45:a4:3b:11:6d ref 1 used 62/61/61 nud reachable timeout 267
10.13.128.1 dev wan3 lladdr ec:c0:1b:df:fd:97 ref 1 used 13003/172/172 nud reachable timeout 38
192.168.100.36 dev br0 lladdr 50:32:37:96:a8:b0 ref 1 used 2824/82/2824 nud reachable timeout 246
fe80::5ad9:d5ff:fe45:2749 dev br0 lladdr 58:d9:d5:45:27:49 router ref 1 used 2440/63/2440 nud reachable timeout 155
2806:2f0:7581:f137:6821:d870:d8ca:e3fd dev br0 lladdr b0:e4:5c:fd:59:72 ref 1 used 2434/60/2434 nud reachable timeout 158
fe80::1259:32ff:fed4:1403 dev br0 lladdr 10:59:32:d4:14:03 ref 1 used 2281/63/2281 nud reachable timeout 155
2806:2f0:7581:f137:49dc:4d8b:f869:4c36 dev br0 lladdr 50:32:37:96:a8:b0 ref 1 used 2445/62/2445 nud reachable timeout 156
2806:2f0:7581:f137:d8ab:5c13:59e5:85c4 dev br0 lladdr b0:e4:5c:fd:59:72 ref 1 used 2445/60/2445 nud reachable timeout 158
fe80::c4d:2d55:ab2d:6c39 dev br0 lladdr fa:45:a4:3b:11:6d ref 1 used 64/62/64 nud reachable timeout 156
2806:2f0:7581:f137:c953:8a7e:b143:3f07 dev br0 lladdr fa:45:a4:3b:11:6d ref 1 used 63/61/63 nud reachable timeout 157
2806:2f0:7581:f137:b2e4:5cff:fefd:5972 dev br0 lladdr b0:e4:5c:fd:59:72 ref 1 used 2344/60/2344 nud reachable timeout 158
fe80::b2e4:5cff:fefd:5972 dev br0 lladdr b0:e4:5c:fd:59:72 ref 1 used 2435/60/2435 nud reachable timeout 158
2806:2f0:7581:f137:adbb:3623:8fd9:658e dev br0 lladdr 50:32:37:96:a8:b0 ref 1 used 2450/62/2450 nud reachable timeout 156
fe80::7832:afff:fec4:7af2 dev br0 lladdr 7a:32:af:c4:7a:f2 ref 1 used 2163/54/2163 nud reachable timeout 164
2806:2f0:7581:f137:4b7:3c7c:3bb5:5420 dev br0 lladdr 50:32:37:96:a8:b0 ref 1 used 2182/63/2182 nud reachable timeout 155
fe80::98:e684:b4ca:2153 dev br0 lladdr 50:32:37:96:a8:b0 ref 1 used 2445/62/2445 nud reachable timeout 156
2806:2f0:7581:f137:1428:cb6b:65ea:ddfb dev br0 lladdr fa:45:a4:3b:11:6d ref 1 used 63/62/63 nud reachable timeout 156
2806:2f0:7581:f137:5ad9:d5ff:fe45:2749 dev br0 lladdr 58:d9:d5:45:27:49 router ref 1 used 2450/63/2450 nud reachable timeout 155

success!

WAP>display wifi neighbor
Scanning neighbors,it will take several seconds, please wait!

CurrentWorkingChannel:4(2.4G) 149(5G)

Neighbor ap number:26
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Mac                SSID                               Channel  BandWidth  MIMO     RSSI     Mode        Security                     WMM      Noise    MaxBitRate
------------------------------------------------------------------------------------------------------------------------------------------------------------------
##############################################################################2.4GHz##############################################################################
------------------------------------------------------------------------------------------------------------------------------------------------------------------
32:23:64:C6:0D:39                                     1        20M        2X2      -58      11b/g/n     WPA2-PSK-AES                 off      -90      144     
10:08:1D:B9:F7:61  Club_Totalplay_WiFi                1        20M        2X2      -85      11b/g/n     OPEN-NONE                    off      -90      144     
50:0F:F5:12:22:F1  FAMALVARADO                        1        20M        2X2      -61      11b/g/n     WPA/WPA2-PSK-AES             off      -90      144     
30:23:64:B6:0D:39  INFINITUMDE60                      1        20M        2X2      -58      11b/g/n     WPA2-PSK-AES                 off      -90      144     
6C:FF:CE:9A:DD:E5  TOTALPLAY_9ADDE2_2.4G              1        20M        2X2      -67      11b/g/n     WPA2-PSK-AES                 off      -90      144     
A4:6D:A4:79:89:A9  Club_Totalplay_WiFi                2        20M        2X2      -94      11b/g/n     OPEN-NONE                    off      -90      144     
90:9A:4A:0D:3D:96  SAAG                               3        40M        2X2      -94      11b/g/n     WPA2-PSK-AES                 off      -90      400     
68:E2:09:0D:26:E2                                     4        20M        2X2      -92      11b/g/n     WPA2-PSK-AES                 off      -90      144     
68:E2:09:0D:26:E0  Totalplay-6AA5                     4        20M        2X2      -91      11b/g/n     WPA2-PSK-AES                 off      -90      144     
C4:A4:02:85:BB:0C  Totalplay-4CA5                     5        20M        2X2      -88      11b/g/n     WPA2-PSK-AES                 off      -90      144     
D8:21:DA:E9:94:A4  INFINITUM5E21                      6        20M        2X2      -95      11b/g/n     WPA2-PSK-AES                 off      -90      144     
A0:3E:8C:12:90:78  INFINITUM5E21-EXT                  6        20M        2X2      -77      11b/g/n     WPA2-PSK-AES                 off      -90      144     
C2:94:AD:B8:1B:7E  Club_Totalplay_WiFi                7        20M        2X2      -86      11b/g/n     OPEN-NONE                    off      -90      130     
C0:94:AD:B8:1B:7E  Totalplay-666B                     7        20M        2X2      -90      11b/g/n     WPA2-PSK-AES                 off      -90      130     
BE:61:E9:42:49:C5                                     10       20M        2X2      -81      11b/g/n     WPA2-PSK-AES                 off      -90      144     
A4:00:E2:CC:B3:FE                                     10       20M        2X2      -63      11b/g/n     WPA2-PSK-AES                 off      -90      144     
A4:00:E2:CC:B3:FF  Club_Totalplay_WiFi                10       20M        2X2      -63      11b/g/n     OPEN-NONE                    off      -90      144     
6C:5A:B0:3D:8E:3D  Silence of the LAN                 10       20M        2X2      -92      11b/g/n     WPA2-PSK-AES                 off      -90      144     
A4:00:E2:CC:B3:FC  Totalplay-6D9F                     10       20M        2X2      -70      11b/g/n     WPA2-PSK-AES                 off      -90      144     
50:A5:DC:D1:14:F3  IZZI-E892                          11       20M        3X3      -78      11b/g/n     WPA2-PSK-AES                 off      -90      217     
------------------------------------------------------------------------------------------------------------------------------------------------------------------
###############################################################################5GHz###############################################################################
------------------------------------------------------------------------------------------------------------------------------------------------------------------
C2:94:AD:B8:1B:80  Club_Totalplay_WiFi                44       80M        2X2      -92      11a/n/ac    OPEN-NONE                    off      -90      867     
C0:94:AD:B8:1B:80  Totalplay-666B-5G                  44       80M        2X2      -93      11a/n/ac    WPA2-PSK-AES                 off      -90      867     
50:0F:F5:12:22:F5  GODISGOOD                          149      80M        2X2      -78      11a/n/ac    WPA/WPA2-PSK-AES             off      -90      867     
6C:FF:CE:9A:DD:E6  TOTALPLAY_9ADDE2                   149      80M        2X2      -75      11a/n/ac    WPA2-PSK-AES                 off      -90      867     
32:23:64:C6:0D:3D                                     161      80M        2X2      -72      11a/n/ac    WPA2-PSK-AES                 off      -90      867     
30:23:64:B6:0D:3D  INFINITUMDE60                      161      80M        2X2      -71      11a/n/ac    WPA2-PSK-AES                 off      -90      867     
------------------------------------------------------------------------------------------------------------------------------------------------------------------

success!
