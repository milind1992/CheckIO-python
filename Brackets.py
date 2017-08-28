# migrated from python 2.7
def checkio(expression):
    # Stack used to store all the brackets that are encountered in the program
    stack=[]
    # Maps the right closing bracket to the right opening bracket
    bracket_dictionary={')':'(',']':'[','}':'{'}
    
    
    for element in expression:
        # If the element is a opening bracket then push the bracket to the stack 
        if element in list(bracket_dictionary.values()):
            stack.append(element)
        # If the element is a closing bracket then pop the top element from the stack and check if it maps to the right opening bracket
        # else return False
        # if the stack is empty then return False 
        elif element in list(bracket_dictionary.keys()):
            try :
                if stack.pop()!=bracket_dictionary[element]:
                    return False
            except IndexError:
                return False
              
    
    # after processing the expression if the stack is not empty then return False 
    # Else return True
    if len(stack)!=0:
        return False
    else:
        return True
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"