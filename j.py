def my_fun():
    my_list=[1,2,3,4,1,2,3,4,1,2,3,4]
    return sum((set(my_list)))

print(my_fun())