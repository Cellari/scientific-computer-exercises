#!/bin/bash

function fibonacci() {
if [ $1 <= 0 ]; then
return 1
fi

a=0
b=1
for (( i=1; i<=$1; i++ ))
do
	fn=$((a + b))
	a=$b
	b=$fn
	# echo "$i: $a"
done
echo $a
}
