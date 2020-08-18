 
# Assumptions:
# can only handle 'unique' entry
# Closed aplication where all the data available offline
# No error handling

""" To enter direct choice in Matrix keep code commented from line 52 to line 91 and
fill and uncomment Boys and GirlsChoice matrix at line 49-50 """

#a = nm.array([[2,5,3,1,4,6],[2,1,3,6,4,5],[3,2,1,6,4,5],[5,2,6,1,3,4],[6,1,2,4,3,5]])
#b = nm.array([[2,5,1,1,2,4],[1,1,2,4,1,2],[3,3,5,2,3,1],[5,4,4,3,4,3],[4,2,3,5,5,5]])

#a = nm.array([[3,2,4,1],[4,1,2,3],[1,2,3,4],[2,3,1,4],[4,2,1,3],[1,2,3,4]])
#b = nm.array([[3,3,1,1],[2,1,3,4],[5,4,2,5],[6,6,6,6],[4,2,4,3],[1,5,5,2]])

#a = nm.array([[1,2,3,4],[1,4,3,2],[4,2,1,3],[3,2,1,4]])
#b = nm.array([[2,4,1,1],[1,1,2,2],[4,2,3,3],[3,3,4,4]])

import numpy as nm
BoyChoice = nm.array([[0]])
GirlChoice = nm.array([[0]])
Choice = nm.array([[0]])
oppChoice = nm.array([[0]])
r = BoyChoice[:]
s = GirlChoice[:]
Boys = []
Girls = []
gender = str
List = []
ext = str
choiceName = str
count = int
oppList = []
done = ''
noBoys = int
noGirls = int



print('Hi there...! Welcome to the KAMAGNI ')
Boys_input = input("Enter names of boys separated by commas: ")
Girls_input = input("Enter names of Girls separated by commas: ")
Boys = Boys_input.split(',')
Girls = Girls_input.split(',')
noBoys = len(Boys)
noGirls = len(Girls)
BoyChoice = nm.zeros((noBoys,noGirls), dtype=nm.int)
GirlChoice = nm.zeros((noGirls,noBoys), dtype=nm.int)

##BoyChoice = nm.array([[1,2,3,4],[1,4,3,2],[4,1,2,3]])
##GirlChoice = nm.array([[2,1,3],[3,1,2],[1,2,3],[1,3,2]])

while Choice.all() == 0 or oppChoice.all() == 0:
    try:
        proceed = 0
        print(Boys+Girls)
        name = input('Enter your name from the above list: ')        
##        if name == 'exit':
##            break
        if name in Boys:
            List = Boys
            oppList = Girls
            Choice = BoyChoice
            oppChoice = GirlChoice
            proceed = 1
        elif name in Girls:
            List = Girls
            oppList = Boys
            Choice = GirlChoice
            oppChoice = BoyChoice
            proceed = 1
        #print ('List: ',List)
        #print ('oppList: ',oppList)
        if proceed == 1:                    
            for choiceName in oppList:
                choiceInt = input('Give a choice rank to '+choiceName+': ')
                indexColm = oppList.index(choiceName)
                indexRow = List.index(name)
                Choice[indexRow,indexColm] = choiceInt            
            print (BoyChoice)
            print (GirlChoice)
            print (GirlChoice.transpose())
        ##        try:
        ##            Choice[indexBoy,indexGirl] = count
        ##        except IndexError:
        ##            Choice
        else:
            print('==Please enter valid entry==')
    except:
        print('you have entered invalid entry')
        pass
#print(';(')
a = BoyChoice
b = GirlChoice.transpose()
l = Boys
m = Girls
#X = []
#J = []
result = {}
break_count = 0
luckCount = 0
input('Enter anything to get results: ')
#for k in range(0,6):
while a.size != 0:
    print('start a\n',a)
    print('start b\n',b)
    print('start r\n',r)
    print('start s\n',s)      
    for x in range(a.shape[0]):
        for j in range(a.shape[1]):           
            #print('x: ',x,' | j: ',j, ' | ',a[x,j],' | ',b[x,j])
            if a[x,j]==1 and b[x,j]==1:
                #X.append(l[x])
                #J.append(m[j])
                result[l[x]] = m[j]
                print(l[x],'<==>',m[j],' | ',x,'<=>',j)
                del l[x]
                del m[j]
                r = nm.delete( a, (x), axis=0)
                r = nm.delete( r, (j), axis=1)
                s = nm.delete( b, (x), axis=0)
                s = nm.delete( s, (j), axis=1)
                break_count = 1
                print('breaking at j: ',j)
                break
            else:
                break_count = 0
                print('else at j: ',j)
        if break_count == 1:
            print('breaking at x: ',x)
            break
##        print('med a\n',a)
##        print('med b\n',b)
##        print('med r\n',r)
##        print('med s\n',s)  
    ## loop Logic
    if nm.array_equal(a,r) and a.shape[0] !=1 and a.shape[1] != 1:
        luckCount=+1
        a[a == 1] = 0
        a[a == 2] = 1
        a[a == 0] = 2
        b[b == 1] = 0
        b[b == 2] = 1
        b[b == 0] = 2
        print('stuck in loop', ' \n a: \n', a, ' \n r: \n', r)
        break
    a = r.argsort(1).argsort(1)+1
    r = a[:]    
    b = s.argsort(0).argsort(0)+1
    s= b[:]
##    print('end a\n',a)
##    print('end b\n',b)
##    print('end r\n',r)
##    print('end s\n',s) 
    print('Luck used',luckCount,'times')
print(' ,-======RESULT======================')
for key in result:
    print(' | ', key,'<==>', result[key])
print(' \'-==================================')