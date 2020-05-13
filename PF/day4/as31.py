#PF-Assgn-31
def check_palindrome(word):
    #Remove pass and write your logic here
    temp_word = word[::-1]
    if word == temp_word:
        return True
    return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")