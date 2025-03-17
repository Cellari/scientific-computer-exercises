#!/bin/bash

function marco() {
export STORED_DIR=$(pwd)
}

function polo() {
if [ -n "$STORED_DIR" ]
then
	cd "$STORED_DIR"
fi
}
