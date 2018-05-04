
def printDay( k  ):
    if(k==0):
        buff="SUN"
    if(k==1):
        buff="MON"
    if(k==2):
        buff="TUES"
    if(k==3):
        buff="WEDNES"
    if(k==4):
        buff="THURS"
    if(k==5):
        buff="FRI"
    if(k==6):
        buff="SATUR"
    buff+="DAY"
    print(buff)
    return

refd=3
refdd=1
refmm=1
refyyyy=1800
day=refd
m=0
print("Enter the DD, MM and YYYY seperately when prompted")
while 1==1:
    dd=int(input("Enter day"))
    mm=int(input("Enter month"))
    yyyy=int(input("Enter year"))
    while m<mm-1:

        if m==0 or m==2 or m==4 or m==6 or m==7 or m==9:
            day=(day+31)%7

        elif m==1:
            day=(day+0)%7
        else:
            day=(day+30)%7
        m+=1
    day=(day+(dd-refdd))%7
    y=refyyyy
    while y<yyyy:
        day=(day+1)%7
        if y%4==0:
            day = (day + 1) % 7
        if y%100==0:
            if y%400==0:
                day=day+0
            else:
                day=(day-1)%7
        y+=1
    printDay(day)
    print("Continue?")
    choice=input()
    if choice=="N" or choice=='n':
        break



