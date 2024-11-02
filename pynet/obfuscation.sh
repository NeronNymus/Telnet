#!/bin/bash

# The intention of this file is to substitute the prints of pynet2.py

FUNC_SIZE="16"
FUNC_SIZE_MIN="16"
FUNC_SIZE_MAX="48"
VAR_SIZE="16"

obfuscate_light(){
	OBFNAME="$1"
	# Perform simple trasnformations
	#sed -i '/^\s*#/d' "$OBFNAME"	# Delete comments
	#sed -i 's/\s*#.*//' "$OBFNAME"	# Delete remaining comments
	#sed -i '/print/d' "$OBFNAME"	# Delete print lines
	sed -i 's/.*print.*/    pass/' "$OBFNAME"	# Substitute print lines with pass
	sed -i 's/\r$//' "$OBFNAME"

	echo "#!/usr/bin/env python3" | cat - "$OBFNAME" > temp_file && mv temp_file "$OBFNAME"
}

# Main flow
file="$1"	# Python script path for obfuscation

[ ! -e "$file" ] && echo "[*] Invalid file in the system"

bname=$(echo "$file" | cut -d '.' -f1)
OBFNAME_LIGHT="pynet2_obf.py"

# Obfucation part

cp "$file" "$OBFNAME_LIGHT"
obfuscate_light "$OBFNAME_LIGHT"

chmod +x "$OBFNAME_LIGHT"

echo "[!] File $OBFNAME obfuscated in $OBFNAME_LIGHT"
