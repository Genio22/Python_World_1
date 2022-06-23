#from numpy import outer


hi = input()
dictionary = {
    '1':'one',
    '2' : 'TWO',
    '3': 'THREE'


}
output= ''
for i in hi:
    output += dictionary.get(i, '!') +  ' '
   # output +=
print(output)