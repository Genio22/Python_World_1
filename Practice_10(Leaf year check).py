def is_leap(year):
    leap = False
# year = int(input())
    a = year/4 ==year //4
    b = year/100 == year//100
    c = year/400 == year//400
    if a :
        e = not b
        if e or c:
            leap = True 
    else:
        leap = False
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))