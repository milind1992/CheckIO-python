# migrated from python 2.7
import re
from unicodedata import digit
from string import digits
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
​
def StrippedWordCheck(word):
    #assuming a word always starts with a Vowel then the even characters should be always VOWELS and odd characters should be CONSONENTS 
    for i in range(0,len(word),2):
        if word[i] not in VOWELS:
            return False
    for i in range(1,len(word),2):
        if word[i] not in CONSONANTS:
            return False
    return True
​
​
def checkio(text):
    # Changing the all the characters in the text to Uppercase
    text=text.upper()
    # Splitting the text into words
    words=re.findall('\w+', text)
    print(words)
    #Variable count the number of stripped words
    StrippedWordcount=0
    
    # For each word in the list 
    for word in words:
        # Check if it is of length 1 , if yes continue to the next word
        if len(word)==1:
            continue
        # Check if the word contains digits , if yes continue to the next word
        if re.match('.*[0-9].*', word)!=None:
            continue
        # Depending on whether the first word is a consonant or a Vowel 
        # use the right pattern to check if the word is a Scattered word , and increment the count accordingly
        
        if word[0] in VOWELS:
            if StrippedWordCheck(word):
                StrippedWordcount+=1
        else :
            if StrippedWordCheck(word[1:]):
                StrippedWordcount+=1 
    # Return the Stripped Word Count 
    return StrippedWordcount
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"