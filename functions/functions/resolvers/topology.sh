#!/bin/bash

# This script for automating the functions to analyze the network topoly of traces.
analyze_topology (){

	traces_path="traces"
	analysis_path="analysis/trace_biyection"

	#grep -ir 'totalplay' "$traces_path"
	grep -ir 'totalplay' "$traces_path" | cut -d '/' -f2 | cut -d '=' -f1,3 | cut -d ' ' -f1 | sed 's/hop=//g' | tee "$analysis_path"
}

# Perform the whois to each public IP available.
whois_topology(){

	public_ips="analysis/uniq_public_ip"
	mkdir -p whois


	while IFS= read -r ip; do
		whois_result_path="whois/whois_${ip}"
		if [ ! -e "$whois_result_path" ]; then
			whois "$ip" | tee "$whois_result_path" &
			sleep 0.5
		fi

	done < "$public_ips"

}
