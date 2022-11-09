#!/usr/bin/env python3

# introductory text
print('Hello, and welcome to the Kuehn gift registration. Please answer all questions as prompted.')

print('What is your name?:')

name=input(' ')

gifts = []

print('What would you like for Christmas? (or enter nothing to stop your list)')

#loop to get input until nothing is entered
while True:

    gift = input()

    if gift==(''):

        break
    gifts = gifts + [gift]

#saves the output of the terminal window to a txt file
giftlist = open('giftlist.txt', 'a+')

print( name + ' has asked for:', file=giftlist)

for gift in gifts:

    print('  ' + gift, file=giftlist)

print('', file=giftlist)
giftlist.close()

#prints in the terminal back what gifts the person asked for
print('Thanks ' + name + '!! Your gifts are:')

for gift in gifts:

    print('  ' + gift)

print('We have saved your gifts to santas list')

#saves to another file with the name as list label and the gifts as a list
list = open('list2.py', "a+")

list.write("%s = %s\n" %(name, gifts))

list.close()
