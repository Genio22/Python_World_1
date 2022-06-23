from ast import Break


password = input('Enter your Name >> ')

while True:
    try:
        #convert into str(), int(), float() 
        convert = str(password)
        count =  len(convert)
        if count < 3:
            print(f'Name must be at least 3 characters')
            break
        
        elif count > 50:
            print(f'Name can not be a maximum of 50 characters')
            break
        else:
            print(f'Hey, {convert}. Name looks good!')
            break
    except ValueError:
        #convert into str(), int(), float()
        print(f'Please type your name properly. We are watching you')
    except Exception as e:
        #It will catch error in string or sentence
        print(e)
