#include "lists.h"

/*
 * reverse_listint - a function that reverses a linked list.
 * @head: double pointer to the head of the linked list.
 * Return: pointer to the first node in the new list.
 */

void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/*
 * is_palindrome - a function in C that checks
 * if a singly linked list is a palindrome.
 * @head: double pointer to the head of the linked list.
 * @Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!dup)
		return (1);
	return (0);
}

