'''
* @Author: Mohammed Salman
* @Date: 2021-11-08 11:59:31
* @Last Modified by:   Mohammed Salman
* @Last Modified time: 2021-11-08 11:59:31
* @Title: Program to replace the string 
'''

import re
str = "Hello <<UserName>>, How are you?"
name = input("Enter A Name With Minimum Three Character: ")
if not re.match("^[aA-zZ]{3,}$", name):
    print("Name Should Have Minimum Three Character")
else:    
    str_new = str.replace('<<UserName>>', name)
    print(str_new) 