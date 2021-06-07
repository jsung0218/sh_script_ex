#!/bin/sh
spdir=`pwd`
filedir=`dirname $0`
while :
do
	echo "Install directory : (default=$spdir) "
	read x
	if [ "$x" = "" ]
	then
    cd $spdir
		break
	fi	
	if [ -d $x ]
	then 
		cd $x
		break
	fi
done

cp -R $filedir .
chmod -R +x example
