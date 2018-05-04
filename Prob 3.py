import getpass
def find(string,char,length):
    j=0
    while j<length:
        #print(string[j],char)
        if(string[j]==char):
            return 1
        j+=1
    return 0


def cows(word,guess):
    cow=0
    bull=0
    i=0
    while i<4:
        #print(i)
        key=find(word,guess[i],4)
        if(key>0):
            if(word[i]==guess[i]):
                cow+=1
            else:

                bull+=1

        i+=1
    print("COWS: ",cow," BULLS: ",bull)

    if(cow==4):
        return 1
    return 0

word = getpass.getpass("Enter a four letter word")
while len(word)!=4:
    word = getpass.getpass("Enter a FOUR letter word") 

i=1
while 1==1:
    print("ENTRE GUESS NO. ",i)
    guess=input()
    if(len(guess)!=4):
        print("Enter a valid string")
        continue

    game=cows(word,guess)
    if(game==1):
        print("You took ",i," guesses to win")
        break
    i+=1
