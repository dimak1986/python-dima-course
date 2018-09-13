
tuple1 = ('string', 'one more')

new_tuple1 = tuple()
for item in tuple1:
    if not isinstance(item, int):
        new_tuple1 += (item, )
    else:
        print('error')
print(new_tuple1)

import copy

var = {'list': [[1, 2], ['a', 'b']], 'tuple': ('foo', 'bar', )}
new_var = copy.deepcopy(var)
var.update({'str': 'string'}) #NEw key and value added
var['list'].append([True, False]) #in dict: 'list' (key) added another list
var['tuple'] += ('baz', ) # New string added to existing 'tuple'

print(var)
print(new_var)
