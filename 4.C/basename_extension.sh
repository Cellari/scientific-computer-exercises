#!/bin/bash

function get_basename() {
filename="${1##*/}"
basename="${filename%%.*}"

echo "$basename"
}

function get_extension() {
filename="${1##*/}"
extension="${filename#*.}"

[ "$filename" == "$extension" ] && extension=""

echo "$extension"
}
