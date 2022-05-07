# -*- coding: utf-8 -*-
"""
Created on Sun May  8 06:36:32 2022

@author: Happy
"""
#作業一
n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end="")
    print()

#作業二
n = int(input("Enter number of rows: "))

for i in range(5,0,-1):
    for j in range(0,i):
        print(i, end="")
    print()
    
#作業三
n = int(input("Enter number of rows: "))

for i in range(9,0,-2):
    for j in range(0,i):
        print(i, end="")
    print()
    
#作業四
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input('Input a number: '))
for i in range(2, n + 1):
    i_is_prime = is_prime(i)
    if i_is_prime:
        print(i)