import re
def checkio(words):
    #steup a regular expression tp set the pattern that we want to check
    regexp=r"[a-zA-Z]+\s[a-zA-Z]+\s[a-zA-Z]+"
    #return True if there is a match , else False if no match found
    return bool(re.search(regexp,words))
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"