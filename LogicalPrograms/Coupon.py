'''
* @Author: Mohammed Salman
* @Date: 2021-11-10 06:09:06
* @Last Modified by:   Mohammed Salman
* @Last Modified time: 2021-11-10 06:09:06
* @Title: To Find The Number Of Random Numbers Needed To Generate N Coupon Numbers
'''

import random
class CouponNumber:
    @staticmethod
    def distinct_coupons():

        coupon = []   #empty list
        random_numbers=0  #no.of random numbers needed to generate distinct coupons
        try:
            number=int(input("Enter The Number Of Coupons You Want To Generate: "))
            print("Distinct Coupon Numbers Generated")
            for element in range(number):
                coupon_number = random.randint(10,100)
                if coupon_number not in coupon:
                    coupon.append(coupon_number)  #adding the distinct random number gnerated to list 
                    print(coupon_number)
                    random_numbers+=1
            else:
                pass           
            print("Total Random Numbers Needed To Get All Distinct Numbers:",end = " ")
            print(random_numbers,end = " ")
        except Exception as err:
            print("Not A Valid Number",err)
CouponNumber.distinct_coupons() 