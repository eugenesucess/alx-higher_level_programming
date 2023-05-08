#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle -> check for repeat
 * @list: pointer to struct
 * return: 0 if no repreat 1 if repeat exist
 */

int check_cycle(listint_t *list)
{
	listint_t *prev = list, *curr = list, *nextList;

	while (prev && curr && curr->next)
	{
		prev = prev->next;
		curr = curr->next;
		nextList = curr;
		nextList = nextList->next;
		if (prev == nextList)
			return (1);
	}
	return (0);
}
