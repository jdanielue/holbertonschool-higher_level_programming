#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - singly linked list
 * @list: header pointer to linked list
 * Return: int 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *liebre = NULL, *tortuga = NULL;
	int i;

	liebre = list;
	tortuga = list;

	while (tortuga != NULL)
	{
		tortuga = tortuga->next;
		if (liebre == list || liebre == tortuga)
			return (1);
	}
	return (0);
}
