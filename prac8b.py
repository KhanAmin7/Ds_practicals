# B. Write a program to implement the concept of linear probing. 
list_ = [113 , 117 , 97 , 100 , 114 , 108 , 116 , 105 , 99]
 
 
hash_values = []
def hash_func(list_):
    list_2 = [None for i in range(11)]
    for i in list_:
        #print(i % len(list_2))
        hash_values.append(i % len(list_2))
        list_2[i % len(list_2)] = i
    print(list_2)
    print(list_)
    print(hash_values)
    print(116 % 11)
    print(97 % 11)
 
print(hash_func(list_))

