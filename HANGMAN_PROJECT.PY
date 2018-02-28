##HANGMAN_PROJECT
##BY - PRANJAL GUPTA 

import turtle,random

#--------------------------------------variables----------------------------------------# 
wrong_attempts = 0
word_list = ['madagascar','ong bak','constantine', 'conjuring', \
              'shrek','hulk','avengers','iron man', \
              'avatar','interstellar','gravity','terminator', \
              'oblivion','argo','xmen','inception','rush','rush hour', \
              'despicable me','cars','sky fall','sky high','casino royale']
guess_word = word_list[random.randint(0,len(word_list)-1)]
append_list = []
input_list = []
#-------------------------------------variables---------------------------------------# 

#------------------------------------FUNCTIONS()---------------------------------------# 
def Init_State():
    turtle.lt(90)
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(100)
    turtle.goto(50,200)
    turtle.rt(90)

def Game_State():
    for i in range (0,len(append_list)):
        print append_list[i],
    print 

def Hangman_Draw(n):
    if n == 1:
        turtle.fd(30)
        turtle.pu()
        turtle.goto(30,150)
        turtle.pd()
    if n == 2:
        turtle.circle(20)
        turtle.pu()
    if n == 3:
        turtle.goto(50,127)
        turtle.pd()
        turtle.fd(75)
    if n == 4:
        turtle.goto(0,10)
        turtle.goto(50,52)
    if n == 5:
        turtle.goto(110,10)
        turtle.pu()
    if n == 6:
        turtle.goto(50,107)
        turtle.pd()
        turtle.goto(90,67)
    if n == 7:
        turtle.goto(50,107)
        turtle.pd()
        turtle.goto(10,67)
        turtle.pu()

def Win_Screen():
    turtle.clear()
    turtle.pu()
    turtle.goto(0,0)
    turtle.write(" CONGRATULATIONS !! YOU WIN !! ",align="center",font=("courier",40))
    
def Lose_Screen():
    turtle.clear()
    turtle.pu()
    turtle.goto(0,0)
    turtle.write(" GAME OVER !! YOU LOSE !! ",align="center",font=("courier",40))
#------------------------------------FUNCTIONS()---------------------------------------#  

#------------------------------------GAME_LOOP()---------------------------------------# 
for i in range (0,len(guess_word)):
    if  guess_word[i] == " " or guess_word[i] ==  'a' or \
        guess_word[i] == 'e' or guess_word[i] == 'i' or \
        guess_word[i] == 'o' or guess_word[i] == 'u':
        append_list.append(guess_word[i])
    else:
        append_list.append("_")



Init_State()
while wrong_attempts <= 7:
    Game_State()
    guess_letter = raw_input ("guess any letter")
    if guess_letter in input_list :
        print guess_letter, "already guessed"
        continue
    else:
        input_list.append(guess_letter)
    
    for i in range (0,len(guess_word)) :
        if guess_word[i] == guess_letter :
            append_list[i] = guess_letter
            
    if guess_letter not in guess_word :
        wrong_attempts += 1
        Hangman_Draw(wrong_attempts)

    if append_list == list(guess_word) and wrong_attempts < 7 :
        print 
        for i in range (0,len(guess_word)) :
            print guess_word[i],
        print 
        print " CONGRATULATIONS !! YOU WIN !! "
        Win_Screen()
        break

    elif append_list != list(guess_word) and wrong_attempts >= 7:
        print 
        for i in range (0,len(guess_word)) :
            print guess_word[i],
        print 
        print " GAME OVER !! YOU LOSE !! "
        Lose_Screen()
        break
    print 

#------------------------------------GAME_LOOP()---------------------------------------#   
        
    
           
    
