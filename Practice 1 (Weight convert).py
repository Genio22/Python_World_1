from logging import exception

while True:
    weight = input('What is your weight = ')
    try:
        eror = int (weight)
        unit = str(input('Type the unit name of your weight (kg) = '))
        unit_1 = unit.lower()
        if unit_1 == 'kg':
            convert_into = str(input('''Type the unit's name of your weight wants to convert (ibs, gm) = '''))
            convert_into_1 = convert_into.lower()
            if convert_into_1 == 'ibs':
                convert = str(eror * 2.20462)
                print(f'Your weight is {convert} ibs')
                break            
            elif convert_into_1 == 'gm':
                convert = str(eror * 1000)
                print('Your weight is ' + convert + ' gm')
                break            
            else :
                print('sorry! we only convert_into ibs and gm')
        else:
            print('sorry! we only except kg unit.')
    except ValueError:
        try:
            eror_1 = float(weight)
            unit = str(input('Type the unit name of your weight (kg) = '))
            unit_1 = unit.lower()
            if unit_1 == 'kg':
                convert_into = str(input('''Type the unit's name of your weight wants to convert (ibs, gm) = '''))
                convert_into_1 = convert_into.lower()
                if convert_into_1 == 'ibs':
                    convert = str(eror_1 * 2.20462)
                    print('Your weight is ' + convert + ' ibs')
                    break
                elif convert_into_1 == 'gm':
                    convert = str(eror_1 * 1000)
                    print('Your weight is ' + convert + ' gm')
                    break
                else :
                    print('sorry! we only convert_into ibs and gm')
            else:
                print('sorry! we only except kg unit.')
        except ValueError:
            print('Please type numbers or decimal numbers :( ')  
        except Exception as e:
            print(e)
            break
    except Exception as e:
        print(e)
        break
