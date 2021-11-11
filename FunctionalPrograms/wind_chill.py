'''
* @Author: Mohammed Salman
* @Date: 2021-11-11 10:21:23
* @Last Modified by:   Mohammed Salman
* @Last Modified time: 2021-11-11 10:21:23
* @Title:To Calculate Wind Chill. 
'''
'''
* @Author: Mohammed Salman
* @Date: 2021-11-10 11:29:43
* @Last Modified by:   Mohammed Salman
* @Last Modified time: 2021-11-10 11:29:43
* @Title:To Calculate Wind Chill.

'''


import math
def wind_chill():
    try:
        t = float(input("Enter A Value For Temperature:"))
        v = float(input("Enter A Value For Wind Velocity:"))
        if (v>=3 and v<=120 and t <=50):
            w=round((35.74 + 0.6215*t + (0.4275*t - 35.75)*math.pow(v,0.16)),2)   #Equation for wind chill
            print("Wind Chill Is :",w,"Degree Fahrenheit")
        else:
             print("Temperature(t) Should Be Less Than 50 degree F And Velocity(v) Should Be Between 3 and 120 mph")   
    except Exception as err:
        print("Root Cause Of Exception Is ::",err)
wind_chill()        