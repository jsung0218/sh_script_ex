#!/bin/sh

host_list="
server1
server2
"

cur_time=`date +%Y%m%d-%H:%M`
email=your@email

for hosts in `echo $host_list`
do
  if ! ping -c 1 $hosts >/dev/null 2>/dev/null
  then
    sleep 2
    if ! ping -c 1 $hosts >/dev/null 2>/dev/null
    then
      echo "$hosts : Server or Network Died" >> $$.tmp
      echo  >> $$.tmp
    fi
  fi
done

if [ -s $$.tmp ]; then
  mail -s "[watch.sh] $cur_time" $email < $$.tmp
fi
rm -f $$.tmp
