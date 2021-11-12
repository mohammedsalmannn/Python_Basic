'''
* @Author: Mohammed Salman
* @Date: 2021-11-10 03:23:06
* @Last Modified by:  Mohammed Salman
* @Last Modified time: 2021-11-10 03:23:06
* @Title: Simulate a gambler who starts with $stake and place fair $1 bets until he/she goes broke (i.e. has no money) or reached $goal
'''

import random
    
bet_amount=1
def gamblerProblem():
    stake=int(input("Enter The The Stake Amount:"))
    goal=int(input("Enter The Amount You Want To Win:"))
    bet_made=int(input("Enter The The Number Of Bets You Want To Make:"))
    no_of_times_won=0
    no_of_time_lost=0
    no_of_bets_made=0

    while(stake >= 0 and stake <= goal and no_of_bets_made < bet_made):
        no_of_bets_made+=1
        gambler_choice=random.random() #generates a random floating-point number in the range (0.0, 1.0)
        
        if gambler_choice>0.5:   #if the random number generated is above 0.5 then the gamble wins, or else he/she looses
            no_of_times_won+=1
            stake=stake+1 
        else:
            no_of_time_lost+=1
            stake=stake-1

    print("Number Of Times Won",no_of_times_won)
    print("Percentage Of Win", (no_of_times_won/bet_made)*100) 
    print("Percentage Of Loss", (no_of_time_lost/bet_made)*100)
    print("Number Of Bets Made", no_of_bets_made) 
    
gamblerProblem()         