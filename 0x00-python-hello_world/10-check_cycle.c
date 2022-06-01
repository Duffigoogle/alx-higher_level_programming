#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head of a listint_t list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *p1;
	listint_t *p2;

	if (list == NULL || list->next == NULL)
		return (0);

	p1 = list;
	p2 = list->next->next;
	while (p1 && p2 && p2->next)
	{
		if (p1 == p2)
			return (1);
		p1 = p1->next;
		p2 = p2->next->next;
	}
	return (0);
}
