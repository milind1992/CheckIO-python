# migrated from python 2.7
# Generator function that generates the Fibonacci series
def fibo():
    a=1
    b=1
    c=1
    yield c
    while(True):
        c=a+b
        b=a
        a=c
        yield c
        
def checkio(opacity):
    
    # Set up the generator function
    f=fibo()
    # Set the initial parameters
    Copacity=10000
    age=0
    year=1
    # Calculate the next fibonacci number in the series , in this case the first one
    Nfibo=next(f)
    
    # Calculate the Opacity in the loop and return the age ones the Calculated opacity is equal to the actual opacity
    while(opacity!=Copacity):
        if(year==Nfibo):
            Copacity=Copacity-year
            Nfibo=next(f)           
        else:
            Copacity=Copacity+1;
        age=age+1;
        year=year+1
    return age
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"