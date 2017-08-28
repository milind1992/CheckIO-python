import string
def find_message(text):
    """Find a secret message"""
    final_string=""
    for i in range (0,len(text)):
        if text[i]in string.ascii_uppercase:
            final_string+=text[i]
            
    return final_string
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"