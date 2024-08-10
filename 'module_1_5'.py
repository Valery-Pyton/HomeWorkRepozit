immutable_var=(1,2,3,4)
print(immutable_var)
immutable_var_2=1,2,3,4
print(immutable_var_2)
immutable_var_3= tuple([1,2,3,4])
immutable_var= 1,2,3,True,"String"
print(immutable_var)  # значения элементов кортежа не меняются,кортеж - неизменяемый объект.

mutable_list=["strawberry","blueberry","blackberry"]
print(mutable_list)
mutable_list[2] ="banana"
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list.extend (['string',2])
print(mutable_list)
mutable_list.remove("strawberry")
print(mutable_list)





