'''
* @Author: Mohammed Salman
* @Date: 2021-11-08 11:15:33
* @Last Modified by:   Mohammed Salman
* @Last Modified time: 2021-11-08 11:15:33
* @Title: Program to find the power of Two
'''
try:
    power = int(input("Enter A power:"))
    if power >31:
        raise ValueError("Entered A Number Greater Than 31")
    number = 1
    for i in range(power):
        number = number *2
        print(number)    
except Exception as err: # err is just a variable name
    print("Root cause of exception is::",err)