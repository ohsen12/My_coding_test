def solution(myString):
    for i in myString:
        if i.isupper():
            myString = myString.replace(i, i.lower())
    return myString.replace('a','A')
    