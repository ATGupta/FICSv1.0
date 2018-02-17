import units
import threading
import English

multiplier=0

def process(st):
    st=seperateLettersNumbersSymbols(st)
    #print(st)
    st=st.split()
    #print(st)
    st=trimArticles(st)
    #print(st)
    st=combineDecimal(st)
    #print(st)
    st=handleApporstrophe(st)
    #print(st)
    st=handleDeterminer(st)
    #print(st)
    checkForMultiplier(st)
    checkHeightUnits(st)
    checkDegreeWord(st)
    checkReferredMeasurements(st)
    return st

def seperateLettersNumbersSymbols(st):
    st2=""
    prev=' '
    for i in range(0, len(st)):
        c=st[i]
        if (ord(c)>=65 and ord(c)<=90)\
            or (ord(c)>=97 and ord(c)<=122):
            if (ord(prev) >= 65 and ord(prev) <= 90)\
                or (ord(prev) >= 97 and ord(prev) <= 122):
                st2=st2+c
                prev=c
            else:
                st2=st2+" "+c
                prev=c

        else:
            if (ord(c)>=48 and ord(c)<=57):
                if(ord(prev)>=48 and ord(prev)<=57):
                    st2=st2+c
                else:
                    st2=st2+" "+c
                    prev=c

            else:
                if c is ' ':
                    st2 = st2 + c
                    prev = c

                else:
                    st2 = st2 + " " + c
                    prev = c

    return st2

def trimArticles(st):
    try:
        for i in range(0,len(st)):
            if st[i] in English.article:
                st.__delitem__(i)
    except IndexError:
        pass
    return st

def combineDecimal(st):
    for i in range(1,len(st)-1):
        try:
            word=st[i]
        except:
            break

        if word is ".":
            try:
                int(st[i - 1])
                int(st[i + 1])
            except ValueError:
                continue

            st[i-1:i+2] = [''.join(st[i-1:i+2])]

    return st

def handleApporstrophe(st):
    for word in st:
        try:
            if word == "'":
                index=st.index(word)
                if st[index+1] != 's':
                    continue

                temp=st[index+2]
                st[index+2]=st[index-1]
                st[index-1]=temp
                st[index]="of"
                st.__delitem__(index+1)

                if st[index - 2] in English.determiner:
                    temp=st[index - 2]
                    st[index-2]=st[index-1]
                    st[index-1]=st[index]
                    st[index]=temp
        except IndexError:
            pass
    return st

def handleDeterminer(st):
    for word in st:
        if word not in English.determiner:
            continue

        try:
            i=st.index(word)
            temp=st[i+1]
            if word == "my":
                st[i+1]="me"
            else:
                if word == "your":
                    st[i + 1] = "you"
                else:
                    if word=="his":
                        st[i + 1] = "he"
                    else:
                        if word=="her":
                            st[i + 1] = "she"
                        else:
                            if word=="their":
                                st[i + 1] = "them"
                            else:
                                if word=="our":
                                    st[i + 1] = "us"
            st[i]=temp
            st.insert(i+1,"of")
        except IndexError:
            pass

    return st

def checkForMultiplier(st):
    global multiplier
    for word in st:
        if word in units.multiplier:
            if word == 'half':
                multiplier=0.5
            else:
                if word == 'double':
                    multiplier=2
                else:
                    if word == 'triple':
                        multiplier=3

def checkHeightUnits(st):
    for word in st:
        value=0
        try:
            value = float(word)
            probableUnit=st[st.index(word)+1]
            if probableUnit in units.displacement['cm']:
                value = value/100
            else:
                if probableUnit in units.displacement['ft']:
                    value = value*12*2.54/100
                else:
                    if probableUnit in units.displacement['km']:
                        value=value*1000
                    else:
                        if probableUnit in units.displacement['m']:
                            pass
                        else:
                            continue
            #if not continued
            threading.Thread(processHeight(value))
            return
        except ValueError or IndexError:
            continue
    return

def checkDegreeWord(st):
    for word in st:
        if word in units.degree:
            index=units.degree.index(word)

            try:
                if st[st.index(word)+1] == "floor":
                    height = (index+1)*units.referredMeasures["floor"]
                    threading.Thread(processHeight(height))
                    return
            except IndexError:#the array has ended, although, continue
                continue
    return

def checkReferredMeasurements(st):
    keys=list(units.referredMeasures.keys())
    for word in st:
        if set('wheels of car'.split()).issubset(st) or \
            set('wheel of car'.split()).issubset(st):
            threading.Thread(processHeight(units.referredMeasures['wheels of car']))
            return

def processHeight(height):
    height=height*multiplier
    print(height,"metres")