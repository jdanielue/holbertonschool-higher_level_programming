#include "lists.h"
/**
 * check_cycle - singly linked list
 * @list: header pointer to linked list
 * Return: int 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *liebre = NULL;
	int i;

	liebre = list;

	while (list != NULL)
	{
		for (i = 0; i < 5; i++)
		{
			liebre = list->next->next;
			if (liebre == NULL)
				return (0);
			if (liebre == list)
				return (1);
		}
	list = list->next;
	}
	return (0);
}
