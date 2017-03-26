# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:55:09 2017

@author: Maharnab
"""
import sys

task = raw_input("Enter 'b' to buy an item, press 'x' to exit: ")

if (task == 'b'):
    listitems = []
    nofitems = []
    priceofitems = []
    
    while True:
        itemcode = raw_input("\nEnter the 8 digit item code. Or press 'q' " + 
                         "to quit: ")
        if (itemcode == 'q'):
            print("\nQuitting ...\n")
            break
        if (len(itemcode) != 8): 
            print("\nYour code is not 8 digits long, please try again.")
        else:
            with open("itemlist.txt") as f:
                for line in f:
                    if itemcode in line:
                        t = line.split(" ")
                        quantity = input("\nHow many number of the " +
                                         "item do you wish to purchase: ")
                        code = t[0]
                        nameofitem = t[1]
                        price = float(t[2])
                        total = (price) * int(quantity)
                        listitems.append(nameofitem)
                        nofitems.append(quantity)
                        priceofitems.append(total)
                        break
    
    print ("Your receipt is: ")
    for i in range(len(listitems)):
        print '\t', nofitems[i], listitems[i],' for the ' +
              'amount of $', priceofitems[i]
    print "Your total is: $ ", sum(priceofitems)
                                
if (task == "x"):
    sys.exit()
