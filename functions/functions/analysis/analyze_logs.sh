#!/bin/bash

# This script is for analyzing logs generated by successfully entering
# into Huawei devices.

# Move into the root path directory
project_path="/media/Kali/home/grimaldi/Bash/Telnet/pynet"
#cd "$project_path"

analysis1(){
	analysis_result="../analysis/authenticated_devices"
	touch "$analysis_result"
	grep -r 'Password is default value' logs | sort -u | cut -d '/' -f2 | cut -d '_' -f1 | tee "$analysis_result" 
}

analysis2(){
	analysis_result="../analysis/authenticated_devices2"
	find logs -type f | parallel grep 'Password is default value' {} | sort -u | cut -d '/' -f2 | cut -d '_' -f1 | tee "$analysis_result"
}

analysis3(){
	analysis_result="../analysis/authenticated_devices3"
	find logs -type f | xargs -P 4 -n 1 grep 'Password is default value' | uniq | cut -d '/' -f2 | cut -d '_' -f1 | tee "$analysis_result"
}

# Analyze the history of number of connections.
previous_number="0"	# Global variable
analysis4(){
	pwd
	file logins_history.txt
	cut -d '[' -f2 logins_history.txt | cut -d ' ' -f1  > temp_numbers.txt # This are all the values every 5 seconds

	# Delete the old one
	csv_file="data_modeling/data_to_model.csv"
	rm "$csv_file"
	touch "$csv_file"

	# We want to calculate the differences between adjacent numbers
	while IFS= read -r number;
	do
		actual_cont=$((number - previous_number))
		echo -e "$number,$actual_cont" | tee -a "$csv_file"
		previous_number="$number"
	done < "temp_numbers.txt"

	# Then generate a report with python
	python_script="data_modeling/model_csv.py"
	csv_path="data_modeling/data_to_model.csv"

	python3 "$python_script" "$csv_path"

}

# Analyze the pings
analysis5(){
	pwd
	#grep -r ping logs
	#grep -r transmitted logs
	#grep -r -A 2 "0% packet loss" logs
	grep -r -A 2 "0% packet loss" logs	| grep -v 100
}

# Analyze the MAC chidl of the WAP's
analysis6(){
	#grep -r -A 100 "HW Addr" pynet/logs | tee analysis/macs_dirty
	#grep -r -H -a "SSID" pynet/logs | tee analysis/macs_dirty2
	#find pynet/logs -type f | parallel -j 4 grep -H -a "SSID" {} | tee analysis/macs_dirty3
	find pynet/logs -type f | parallel -j 32 grep -H -a "SSID" {} | sed 's/pynet\/logs\///g; s/_log//g' | tee analysis/macs_dirty4.csv
	sort -V -o -u analysis/macs_dirty4 analysis/macs_dirty4.csv
}

# This function analyze the previous results
analysis7(){
	sed -i 's/pynet\/logs\///g; s/_log//g; s/:/,/; s/[[:space:]]\+/,/g; s/,\+/,/g; s/,$//; s/,SSID[0-9]\+//g' analysis/macs_dirty4.csv
	#cat analysis/macs_dirty4 | parallel --pipe -j 16 sed 's/pynet\/logs\///g; s/_log//g; s/:/,/; s/[[:space:]]\+/,/g; s/,\+/,/g; s/,$//' | tee analysis/macs6.csv
}

#analysis1
#analysis2
#analysis3
#analysis4
#analysis5
#analysis6
analysis7