'''
* @Author: Mohammed Salman
* @Date: 2021-11-08 11:09:33
* @Last Modified by:   Mohammed Salman
* @Last Modified time: 2021-11-08 11:09:33
* @Title: Program to find the given is leap year or  not 
'''
import re
userInputYear = input("Enter A Year: ")
if not re.match("^[0-9]{4}$", userInputYear):
    print("Year Should Be Of 4 Digit Number")
if int(userInputYear)%4 == 0:
    if (int(userInputYear)%100) != 0 | (int(userInputYear)%400 == 0):
        print(userInputYear,":Leap Year")
    else:
        print(userInputYear, ":Not A Leap Year")
else:
    print(userInputYear, ":Not A Leap Year")