print("welcome to quiz gamae ")
name=input("enter your name ")
print("welcome ",name, "our gamw")
play= input("do you want to play our game (yes/no)  ")
score=0
if play.lower() != "yes":
    quit()

print("okay let play ")

ans=input("1 day of a week ? ")
if ans.lower() == "monday" :
    print("correct")
    score+=1
else :
        print("wrong")

ans=input("2 day of a week ? ")
if ans.lower() == "tuesday" :
    print("correct")
    score+=1
else :
        print("wrong")
ans=input("3 day of a week ? ")
if ans.lower() == "wenesday" :
    print("correct")
    score+=1
else :
        print("wrong")
ans=input("4 day of a week ? ")
if ans.lower() == "thursday" :
    print("correct")
    score+=1
else :
        print("wrong")
ans=input("5 day of a week ? ")
if ans.lower() == "friday" :
    print("correct")
    score+=1
else :
        print("wrong")
ans=input("6 day of a week ? ")
if ans.lower() == "saturday" :
    print("correct")
    score+=1
else :
        print("wrong")
ans=input("7 day of a week ? ")
if ans.lower() == "sunday" :
    print("correct")
    score+=1
else :
        print("wrong")

print("your got : ",score ,"correct answer")
print("your score : ",score)
print("your score precentage",((score/7)*100))
