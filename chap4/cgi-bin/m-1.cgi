#!/bin/sh

parse() {
fields=`echo $1| sed -e "s/^/export r_type=\"/" -e "s/\|/\" r_path=\"/" -e "s/\|/\" r_title=\"/" -e "s/\|/\" r_content=\"/" -e "s/$/\"/"`
eval $fields
}

print_http_header() {
if echo "$HTTP_USER_AGENT"  | grep Mozilla  > /dev/null
then
  echo "Content-Type: text/html"
  export c_type="mhtml" newline="<br>"
else 
  echo "Content-Type: text/vnd.wap.wml;charset=ks_c_5601-1987"
  export c_type="wml" newline="<br/>"
fi
echo
}

print_header() {
  if [ "$c_type" = "mhtml" ];then
    echo "<html>"
    echo "$r_title$newline"
  else
    cat <<EOM
<?xml version="1.0" encoding="KS_C_5601-1987"?>
<!DOCTYPE wml PUBLIC "-//WAPFORUM//DTD WML 1.1//EN" "http://www.wapforum.org/DTD/wml_1.1.xml">
<wml>
<template>
<do type="options" label="Back">
<prev/>
</do>
</template>
<card>
<p align="center">$r_title</p>
<p align="left">
EOM
  fi
}

print_footer() {
  if [ "$c_type" = "mhtml" ];then
    echo "</html>"
  else
    echo "</p></card></wml>"
  fi
}


print_mobile() {

if [ "$1" = "" ]; then
  url="/home"
else
  url=$1
fi
record=`grep "|$url|" mobile.data`
parse "$record"

print_http_header
print_header

if [ "$r_type" = "D" ];then
  grep "|$url/[^/|]*|" mobile.data | while read record
  do
    parse "$record"
    if [ "$r_type" = "L" ];then
      echo "<a href=\"$r_content\">$r_title</a>$newline"
    else
      echo "<a href=\"/cgi-bin/m-1.cgi?url=$r_path\">$r_title</a>$newline"
    fi
  done
elif [ "$r_type" = "C" ];then
  if [ "$c_type" = "wml" ];then
    echo "$r_content" |sed -e "s/<br>/<br\/>/g"
  else
    echo "$r_content" 
  fi  
fi

print_footer

}

. ./var16.sh

if [ "X$REQUEST_METHOD" = "XPOST" -a "$CONTENT_LENGTH" -gt 0 ]; then
  QUERY_STRING="${QUERY_STRING}&"`dd count=$CONTENT_LENGTH bs=1 2> /dev/null`
fi

if [ "X$QUERY_STRING" != "X" ]; then
query=`echo "$QUERY_STRING\"" | sed -e "s/^&*//" -e "s/&/\";/g" -e "s/=/=\"/g" -e "s/+/ /g" -e "s/%/\\$C_/g" -e "s/C_[0-9a-fA-F][0-9a-fA-F]/\{&\}/g"`
eval $query
fi

print_mobile $url
