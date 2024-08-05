WAP>su
success!
SU_WAP>?
acc get accesslimit
SU_WAP>?
add wifi filter index [1-8] mac {mac}
SU_WAP>?
[Command]: amp add policy-stats pon
[Usage]: amp add policy-stats pon vlan [1:4095] [pri [0:7]]
SU_WAP>?
[Command]: amp add policy-stats port
[Usage]: amp add policy-stats port id [portid] vlan [1:4095] [pri [0:7]]
SU_WAP>?
[Command]: amp add stats gemport
[Usage]: amp add stats gemport id [1:4094]
SU_WAP>?
[Command]: amp clear policy-stats pon
[Usage]: amp clear policy-stats pon
SU_WAP>?
[Command]: amp clear policy-stats port
[Usage]: amp clear policy-stats port [id [portid]]
amp clear policy-stats port: Clear all ports stats.
amp clear policy-stats port id [portid]: Clear the spec port stats.
SU_WAP>?
[Command]: amp clear stats gemport
[Usage]: amp clear stats gemport [id [1:4094]]
amp clear stats gemport: Clear all gemports stats.
amp clear stats gemport id [1:4094]: Clear the spec gemport stats.
SU_WAP>?
[Command]: amp del policy-stats pon
[Usage]: amp del policy-stats pon vlan [1:4095] [pri [0:7]]
SU_WAP>?
[Command]: amp del policy-stats port
[Usage]: amp del policy-stats port id [portid] vlan [1:4095] [pri [0:7]]
SU_WAP>?
[Command]: amp del stats gemport
[Usage]: amp del stats gemport id [1:4094]
SU_WAP>?
[Usage]:
ampcmd show emac stat {0|1|2|3|4}
0: emac message queue
1: emac up traffic
2: emac down traffic
3: kernel oam
4: config
SU_WAP>?
[Usage]:ampcmd show flow all
SU_WAP>?
[Usage]:ampcmd show flow index {index}
SU_WAP>?
[Usage]:ampcmd show log
SU_WAP>?
[Usage]:ampcmd trace all {on|off}
SU_WAP>?
[Usage]:ampcmd trace cli {on|off}
SU_WAP>?
[Usage]:ampcmd trace dpoe {on|off}
SU_WAP>?
[Usage]:ampcmd trace drv {on|off}
SU_WAP>?
[Usage]:ampcmd trace emac {on|off}
SU_WAP>?
[Usage]:ampcmd trace emap {on|off}
SU_WAP>?
[Usage]:ampcmd trace eth {on|off}
SU_WAP>?
[Usage]:ampcmd trace gmac {on|off}
SU_WAP>?
[Usage]:ampcmd trace gmap {on|off}
SU_WAP>?
[Usage]:ampcmd trace onu {on|off}
SU_WAP>?
[Usage]:ampcmd trace optic {on|off}
SU_WAP>?
[Usage]:ampcmd trace qos {on|off}
SU_WAP>?
[Usage]:appmcmd debug switch [0:off,1:on]
SU_WAP>?
[Usage]:appmcmd regplat
SU_WAP>?
[Usage]:appmcmd show type [type-id]
[Note for type]:
	type-1: show local info.;
	type-2: show plug-in center info.;
	type-3: show cloud platform info.;
SU_WAP>?
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
SU_WAP>?
bbsp add policy-stats btv ip { ipaddr [ vlan [int] ] [ port [int] | mac [string] | userip [string] ] }
SU_WAP>?
bbsp clear policy-stats btv all
SU_WAP>?
bbsp clear policy-stats wan id [wanid | all]
SU_WAP>?
bbsp del policy-stats btv ip { ipaddr [ vlan [int] ] [ port [int] ] }
SU_WAP>?
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
SU_WAP>?
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
SU_WAP>?
Usage: 
Broadband debug ethoam    {on | off | pkt NUMBER}
                ker_route
                lswadp
                ptpdrv  {all | eth | pon | wifi | radio | igmp | icmp | arp | dhcp} {on | off | pkt NUMBER}
                pkt { {all | off} {PROTOCOL | EXPRESSION | DEVICE} }

SU_WAP>?
Usage: 
Broadband display ethoam
                  ker_ethoam
                  ptpdrv {dbm | stat | rate}
                  soc {cnt | clrcnt | gpon | ifc | ofc | sfc | bridge | eth | l3 | queue | flow | l2 | dscptable | macfilter | car | btv | bc VLANID}
                  l2mac
                  wlwan 

SU_WAP>?
btv start period-stats ip ipaddr [ vlan vlan ] { port port | mac mac | userip userip } interval interval duration duration
SU_WAP>?
btv stop period-stats
SU_WAP>?
USAGE:check security config and display the result.
SU_WAP>?
chipdebug
chipdebug clearall
chipdebug soc drop
chipdebug soc rx
chipdebug soc tx
SU_WAP>?
[Usage]:chipdebug clearall
SU_WAP>?
[Usage]:chipdebug soc drop
SU_WAP>?
[Usage]:chipdebug soc rx
SU_WAP>?
[Usage]:chipdebug soc tx
SU_WAP>?
[Command]: clear amp pq-stats
[Usage]: clear amp pq-stats tcont-llid [id] queue [queueid]
SU_WAP>?
USAGE:
     clear lastword -- clean lastowrd records.
SU_WAP>?
[Command]: clear pon statistics
SU_WAP>?
clear poncnt dnstatistic [portid {id}]
SU_WAP>?
clear poncnt gemport upstatistic gemportid {gemportid} [portid {id}]
SU_WAP>?
clear poncnt upstatistic [portid {id}]
SU_WAP>?
[Command]: clear port statistics portid
[Usage]: clear port statistics portid [portid]
SU_WAP>?
clear reogue flag
SU_WAP>?
USAGE:
     clear sfwd drop statistics -- Clear the forward drop packets statistics.
SU_WAP>?
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
SU_WAP>?
USAGE:
     component delete all  -- delete all softwore component pack. it take effects after reboot.
SU_WAP>?
[Usage]: ctrgcmd cloud method {method} 
OPTIONS:
    method: GetAll, GetPlat;
SU_WAP>?
[Usage]: ctrgcmd debug type {type-id} [bus {bus-name}]
OPTIONS:
    type: 1 start dbus-monitor for debug.;
          2 show dbus-monitor debug info.;
          3 clear dbus-monitor process.;
    bus: bus name for dbus-monitor,optional parameter.;
SU_WAP>?
[Usage]: ctrgcmd frmwork method {method} [name {name}]
OPTIONS:
    method:GetAll Pause;
    name:frmwork stop time (0 - 65535min),optional parameter.;
SU_WAP>?
[Usage]: ctrgcmd logread
SU_WAP>?
[Usage]: ctrgcmd plugin method {method} [name {name}]
OPTIONS:
    method: List, Stop, Run, Uninstall.;
    name: plugin name,optional parameter.;
SU_WAP>?
[Usage]: ctrgcmd send bus {bus-name} obj {object-name} method {method} [intf {interface-name}]
OPTIONS:
    bus: bus name.;
    obj: object name.;
    method: method name.;
    intf: interface name,optional parameter.;
SU_WAP>?
[Usage]: ctrgcmd show type {type-id}
OPTIONS:
    type: 1 show history framework run log.;
          2 show current framework run log.;
          3 show framework start log.;
          4 show saf version.;
          5 show saf info.;
          6 show package versions.;
SU_WAP>?
debug dsp down msg
SU_WAP>?
debug dsp msg
SU_WAP>?
debug dsp up msg
SU_WAP>?
debug ifm info [0|1] error [0|1] step [0|1] pkt [0|1]
SU_WAP>?
debug qoscfg [ info swt1 | step swt2 | error swt3 ]*
SU_WAP>?
debug rtp stack
SU_WAP>?
debug sample mediastar
SU_WAP>?
debugging dsp diagnose port {[0,7]} type {1:tonedetect,2:jbdata,3:all} mode {0:once,1:over}
SU_WAP>?
debugging dsp para diagnose port {[0,7]}
SU_WAP>?
debugging dsp record autostop {[1,1440]}
SU_WAP>?
debugging dsp t38diag port {[0,7]}
SU_WAP>?
del wifi filter index [1-8] mac {mac}
SU_WAP>?
dhcp client attach interface intfname
SU_WAP>?
dhcp client detach interface intfname
SU_WAP>?
dhcp client6 attach interface intfname
SU_WAP>?
dhcp client6 detach interface intfname
SU_WAP>?
dhcp server pool config index index [gateway ip] [netmask netmask] [start start_ip] [end end_ip] [dns dns_ip]
SU_WAP>?
dhcp server pool disable index [poolIndex]
SU_WAP>?
dhcp server pool enable index [poolIndex]
SU_WAP>?
dhcp server pool lease config index index leasetime time
SU_WAP>?
dhcp server pool option add poolindex poolindex tag tag value value
SU_WAP>?
dhcp server pool option del poolindex poolindex index index
SU_WAP>?
dhcp server pool option flush poolindex poolindex
SU_WAP>?
dhcp server pool restart
SU_WAP>?
diagnose
SU_WAP>?
display access mode
SU_WAP>?
display access system info
SU_WAP>?
display aclservicesrule
SU_WAP>?
[Command]: display amp policy-stats pon
SU_WAP>?
[Command]: display amp policy-stats port
[Usage]: display amp policy-stats port [id [portid]]
display amp policy-stats port: display all ports stats.
display amp policy-stats port id [portid]: display the spec port stats.
SU_WAP>?
[Command]: display amp pq-stats 
[Usage]: display amp pq-stats tcont-llid [id] queue [queueid]
SU_WAP>?
[Command]: display amp stats gemport
[Usage]: display amp stats gemport [id [1:4094]]
display amp stats gemport: Display all gemports stats.
display amp stats gemport id [1:4094]: Display the spec gemport stats.
SU_WAP>?
display apmChipStatus
SU_WAP>?
USAGE:display appcert info -- display app root certificate info
SU_WAP>?
display backup file list
SU_WAP>?
USAGE:
     display batteryStatus -- get available capacity of battery
SU_WAP>?
[Command]:display bbsp log
SU_WAP>?
display bbsp stats btv ip { ipaddr [ port [int] ] | all }
SU_WAP>?
display bbsp stats wan id {wanid | all}
SU_WAP>?
display bms
display bmsxml crc
SU_WAP>?
USAGE:
     display bmsxml crc  -- show bmsxml crc information.
SU_WAP>?
USAGE:
     display board-temperatures -- display board-temperatures including Bob Soc Wifi RF
SU_WAP>?
USAGE:
     display board2Item -- get board2 item of board
SU_WAP>?
USAGE:
     display boardItem -- get board item of board
SU_WAP>?
USAGE:
     display boardItem -- get bom item of board
SU_WAP>?
display broadband info
SU_WAP>?
USAGE:display childcert info -- display child certificate info
SU_WAP>?
display connection
display connection all
SU_WAP>?
display connection all
SU_WAP>?
USAGE: display cpu info
SU_WAP>?
display current-configuration [grep {value}]
SU_WAP>?
USAGE:
      display cwmp debug ---- display cwmp debug level
SU_WAP>?
USAGE: display the device register acs status
SU_WAP>?
display ddns info interface {intfname}
SU_WAP>?
display debug info dhcp6c wanname [wanname]
SU_WAP>?
display debug info dhcp6s
SU_WAP>?
display debug info pppoev6
SU_WAP>?
display debug info ra wanname [wanname]
SU_WAP>?
USAGE:
     display debuglog info  -- show all debuglog information.
SU_WAP>?
display debugwifilog info
SU_WAP>?
USAGE:display device-cert info
SU_WAP>?
USAGE:
     display deviceInfo -- get device info of board, such as upport mode, release time, model name, and so on
SU_WAP>?
display dhcp client
display dhcp client all
display dhcp client6
display dhcp client6 all
SU_WAP>?
display dhcp client {all | interface intfname}
SU_WAP>?
display dhcp client6
display dhcp client6 all
SU_WAP>?
display dhcp client6 {all | interface intfname}
SU_WAP>?
display dhcp server pool
display dhcp server pool all
display dhcp server pool option
SU_WAP>?
display dhcp server pool {all | index poolindex}
SU_WAP>?
display dhcp server pool option poolindex poolindex
SU_WAP>?
display dhcp server static
SU_WAP>?
display dhcp server user
display dhcp server user all
SU_WAP>?
display dhcp server user {all | index userIndex}
SU_WAP>?
display dhcp_em result
SU_WAP>?
display diagnose info
SU_WAP>?
display dns proxy info interface intfname
SU_WAP>?
display dnsserver static domain
SU_WAP>?
display dpst
display dpst all
SU_WAP>?
[Command]:display dpst all
SU_WAP>?
display dsp channel para
SU_WAP>?
display dsp channel running status
SU_WAP>?
display dsp channel status
SU_WAP>?
display dsp chip stat
SU_WAP>?
display dsp codec status
SU_WAP>?
display dsp interrupt stat
SU_WAP>?
[Command]: display dynamic route [Usage]: display dynamic route [proto {rip}]
SU_WAP>?
display eaiinfo
SU_WAP>?
USAGE:display edge_ont info onuid [0-15, 255]
SU_WAP>?
display epon ont info 
SU_WAP>?
display ethoam ma info mdins [int] mains [int]
SU_WAP>?
display ethoam md info mdins [int]
SU_WAP>?
display ethoam mep info mdins[int] mains [int] mepins [int]
SU_WAP>?
display ethoam mep perf mdinst [int] mainst [int] mepinst [int]
SU_WAP>?
display femPar info
SU_WAP>?
display femPar version
SU_WAP>?
display ffwd table type all
SU_WAP>?
display file
SU_WAP>?
display filter rf (0 band-pass; 1 low-pass; 2 high-pass)
SU_WAP>?
USAGE:
     display firewall rule [ chain [string] ] [ address-family {inet | inet6} ]
SU_WAP>?
USAGE:display flashlock status
SU_WAP>?
usage:display flow id {all | flowid} for:get flow info
SU_WAP>?
display ftp config status
SU_WAP>?
display if name [ifname/all]
SU_WAP>?
display igmp
display igmp config
SU_WAP>?
display igmp config
SU_WAP>?
USAGE:
     display inner version -- get software version, including B version!
SU_WAP>?
display ip interface interface interface
SU_WAP>?
display ip neigh
SU_WAP>?
[Command]:display ip route [address-family Family]
	 OPTIONS: address-family: inet(IPv4,default)/inet6(IPv6)
SU_WAP>?
display ip6tables filter
SU_WAP>?
display iptables filter
SU_WAP>?
display iptables mangle
SU_WAP>?
display iptables nat
SU_WAP>?
display iptables raw
SU_WAP>?
display jb grid status
SU_WAP>?
display jb para
SU_WAP>?
display lan mac filter
SU_WAP>?
USAGE:	
     display lanmac -- get lan mac of board
SU_WAP>?
display lanport workmode
SU_WAP>?
display last call log port {[0,7] |all}
SU_WAP>?
USAGE:
     display lastword  -- Displays the current lastword.
     display lastword type old  -- Displays the lastword for the last time and the lastword for the last 2 times.
     display lastword type startup  -- Displays the lastword for startup time.
SU_WAP>?
USAGE:
     display log info  -- show all log information.
SU_WAP>?
display mac ap
display mac ap brief
SU_WAP>?
display mac ap brif
SU_WAP>?
display macaddress
display macaddress timer
SU_WAP>?
display macaddress timer
SU_WAP>?
USAGE:
     display machineItem -- get machine item of board
SU_WAP>?
display memory detail
SU_WAP>?
USAGE:
     display memory info  -- show memory usage.
SU_WAP>?
display microwave ctrl info
SU_WAP>?
[Usage]:
display msg-queue : display all msg queue.
display msg-queue [appname {value}] : display the msg queue by process name.
SU_WAP>?
display nat port mapping { interface IntfName [index Index] | internal-ip ip }
SU_WAP>?
display NCE info
SU_WAP>?
USAGE:
     display nff log  -- show all nff log information.
SU_WAP>?
display np statistics
SU_WAP>?
display oaml2shell ethvlan
SU_WAP>?
display onu info(regstatus, onuid, xpon module)
SU_WAP>?
display optic [device {opticdev}]
SU_WAP>?
USAGE:
     display optmode -- display info of optic module
SU_WAP>?
get ont ploam password
SU_WAP>?
display policy route all
SU_WAP>?
[Command]: display pon statistics
SU_WAP>?
display poncnt dnstatistic [portid {id}]
SU_WAP>?
display poncnt gemport upstatistic gemportid {gemportid} [portid {id}]
SU_WAP>?
display poncnt upstatistic [portid {id}]
SU_WAP>?
[Command]: display port statistics 
[Usage]: display port statistics portid [portid]
SU_WAP>?
[Command]: display portstatistics 
[Usage]: display portstatistics portnum [portid]
SU_WAP>?
display ppp interface interface interface
SU_WAP>?
display pppoe client
display pppoe client all
SU_WAP>?
display pppoe client {all | interface intfname}
SU_WAP>?
display pppoe_em result
SU_WAP>?
USAGE:
     display productmac -- get product mac of board
SU_WAP>?
display the loading progress of package
pack: firmware
cfg: config xml file
bundle: bundle file
SU_WAP>?
USAGE:display radio stats
SU_WAP>?
display rf config (switch: on/off; state:on/off )
SU_WAP>?
USAGE:
     display rfpi -- get rfpi of board
SU_WAP>?
USAGE:display rootcert info -- display root certificate info
SU_WAP>?
display rtp stack channel stat
SU_WAP>?
display rtp stack chip stat
SU_WAP>?
display rtp stack para
SU_WAP>?
display rtp stack version
SU_WAP>?
USAGE:
     display sfwd drop statistics -- Displays the forward drop packets statistics.
SU_WAP>?
USAGE:
     display sfwd port statistics -- Displays the port RX/TX packets statistics.
SU_WAP>?
USAGE:
     display sn -- get serial number of board
SU_WAP>?
USAGE:display specsn
SU_WAP>?
USAGE:
    display ssh authentication-type
OPTIONS:
    mode:0 is password mode, 1 is password-publickey mode
SU_WAP>?
USAGE: 
  display ssh-hostkey fingerprint
SU_WAP>?
USAGE:display startcode version -- display startcode version
SU_WAP>?
USAGE:
     display startup info  -- show startup information in ring buffer.
SU_WAP>?
display swm bootstate
SU_WAP>?
display swm state
SU_WAP>?
display sysinfo  -- get cpu ,memory condition and time
SU_WAP>?
USAGE:
     display syslog -- get syslog enable and level
SU_WAP>?
display system info
SU_WAP>?
display timeout
SU_WAP>?
USAGE:
    display timer type {value}
OPTIONS:
    type: 5:dst
SU_WAP>?
USAGE: display tr069 info -- get tr069 server info
SU_WAP>?
USAGE:
     display usb devList -- get usb device list which can be used!
SU_WAP>?
display user device [ip ipAddress | mac macAddress]
SU_WAP>?
USAGE:
     display version: get hardware version, software version, bios verison of board
SU_WAP>?
USAGE:
    display voicelinetest portnum {[1,8] | all}
OPTIONS:
    portnum : value range{[1,8] | all}
SU_WAP>?
display voip dsp jbdata port {[0,7]} channel {[0,3] |all}
SU_WAP>?
display voip dsp para diagnose state
SU_WAP>?
display voip dsp para diagnose statistics port {[0,7]}
SU_WAP>?
display voip dsp tonedetect port {[0,7]} channel {[0,3] |all} dir {0:up,1:down,2:all}
SU_WAP>?
display voip dtmfdiag state
SU_WAP>?
display voip dtmfsimpara paratype {[0,1]}
SU_WAP>?
display voip info
SU_WAP>?
display voip rightflag port {[0,7]}
SU_WAP>?
display voip ring info port {[0,7]}
SU_WAP>?
display voip rtpdiag port {[0,7]} dir {0:tx,1:rx,2:all}
SU_WAP>?
display voip tone info port {[0,7]}
SU_WAP>?
display wan layer all
SU_WAP>?
display waninfo
display waninfo all
display waninfo all detail
SU_WAP>?
display waninfo all
display waninfo all detail
SU_WAP>?
display waninfo all detail
SU_WAP>?
USAGE:
     display wanmac -- get wan mac of board
SU_WAP>?
display wifi ap
SU_WAP>?
display wifi associate
SU_WAP>?
USAGE: display wifi calibrate mode
SU_WAP>?
display wifi filter index [1-8]
SU_WAP>?
display wifi information
SU_WAP>?
display wifi multicast
SU_WAP>?
display wifi neighbor
SU_WAP>?
USAGE: get wifi pa type
SU_WAP>?
display wifi radio
SU_WAP>?
display wifi smartant status wifichip {0|1}
SU_WAP>?
display wifichip
SU_WAP>?
display wlan config wlaninst {wlaninst}
OPTIONS: 
    wlaninst: wlaninst ,value range [1-8]
SU_WAP>?
display wlan staevent
SU_WAP>?
display wlan stainfo [mac {mac}]
OPTIONS: 
    mac: sta mac
SU_WAP>?
USAGE:
     display wlanmac -- display wlan mac address
SU_WAP>?
display zsp version
SU_WAP>?
USAGE:
     firewall log [ chain [string] | chain [string] rule [int] ]
SU_WAP>?
flush dhcp server pool index [poolIndex]
SU_WAP>?
flush dnsserver cache
SU_WAP>?
[Usage]:
fttr dfx clear {0|1}
0: clear debug log
1: clear error log
SU_WAP>?
[Usage]:
fttr dfx showinfo {0|1}
0: show debug log
1: show error log
SU_WAP>?
[Usage]:
fttr gmacdrv execcmd {type}
2: show gmac cnt
3: clear gmac cnt
9 {onuid}: show bip err
13 {bwCapLen}{bwCapMode}{bwCapCfg}: show bwmap config info
14 {saveDwordNum}: report to file
15: show gmac statistics
16 {onuid}: show bwmap statistics per second
17: show rogue onu info
18 {0|1}: set Lan-Optic tx switch
19: show Lan-Optic tx switch
SU_WAP>?
[Usage]:
fttr print olt omci on
                    off
                    mib {onuid}
SU_WAP>?
[Usage]:
fttr reg showinfo {type}
0: show port info
1: show slot info
3: show login info
4: show logout info
5: show black list
6: show on-off line info
SU_WAP>?
[Usage]:fttr set debugont {onuid}
SU_WAP>?
[Usage]:
fttr show onlineedgeont
          omcistatinfo
          debugont
          failinfo
          edgeontinfo
          edgeontinfo {onuid}
          ontpathinfo {onuid}
          saveinfo {onuid}
SU_WAP>?
get ap retrans wandeviceinst [1]
SU_WAP>?
get battery alarm policy
SU_WAP>?
get battery alarm status
SU_WAP>?
get ip conntrack
SU_WAP>?
get mac agingtime
SU_WAP>?
get ont oamfrequency
SU_WAP>?
Get opm switch
SU_WAP>?
USAGE: get optic debug info
SU_WAP>?
USAGE: get optic par info 
SU_WAP>?
USAGE: get optic phy type
SU_WAP>?
get optic txmode
SU_WAP>?
get poncnt upgemport
SU_WAP>?
get port config portid [1-5]
SU_WAP>?
get port isolate
SU_WAP>?
get rogue status
SU_WAP>?
USAGE:
     display samba speedUp
SU_WAP>?
get testself
SU_WAP>?
USAGE:
    get wifi atm band {band}
OPTIONS:
    para: band   -- a means 5G, b means 2G

SU_WAP>?
get wifi para laninst [1]
SU_WAP>?
get wlan advance laninst [1] wlaninst [1-4]|[1-8]
SU_WAP>?
get wlan associated laninst [1] wlaninst [1-4]|[1-8] deviceinst {deviceinstid}
SU_WAP>?
get wlan basic laninst [1] wlaninst [1-4]|[1-8]
SU_WAP>?
USAGE:
    get wlan enable laninst 1
SU_WAP>?
get wlan isolate wlaninst {wlaninst}
OPTIONS: 
    wlaninst: wlaninst ,value range [1-8]
SU_WAP>?
get wlan stats laninst [1] wlaninst [1-4]|[1-8]
SU_WAP>?
get wlan wps laninst [1] wlaninst [1-4]|[1-8]
SU_WAP>?
ifconfig
SU_WAP>?
igmp add mirror filter ip ipaddr
SU_WAP>?
igmp clear statistics
SU_WAP>?
igmp del mirror filter ip ipaddr
SU_WAP>?
igmp disable
SU_WAP>?
igmp enable [ proxy switch | snooping switch | version igmpversion | robustness robustness | query-interval interval | query-response-interval interval | last-member-interval interval | last-member-count count | last-member-response-interval interval | startup-query-interval interval | startup-query-count count | unsolicited-report-interval interval ]*
SU_WAP>?
igmp get debug switch [ para1 [int] | para1 [int] para2 [int] ]
SU_WAP>?
igmp get flow info
SU_WAP>?
igmp get global cfg
SU_WAP>?
igmp get iptv
SU_WAP>?
igmp get mirror filter ip
SU_WAP>?
igmp get multilmac
SU_WAP>?
igmp get port multicast config
SU_WAP>?
igmp get statistics
SU_WAP>?
igmp set debug switch enable [0,1] para [int]
SU_WAP>?
igmp set iptv { igmpenable [int] | proxyenable [int] | 
snoopingenable [int] | robustness [int] | genqueryinterval [int] | genresponsetime [int] | spquerynumber [int] | spqueryinterval [int] | 
spresponsetime [int] | tosmark [int] | primark [int] | igmpversion [int] | mldproxyenable [int] | mldsnoopingenable [int] | mldversion [int]}
SU_WAP>?
ip -6 neigh
SU_WAP>?
ip -6 route
SU_WAP>?
ip -6 rule
SU_WAP>?
ip interface config interface interface { status status | ipv4status ipv4status | ipv6status ipv6status | mtu mtu } *
SU_WAP>?
ip neigh
SU_WAP>?
ip route
ip route show
SU_WAP>?
[Command]:ip route show [table table_name|table_id]
SU_WAP>?
ip rule
SU_WAP>?
USAGE:jvmcmd map histo
SU_WAP>?
USAGE:jvmcmd stack trace
SU_WAP>?
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
SU_WAP>?
lan mac filter add mac macaddress
SU_WAP>?
lan mac filter delete mac macaddress
SU_WAP>?
lan mac filter disable
SU_WAP>?
lan mac filter enable [policy policy]
SU_WAP>?
lan mac filter flush
SU_WAP>?
load fem par by {tftp|sftp} [svrip {ip addr}] [par_name {file name}] [user {user name}] [pwd {password}] [port {port}]
SU_WAP>?
load pack by {https|sftp|ftp|tftp|http} svrip {ip addr} remotefile {file name} [user {user name}] [pwd {password}] [port {port}]. Attention: Only some boards support ftp|tftp|http service
SU_WAP>?
load ssh-pubkey by {tftp|ftp|https|sftp} svrip {ip addr} remotefile {file name} [user {user name}] [pwd {password}] [port {port}]
SU_WAP>?
logout
SU_WAP>?
macaddress timer value[10-86400, 0:no-aging]
SU_WAP>?
USAGE:
     make ssh hostkey type {value} bits {value}
OPTIONS:
     type Type of key to generate. One of: rsa/ecdsa
     bits Key size in bits, RSA should be a multiple of 8 between 2048 and 4096
           ECDSA has sizes 256 384 521 
SU_WAP>?
USAGE:
     mid get  -- show mid switch information.
SU_WAP>?
USAGE:
     mid off  -- turn all mid switch off.
SU_WAP>?
USAGE:
     mid set mid {value} flag {value} [pidmask {value}] [nextboot {value}]
SU_WAP>?
napt cli para [int]
SU_WAP>?
netstat -na
SU_WAP>?
nslookup domain domain [ server server | interface interface | repnum repnum ] *
SU_WAP>?
[Command]:print all lmc event log
SU_WAP>?
[Command]:oamcmd clear log
SU_WAP>?
[Usage]:
oamcmd debug debugtype {[msg|0]|[trace|1][savemsg|2]|[alarm|3]} debugswitch {[on|1]|[off|0]} [llid [llid]]
msg|0-oam msg print, trace|1-trace print, savemsg|2-save oam msg, alarm|3-alarm debug
off|0-debug off, on|1-debug on
llid:llid index (1-8)
example: oamcmd debug debugtype msg debugswitch on
SU_WAP>?
[Command]:oamcmd error log
SU_WAP>?
[Usage]:oamcmd pdt show log
SU_WAP>?
[Usage]:oamcmd show flow portid [portid] 
portid---the id of eth port
SU_WAP>?
[Command]:print all saved log
SU_WAP>?
[Usage]:
omcicmd alarm show meid [me-id] instid [inst-id]
me-id: 65535 show all alarm
inst-id: 65535 show inst alarm
SU_WAP>?
[Command]:clear all omci & error log [Usage]: show error log portid [int]
SU_WAP>?
[Usage]:omcicmd debug debugtype {[msg|0]|[trace|1]|[savemsg|2]|[noprtmsg|3]} debugswitch {[off|0]|[on|1]}
msg|0-omci_print trace|1-trace_print savemsg|2-omci_save noprtmsg|3-not_print_omci_msg
off|0-disable on|1-enable
SU_WAP>?
[Command]:show error log [Usage]: show error log portid [int]
SU_WAP>?
[Usage]:omcicmd mib show meid [me-id] instid [inst-id] 
me-id: 65535 show all me and inst info 
inst-id: 65535 show all inst info
SU_WAP>?
[Usage]:omcicmd pdt show log
SU_WAP>?
[Usage]:omcicmd pm show meid [me-id] instid [inst-id] portid [int]
me-id: 65535 show all me and inst info
inst-id: 65535 show all inst info
SU_WAP>?
[Usage]:omcicmd show flow type [typeid]
0:All
1:AniportObj Cfg
2:UniportObj Cfg
3:GemportObj Cfg
4:FlowObj Cfg
5:All the flow ID
6:All the flow entry
SU_WAP>?
[Command]:print all saved log [Usage]: print all saved log portid [int]
SU_WAP>?
[Command]:omcicmd show qos
SU_WAP>?
osgicmd debug level [0:CLOSE, 1:Error, 2:Warning, 3:Info, 4:Debug]
SU_WAP>?
osgicmd get debug [bundleid [-1:all,bundleid]]
SU_WAP>?
osgicmd plugin permission bundleid [int]
SU_WAP>?
osgicmd set debug bundleid [-1:all,bundleid] switch [0:off,1:on]
SU_WAP>?
osgicmd show bundleresource
SU_WAP>?
osgicmd show bundlestate
SU_WAP>?
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
SU_WAP>?
[Usage]: plugcmd show state
SU_WAP>?
[Usage]: plugcmd start name [name]
OPTIONS:
    name: plugin name;
    
SU_WAP>?
[Usage]: plugcmd stop name [name]
OPTIONS:
    name: plugin name;
    
SU_WAP>?
[Usage]: plugcmd uninstall name [name]
OPTIONS:
    name: plugin name;
    
SU_WAP>?
[Usage]:plugincmd debug type {type} mid {mid} level {level}
[Note]:
	type:  plugin type;
	mid:   ID of the module;
	level: debug level;
SU_WAP>?
ppp interface config interface interface { status status | ipcpstatus ipcpstatus | ipv6cpstatus ipv6cpstatus | mru mru } *
SU_WAP>?
ppp l2log disable
SU_WAP>?
ppp l2log enable [port port_id | mac mac]
SU_WAP>?
pppoe client attach interface intfname
SU_WAP>?
pppoe client detach interface intfname
SU_WAP>?
qoscfg get
SU_WAP>?
quit
SU_WAP>?
USAGE
     reset -- reset board
SU_WAP>?
restore backup [file {value}]
SU_WAP>?
restore manufactory
SU_WAP>?
route get default ----- get the default route
SU_WAP>?
route get static instance [instanceid]
SU_WAP>?
Save data.
SU_WAP>?
Save log from buff to flash immediately, example: save log
SU_WAP>?
session cli mode [0:to cpu,1:to session,2:to router] tunnel [0:none,1:tunnel]
SU_WAP>?
USAGE:
    set ap retrans wandeviceinst [1] enable {0/1}
SU_WAP>?
USAGE:
    set apssh mac {mac addr} enable {0/1}
SU_WAP>?
USAGE:
    set aptelnet mac {mac addr} enable {0/1}
SU_WAP>?
set bbsp optimization enable [0|1]
SU_WAP>?
USAGE:
     set collect level {value}
OPTIONS:
     level: 0: default, not contains senstive information.
            1: contains senstive information 
SU_WAP>?
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
SU_WAP>?
USAGE:
    set ethportmirror sourceport {value} destport {value} mirrordate {0:out/1:in/2:all} enable {0/1}
OPTIONS:
    sourceport  : value range [1-8:eth/9:cpu/10:pon/edge onu:20-35/ssid0-ssid15:100-115]
    destport    : value range [1-8] 
    mirrordate  : {0:out/1:in/2:all}
    enable      : {0/1}
SU_WAP>?
USAGE:
     set flashlock {status [0,1]}
OPTIONS:
     status: Between 0 and 1. 0 means disable flash lock; 1 means enable flash lock.
SU_WAP>?
USAGE:
    set iaccess speed period [2: 60]
SU_WAP>?
set lanport qbuf cell [num]
SU_WAP>?
set led switch [on/off/recovery/flash]
SU_WAP>?
set llid qmode [1|2] : 1 for 4 llid, 2 for 8 llid
SU_WAP>?
USEAGE: set microwave ctrl mode [0~2] scanInterval [...] scanCount [...]
OPTIONS:
    mode 0 means Disable 1 means InterferenceTrigger 2 means CycleCheck
    scanInterval means microwave-interference scan interval
    scanCount means the count of non-microwave-interference. if reaches to it, our device will stop scan.
SU_WAP>?
[Usage]: set NCE url {url}
SU_WAP>?
set newparentalctrl
set newparentalctrl stats
SU_WAP>?
set newparentalctrl stats type [type] period [period]
SU_WAP>?
[Command]: set opticdata print
[Command]: set opticdata print {[on]|[off]}
SU_WAP>?
set port isolate switch { enable | enable ontoflash | disable | disable ontoflash | undef }
SU_WAP>?
USAGE:
    set portmirror sourceport {value} destport {value} mirrordata {0:out/1:in/2:all} enable {0/1}
OPTIONS:
    sourceport  : value range [1-5:eth/9:cpu/10:pon/edge onu:20-35/ssid0-ssid15:100-115]
    destport    : value range [1-5] 
    mirrordata  : {0:out/1:in/2:all}
    enable      : {0/1}
SU_WAP>?
USAGE:
     set ringchk debug value[int] 
OPTIONS:
     debug:  0  disables the debugging function.
             1  enables the debugging function.
             2  disables the ringchk function on the port.
             3  enables the ringchk function on the port.
SU_WAP>?
USAGE:
     set samba speedUp {value}
OPTIONS:
     level:  0  close samba speed up.
             1  open samba speed up.
SU_WAP>?
USAGE:set ssid index[1-4] | [1-8] [para{value}] 
OPTIONS: 
    name--SSID name
    visible--1 means Advertisement enabled,0 means disabled
    security--None, WEP-128 | WEP-64, WPA2-Personal | WPA-Personal, WPA-WPA2-Personal, WPA-Enterprise, WPA2-Enterprise, WPA-WPA2-Enterprise
    password--password
SU_WAP>?
set timeout
SU_WAP>?
set userpasswd
SU_WAP>?
USAGE:
	set voice announcement switch {[0,2]}
OPTIONS:
	switch : { 0:disable, 1:temporarily enable, 2:enable }
SU_WAP>?
USAGE:
	set voice dtmfmethod mode {[0,2]} {mgno [0,1]}
OPTIONS:
	mode : {0:InBand, 1:RFC2833, 2:SIPInfo}
SU_WAP>?
USAGE:
    set voicedebug switch {on|off}
OPTIONS:
    switch       : {on:enable,off:disable}
SU_WAP>?
USAGE:
    set voicedsploop enable {[0,1]} type {0:TDM,1:IP} port {[1,8]}
OPTIONS:
    enable  : {0:disable,1:enable}
    type    : {0:TDM,1:IP}
    port    : {[1,8]}
SU_WAP>?
USAGE:
    set voicelinetest portnum {[1,8] | all}
OPTIONS:
    portnum : value range{[1,8] | all}
SU_WAP>?
USAGE:
    set voiceportloop enable {[0,1]} type {0:TDM,1:IP} port {[1,8]}
OPTIONS:
    enable  : {0:disable,1:enable}
    type    : {0:TDM,1:IP}
    port    : {[1,8]}
SU_WAP>?
USAGE:
    set VoiceSignalingPrint switch {on|off}
OPTIONS:
    switch  : {on:enable,off:disable}
SU_WAP>?
USAGE:
	set voip clip port{[0,7]} mode{[0,4]}
OPTIONS:
	mode : {0:Sdmf-fsk,1:Mdmf-fsk,2:Dtmf,3:R1.5,4:etsi}
SU_WAP>?
USAGE:
	set voip dsptemplate port {[0,7]} templatename {[0,4]}
OPTIONS:
	templatename : {0:highspeed_modem,1:lowspeed_modem,2:staticjbmode,3:alarmdevice,4:clear templatename}
SU_WAP>?
set voip dtmfdebug switch {[0:disable, 1:enable]} printlevel {[0,2]} autostop {[10,720]}
SU_WAP>?
set voip dtmfdetfilter port {[0,7]} value {[0,3400]}
SU_WAP>?
set voip dtmfdiag start port {[0,7]} mode {0:dial, 1:voice, 2:manualsingle, 3:manualloop}
SU_WAP>?
set voip dtmfdiag stop
SU_WAP>?
set voip dtmfsimpara reset {[0,1]} paratype {[0,1]} detectmode {[0,3]} loweradjust {[-200,600]} negativetwistadjust {[-100,100]} positivetwistadjust {[-100,100]} snr1250_1800adjust {[-200,200]} snr1800_4000adjust {[-200,200]} snr900_1250adjust {[-200,200]} snradjust {[-200,200]} snrdialadjust {[-200,200]} snrdialup_900adjust {[-200,200]}
SU_WAP>?
set voip dtmfsimu start mode{0:general simulation, 1:shift point simulation, 2:missing number simulation} printflag [0,7] analysislevel [0,2]
SU_WAP>?
set voip dtmfsimu stop
SU_WAP>?
set voip fax T38 enable {0:disable,1:enable} {mgno [0,1]}
SU_WAP>?
set voip faxmodem switch mode {0:selfswitch, 1:negotiation} {mgno [0,1]}
SU_WAP>?
set voip highpassfilter port{[0,7]} enable {0:disable,1:enable}
SU_WAP>?
USAGE:
	set voip portgain port {[0,7]} recvgain {[-12, 0]} {sendgain [-6, 6]}
OPTIONS:
	gainvalue : the step is 0.5
SU_WAP>?
set voip rtpdiag port {[0,7]} switch {on|off} tx-threshold {[10,200]} rx-threshold {[10,200]} stoptime {[1,48]}
SU_WAP>?
set voip sipprofile index [index] value [value] {mgno [0,1]}
SU_WAP>?
USAGE:
    set wifi ap optimize band {band}
OPTIONS:
    band:    a means 5G ,b means 2G
SU_WAP>?
USAGE:
    set wifi atm band {band} period {value}
OPTIONS:
    para: band   -- a means 5G, b means 2G
    para: period -- default 10s

SU_WAP>?
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

SU_WAP>?
set wifi filter index [1-8] mode [0-2]
SU_WAP>?
set wifi para laninst [1] [para {value}]
OPTIONS:
	para: txpower
	value: 10/20/30/40/50/60/80
SU_WAP>?
USAGE:
    set wifi radio band {band} [enable {value}] [channel {value}]
OPTIONS:
    band:    a means 5G ,b means 2G
    enable:  0 means disable ,1 means enable
    channel: Specifies the ID of a 2.4G channel or 5G channel. If the value is auto, the ONT automatically selects a channel
SU_WAP>?
USAGE:
    set wlan basic laninst [1] wlaninst [1-4]|[1-8] [para {value}]
OPTIONS:
    para: enable -- SSID Enable
          regdomain -- Regulatory Domain
          standard -- IEEE 802.11 mode
          power -- transmit power levels supported
          channel -- Current radio channel
          autochannel -- Enable automatic channel selection
          ht20 -- Channel width
          ssid -- SSID
          ssidhide -- SSID Advertisement Enabled
          rate -- Maximum bit rate(Mbps)
          wmmenable -- WMM Enable
          beaconType -- Beacon Type
          basicencryptionmodes -- Basic Encryption Modes
          basicauthenticationmode -- Basic Authentication Mode
          wpaencryptionmodes -- WPA Encryption Modes
          wpaauthenticationmode -- WPA Authentication Mode
          ieee11iencryptionmodes -- IEEE11i Encryption Modes
          ieee11iauthenticationmode -- IEEE11i Authentication Mode
          wepkeyindex -- WEP Key Index
          wepencryptionlevel -- WEP Encryption Level
          radiuserver -- Radius Server
          radiusport -- Radius Port
          radiuskey -- Radius Key
          grouprekey -- Key update interval
          associatenum -- Maximum associate number
          powerlevel -- Power level
          powervalue -- Power Value(dBm)
          wpskeyword -- WPS Key Word
          serviceenable -- Service Enable
          retrytimeout -- Retry Timeout
          wpaandieee11iencryptionmodes -- WPA and IEEE11i Encryption Modes
          wpaandieee11iauthenticationmode -- WPA and IEEE11i Authentication Mode          
          hwstandard -- HW Standard
          bindingmode -- Binding Mode
          bindingvlan -- Binding Vlan
          lowerlayers -- Lower Layers
    value: refer to Huawei xml interface(new).xls
SU_WAP>?
USAGE:
    set wlan enable laninst 1 [enable {0/1}] [action {0/1}] -- enable/disable wlan
OPTIONS:
    enable: 0 means disable wlan, 1 means enable wlan
    action: 0 means take effect and do not save flash, 1 means do not take effect and save flash
SU_WAP>?
USAGE:set wlan isolate wlaninst {wlaninst} [enable {value}] 
OPTIONS: 
    wlaninst: wlaninst ,value range [1-8]
    enable--1 means enable,0 means disable
SU_WAP>?
USAGE:
    set wlan staboost band {band} [add {stamac} during {times}] [del {stamac}] [show all]
OPTIONS:
    para: band   -- a means 5G, b means 2G
          add    -- Add StaMac
          during -- Duration times
          del    -- Del StaMac
          show   -- All Boost Stainfo

SU_WAP>?
USAGE:
     sfwd port statistics oper {start|stop|clear} -- start|stop|clear the port RX/TX packets statistics.
SU_WAP>?
shell
SU_WAP>?
[Usage]: show diagnose [portid {0-1}]
SU_WAP>?
smartapi glog clear
SU_WAP>?
smartapi glog display
SU_WAP>?
smartapi glog set enable [enable]
SU_WAP>?
USAGE:
    ssh authentication-type mode {value} 
OPTIONS:
    mode:0 is password mode, 1 is password-publickey mode
SU_WAP>?
USAGE:
     ssh remote ip {ip} port {port} -- ssh to remote ip address.
SU_WAP>?
[Usage]:
start diagnose type {bwmap|ploam-d|ploam-u|dbru|gemport-d|bwmap-dbru} scope {all|local|error|spec-id} [value msg-count-or-id-value] [portid {0-1}]
[Note]:
    The XG-PON does not support 'ploam-u' capturing;
    when 'type' set to {bwmap}, 'scope' can be specified as {all|error|spec-id}, or {local} for GPON only; 
    when 'type' set to {ploam-d}, 'scope' can be specified as {all|local|error|spec-id};
    when 'type' set to {ploam-u}, 'scope' can be specified as {all|spec-id};
    when 'type' set to {dbru}, 'scope' can be specified as {local|spec-id};
    when 'type' set to {gemport-d}, 'scope' can be specified as {error};
    when 'type' set to {bwmap-dbru}, 'scope' can be specified as {all};
    when 'scope' set to {all|local|error}, 'value' indicates the number of message to capture;
    when 'scope' set to {spec-id}, 'value' indicates the specific ID;
SU_WAP>?
USAGE:
     stats clear protoc {ProctocolName} [mod {ModuleType}] [client {Client}]
OPTIONS:     
     ProctocolName:igmp|arp|dhcpd|dhcpc|pppoec|dhcp6c|dhcp6s|icmpv6|unknown
     ModuleType:ker|userapp|all
     Client:wanX|all,example:wan1,wan2
SU_WAP>?
USAGE:
     stats display protoc {ProctocolName} [mod {ModuleType}] [client {Client}]
OPTIONS:     
     ProctocolName:igmp|arp|dhcpd|dhcpc|pppoec|dhcp6c|dhcp6s|icmpv6|unknown
     ModuleType:ker|userapp|all
     Client:wanX|all,example:wan1,wan2
SU_WAP>?
[Usage]: stop diagnose [portid {0-1}]
SU_WAP>?
su
SU_WAP>?
USAGE:
     telnet remote ip {ip} port {port} -- telnet to remote ip address.
SU_WAP>?
USAGE:test apdev.
SU_WAP>?
USAGE:test tr069 inform end to display the result.
SU_WAP>?
USAGE:test tr069 inform start to send tr069 inform.
SU_WAP>?
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
SU_WAP>?
trafficdump [location {input,output,drop,forward} | version {v4,v6} | -telnet {enable,disable} | +mac {enable,disable} | ip {address} | protocol {tcp,udp,icmp,igmp,arp} | tcpportlist {int,int,..} | udpportlist {int,int,..} | interface {interfacelist}] 
SU_WAP>?
USAGE:
     udm clear log  -- clear udm debug log usage.
SU_WAP>?
USAGE:
     udm show log  -- show udm debug log usage.
SU_WAP>?
undo debugging dsp diagnose port {[0,7]}
SU_WAP>?
undo debugging dsp para diagnose port {[0,7]}
SU_WAP>?
undo debugging dsp record
SU_WAP>?
undo debugging dsp t38diag port {[0,7]}
SU_WAP>?
USAGE:
     undo firewall log [ chain [string] | chain [string] rule [int] ]
SU_WAP>?
voice net diagnose start
SU_WAP>?
voice remote diagnose server set wanname {[portname]} localtransport [int] remoteip [ip] remotetransport [int]
SU_WAP>?
voice remote diagnose set enable {[0,1]} port {[0,7]} timerautostop {[1,43200]} diagtype {all|signal|media}
SU_WAP>?
vspa clear rtp statistics port {[0,7]}
SU_WAP>?
vspa debug module {[0,999]} cmd {[0,999]} subcmd {[0,999]} 
SU_WAP>?
vspa display conference info
SU_WAP>?
vspa display digitmap info
SU_WAP>?
vspa display dsp running info index {[0,3]} mode {0:all, 1:summary}
SU_WAP>?
vspa display dsp state
SU_WAP>?
vspa display dsp template info
SU_WAP>?
vspa display mg if state mg {[0,1]}
SU_WAP>?
vspa display mg info
SU_WAP>?
vspa display online user info
SU_WAP>?
vspa display port status
SU_WAP>?
vspa display profilebody info
SU_WAP>?
vspa display rtp statistics port {[0,7]}
SU_WAP>?
vspa display service log
SU_WAP>?
vspa display signal scene info mg {[0,1]} scene [scenename]
SU_WAP>?
vspa display signal scene list
SU_WAP>?
vspa display user call state port {[0,7]}
SU_WAP>?
vspa display user status
SU_WAP>?
vspa reset mg {[0,1]} type {0:service restored,1:cold start,2:warm start,3:capabilities change}
SU_WAP>?
vspa shutdown mg num {[0,1]} type {0:gracefully close,1:forced close}
SU_WAP>?
USAGE:
     wap list [format {0|1}] [path {value}] -- show directorys and files information.
SU_WAP>?
USAGE:
     wap ps  -- show process and thread information.
SU_WAP>?
wap top
SU_WAP>?
wifi del fem calibration
SU_WAP>?
wifi del fem par
SU_WAP>?
wifi smartant set [wifichip {0|1 (2.4g|5g)}] [switch {0|1}] [mode {auto|OMNI_fix|SEPA_fix}] [chainmask {10|5|9|6}]
SU_WAP>?

---------------- Help --------------
[Usage]:wificmd show connect log  {2G|5G|All}

[Usage]:wificmd show config log  {2G|5G|All}

[Usage]:wificmd show debug log {2G|5G|All}

[Usage]:wificmd show sta

[Usage]:wificmd show sta statistic

[Usage]:wificmd set debug level {0|1|2|3|4}
    0:disable
    1:error
    2:warning
    3:info
    4:debug

SU_WAP>
