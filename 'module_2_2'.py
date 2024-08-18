first=123
second=113
third=123

if first==second and second==third :
    print(input(3))
elif first == third or second > third :
    print(input(2))
elif second== first and third==second :
    print(input(0))
else:
    print(input('Ни одно условие не выполнено'))
