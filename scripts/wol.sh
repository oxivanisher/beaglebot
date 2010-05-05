#!/bin/bash

#load hosts
. scripts/wol.cfg

ETHERWAKE=$(which etherwake)

if [ "$1" == "" ];
	echo "hosts available:"
else
	echo "waking xxx"
fi

#$ETHERWAKE 
