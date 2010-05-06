#!/bin/bash

. config/wol.cfg

if [ "$1" == "" ];
then
	echo -e "hosts available:"

	IFS=";"
	while read MAC NAME
	do
		echo -e "$NAME "
	done < config/wol-hosts.cfg
else
	bool=0

	IFS=";"
	while read MAC NAME
	do
		if [ "$1" == "$NAME" ];
		then
			echo -e "Waking $NAME ($MAC)"
			etherwake $OPTS $MAC
			bool=1
		fi
	done < config/wol-hosts.cfg

	if [ $bool -eq 0 ];
	then
		echo -e "No host found named: $1"
	fi
fi
