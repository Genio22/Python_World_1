
started =  False
i = 1
while True:
    command = input("> ").lower()
    
    if command == "start":
        if started:
            print('car is already started')
        else:
            started = True
            print('Car is started...Ready to go')
    elif command == 'help':
        if i<3:

            print(f'''

start - to start the car
stop - to stop the car
quit - to quit the game

''')
            i=i+1
        elif i<=9:
            print(f'''

start - to start the car
stop - to stop the car
quit - to quit the game

''')
        else:
            print('Read the instraction carefully first.')

    elif command == 'stop':
        if started:
            print('Car is already stopped')
        else:
            started = True
            print('Car has stopped.')
    elif command == 'quit':
        print(f'''

I hope you like this game.  :)

''') 
        break
    else:
        print("Sorry, I don't get it. please type 'help' in the terminal. Thank you.")


#    break
