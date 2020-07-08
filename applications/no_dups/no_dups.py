def no_dups(s):
    # Your code here
    cache = {}
    ourArr = s.split(" ")
    newStr = ""
    for i in range(len(ourArr)):
        if ourArr[i] in cache:
            cache[ourArr[i]] += 1
        else:
            cache[ourArr[i]] = 1
            newStr += ourArr[i] + " "
    if newStr.endswith(" "):
        return newStr[:-1]
    else:
        return newStr


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
