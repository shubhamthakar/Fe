import random
inpt=input("multiplayer game y/n")
if inpt=="n":
    f=open("words.txt","r")
    content=f.read().split('\n')                      #content is list of words
    oword=list(random.choice(content))                #original word(oword) is list of alphabets
    for i in range (0,len(oword)):
        if oword[i] == " ":                                           #repalcing space with underscore
            oword[i]="_"
elif inpt=="y":
    content=input("Player 1 Enter Movie name")
    oword=list(content)
    for i in range (0,len(oword)):
        if oword[i]==" ":
            oword[i]="_"
else:
    print("Enter a valid input")
#print(oword)
length=len(oword)
uword=[]
for i in range (0,length):
    uword.append("_")                                               #creating a list of underscores
i=length
flag=0
while((i+2)!=0):
    print("You have ",i+2," attempts left")
    a=input("Enter an alphabet")
    counter=0
    for j in range (0,length):
        if a=="_":
            print("Enter a valid lower case alphabet")
            counter=1
            break
        elif a==uword[j]:
            print("You have already entered this alphabet earlier")
            counter=1
            break
        elif ord(a)<97 or ord(a)>122:
            print("Enter a valid lower case alphabet")
            counter=1
            break
        elif a==oword[j]:
            uword[j]=a
            counter=1
    if(counter==0):
        print("Try another alphabet")
        i=i-1
    print(uword)
    if (uword==oword):
        print("Congratulations!! you have guessed the movie")
        flag=1
        break
if flag==0:
    print("Sorry no attempts left. The movie was ",oword," Try again")