'''
* @Author: Mohammed Salman
* @Date: 2021-11-10 10:59:33
* @Last Modified by:   Mohammed Salman
* @Last Modified time: 2021-11-10 10:59:33
* @Title:To calculate euclidean distance of x and y co-ordinates.
'''

import math
class Distance:
    @staticmethod
    def euclidean_distance():
        try:
            x_point = int(input("Enter The Number For X-Point : ")) 
            y_point = int(input("Enter The Number For Y-Point : "))
            
            distance_formula=math.sqrt(math.pow(x_point,2) + math.pow(y_point,2))#Formula To Calculate Euclidean Distance
            print("Euclidean Distance From The Points (x,y) Is :",distance_formula)
        except Exception as err:
            print("** Error **", err) 
            print("Enter Only Numbers")
Distance.euclidean_distance()   