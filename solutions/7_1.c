#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){

	FILE* ptr =fopen("uni.dat","w");
	int simlen=1000000;
	srand(time(0));
	for(int i=0;i<simlen;i++){
		char s[100000];
		sprintf(s,"%lf\n",(double)rand()/(double)RAND_MAX);
		fprintf(ptr,"%s",s);
	}

	fclose(ptr);

}