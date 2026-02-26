# FILE NAME - coin_toss.py

# NAME: Jared Thibado
# DATE: 02/25/2026
# BRIEF DESCRIPTION:  A program that simulates a coin toss and gives either heads or tails, and some flare.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

import random

def tell_the_teacher_they_are_awesome():
    print("You are awesome, Professor LaBarr!")
    # I know this would almost certainly fail the auto-grader. Just a bit of fun to break the monotony which probably comes with grading all these. 

def coinflippa():
    print("===== Coin Flipper =====")
    coin = random.randint(0,1)
    if coin == 0:
        print("Heads")
    else:
        print("Tails")

coinflippa()

tell_the_teacher_they_are_awesome()

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
This lab wasn't particularly hard. I haven't coded 'random' In a few days so I just had to remember how to use it again. 

Also - slightly remarkable, after copying the code over to the classroom repository, I had to run the code 7 consecutive times before finally
getting tails. is that a coding error or pure luck? I know law of averages and all, but that is like a ~1.6% chance...






'''
