# import needed libraries
import string

# Funny Colorful in ASCII when program start
title = """\033[94m
\033[1;31m██████╗\033[0m     \033[1;32m███████╗\033[0m    \033[1;33m███████╗\033[0m    \033[1;34m███████╗\033[0m
\033[1;31m██╔══██╗\033[0m    \033[1;32m██╔════╝\033[0m    \033[1;33m██╔════╝\033[0m    \033[1;34m██╔════╝\033[0m
\033[1;31m██████╔╝\033[0m    \033[1;32m███████╗\033[0m    \033[1;33m███████╗\033[0m    \033[1;34m█████╗\033[0m  
\033[1;31m██╔═══╝\033[0m     \033[1;32m╚════██║\033[0m    \033[1;33m╚════██║\033[0m    \033[1;34m██╔══╝\033[0m  
\033[1;31m██║\033[0m         \033[1;32m███████║\033[0m    \033[1;33m███████║\033[0m    \033[1;34m███████╗\033[0m
\033[1;31m╚═╝\033[0m         \033[1;32m╚══════╝\033[0m    \033[1;33m╚══════╝\033[0m    \033[1;34m╚══════╝\033[0m
\033[1;31mPassword    \033[1;32mSecurity    \033[1;33mStrength    \033[1;34mEvaluator
\033[0m"""

print(title)

def main():
    # user add the password to check
    password = input("\033[1;31mEnter The Password: \n\033[0m")
    if password == "":
        print("\033[1;31mNo Input!! Try again\n\033[0m")
        return main()
    
    # get the length of passwrod that user added
    lenght = len(password)
    level = 0 
    
    # make a bool variables of rules we need to check out
    lowercase = False
    uppercase = False
    digits = False
    symbols = False

    # loop in the password looking for if rules done
    for i in password:
        if i in string.ascii_lowercase:
            lowercase = True
        if i in string.ascii_uppercase:
            uppercase = True
        if i in string.digits:
            digits = True
        if i not in string.ascii_lowercase and i not in string.ascii_uppercase and i not in string.digits:
            symbols = True
    
    # print new values of rules
    print("\nwhat we found in your password(",password,"):")  
    print("contain lowercase: ", lowercase)
    print("contain uppercase: ", uppercase)
    print("contain digits: ", digits)
    print("contain symbols: ", symbols)
    print("length of password: ", lenght)
    
    # here we decied what level of strong of the password
    if lenght > 8:
        level += 1

    if lowercase == True:
        level += 1

    if uppercase == True:
        level += 1

    if digits == True:
        level += 1

    if symbols == True:
        level += 1

    # if all done but password less than 6 letters wo it will be week password
    if lenght < 6:
        level = 1

    # output how much password strong with some colors for every level
    if level == 1:
        print("\033[1;31mWeek Password! level is:",level,"\033[0m")

    if level == 2:
        print("\033[1;34mBad Password, level is:",level,"\033[0m")

    if level == 3:
        print("\033[1;33mMedium Password, level is:",level,"\033[0m")

    if level == 4:
        print("\033[1;92mGood Password, level is:",level,"\033[0m")

    if level == 5:
        print("\033[1;32mStrong Password, level is:",level,"\033[0m")
        
    # ask for test other password
    while True:
        q = input("\nAgain? (y/n) ")
        if q == "y" or q == "":
            return main()
        elif q == "n":
            exit()       
        else:
            print("\033[1;31mwronge input!\033[0m")
            
# call main function
main()
