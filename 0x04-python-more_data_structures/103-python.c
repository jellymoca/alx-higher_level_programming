#include <stdio.h>
#include <Python.h>

/**
* print_python_list - Prints list information
*
* @p: Python Object
* Return: no return
*/

void print_python_list(PyObject *p)
{
Py_ssize_t size, alloc, i;
PyObject *item;

size = PyList_Size(p);
alloc = ((PyListObject *)p)->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
* print_python_bytes - Prints bytes information
*
* @p: Python Object
* Return: no return
*/

void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *s;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
s = PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", s);

printf("  first %ld bytes: ", (size < 10) ? size : 10);
for (i = 0; i < ((size < 10) ? size : 10); i++)
printf("%02x%c", (unsigned char)s[i], i == 9 ? '\n' : ' ');
}
