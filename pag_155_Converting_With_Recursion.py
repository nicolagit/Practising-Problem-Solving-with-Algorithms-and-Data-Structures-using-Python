'''
Created on Jul 26, 2020

@author: nicola
'''

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]
    
print(toStr(769,10))
print(toStr(10,2))
