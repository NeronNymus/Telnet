WAP>?
acc get accesslimit
WAP>?
add wifi filter index [1-8] mac {mac}
WAP>?
[Command]: amp add policy-stats pon
[Usage]: amp add policy-stats pon vlan [1:4095] [pri [0:7]]
WAP>?
[Command]: amp add policy-stats port
[Usage]: amp add policy-stats port id [portid] vlan [1:4095] [pri [0:7]]
WAP>?
[Command]: amp add stats gemport
[Usage]: amp add stats gemport id [1:4094]
WAP>?
[Command]: amp clear policy-stats pon
[Usage]: amp clear policy-stats pon
WAP>?
[Command]: amp clear policy-stats port
[Usage]: amp clear policy-stats port [id [portid]]
amp clear policy-stats port: Clear all ports stats.
amp clear policy-stats port id [portid]: Clear the spec port stats.
WAP>?
[Command]: amp clear stats gemport
[Usage]: amp clear stats gemport [id [1:4094]]
amp clear stats gemport: Clear all gemports stats.
amp clear stats gemport id [1:4094]: Clear the spec gemport stats.
WAP>?
[Command]: amp del policy-stats pon
[Usage]: amp del policy-stats pon vlan [1:4095] [pri [0:7]]
WAP>?
[Command]: amp del policy-stats port
[Usage]: amp del policy-stats port id [portid] vlan [1:4095] [pri [0:7]]
WAP>?
[Command]: amp del stats gemport
[Usage]: amp del stats gemport id [1:4094]
WAP>?
[Usage]:
ampcmd show emac stat {0|1|2|3|4}
0: emac message queue
1: emac up traffic
2: emac down traffic
3: kernel oam
4: config
WAP>?
[Usage]:ampcmd show flow all
WAP>?
[Usage]:ampcmd show flow index {index}
WAP>?
[Usage]:ampcmd show log
WAP>?
[Usage]:ampcmd trace all {on|off}
WAP>?
[Usage]:ampcmd trace cli {on|off}
WAP>?
[Usage]:ampcmd trace dpoe {on|off}
WAP>?
[Usage]:ampcmd trace drv {on|off}
WAP>?
[Usage]:ampcmd trace emac {on|off}
WAP>?
[Usage]:ampcmd trace emap {on|off}
WAP>?
[Usage]:ampcmd trace eth {on|off}
WAP>?
[Usage]:ampcmd trace gmac {on|off}
WAP>?
[Usage]:ampcmd trace gmap {on|off}
WAP>?
[Usage]:ampcmd trace onu {on|off}
WAP>?
[Usage]:ampcmd trace optic {on|off}
WAP>?
[Usage]:ampcmd trace qos {on|off}
WAP>?
[Usage]:appmcmd debug switch [0:off,1:on]
WAP>?
[Usage]:appmcmd regplat
WAP>?
[Usage]:appmcmd show type [type-id]
[Note for type]:
	type-1: show local info.;
	type-2: show plug-in center info.;
	type-3: show cloud platform info.;
WAP>?
Usage: 
arping -I IFACE [-fqbDUA] [-c CNT] [-w TIMEOUT] [-s SRC_IP] DST_IP

Send ARP requests/replies

        -f              Quit on first ARP reply
        -q              Quiet
        -b              Keep broadcasting, don't go unicast
        -D              Exit with 1 if DST_IP replies
        -U              Unsolicited ARP mode, update your neighbors
        -A              ARP answer mode, update your neighbors
        -c N            Stop after sending N ARP requests
        -w TIMEOUT      Seconds to wait for ARP reply
        -I IFACE        Interface to use (default eth0)
        -s SRC_IP       Sender IP address
        DST_IP          Target IP address
WAP>?
bbsp add policy-stats btv ip { ipaddr [ vlan [int] ] [ port [int] | mac [string] | userip [string] ] }
WAP>?
bbsp clear policy-stats btv all
WAP>?
bbsp clear policy-stats wan id [wanid | all]
WAP>?
bbsp del policy-stats btv ip { ipaddr [ vlan [int] ] [ port [int] ] }
WAP>?
USAGE:
     bbspara [display {xxx}] 
OPTIONS:
     display: wan show layer all
              mac show all
              fw show all
              fw show stats
              vbr-fw show stat
              user_flow show
              user_flow show ctp
              user_flow bctbl br
              vbridge bridge-info
              vbridge uni-binding
              vbridge nni-binding
              vbridge uplink-binding
              vbridge port-binding
              ffwd show all
              ffwd show stat
              l2ffwd acc-item
              napt show all
              ctp show_ctp all
              ctp show_ctp detail
              acl show chain all
              route show
              tunnel show all
WAP>?
USAGE:
     bbspcmd [para {xxx}] 
OPTIONS:
     para:    vbr-fw clean vbr-id
              vbr-fw dbg hook
              vbr-fw dbg all
              vbr-fw dbg vbr-id
              fw dbg pktinfo info
              ffwd dbg all
              ffwd dbg timer
              ffwd dbg event
              ffwd dbg lsw
              ffwd dbg napt
              ffwd dbg fwd
              cpu dbg on
              cpu dbg off
              dbg
              cmd_debug on
              cmd_debug off
WAP>?
Usage: 
Broadband debug ethoam    {on | off | pkt NUMBER}
                ker_route
                lswadp
                ptpdrv  {all | eth | pon | wifi | radio | igmp | icmp | arp | dhcp} {on | off | pkt NUMBER}
                pkt { {all | off} {PROTOCOL | EXPRESSION | DEVICE} }

WAP>?
Usage: 
Broadband display ethoam
                  ker_ethoam
                  ptpdrv {dbm | stat | rate}
                  soc {cnt | clrcnt | gpon | ifc | ofc | sfc | bridge | eth | l3 | queue | flow | l2 | dscptable | macfilter | car | btv | bc VLANID}
                  l2mac
                  wlwan 

WAP>?
btv start period-stats ip ipaddr [ vlan vlan ] { port port | mac mac | userip userip } interval interval duration duration
WAP>?
btv stop period-stats
WAP>?
chipdebug
chipdebug clearall
chipdebug soc drop
chipdebug soc rx
chipdebug soc tx
WAP>?
[Usage]:chipdebug clearall
WAP>?
[Usage]:chipdebug soc drop
WAP>?
[Usage]:chipdebug soc rx
WAP>?
[Usage]:chipdebug soc tx
WAP>?
[Command]: clear amp pq-stats
[Usage]: clear amp pq-stats tcont-llid [id] queue [queueid]
WAP>?
USAGE:
     clear lastword -- clean lastowrd records.
WAP>?
[Command]: clear pon statistics
WAP>?
clear poncnt dnstatistic [portid {id}]
WAP>?
clear poncnt gemport upstatistic gemportid {gemportid} [portid {id}]
WAP>?
clear poncnt upstatistic [portid {id}]
WAP>?
[Command]: clear port statistics portid
[Usage]: clear port statistics portid [portid]
WAP>?
clear reogue flag
WAP>?
USAGE:
     clear sfwd drop statistics -- Clear the forward drop packets statistics.
WAP>?
Usage:
collect debug info [OPTIONS]

collect debug infomations

Options:
        ssmp           Only collect ssmp debug infomation
        voice          Only collect voice debug infomation
        bbsp           Only collect bbsp debug infomation
        amp            Only collect amp debug infomation
        ldsp           Only collect ldsp debug infomation
        smart          Only collect smart debug infomation
        wlan           Only collect wlan debug infomation
        all            Collect all debug info(default)
        history        Get all debug info from cache
WAP>?
USAGE:
     component delete all  -- delete all softwore component pack. it take effects after reboot.
WAP>?
[Usage]: ctrgcmd debug type {type-id} [bus {bus-name}]
OPTIONS:
    type: 1 start dbus-monitor for debug.;
          2 show dbus-monitor debug info.;
          3 clear dbus-monitor process.;
    bus: bus name for dbus-monitor,optional parameter.;
WAP>?
[Usage]: ctrgcmd send bus {bus-name} obj {object-name} method {method} [intf {interface-name}]
OPTIONS:
    bus: bus name.;
    obj: object name.;
    method: method name.;
    intf: interface name,optional parameter.;
WAP>?
[Usage]: ctrgcmd show type {type-id}
OPTIONS:
    type: 1 show history framework run log.;
          2 show current framework run log.;
          3 show framework start log.;
          4 show saf version.;
          5 show saf info.;
          6 show package versions.;
WAP>?
debug dsp down msg
WAP>?
debug dsp msg
WAP>?
debug dsp up msg
WAP>?
debug ifm info [0|1] error [0|1] step [0|1] pkt [0|1]
WAP>?
debug qoscfg [ info swt1 | step swt2 | error swt3 ]*
WAP>?
debug rtp stack
WAP>?
debug sample mediastar
WAP>?
debugging dsp diagnose port {[0,7]} type {1:tonedetect,2:jbdata,3:all} mode {0:once,1:over}
WAP>?
debugging dsp para diagnose port {[0,7]}
WAP>?
debugging dsp record autostop {[1,1440]}
WAP>?
debugging dsp t38diag port {[0,7]}
WAP>?
del wifi filter index [1-8] mac {mac}
WAP>?
dhcp client attach interface intfname
WAP>?
dhcp client detach interface intfname
WAP>?
dhcp client6 attach interface intfname
WAP>?
dhcp client6 detach interface intfname
WAP>?
dhcp server pool config index index [gateway ip] [netmask netmask] [start start_ip] [end end_ip] [dns dns_ip]
WAP>?
dhcp server pool disable index [poolIndex]
WAP>?
dhcp server pool enable index [poolIndex]
WAP>?
dhcp server pool lease config index index leasetime time
WAP>?
dhcp server pool option add poolindex poolindex tag tag value value
WAP>?
dhcp server pool option del poolindex poolindex index index
WAP>?
dhcp server pool option flush poolindex poolindex
WAP>?
dhcp server pool restart
WAP>?
diagnose
WAP>?
display access mode
WAP>?
display access system info
WAP>?
display aclservicesrule
WAP>?
[Command]: display amp policy-stats pon
WAP>?
[Command]: display amp policy-stats port
[Usage]: display amp policy-stats port [id [portid]]
display amp policy-stats port: display all ports stats.
display amp policy-stats port id [portid]: display the spec port stats.
WAP>?
[Command]: display amp pq-stats 
[Usage]: display amp pq-stats tcont-llid [id] queue [queueid]
WAP>?
[Command]: display amp stats gemport
[Usage]: display amp stats gemport [id [1:4094]]
display amp stats gemport: Display all gemports stats.
display amp stats gemport id [1:4094]: Display the spec gemport stats.
WAP>?
display apmChipStatus
WAP>?
display backup file list
WAP>?
USAGE:
     display batteryStatus -- get available capacity of battery
WAP>?
[Command]:display bbsp log
WAP>?
display bbsp stats btv ip { ipaddr [ port [int] ] | all }
WAP>?
display bbsp stats wan id {wanid | all}
WAP>?
display bms
display bmsxml crc
WAP>?
USAGE:
     display bmsxml crc  -- show bmsxml crc information.
WAP>?
USAGE:
     display board-temperatures -- display board-temperatures including Bob Soc Wifi RF
WAP>?
USAGE:
     display board2Item -- get board2 item of board
WAP>?
USAGE:
     display boardItem -- get board item of board
WAP>?
USAGE:
     display boardItem -- get bom item of board
WAP>?
display broadband info
WAP>?
display connection
display connection all
WAP>?
display connection all
WAP>?
USAGE: display cpu info
WAP>?
display current-configuration [grep {value}]
WAP>?
USAGE:
      display cwmp debug ---- display cwmp debug level
WAP>?
USAGE: display the device register acs status
WAP>?
display ddns info interface {intfname}
WAP>?
display debug info dhcp6c wanname [wanname]
WAP>?
display debug info dhcp6s
WAP>?
display debug info pppoev6
WAP>?
display debug info ra wanname [wanname]
WAP>?
USAGE:
     display debuglog info  -- show all debuglog information.
WAP>?
display debugwifilog info
WAP>?
USAGE:display device-cert info
WAP>?
USAGE:
     display deviceInfo -- get device info of board, such as upport mode, release time, model name, and so on
WAP>?
display dhcp client
display dhcp client all
display dhcp client6
display dhcp client6 all
WAP>?
display dhcp client {all | interface intfname}
WAP>?
display dhcp client6
display dhcp client6 all
WAP>?
display dhcp client6 {all | interface intfname}
WAP>?
display dhcp server pool
display dhcp server pool all
display dhcp server pool option
WAP>?
display dhcp server pool {all | index poolindex}
WAP>?
display dhcp server pool option poolindex poolindex
WAP>?
display dhcp server static
WAP>?
display dhcp server user
display dhcp server user all
WAP>?
display dhcp server user {all | index userIndex}
WAP>?
display dhcp_em result
WAP>?
display diagnose info
WAP>?
display dns proxy info interface intfname
WAP>?
display dnsserver static domain
WAP>?
display dpst
display dpst all
WAP>?
[Command]:display dpst all
WAP>?
display dsp channel para
WAP>?
display dsp channel running status
WAP>?
display dsp channel status
WAP>?
display dsp chip stat
WAP>?
display dsp codec status
WAP>?
display dsp interrupt stat
WAP>?
[Command]: display dynamic route [Usage]: display dynamic route [proto {rip}]
WAP>?
display eaiinfo
WAP>?
USAGE:display edge_ont info onuid [0-15, 255]
WAP>?
display epon ont info 
WAP>?
display ethoam ma info mdins [int] mains [int]
WAP>?
display ethoam md info mdins [int]
WAP>?
display ethoam mep info mdins[int] mains [int] mepins [int]
WAP>?
display ethoam mep perf mdinst [int] mainst [int] mepinst [int]
WAP>?
display femPar info
WAP>?
display femPar version
WAP>?
display ffwd table type all
WAP>?
display file
WAP>?
display filter rf (0 band-pass; 1 low-pass; 2 high-pass)
WAP>?
USAGE:
     display firewall rule [ chain [string] ] [ address-family {inet | inet6} ]
WAP>?
USAGE:display flashlock status
WAP>?
usage:display flow id {all | flowid} for:get flow info
WAP>?
display ftp config status
WAP>?
display igmp
display igmp config
WAP>?
display igmp config
WAP>?
USAGE:
     display inner version -- get software version, including B version!
WAP>?
display ip interface interface interface
WAP>?
display ip neigh
WAP>?
[Command]:display ip route [address-family Family]
	 OPTIONS: address-family: inet(IPv4,default)/inet6(IPv6)
WAP>?
display ip6tables filter
WAP>?
display iptables filter
WAP>?
display iptables mangle
WAP>?
display iptables nat
WAP>?
display iptables raw
WAP>?
display jb grid status
WAP>?
display jb para
WAP>?
display lan mac filter
WAP>?
USAGE:	
     display lanmac -- get lan mac of board
WAP>?
display lanport workmode
WAP>?
WAP>?
USAGE:
     display lastword  -- Displays the current lastword.
     display lastword type old  -- Displays the lastword for the last time and the lastword for the last 2 times.
     display lastword type startup  -- Displays the lastword for startup time.
WAP>?
USAGE:
     display log info  -- show all log information.
WAP>?
display mac ap
display mac ap brief
WAP>?
display mac ap brif
WAP>?
display macaddress
display macaddress timer
WAP>?
display macaddress timer
WAP>?
USAGE:
     display machineItem -- get machine item of board
WAP>?
display memory detail
WAP>?
USAGE:
     display memory info  -- show memory usage.
WAP>?
display microwave ctrl info
WAP>?
[Usage]:
display msg-queue : display all msg queue.
display msg-queue [appname {value}] : display the msg queue by process name.
WAP>?
display nat port mapping { interface IntfName [index Index] | internal-ip ip }
WAP>?
display NCE info
WAP>?
USAGE:
     display nff log  -- show all nff log information.
WAP>?
display np statistics
WAP>?
display oaml2shell ethvlan
WAP>?
display onu info(regstatus, onuid, xpon module)
WAP>?
display optic [device {opticdev}]
WAP>?
USAGE:
     display optmode -- display info of optic module
WAP>?
display policy route all
WAP>?
[Command]: display pon statistics
WAP>?
display poncnt dnstatistic [portid {id}]
WAP>?
display poncnt gemport upstatistic gemportid {gemportid} [portid {id}]
WAP>?
display poncnt upstatistic [portid {id}]
WAP>?
[Command]: display port statistics 
[Usage]: display port statistics portid [portid]
WAP>?
[Command]: display portstatistics 
[Usage]: display portstatistics portnum [portid]
WAP>?
display ppp interface interface interface
WAP>?
display pppoe client
display pppoe client all
WAP>?
display pppoe client {all | interface intfname}
WAP>?
display pppoe_em result
WAP>?
USAGE:
     display productmac -- get product mac of board
WAP>?
display the loading progress of package
pack: firmware
cfg: config xml file
bundle: bundle file
WAP>?
WAP>?
display rf config (switch: on/off; state:on/off )
WAP>?
USAGE:
     display rfpi -- get rfpi of board
WAP>?
display rtp stack channel stat
WAP>?
display rtp stack chip stat
WAP>?
display rtp stack para
WAP>?
display rtp stack version
WAP>?
USAGE:
     display sfwd drop statistics -- Displays the forward drop packets statistics.
WAP>?
USAGE:
     display sfwd port statistics -- Displays the port RX/TX packets statistics.
WAP>?
USAGE:
     display sn -- get serial number of board
WAP>?
USAGE:display specsn
WAP>?
USAGE:
    display ssh authentication-type
OPTIONS:
    mode:0 is password mode, 1 is password-publickey mode
WAP>?
USAGE: 
  display ssh-hostkey fingerprint
WAP>?
USAGE:
     display startup info  -- show startup information in ring buffer.
WAP>?
display swm bootstate
WAP>?
display swm state
WAP>?
display sysinfo  -- get cpu ,memory condition and time
WAP>?
USAGE:
     display syslog -- get syslog enable and level
WAP>?
display system info
WAP>?
display timeout
WAP>?
USAGE:
    display timer type {value}
OPTIONS:
    type: 5:dst
WAP>?
USAGE: display tr069 info -- get tr069 server info
WAP>?
USAGE:
     display usb devList -- get usb device list which can be used!
WAP>?
display user device [ip ipAddress | mac macAddress]
WAP>?
USAGE:
     display version: get hardware version, software version, bios verison of board
WAP>?
USAGE:
    display voicelinetest portnum {[1,8] | all}
OPTIONS:
    portnum : value range{[1,8] | all}
WAP>?
display voip dsp jbdata port {[0,7]} channel {[0,3] |all}
WAP>?
display voip dsp para diagnose state
WAP>?
display voip dsp para diagnose statistics port {[0,7]}
WAP>?
display voip dsp tonedetect port {[0,7]} channel {[0,3] |all} dir {0:up,1:down,2:all}
WAP>?
display voip dtmfdiag state
WAP>?
display voip dtmfsimpara paratype {[0,1]}
WAP>?
display voip info
WAP>?
display voip rightflag port {[0,7]}
WAP>?
display voip ring info port {[0,7]}
WAP>?
display voip rtpdiag port {[0,7]} dir {0:tx,1:rx,2:all}
WAP>?
display voip tone info port {[0,7]}
WAP>?
display wan layer all
WAP>?
display waninfo
display waninfo all
display waninfo all detail
WAP>?
display waninfo all
display waninfo all detail
WAP>?
display waninfo all detail
WAP>?
USAGE:
     display wanmac -- get wan mac of board
WAP>?
display wifi ap
WAP>?
display wifi associate
WAP>?
USAGE: display wifi calibrate mode
WAP>?
display wifi filter index [1-8]
WAP>?
display wifi information
WAP>?
display wifi multicast
WAP>?
display wifi neighbor
WAP>?
USAGE: get wifi pa type
WAP>?
display wifi radio
WAP>?
display wifi smartant status wifichip {0|1}
WAP>?
display wifichip
WAP>?
display wlan config wlaninst {wlaninst}
OPTIONS: 
    wlaninst: wlaninst ,value range [1-8]
WAP>?
display wlan staevent
WAP>?
display wlan stainfo [mac {mac}]
OPTIONS: 
    mac: sta mac
WAP>?
USAGE:
     display wlanmac -- display wlan mac address
WAP>?
display zsp version
WAP>?
USAGE:
     firewall log [ chain [string] | chain [string] rule [int] ]
WAP>?
flush dhcp server pool index [poolIndex]
WAP>?
flush dnsserver cache
WAP>?
get ap retrans wandeviceinst [1]
WAP>?
get battery alarm status
WAP>?
get ip conntrack
WAP>?
get mac agingtime
WAP>?
get ont oamfrequency
WAP>?
Get opm switch
WAP>?
USAGE: get optic debug info
WAP>?
USAGE: get optic par info 
WAP>?
USAGE: get optic phy type
WAP>?
get optic txmode
WAP>?
get poncnt upgemport
WAP>?
get port config portid [1-5]
WAP>?
get port isolate
WAP>?
get rogue status
WAP>?
get testself
WAP>?
USAGE:
    get wifi atm band {band}
OPTIONS:
    para: band   -- a means 5G, b means 2G

WAP>?
get wifi para laninst [1]
WAP>?
get wlan advance laninst [1] wlaninst [1-4]|[1-8]
WAP>?
get wlan associated laninst [1] wlaninst [1-4]|[1-8] deviceinst {deviceinstid}
WAP>?
get wlan basic laninst [1] wlaninst [1-4]|[1-8]
WAP>?
USAGE:
    get wlan enable laninst 1
WAP>?
get wlan isolate wlaninst {wlaninst}
OPTIONS: 
    wlaninst: wlaninst ,value range [1-8]
WAP>?
get wlan stats laninst [1] wlaninst [1-4]|[1-8]
WAP>?
get wlan wps laninst [1] wlaninst [1-4]|[1-8]
WAP>?
ifconfig
WAP>?
igmp add mirror filter ip ipaddr
WAP>?
igmp clear statistics
WAP>?
igmp del mirror filter ip ipaddr
WAP>?
igmp disable
WAP>?
igmp enable [ proxy switch | snooping switch | version igmpversion | robustness robustness | query-interval interval | query-response-interval interval | last-member-interval interval | last-member-count count | last-member-response-interval interval | startup-query-interval interval | startup-query-count count | unsolicited-report-interval interval ]*
WAP>?
igmp get debug switch [ para1 [int] | para1 [int] para2 [int] ]
WAP>?
igmp get flow info
WAP>?
igmp get global cfg
WAP>?
igmp get iptv
WAP>?
igmp get mirror filter ip
WAP>?
igmp get multilmac
WAP>?
igmp get port multicast config
WAP>?
igmp get statistics
WAP>?
igmp set debug switch enable [0,1] para [int]
WAP>?
ip -6 neigh
WAP>?
ip -6 route
WAP>?
ip -6 rule
WAP>?
ip interface config interface interface { status status | ipv4status ipv4status | ipv6status ipv6status | mtu mtu } *
WAP>?
ip neigh
WAP>?
ip route
ip route show
WAP>?
[Command]:ip route show [table table_name|table_id]
WAP>?
ip rule
WAP>?
USAGE:jvmcmd map histo
WAP>?
USAGE:jvmcmd stack trace
WAP>?
USAGE:
     jvmcmd stat option {value} 
OPTIONS:
     option: 1   class             Statistics on the behavior of the class loader.
             2   compiler          Statistics of the behavior of the HotSpot Just-in-Time compiler.
             3   gc                Statistics of the behavior of the garbage collected heap.
             4   gccapacity        Statistics of the capacities of the generations and their corresponding spaces.
             5   gccause           Summary of garbage collection statistics (same as -gcutil), with the cause of the last and current (if applicable) garbage collection events.
             6   gcmetacapacity    Statistics of the sizes of the permanent generation.
             7   gcnew             Statistics of the behavior of the new generation.
             8   gcnewcapacity     Statistics of the sizes of the new generations and its corresponding spaces.
             9   gcold             Statistics of the behavior of the old and permanent generations.
             10  gcoldcapacity     Statistics of the sizes of the old generation.
             11  gcutil            Summary of garbage collection statistics.
             12  printcompilation  HotSpot compilation method statistics.
WAP>?
lan mac filter add mac macaddress
WAP>?
lan mac filter delete mac macaddress
WAP>?
lan mac filter disable
WAP>?
lan mac filter enable [policy policy]
WAP>?
lan mac filter flush
WAP>?
load fem par by {tftp|sftp} [svrip {ip addr}] [par_name {file name}] [user {user name}] [pwd {password}] [port {port}]
WAP>?
load pack by {https|sftp|ftp|tftp|http} svrip {ip addr} remotefile {file name} [user {user name}] [pwd {password}] [port {port}]. Attention: Only some boards support ftp|tftp|http service
WAP>?
load ssh-pubkey by {tftp|ftp|https|sftp} svrip {ip addr} remotefile {file name} [user {user name}] [pwd {password}] [port {port}]
WAP>?
logout
WAP>?
macaddress timer value[10-86400, 0:no-aging]
WAP>?
USAGE:
     make ssh hostkey type {value} bits {value}
OPTIONS:
     type Type of key to generate. One of: rsa/ecdsa
     bits Key size in bits, RSA should be a multiple of 8 between 2048 and 4096
           ECDSA has sizes 256 384 521 
WAP>?
USAGE:
     mid get  -- show mid switch information.
WAP>?
USAGE:
     mid off  -- turn all mid switch off.
WAP>?
USAGE:
     mid set mid {value} flag {value} [pidmask {value}] [nextboot {value}]
WAP>?
napt cli para [int]
WAP>?
netstat -na
WAP>?
nslookup domain domain [ server server | interface interface | repnum repnum ] *
WAP>?
[Command]:print all lmc event log
WAP>?
[Command]:oamcmd clear log
WAP>?
[Usage]:
oamcmd debug debugtype {[msg|0]|[trace|1][savemsg|2]|[alarm|3]} debugswitch {[on|1]|[off|0]} [llid [llid]]
msg|0-oam msg print, trace|1-trace print, savemsg|2-save oam msg, alarm|3-alarm debug
off|0-debug off, on|1-debug on
llid:llid index (1-8)
example: oamcmd debug debugtype msg debugswitch on
WAP>?
[Command]:oamcmd error log
WAP>?
[Usage]:oamcmd pdt show log
WAP>?
[Usage]:oamcmd show flow portid [portid] 
portid---the id of eth port
WAP>?
[Command]:print all saved log
WAP>?
[Usage]:
omcicmd alarm show meid [me-id] instid [inst-id]
me-id: 65535 show all alarm
inst-id: 65535 show inst alarm
WAP>?
[Command]:clear all omci & error log [Usage]: show error log portid [int]
WAP>?
[Usage]:omcicmd debug debugtype {[msg|0]|[trace|1]|[savemsg|2]|[noprtmsg|3]} debugswitch {[off|0]|[on|1]}
msg|0-omci_print trace|1-trace_print savemsg|2-omci_save noprtmsg|3-not_print_omci_msg
off|0-disable on|1-enable
WAP>?
[Command]:show error log [Usage]: show error log portid [int]
WAP>?
[Usage]:omcicmd mib show meid [me-id] instid [inst-id] 
me-id: 65535 show all me and inst info 
inst-id: 65535 show all inst info
WAP>?
[Usage]:omcicmd pdt show log
WAP>?
[Usage]:omcicmd pm show meid [me-id] instid [inst-id] portid [int]
me-id: 65535 show all me and inst info
inst-id: 65535 show all inst info
WAP>?
[Usage]:omcicmd show flow type [typeid]
0:All
1:AniportObj Cfg
2:UniportObj Cfg
3:GemportObj Cfg
4:FlowObj Cfg
5:All the flow ID
6:All the flow entry
WAP>?
[Command]:print all saved log [Usage]: print all saved log portid [int]
WAP>?
[Command]:omcicmd show qos
WAP>?
osgicmd debug level [0:CLOSE, 1:Error, 2:Warning, 3:Info, 4:Debug]
WAP>?
osgicmd get debug [bundleid [-1:all,bundleid]]
WAP>?
osgicmd plugin permission bundleid [int]
WAP>?
osgicmd set debug bundleid [-1:all,bundleid] switch [0:off,1:on]
WAP>?
osgicmd show bundleresource
WAP>?
osgicmd show bundlestate
WAP>?
Usage: 
ping [OPTIONS] HOST

Send ICMP ECHO_REQUEST packets to network hosts

Options:
        -4,-6           Force IP or IPv6 name resolution
        -F              Set the don't fragment bit
        -c CNT          Send only CNT pings
        -s SIZE         Send SIZE data bytes in packets (default:56)
	-t TTL          Set TTL
        -I IFACE/IP     Use interface or IP address as source
        -W SEC          Seconds to wait for the first response (default:10)
                        (after all -c CNT packets are sent)
        -w SEC          Seconds until ping exits (default:infinite)
                        (can exit earlier with -c CNT)
        -q              Quiet, only displays output at start
                        and when finished
	-p              Pattern to use for payload
        -i INTERVAL     Interval
WAP>?
[Usage]: plugcmd show state
WAP>?
[Usage]: plugcmd start name [name]
OPTIONS:
    name: plugin name;
    
WAP>?
[Usage]: plugcmd stop name [name]
OPTIONS:
    name: plugin name;
    
WAP>?
[Usage]: plugcmd uninstall name [name]
OPTIONS:
    name: plugin name;
    
WAP>?
[Usage]:plugincmd debug type {type} mid {mid} level {level}
[Note]:
	type:  plugin type;
	mid:   ID of the module;
	level: debug level;
WAP>?
ppp interface config interface interface { status status | ipcpstatus ipcpstatus | ipv6cpstatus ipv6cpstatus | mru mru } *
WAP>?
pppoe client attach interface intfname
WAP>?
pppoe client detach interface intfname
WAP>?
qoscfg get
WAP>?
quit
WAP>?
USAGE
     reset -- reset board
WAP>?
restore backup [file {value}]
WAP>?
restore manufactory
WAP>?
route get default ----- get the default route
WAP>?
Save data.
WAP>?
Save log from buff to flash immediately, example: save log
WAP>?
session cli mode [0:to cpu,1:to session,2:to router] tunnel [0:none,1:tunnel]
WAP>?
USAGE:
    set ap retrans wandeviceinst [1] enable {0/1}
WAP>?
USAGE:
    set apssh mac {mac addr} enable {0/1}
WAP>?
USAGE:
    set aptelnet mac {mac addr} enable {0/1}
WAP>?
USAGE:
     set cwmp debug level {value} [host {value}] [port {value}] 
OPTIONS:
     level:  0  Close debug info.
             1  Open receive info.
             2  Open send info.
             4  Open debug info.
             8  Open warnning info.
             16 Open error info.
     host :  server host name, should be less than 32;
     port :  server port
WAP>?
USAGE:
    set ethportmirror sourceport {value} destport {value} mirrordate {0:out/1:in/2:all} enable {0/1}
OPTIONS:
    sourceport  : value range [1-8:eth/9:cpu/10:pon/edge onu:20-35/ssid0-ssid15:100-115]
    destport    : value range [1-8] 
    mirrordate  : {0:out/1:in/2:all}
    enable      : {0/1}
WAP>?
USAGE:
    set iaccess speed period [2: 60]
WAP>?
set led switch [on/off/recovery/flash]
WAP>?
USEAGE: set microwave ctrl mode [0~2] scanInterval [...] scanCount [...]
OPTIONS:
    mode 0 means Disable 1 means InterferenceTrigger 2 means CycleCheck
    scanInterval means microwave-interference scan interval
    scanCount means the count of non-microwave-interference. if reaches to it, our device will stop scan.
WAP>?
[Usage]: set NCE url {url}
WAP>?
set newparentalctrl
set newparentalctrl stats
WAP>?
set newparentalctrl stats type [type] period [period]
WAP>?
[Command]: set opticdata print
[Command]: set opticdata print {[on]|[off]}
WAP>?
set port isolate switch { enable | enable ontoflash | disable | disable ontoflash | undef }
WAP>?
USAGE:
    set portmirror sourceport {value} destport {value} mirrordata {0:out/1:in/2:all} enable {0/1}
OPTIONS:
    sourceport  : value range [1-5:eth/9:cpu/10:pon/edge onu:20-35/ssid0-ssid15:100-115]
    destport    : value range [1-5] 
    mirrordata  : {0:out/1:in/2:all}
    enable      : {0/1}
WAP>?
USAGE:
     set ringchk debug value[int] 
OPTIONS:
     debug:  0  disables the debugging function.
             1  enables the debugging function.
             2  disables the ringchk function on the port.
             3  enables the ringchk function on the port.
WAP>?
USAGE:set ssid index[1-4] | [1-8] [para{value}] 
OPTIONS: 
    name--SSID name
    visible--1 means Advertisement enabled,0 means disabled
    security--None, WEP-128 | WEP-64, WPA2-Personal | WPA-Personal, WPA-WPA2-Personal, WPA-Enterprise, WPA2-Enterprise, WPA-WPA2-Enterprise
    password--password
WAP>?
set timeout
WAP>?
set userpasswd
WAP>?
USAGE:
	set voice announcement switch {[0,2]}
OPTIONS:
	switch : { 0:disable, 1:temporarily enable, 2:enable }
WAP>?
USAGE:
	set voice dtmfmethod mode {[0,2]} {mgno [0,1]}
OPTIONS:
	mode : {0:InBand, 1:RFC2833, 2:SIPInfo}
WAP>?
USAGE:
    set voicedebug switch {on|off}
OPTIONS:
    switch       : {on:enable,off:disable}
WAP>?
USAGE:
    set voicedsploop enable {[0,1]} type {0:TDM,1:IP} port {[1,8]}
OPTIONS:
    enable  : {0:disable,1:enable}
    type    : {0:TDM,1:IP}
    port    : {[1,8]}
WAP>?
USAGE:
    set voicelinetest portnum {[1,8] | all}
OPTIONS:
    portnum : value range{[1,8] | all}
WAP>?
USAGE:
    set voiceportloop enable {[0,1]} type {0:TDM,1:IP} port {[1,8]}
OPTIONS:
    enable  : {0:disable,1:enable}
    type    : {0:TDM,1:IP}
    port    : {[1,8]}
WAP>?
USAGE:
    set VoiceSignalingPrint switch {on|off}
OPTIONS:
    switch  : {on:enable,off:disable}
WAP>?
USAGE:
	set voip clip port{[0,7]} mode{[0,4]}
OPTIONS:
	mode : {0:Sdmf-fsk,1:Mdmf-fsk,2:Dtmf,3:R1.5,4:etsi}
WAP>?
USAGE:
	set voip dsptemplate port {[0,7]} templatename {[0,4]}
OPTIONS:
	templatename : {0:highspeed_modem,1:lowspeed_modem,2:staticjbmode,3:alarmdevice,4:clear templatename}
WAP>?
set voip dtmfdebug switch {[0:disable, 1:enable]} printlevel {[0,2]} autostop {[10,720]}
WAP>?
set voip dtmfdetfilter port {[0,7]} value {[0,3400]}
WAP>?
set voip dtmfdiag start port {[0,7]} mode {0:dial, 1:voice, 2:manualsingle, 3:manualloop}
WAP>?
set voip dtmfdiag stop
WAP>?
set voip dtmfsimpara reset {[0,1]} paratype {[0,1]} detectmode {[0,3]} loweradjust {[-200,600]} negativetwistadjust {[-100,100]} positivetwistadjust {[-100,100]} snr1250_1800adjust {[-200,200]} snr1800_4000adjust {[-200,200]} snr900_1250adjust {[-200,200]} snradjust {[-200,200]} snrdialadjust {[-200,200]} snrdialup_900adjust {[-200,200]}
WAP>?
set voip dtmfsimu start mode{0:general simulation, 1:shift point simulation, 2:missing number simulation} printflag [0,7] analysislevel [0,2]
WAP>?
set voip dtmfsimu stop
WAP>?
set voip fax T38 enable {0:disable,1:enable} {mgno [0,1]}
WAP>?
set voip faxmodem switch mode {0:selfswitch, 1:negotiation} {mgno [0,1]}
WAP>?
set voip highpassfilter port{[0,7]} enable {0:disable,1:enable}
WAP>?
USAGE:
	set voip portgain port {[0,7]} recvgain {[-12, 0]} {sendgain [-6, 6]}
OPTIONS:
	gainvalue : the step is 0.5
WAP>?
set voip rtpdiag port {[0,7]} switch {on|off} tx-threshold {[10,200]} rx-threshold {[10,200]} stoptime {[1,48]}
WAP>?
set voip sipprofile index [index] value [value] {mgno [0,1]}
WAP>?
USAGE:
    set wifi ap optimize band {band}
OPTIONS:
    band:    a means 5G ,b means 2G
WAP>?
USAGE:
    set wifi atm band {band} period {value}
OPTIONS:
    para: band   -- a means 5G, b means 2G
    para: period -- default 10s

WAP>?
USAGE:
    set wifi expert band {band} [bandwidth {value}] [guardinterval {value}] [dtim {value}] [nss {value}] [mcs {value}] [pmf {value}] [occac {value}] [txbf {value}] [scs {value}] [beaconperiod {value}]
OPTIONS:
    band:    a means 5G ,b means 2G
    bandwidth:  20M/40M/Auto for 2.4G, 80M/40M/20M/Auto for 5G
    guardinterval: short means 400ns,long means 800ns, auto means auto-adapt.
    dtim:  DTIM period, value range [1-255]
    nss:  the maximum number of spatial streams, value range [1-4]
    mcs:  the current MCS rate, 0 means auto
    pmf:  Protected Management Frames(802.11w), 0 means disabled, 1 means enable
    occac:  Off Channel CAC,  0 means disable, 1 means enable 
    txbf:  Tx Beamforming, 0 means disable, 1 means enable 
    scs:  Smart channel selection, 0 means disable, 1 means enable
    beaconperiod : Beacon Interval, value range [20-1000]

WAP>?
set wifi filter index [1-8] mode [0-2]
WAP>?
set wifi para laninst [1] [para {value}]
OPTIONS:
	para: txpower
	value: 10/20/30/40/50/60/80
WAP>?
USAGE:
    set wifi radio band {band} [enable {value}] [channel {value}]
OPTIONS:
    band:    a means 5G ,b means 2G
    enable:  0 means disable ,1 means enable
    channel: Specifies the ID of a 2.4G channel or 5G channel. If the value is auto, the ONT automatically selects a channel
WAP>?
USAGE:set wlan isolate wlaninst {wlaninst} [enable {value}] 
OPTIONS: 
    wlaninst: wlaninst ,value range [1-8]
    enable--1 means enable,0 means disable
WAP>?
USAGE:
    set wlan staboost band {band} [add {stamac} during {times}] [del {stamac}] [show all]
OPTIONS:
    para: band   -- a means 5G, b means 2G
          add    -- Add StaMac
          during -- Duration times
          del    -- Del StaMac
          show   -- All Boost Stainfo

WAP>?
USAGE:
     sfwd port statistics oper {start|stop|clear} -- start|stop|clear the port RX/TX packets statistics.
WAP>?
USAGE:
    ssh authentication-type mode {value} 
OPTIONS:
    mode:0 is password mode, 1 is password-publickey mode
WAP>?
USAGE:
     ssh remote ip {ip} port {port} -- ssh to remote ip address.
WAP>?
USAGE:
     stats clear protoc {ProctocolName} [mod {ModuleType}] [client {Client}]
OPTIONS:     
     ProctocolName:igmp|arp|dhcpd|dhcpc|pppoec|dhcp6c|dhcp6s|icmpv6|unknown
     ModuleType:ker|userapp|all
     Client:wanX|all,example:wan1,wan2
WAP>?
USAGE:
     stats display protoc {ProctocolName} [mod {ModuleType}] [client {Client}]
OPTIONS:     
     ProctocolName:igmp|arp|dhcpd|dhcpc|pppoec|dhcp6c|dhcp6s|icmpv6|unknown
     ModuleType:ker|userapp|all
     Client:wanX|all,example:wan1,wan2
WAP>?
su
WAP>?
USAGE:
     telnet remote ip {ip} port {port} -- telnet to remote ip address.
WAP>?
USAGE:test apdev.
WAP>?
USAGE:test tr069 inform end to display the result.
WAP>?
USAGE:test tr069 inform start to send tr069 inform.
WAP>?
Usage: 
traceroute [-m MAXTTL | -p PORT | -q PROBES | -s SRC_IP | -t TOS | -w WAIT_SEC | -i IFACE | -z PAUSE_MSEC | para ] host [ packetlen ]

Trace the route to HOST

Options:
        -m      Max time-to-live (max number of hops)
        -p      Base UDP port number used in probes (default 33434)
        -q      Number of probes per TTL (default 3)
        -s      IP address to use as the source address
        -t      Type-of-service in collector packets (default 0)
        -w      Time in seconds to wait for a response (default 3)
        -i      Interface
        -z      pause time
        para    Other suffix parameter(-F | -I | -l | -d | -n | -r | -v | -4,-6)
WAP>?
trafficdump [location {input,output,drop,forward} | version {v4,v6} | -telnet {enable,disable} | +mac {enable,disable} | ip {address} | protocol {tcp,udp,icmp,igmp,arp} | tcpportlist {int,int,..} | udpportlist {int,int,..} | interface {interfacelist}] 
WAP>?
USAGE:
     udm clear log  -- clear udm debug log usage.
WAP>?
USAGE:
     udm show log  -- show udm debug log usage.
WAP>?
undo debugging dsp diagnose port {[0,7]}
WAP>?
undo debugging dsp para diagnose port {[0,7]}
WAP>?
undo debugging dsp record
WAP>?
undo debugging dsp t38diag port {[0,7]}
WAP>?
USAGE:
     undo firewall log [ chain [string] | chain [string] rule [int] ]
WAP>?
voice net diagnose start
WAP>?
voice remote diagnose server set wanname {[portname]} localtransport [int] remoteip [ip] remotetransport [int]
WAP>?
voice remote diagnose set enable {[0,1]} port {[0,7]} timerautostop {[1,43200]} diagtype {all|signal|media}
WAP>?
vspa clear rtp statistics port {[0,7]}
WAP>?
vspa debug module {[0,999]} cmd {[0,999]} subcmd {[0,999]} 
WAP>?
vspa display conference info
WAP>?
vspa display digitmap info
WAP>?
vspa display dsp running info index {[0,3]} mode {0:all, 1:summary}
WAP>?
vspa display dsp state
WAP>?
vspa display dsp template info
WAP>?
vspa display mg if state mg {[0,1]}
WAP>?
vspa display mg info
WAP>?
vspa display online user info
WAP>?
vspa display port status
WAP>?
vspa display profilebody info
WAP>?
vspa display rtp statistics port {[0,7]}
WAP>?
vspa display service log
WAP>?
vspa display signal scene info mg {[0,1]} scene [scenename]
WAP>?
vspa display signal scene list
WAP>?
vspa display user call state port {[0,7]}
WAP>?
vspa display user status
WAP>?
vspa reset mg {[0,1]} type {0:service restored,1:cold start,2:warm start,3:capabilities change}
WAP>?
vspa shutdown mg num {[0,1]} type {0:gracefully close,1:forced close}
WAP>?
USAGE:
     wap list [format {0|1}] [path {value}] -- show directorys and files information.
WAP>?
USAGE:
     wap ps  -- show process and thread information.
WAP>?
wap top
WAP>?
wifi del fem calibration
WAP>?
wifi del fem par
WAP>?
wifi smartant set [wifichip {0|1 (2.4g|5g)}] [switch {0|1}] [mode {auto|OMNI_fix|SEPA_fix}] [chainmask {10|5|9|6}]
