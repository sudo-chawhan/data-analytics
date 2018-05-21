#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){

	FILE* ptr =fopen("s.txt","w");
	int simlen=1000000;
	srand(time(0));
	for(int i=0;i<simlen;i++){
		double si=0;
		for(int j=0;j<12;j++){
			double s=(double)rand()/(double)RAND_MAX;
			si+=s;
		}
		si-=6;
		char s[100000];
		sprintf(s,"%lf\n",si);
		fprintf(ptr,"%s",s);
	}

	fclose(ptr);

}