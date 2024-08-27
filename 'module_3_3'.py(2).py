def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [31, 'Valeriya', True]
values_dict = {'a': 1, 'b': 5, 'c': 10}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['kitty', 10]
print_params(*values_list_2)