'''
Created on 26-Aug-2016
​
@author: milind
'''
def checkio(numbers_array): 
    # Convert the tuple to a List 
    numbers=list(numbers_array)
    # Use bubble sort to sort the list , but while comparing 
    # compare the absolute values 
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if abs(numbers[i])>abs(numbers[j]):
                temp=numbers[i]
                numbers[i]=numbers[j]
                numbers[j]=temp
                
    return numbers
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)
    
    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"