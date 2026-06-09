import random
import string
def code(message):
    '''
    Coding:
        if the word contains atleast 3 characters, remove the first letter and append it at the end:
            now append three random characters at the starting and at the end
        else:
         simply reverse the string
    '''
    answer=''
    if len(message) >= 3:
        answer = message[1:]+message[0]
        for i in range(3):
            answer = string.ascii_lowercase[random.randint(0,25)] + answer + string.ascii_lowercase[random.randint(0,25)]
    else:
        answer=message[::-1]
    return answer
def decode(message):
    '''
    Decoding:
        if the word contains atleast 3 characters, remove three characters from the starting and end:
            now remove the last letter and append it at the beginnig
        else:
            simply reverse the string
    '''
    answer=''
    if len(message) >=3:
        answer = message[3:len(message)-3]
        answer = answer[len(answer)-1] + answer[:len(answer)-1]
    else:
        answer = message[::-1]
    return answer


s='''Hello user!! This is a morse code translator
which will either code normal english into
the morse language or decode it into English.

Do you want to Code or Decode??'''
print(s)
n = input()
if n == "Code" or n == "code" or n == "CODE":
    print("\nWhat is the normal message sent?")
    message = input()
    print(f"\nThe translation of this word turns to \"{code(message)}\"")
elif n == "Decode" or n == "decode" or n == "DECODE":
    print("What is the morse message sent?\n")
    message = input()
    print(f"The translation of this message turns to \"{decode(message)}\"")
else:
    print("Please enter valid input!!")
        