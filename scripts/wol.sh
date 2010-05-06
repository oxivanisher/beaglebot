#!/bin/bash

ETHERWAKE=$(which etherwake)

if [ "$1" == "" ];
then
	echo -e "hosts available:\n"

	IFS=";"
	while read MAC NAME
	do
		echo -e "$NAME "
	done < scripts/wol.cfg
else
	bool=0

	IFS=";"
	while read MAC NAME
	do
		if [ "$1" == "$NAME" ];
		then
			echo -e "Waking $NAME ($MAC)"
			$ETHERWAKE $MAC
			bool=1
		fi
	done < scripts/wol.cfg

	if [ $bool -eq 0 ];
	then
		echo -e "No host found named: $1"
	fi
fi
