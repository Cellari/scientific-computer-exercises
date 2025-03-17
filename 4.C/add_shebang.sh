#!/bin/bash

SHEBANG="#!/bin/bash"

for var in "$@"
do
	FIRST_LINE=$(less "$var" | head -n 1)
	if  [ "$SHEBANG" != "$FIRST_LINE" ]
	then
		x=$(echo "$SHEBANG"; cat "$var")
		echo "$x" > "$var"
		echo "$SHEBANG added to $var"
	fi
done
