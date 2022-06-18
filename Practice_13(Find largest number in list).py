list  = [int(item) for item in input("Enter the list items : ").split()]  #input(list([list]))#[2,3,555555,67676676,8]
print(list)
max = list[0]
for i in list:
    if i> max:
        max = i
print (max)
