from bs4 import BeautifulSoup as BS
import urllib.request
def convert_spaces(s):
    x=0
    
    while(x<len(s)):
        if(s[x]==' '):
            s=s[:x]+'_'+s[x+1:]
        x+=1
    return str(s)
while 1==1:
    word=input("Enter a word : ")
    word=convert_spaces(word)

    source="https://en.oxforddictionaries.com/definition/"+word
    page=urllib.request.urlopen(source)
    body=page.read()
    soup=BS(body, 'html.parser')
    page.close()
    abc=soup.find_all("span",class_="ind" )
    if(len(abc)):
        for it in abc:
            char=str(it)
            actual_char=char[18:len(char)-7]
            #print("This word means : ")
            print(actual_char)
            print('\n')
            break
    else:
        print("Word not valid")
    choice=input("Press Y to continue, N to exit : ")
    if(choice=='N' or choice=='n'):
        break

    
