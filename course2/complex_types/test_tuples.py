
tuple1 = ('string', 'one more')

new_tuple1 = tuple()
for item in tuple1:
    if not isinstance(item, int):
        new_tuple1 += (item, )
    else:
        print('error')
print(new_tuple1)
