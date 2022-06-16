def is_leap(year):
    leap = True
    a = year/4
    b = year/100
    c = year/400
    d = year//400
    if a and b and c==d:
        leap = True  
    else:
        leap = False
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))