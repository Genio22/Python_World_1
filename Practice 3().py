


price = input('''
Price of the house is 1M tk
How much credit do you have? >> 
''')
house_price = 10000000
try:
    con_price = int(price)
    
    if con_price >= house_price:
        calculation = (house_price * 90) / 100
        pay = con_price - calculation
        print(f'So you have to pay {pay} tk out of {calculation} tk with 10% discount')
    elif con_price < house_price :
        calculation = (house_price * 80) / 100
        pay = calculation - con_price
        print(f'So you have to pay {pay} tk out of {calculation} tk with 20% discount')
except ValueError:
    try:
        con_price =  float(price)
        if con_price >= house_price:
            calculation = (house_price * 10) / 100
            pay = con_price - calculation
            print(f'So you have to pay {pay} tk out of {calculation} tk with 10% discount')

        elif con_price < house_price :
            calculation = (house_price * 20) / 100
            pay = calculation - con_price
            print(f'So you have to pay {pay} tk out of {calculation} tk with 20% discount')
    except ValueError:
        print('Please type number :(')
except Exception as e:
       print(e)

