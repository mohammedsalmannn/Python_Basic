'''
* @Author: Mohammed Salman
* @Date: 2021-11-10 11:29:43
* @Last Modified by:   Mohammed Salman
* @Last Modified time: 2021-11-10 11:29:43
* @Title:To find the roots of the quadratic equation  ax**2 + bx + c = 0

'''

#Importing cmath module to perform complex square roots.
import cmath 

def quadratic_equation():
    try:
        a = int(input("Enter The Value Of a:"))
        b = int(input("Enter The Value Of b:"))
        c = int(input("Enter The Value Of c:"))
    
        delta=(b*b)-(4*a*c) #discriminant

        #Calculating root one of the quadratic equation
        root_one=((-b) + (cmath.sqrt(delta)))/(2*a)
        root_one=complex(round(root_one.real,2),round(root_one.imag,2))

        #Calculating root two of the quadratic equation
        root_two=((-b)-(cmath.sqrt(delta)))/(2*a)
        root_two=complex(round(root_two.real,2),round(root_one.imag,2))

        #Printing root one and root two 
        print("Root One Of The Equation:",root_one)
        print("Root Two Of The Equation:",root_two)
        
    except Exception as err:
        print("Root Cause Of Exception Is ::",err)
quadratic_equation()    