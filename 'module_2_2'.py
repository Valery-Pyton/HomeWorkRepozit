first=123
second=113
third=123

if first==second and second==third :
    print(3)
elif first == third or second > third :
    print(2)
elif second== first and third==second :
    print(0)
else:
    print('Ни одно условие не выполнено')
