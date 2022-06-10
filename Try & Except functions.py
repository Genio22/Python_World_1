
try:
    #convert into str(), int(), float() 
    convert = int()
except ValueError:
    #convert into str(), int(), float()
    convert =  float() 
except Exception as e:
    #It will catch error in string or sentence
    print(e)
