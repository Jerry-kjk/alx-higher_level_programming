#include "Pyhton.h"
#include <stdio.h>

/**
 * print_python_list - a function that gives data of the PyListObject
 * @p: the PyObject
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	size = PyList_Size(p);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - a function that cheks data of the PyBytesObject
 * @p: the PyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
	for (i = 0; i <= size && i < 10; i++)
	{
		printf("%02x", (unsigned char)string[i]);
		if (i + 1 < 10 && i + 1 <= size)
		{
			printf(" ");
		}
	}
	printf("\n");
}

/**
 * print_python_float - a function that cheks data of the PyFloatObject
 * @p: the PyObject
 */

void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = PyFloat_AsDouble(p);
	printf("  value: %f\n", value);
}
