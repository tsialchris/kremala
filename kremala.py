print('Αυτό είναι ένα παιχνίδι κρεμάλας')
i=0
check=['','','','','','','','','','']
w0=['μ','α','κ','α','ρ','ο','ν','ι','α']
w1=['α','θ','η','ν','α']
w2=['θ','ε','σ','σ','α','λ','ο','ν','ι','κ','η']
w3=['λ','ε','υ','κ','ω','σ','ι','α']
w4=['π','α','ν','ε','π','ι','σ','τ','η','μ','ι','ο']
w5=['π','ο','ρ','τ','ο','φ','ο','λ','ι']
w6=['λ','ο','υ','λ','ο','υ','δ','ι']
w7=['π','ο','ρ','τ','ο','κ','α','λ','α','δ','α']
w8=['β','ι','β','λ','ι','ο','θ','η','κ','η']
w9=['σ','τ','α','τ','ι','σ','τ','ι','κ','η']
list1=[w0,w1,w2,w3,w4,w5,w6,w7,w8,w9]
score=0
while(i<10):
    wrongletters=['','','','','','','','','','','','','','','','','','','','','']#wrong letters list
    print('')
    ws = int(input("Τώρα δώσε έναν αριθμό από το 0 έως το 9 για την τυχαία επιλογη λέξης: "))
    while(ws>9 or ws<0):
        ws = int(input("ΣΦΑΛΜΑ, Δώσε έναν αριθμό από το 0 έως το 9 για την τυχαία επιλογη λέξης: "))
    j=0
    while(j<10):
        if(ws == check[j]):
            ws = int(input("Δώσε έναν αριθμό, που δεν έχεις ξαναδώσει για την τυχαία επιλογη λέξης: "))
            while(ws>9 or ws<0):
                ws = int(input("ΣΦΑΛΜΑ, Δώσε έναν αριθμό από το 0 έως το 9 για την τυχαία επιλογη λέξης: "))
            j=-1
        j=j+1
    check[i]=ws
    y=0
    while(y<len(list1[ws])):
        wordcheck=(['_']*(len(list1[ws])))
        print(wordcheck[y],end=" ")
        y=y+1
    print('')
    lcheck=0
    if(ws==0):
        c=w0
    if(ws==1):
        c=w1
    if(ws==2):
        c=w2
    if(ws==3):
        c=w3
    if(ws==4):
        c=w4
    if(ws==5):
        c=w5
    if(ws==6):
        c=w6
    if(ws==7):
        c=w7
    if(ws==8):
        c=w8
    if(ws==9):
        c=w9
    letter = str(input("Δώσε γράμμα: "))
    while(lcheck<9):
        print('')
        y=0
        calc=0
        breakcontrol = 0
        while(letter in wordcheck):#same letter check
            letter = str(input("Δώσε ένα διαφορετικό γράμμα: "))
        while(y<len(c)):
            if(letter == c[y]):
                calc=1
                wordcheck[y]=letter
            y=y+1
        if(calc==0):#wrong letters counter
            wrongletters[lcheck]=letter
            lcheck=lcheck+1
            if(lcheck==9):
                print("|---------|")
                print("|          Ο")
                print("|        / | \\")
                print("|          |")
                print("|        _/ \_")
                print("|        ####")
                print("|        fire")
                print("η λέξη, που έψαχνες ήταν: ",end="")
                counter=0
                while(counter<len(c)):
                    print(c[counter],end="")
                    counter=counter+1
                break
            elif(lcheck==8):
                print("|---------|")
                print("|          Ο")
                print("|        / | \\")
                print("|          |")
                print("|        _/ \_")
                print("|        ####")
                print("|")
            elif(lcheck==7):
                print("|---------|")
                print("|          Ο")
                print("|        / | \\")
                print("|          |")
                print("|        _/ \_")
                print("|        ##")
                print("|")
            elif(lcheck==6):
                print("|---------|")
                print("|          Ο")
                print("|        / | \\")
                print("|          |")
                print("|        _/ \_")
                print("|")
                print("|")
            elif(lcheck==5):
                print("|---------|")
                print("|          Ο")
                print("|        / | \\")
                print("|          |")
                print("|           \_")
                print("|")
                print("|")
            elif(lcheck==4):
                print("|---------|")
                print("|          Ο")
                print("|        / | \\")
                print("|          |")
                print("|")
                print("|")
                print("|")
            elif(lcheck==3):
                print("|---------|")
                print("|          Ο")
                print("|          | \\")
                print("|          |")
                print("|")
                print("|")
                print("|")
            elif(lcheck==2):
                print("|---------|")
                print("|          Ο")
                print("|          |")
                print("|          |")
                print("|")
                print("|")
                print("|")
            elif(lcheck==1):
                print('|---------|')
                print('|         Ο')
                print('|')
                print('|')
                print('|')
                print('|')
                print('|')
            print("Λάθος γράμμα, απέμειναν " +str(9-lcheck)+ " προσπάθειες")
            n=0
            print('')
            print('Τα λανθασμένα γράμματα, που έχεις δώσει είναι: ')
            while(n<len(wrongletters)):#word print
                print(wrongletters[n],end=" ")
                n=n+1
            print('')
            
        n=0
        while(n<len(list1[ws])):#word print
            print(wordcheck[n],end=" ")
            n=n+1
        p=0
        while(wordcheck[p]!='_'):#checks if word has any unfound letters
            if(p==(len(wordcheck)-1)):
                breakcontrol = 1
                break
            p=p+1
        if(breakcontrol==1):
            score=score+10
            break
        print('')
        letter = str(input("Δώσε γράμμα: "))
    i=i+1
print('')
if(score>80):
    print('score: '+str(score)+' Είσαι ο κυρίαρχος της κρεμάλας')
elif(score>60):
    print('score: '+str(score)+' Πολύ καλά')
elif(score>40):
    print('score: '+str(score)+' Δεν τα πήγες κι άσχημα')
elif(score>30):
    print('score: '+str(score)+' Είσαι μισοκρεμασμένος')
elif(score>10):
    print('score: '+str(score)+' Κρεμάλα, που σου χρειάζεται')
else:
    print('score: '+str(score))
            
