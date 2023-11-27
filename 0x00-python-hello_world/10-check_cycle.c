#include "lists.h"

/**
 * check_cycle - as the name suggests, check if there is a cycle
 * @list: the linked list to check
 * Return: 0 for none and 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ahead;
	listint_t *prev;

	if (list == NULL)
		return (0);

	prev = list;
	ahead = list->next;

	while (prev != NULL && ahead != NULL && ahead->next != NULL)
	{
		if (prev == ahead)
			return (1);

		prev = prev->next;
		ahead = ahead->next->next;
	}

	return (0);
}
