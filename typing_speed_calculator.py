from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(userinput)/time_r
    return round(speed) 

if __name__ == '__main__':

    while True:
        chk = input("Ready to test : y/n : ")
        if chk == "y":
            test = ["A paragraph is self contained unit of discourse in writing dealing with a particular pont or idea.", "My name is Vishal Kumar", "Welcome to My TechWorld"]

            test1 = r.choice(test)
            print("*****Typing Speed*****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input("Enter The Text : ")
            time_2 = time()

            print('Speed : ',speed_time(time_1, time_2, testinput),"w/sec")
            print('Error : ',mistake(test1, testinput))
        elif chk == "n":
            print("Thanks to give test")
            break
        else:
            print("Wrong Input")