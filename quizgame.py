print("Welcome To Quiz Game")
play = input("do you want to play a game? ").lower()
if play !="yes":
    quit()

answer = input("who is CEO of Tesla? ").lower()
score = 0
if answer =="elon musk":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("who is CEO of google? ").lower()
if answer =="sundar pitchai":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("which is capital of india? ").lower()
if answer =="new delhi":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("12+3*2? ").lower()
if answer == 18:
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("AI stands for?  ").lower()
if answer =="artificial intelligence":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("who is a former indian cricket team captain? ").lower()
if answer =="virat kohli":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("CPU stands for? ").lower()
if answer =="central processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("RAM stands for? ").lower()
if answer =="random access memory":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("who won an oscar in music in india? ").lower()
if answer =="ar rahman":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("capital of tamilnadu? ").lower()
if answer =="chennai":
    print("correct")
    score+=1
else:
    print("incorrect")

print("you got ",score,"scores in this quiz game")
print("you got",(score/10)*100,"%.")

