#!/bin/sh

cd /
today=`date +%Y%m%d`
host=`hostname -s`
backup_dir=/tmp
OS_type=`uname`

day_before() {
  if [ "$OS_type" = "FreeBSD" ]; then
    date -v-$1d +%Y%m%d
  elif [ "$OS_type" = "Linux" ]; then
    date -d-$1day +%Y%m%d
  fi
}

backup_list="
etc
var
home/data
"

backup_exclude_list="
--exclude var/db
--exclude var/spool
--exclude var/tmp
"

delete_list="
/home/data/`day_before 7`/*
"

compress_list="
/home/data/`day_before 1`/*
"


if [ "X$delete_list" != "X" ]; then
  rm -rf `echo $delete_list`
fi

if [ "X$compress_list" != "X" ]; then
  gzip `echo $compress_list`
fi

if [ "X$backup_list" != "X" ]; then
  if [ ! -s $backup_dir/$host-$today.tgz ];then
    tar `echo $backup_exclude_list` -cpvzf $backup_dir/$host-$today.tgz `echo $backup_list`
  fi
fi

