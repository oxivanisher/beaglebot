#!/bin/bash

rm -f ~/button.1
mkfifo ~/button.1
exec 9<> ~/button.1

od -x /dev/input/event0  2>&1 &

while read event <&9
do
	echo "Key Pressed!"
done



#z="7"
#num=0
#while true #[ "a"$z != "a8" ]
#do
	#skip=$num 
#	z=$(dd bs=1 count=1 if=/dev/input/event0 2> /dev/null)
#	num=$((num+1))
#	echo $num:$z
#	case "$z" in
#		8 ) echo -n 8
#		;;

#		[0-7] ) echo -n X ;;
#		9 ) echo -n X
#		;;

#		[a-zA-Z] ) echo -n .
#		;;

#		* ) echo -n $z .
#		;;
#	esac
#done
