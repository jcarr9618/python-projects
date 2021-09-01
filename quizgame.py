print ("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay. Let's play then: ")
score = 0
answer = input ("What does the acronym CPU stand for? ")
if answer.lower() == "central processing unit":
    print ('Correct!')
    score +=1
else: 
    print ('Incorrect! ')

answer = input ("What does the acronym VDU stand for? ")
if answer.lower() == "visual display unit":
    print ('Correct!')
    score +=1
else: 
    print ('Incorrect! ')
    
answer = input ("What does the acronym GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print ('Correct!')
    score +=1
else: 
    print ('Incorrect! ')
    
answer = input ("What does the acronym PSU stand for? ")
if answer.lower() == "power supply unit":
    print ('Correct!')
    score +=1
else: 
    print ('Incorrect! ')

print ("You got " + str((score/4) * 100) + "%.")


    
