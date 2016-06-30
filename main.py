import os
import math
import subprocess
import random
import urllib
fname = open('name','r')
name = fname.read()
fname.close()
fcolor = open("color","r")
color = fcolor.read()
fcolor.close()
os.system('color %s' % color)
print("Hey %s, here we are again !\n" % name)
os.system('pause')
os.system('cls')
i=0
while i==0:
    os.system('cls')
    print('Kurti\n____________________________________________________________________________\n')
    print("Type a command or write 'help' for the commands list.\n")
    fspeak = open('speak','w')
    fspeak.write('Scrivi un comando')
    fspeak.close()
    os.system('start speak.exe')
    action = input('')
    if action=='help':
        print('I can perform a lot of function, this is a list of the principal commands:\n')
        fspeak = open('speak','w')
        fspeak.write('Ecco una lista dei comandi principali')
        fspeak.close()
        os.system('start speak.exe')
        print("calculator() --> Open the calculator (You can also type <<I want to do a calculation>>)")
        print('learn() --> With this command I can learn new definitions')
        print('read() --> With this command I can learn new definitions')
        print("ip() --> Control your connection status(You can also type <<I want to see my Internet connection>>)\n")
        print("For change the text color, type <<I don't like this color>>")
        os.system('pause')
        os.system('cls')
    if action == 'calculator' or action=="I want to do a calculation":
        os.system('start calculator.py')
        os.system('cls')
    if action=='learn':
        fspeak = open('speak','w')
        fspeak.write('Di che si tratta ?')
        fspeak.close()
        os.system('start speak.exe')
        oggetto=input("Define the object: ")
        fspeak = open('speak','w')
        fspeak.write("Cos'è %s" % oggetto)
        fspeak.close()
        os.system('start speak.exe')
        definizione=input("What is %s ?\n" % oggetto)
        foggetto=open(oggetto,'w')
        foggetto.write(definizione)
        foggetto.close()
    if action=='read':
        fspeak = open('speak','w')
        fspeak.write('Di che si tratta ?')
        fspeak.close()
        os.system('start speak.exe')
        oggetto=input('Definition to read: ')
        if os.path.exists(oggetto):
            foggetto=open(oggetto,'r')
            definizione=foggetto.read()
            foggetto.close()
            fspeak = open('speak','w')
            fspeak.write('%s' % oggetto)
            fspeak.close()
            os.system('start speak.exe')
            print('%s:' % oggetto)
            fspeak = open('speak','w')
            fspeak.write('%s' % definizione)
            fspeak.close()
            os.system('start speak.exe')
            print('%s' % definizione)
            os.system('pause')
        else:
            print("The definition doesn't exists. To add one type 'learn'")
            os.system('pause')
    if action=='ip' or action=="I want to see my Internet connection":
        os.system('ipconfig')
        os.system('pause')
    if action=='shutdown':
        boolean=input('Do you really want to turn off your PC ?[Y/N]\n')
        if boolean=='S':
            os.system('shutdown -s')
        else:
            print('Operation canceled.')
            os.system('pause')
    if action=='notepad':
        subprocess.Popen('notepad.exe')
    if action=="hello it's me":
        print("I was wondering if after all these years you'd like to meet")
        os.system('pause')
    if action=="game":
        print('We play !\n')
        os.system('pause')
        os.system('cls')
        x=random.randint(1,10)
        tentativi=3
        t=0
        while t==0:
            print('GUESS THE NUMBER\n____________________________________________________________________________\n')
            print('I thought a random number 1 to 10. Try to guess it !')
            if tentativi != 0:
                n_gioco=int(input('Try a number: '))
                tentativi=tentativi-1
                if n_gioco==x:
                    print('Compliments ! You guessed.\n')
                    os.system('pause')
                    t=1
                else:
                    print('Oh no, You were wrong !\n')
                    if n_gioco > x:
                        print('The number I thought is minor\n')
                        os.system('pause')
                        os.system('cls')
                    if n_gioco < x:
                        print('The number I thought is major\n')
                        os.system('pause')
                        os.system('cls')
            else:
                print('Game over, you finished your attempts. :(')
                os.system('pause')
                t=1
    if action=="exit":
        print("Bye bye %s\n" % name)
        os.system('pause')
        i=1
    if action=="I don't like this color":
        print("1 = Blue\n2 = Green\n4 = Bordeaux\n5 = Violet\n8 = Grey\nb = White Blue\nc = Red\ne = Yellow\nf = White")
        color = input("What's your favourite color ?\n")
        os.system("color %s" % color)
        fcolor = open("color","w")
        fcolor.write(color)
        fcolor.close()
        print("New text color saved !\n")
        os.system('pause')
    if action=="Kurti":
        print('Sempre a disposizione')
        os.system('pause')
    if action=="kurti":
        print('Sempre a disposizione')
        os.system('pause')
    if action=="hello":
        print("Hello, %s\n" % name)
        y=random.randint(1,3)
        if y==1:
            status=input("How are you ?\n")
            print("What's your favourite sport ?\n")
        if y==2:
            status=input("How do you feel like ?\n")
            print("What's your favourite song ?\n")
        if Y==3:
            status=input("How do you feel like today ?\n")
            print("What's your favourite film ?\n")
