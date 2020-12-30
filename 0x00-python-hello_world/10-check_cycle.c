#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - singly linked list
 * @list: header pointer to linked list
 * Return: int 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *tortuga = NULL, *liebre;

	tortuga = list;
	liebre = list;


	while (liebre != NULL)
	{
		if (tortuga == NULL)
			return (0);

		tortuga = tortuga->next;
		liebre = tortuga->next->next;

		if (liebre == list || liebre == tortuga)
			return (1);
	}
	return (0);
}
