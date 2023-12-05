#include "lists.h"

/**
 * is_palindrome - find if linked list is same forward and backwards
 * @head: start of the linked list
 * Return: 0 for not and 1 for palindrome
 */
int is_palindrome(listint_t **head)
{
	int i, j, len = 0;
	listint_t *current = *head;
	listint_t *temp_head = NULL, *prev;
	listint_t *temp_next = NULL, *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (current != NULL)
	{
		len++;
		current = current->next;
	}

	current = *head;
	temp_head = current;

	for (i = 0; i < len / 2; i++)
		current = current->next;
	prev = current;

	for (i = 0; i < len / 2; i++)
	{
		temp_next = temp_head->next;
		temp = temp_next->next;
		temp_head->next = temp;
		temp_head = temp_next;
	}

	temp

	/* Palindrome logic */
	for (i = 0; i < len / 2; i++)
	{
		
	}
	return (1);
}
