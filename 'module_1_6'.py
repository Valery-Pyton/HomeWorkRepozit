my_dict={'Lera':1992,'Masha':2000,'Olga':2016,'Oleg':2020}
print(my_dict['Lera'])
my_dict['Pavel']= 2003
print(my_dict)
print(my_dict.get('Max'))
my_dict['Sasha']=2022
my_dict['Misha']=2023
print(my_dict)
print(my_dict.pop('Masha'))
print(my_dict)


my_set={3,5,10,15,17,3,5,10,'String',True,3,5,10}
print(my_set)
print(list(my_set))
my_set={3,5,10,15,17,3,5,10,'String',True,3,5,10}
my_set.add(4)
print(my_set)
my_set={True, 17, 3, 'String', 5, 4, 10, 15}
my_set.add(20)
print(my_set)
{True, 3, 4, 5, 10, 'String', 15, 17, 20}
list=[True, 'String', 3, 4, 5, 10, 15, 17, 20]
my_set=set(list)
my_set.remove(17)
print(my_set)










