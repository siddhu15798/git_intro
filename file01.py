from itertools import permutations

def Permutations(str):
    PL = []
    for i in range(1, len(str)+1):  
        n = permutations(str, i)
        for j in list(n):
            PL.append(''.join(j))
    return PL

def isPalindrome(n):
    x = []
    for i in n:
        str1 = i
        str2 = str1[::-1]
        if str1 == str2:
            x.append(str1)
    return x

z = input("enter the string \n")
a = Permutations(z)
b = isPalindrome(a)
print(set(b))