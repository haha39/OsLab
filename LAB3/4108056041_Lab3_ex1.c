#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc,char **argv)
{
	printf("Real Uid = %d\n""effective Uid = %d\n",getuid(),geteuid());
	return 0;
}

