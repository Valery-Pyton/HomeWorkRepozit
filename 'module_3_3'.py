def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
    print_params()
    print(b=25)
    print_params(c=[1,2,3])

    print()
    values_list= [Valeriya,31,True]
    print_params(*values_list)
    values_dict = {'a': 'text', 'b': False, 'c': 33}
    print_params(**values_dict)

    print()
    values_list_2 = [54.32, 'Строка']
    print_params(*values_list_2, 42)

