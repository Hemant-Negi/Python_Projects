# 1.understand the problem
# 2.think
# 3.algorithm
# 4.main logic
# 5.Modify
# YOU + Machine + Internet + Programming

import random
print("""                           
        This is a Dice Simulator           """)
x = 'y'
while(x == 'y'):
    num = random.randint(1, 6)
    print("        Number on dice is:          ")
    if(num == 1):
        print("""
             ---------
            |         |
            |    *    |
            |         |
            ----------
            """)
    elif(num == 2):
        print("""
            -----------
            |         |
            |  *   *  |
            |         |
            ----------
            """)
    elif(num == 3):
        print("""
             ---------
            |         |
            | *  *  * |
            |         |
            ----------
            """)
    elif(num == 4):
        print("""
            -----------
            |  *    *  |
            |          |
            |  *    *  |
            ------------
            """)
    elif(num == 5):
        print("""
             ----------
            |  *    *  |
            |    *     |
            |  *    *  |
            ------------
            """)
    elif(num == 6):
        print("""
             ----------
            |  *    *  |
            |  *    *  |
            |  *    *  |
            ------------
            """)
    x=input("y to continue:")
