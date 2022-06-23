phone =  input('> ')
num_dic = {

    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three'
}

print ('''

    Method 1

''')
string = ''
for store in phone:
    string += num_dic.get(store, '!') + ' ' 
print (string)


print ('''

    Method 2

''')
for store in phone:
    if store == '1':
        print('one')
    elif store == '2':
        print('Two')
    elif store == '3':
        print('three')
    else:
        print('!')
