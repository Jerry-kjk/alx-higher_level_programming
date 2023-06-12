#include "lists.h"

/*
 * is_palindrome - a function in C that checks
 * if a singly linked list is a palindrome.
 * @head: double pointer to the head of the linked list.
 * @Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *cp = *head;
	int buff[10240], init = 0, end = 0;

	if (!*head || !((*head)->next))
		return (1);

	while (cp)
	{
		buff[end] = cp->n;
		cp = cp->next;
		end++;
	}

	end--;

	while (init <= end / 2)
	{
		if (buff[init] != buff[end - init])
			return (0);
		init++;
	}

	return (1);
}
