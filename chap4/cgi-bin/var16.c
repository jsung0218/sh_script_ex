#include <stdio.h>

void main()
{
 int i;
 char del[3]=" ";
 printf("export ");
 for(i=1;i<0x100;i++) {
	if(i == 0x22 || i == 0x5c || i == 0x60) {
    printf("C_%02X=\"\\%c\"%s",i,i,del);
		if((i & 0x0f) > 0x09 || (i & 0xf0) > 0x90)
      printf("C_%02x=\"\\%c\"%s",i,i,del); 
	} else { 
    printf("C_%02X=\"%c\"%s",i,i,del);
		if((i & 0x0f) > 0x09 || (i & 0xf0) > 0x90)
     printf("C_%02x=\"%c\"%s",i,i,del);
	}
 }
}
