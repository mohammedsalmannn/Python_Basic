'''
* @Author: Mohammed Salman
* @Date: 2021-11-08 10:59:33
* @Last Modified by:   Mohammed Salman
* @Last Modified time: 2021-11-08 10:59:33
* @Title: Program to find the harmonic number
'''

try:
    number = int(input("Enter A Number: "))
    assert number!=0
except:
    print("Number Is Zero")
else:    
    harmonic=0
    for i in range(1,number+1):
        harmonic=harmonic+1/i
        print(harmonic)