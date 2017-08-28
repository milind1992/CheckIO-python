def checkio(data):
​
    count=1
    data =str(data)
    rdata=data[::-1]
    # Dictionary used to Map the digits place to Roman Numbers
    Conv = {1: 'VI', 2: 'LX', 3: 'DC', 4: '_M'}
    roman_num=''
    Cplace=''
​
    # Go one digit at a time.
    # There are different symbols for 1,4,9 and 5
    # Using if condition to assign a Seperate symbol
    for digit in rdata:
        if int(digit)==4:
            Cplace=Conv[count][::-1]+Cplace
        elif int(digit)==9:
            Cplace=Conv[count][1]+Conv[count+1][1]
        elif int(digit)>=5:
            Cplace=Conv[count][0]+Cplace
            Cplace=Cplace+Conv[count][1]*(int(digit)%5)
        else:
            Cplace = Cplace + Conv[count][1] * (int(digit) % 5)
​
        roman_num=Cplace+roman_num
        count=count+1
​
        Cplace=''
    return roman_num
​
if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'