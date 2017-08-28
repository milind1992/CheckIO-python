# migrated from python 2.7
import re
​
def checkio(data):
​
    # checking if the input variable is in the required format
    caps=".*[A-Z]+.*"
    small=".*[a-z]+.*"
    digits=".*[0-9]+.*"
     
    #Checking one condition at a time
    if len(data)<10:
        return False   
    elif bool(re.match(caps, data))==False:
        return False
    elif bool(re.match(small, data))==False:
        return False
    elif bool(re.match(digits, data))==False:
        return False
    #If all the conditions are met then return True
    else : 
        return True
​
#Some hints
#Just check all conditions
​
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"