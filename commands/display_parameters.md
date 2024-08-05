display amp policy-stats port id [portid]: display the spec port stats.
display amp stats gemport id [1:4094]: Display the spec gemport stats.
display bbsp stats btv ip { ipaddr [ port [int] ] | all }
display bbsp stats wan id {wanid | all}
display current-configuration [grep {value}]
display ddns info interface {intfname}
display debug info dhcp6c wanname [wanname]
display debug info ra wanname [wanname]
display dhcp client {all | interface intfname}
display dhcp client6 {all | interface intfname}
display dhcp server pool {all | index poolindex}
display dhcp server user {all | index userIndex}
display ethoam ma info mdins [int] mains [int]
display ethoam md info mdins [int]
display ethoam mep info mdins[int] mains [int] mepins [int]
display ethoam mep perf mdinst [int] mainst [int] mepinst [int]
display filter rf (0 band-pass; 1 low-pass; 2 high-pass)
display if name [ifname/all]
display last call log port {[0,7] |all}
display msg-queue [appname {value}] : display the msg queue by process name.
display nat port mapping { interface IntfName [index Index] | internal-ip ip }
display onu info(regstatus, onuid, xpon module)
display optic [device {opticdev}]
display poncnt dnstatistic [portid {id}]
display poncnt gemport upstatistic gemportid {gemportid} [portid {id}]
display poncnt upstatistic [portid {id}]
display pppoe client {all | interface intfname}
display rf config (switch: on/off; state:on/off )
display user device [ip ipAddress | mac macAddress]
display voip dsp jbdata port {[0,7]} channel {[0,3] |all}
display voip dsp para diagnose statistics port {[0,7]}
display voip dsp tonedetect port {[0,7]} channel {[0,3] |all} dir {0:up,1:down,2:all}
display voip dtmfsimpara paratype {[0,1]}
display voip rightflag port {[0,7]}
display voip ring info port {[0,7]}
display voip rtpdiag port {[0,7]} dir {0:tx,1:rx,2:all}
display voip tone info port {[0,7]}
display wifi filter index [1-8]
display wifi smartant status wifichip {0|1}
display wlan config wlaninst {wlaninst}
display wlan stainfo [mac {mac}]
