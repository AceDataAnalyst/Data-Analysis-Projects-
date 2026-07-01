dict={x:x**2 for x in range (1,11)}
print(dict)

print(f"value of key 5:{dict[5]}")
keys=dict.keys()
print(keys)

dict[11] =121
dict.pop(1)
print(dict)


for key,values in dict.items():
    print(f'{key}:{values}')


d={x:x**3 for x in range (1,11)}
print(d)
