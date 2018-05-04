import math

def romtodec(roman):
    key1 = {'I': 1, 'C': 100, 'X': 10, 'V': 5, 'M': 1000, 'L': 50, 'D': 500}
    front=0
    end=len(roman)
    #print(end)
    sum=0
   # print(key[roman[front]]+key[roman[front+1]])
    while(front<end):
       # print(key[roman[front]]<key[roman[(front+1)]])
        if(front+1<end and key1[roman[front]]<key1[roman[(front+1)]]):
            sum=sum-key1[roman[front]]+key1[roman[front+1]]
            front=front+2
           # print(sum)
            #print(front)
            #print("CASE 1")
        else:
            sum = sum + key1[roman[front]]
            front+=1
            #print(sum)
            #print(front)
            #print("CASE 2")
    return sum
def dectorom(decimal):
    rom=""
    i=1
    key = {1: 'I', 100: 'C', 10: 'X', 5: 'V',  1000:'M',50:'L',500:'D',4:'IV',9:'IX',90:'XC', 40:'XL', 900:'CM'}
   # buff = (decimal % (10 ** i)) * (10 ** (i - 1))
   # print(buff)
    #print(buff not in key)
    while True:
        print("decimal")
        print(decimal)
        buff = (decimal) * (10 ** (i - 1))
        print(buff)
        while(buff not in key and buff>0):
            rom+key[10**(i-1)]
            buff=buff-(10**(i-1))
            print("in loop"+rom)
            print(buff)
           # print(rom)

        rom=rom+(key.get(buff))
        print(rom)
        decimal =(decimal//10)
        i+=1
        if decimal==0:
            break

    return rom

while True:
    #print(key1.get(4))
    choice=input("Enter choice: r for ROman to dec,d for vice versa")
    if(choice=='r'):
        roman=input("Enter the roman numeral")
        print (romtodec(roman))
        #print(key['M'])
    elif(choice=='d'):
        decimal=int(input("Enter the decimal number"))
        print (dectorom(decimal))
    choice=input("continue?")
    if(choice=='n'):
        break
