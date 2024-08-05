# Some commands for testing in the proxy for analyzing responses.

# wap list = ls
## the syntax change a few
wap list format 1 path /bin \r\n

wap list format 1 path /bin/busybox.nosuid \r\n

/bin/busybox.nosuid --list\r\n

/bin/busybox.nosuid echo "test"\r\n
 
display current-configuration grep portmirror
display current-configuration grep eth1
