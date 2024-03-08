#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
* infinite_while - creates an infinite loop to make the program hang
* Return: 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - creates 5 zombie processes
* Return: 0 on success
*/
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == -1)
		{
			perror("fork");
			return (1);
		}
		else if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}

	infinite_while();

	return (0);
}
