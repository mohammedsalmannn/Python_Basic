'''
* @Author: Mohammed Salman
* @Date: 2021-11-08 10:59:33
* @Last Modified by:   Mohammed Salman
* @Last Modified time: 2021-11-08 10:59:33
* @Title: Program to find the flip percent of head and tail 
'''
import random

def flipCoin():
    noOfFlip = int(input("Please Enter The Number Of Times You Want To Flip A Coin: "))
    tail = 0
    head = 0
    for toss in range(noOfFlip):
        toss=random.random() #will generate a random floating-point number in the range (0.0, 1.0)
        if toss <0.5:
            tail+=1
        else:
            head+=1
        percentHead=(head/noOfFlip)*100
        percentTail=100 - percentHead 
    print("Percentage Of Head:",percentHead,"vs","Percentage Of Tail:",percentTail)
flipCoin()