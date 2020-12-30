#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert a node.
 *@head: pointer to a head
 *@number: number to be inserted
 * Return: new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp, *temp2;


	new_node = malloc(sizeof(listint_t));
	temp = *head;
	temp2 = *head;


	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (temp->n > new_node->n)
	{
		*head = new_node;
		new_node->next = temp;
		return (new_node);
	}
	else
	{
		while (temp != NULL)
		{
			temp2 = temp;
			temp = temp->next;
			if (temp->n > new_node->n)
			{
				new_node->next = temp;
				temp2->next = new_node;
				return (new_node);
			}
		}
	}
	return (new_node);
}
