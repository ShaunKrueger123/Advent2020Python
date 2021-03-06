
import numpy as np
import re

def day2():
    file1 = open('day2.txt', 'r')
    Lines = file1.readlines()
    password=[]
    num=0
    num2=0
    for line in Lines:
        password.append(re.split('[\' : -]', line))
    length=len(password)
    file1.close()
    for i in range(length):
        counting=password[i][4].count(password[i][2])
        if(counting>=int(password[i][0]) and counting<=int(password[i][1])):
            num=num+1
        if((password[i][4][int(password[i][0])-1]==password[i][2]) ^ (password[i][4][int(password[i][1])-1]==password[i][2])):
            num2=num2+1
    print(num)
    print(num2)

def day3():
    with open("day3.txt","rt") as infile:
        matrix = [list(line.strip()) for line in infile.readlines()]
    print(matrix[0][0])
    mapheight=len(matrix)
    maplength=len(matrix[0])
    print(mapheight,maplength)
    directions=[[1,1],[3,1],[5,1],[7,1],[1,2]]
    treepaths=[]
    for i in directions:
        shiftdown=i[1]
        shiftover=i[0]
        over=0
        tree=0
        step=0
        height=0
        while(height<mapheight-1):
            step=step+1
            over=over+shiftover
            if(over>=maplength):
                over=over-maplength
            height=height+shiftdown
            if(matrix[height][over]=='#'):
                tree=tree+1
        treepaths.append(tree)
    print(treepaths)
    value=1
    for i in treepaths:
        value=value*i
    print(value)
            #2413152000 too high


def day4():

    file1 = open('day4.txt', 'r')
    Lines = file1.readlines()
    password=[]
    num=0
    valid=0
    for line in Lines:
        if line=='\n':
            if(num==7):
                valid=valid+1
            num=0
        else:
            if('byr:' in line):
                if(int(line.partition('byr:')[2][:4])>=1920 and int(line.partition('byr:')[2][:4])<=2002):
                    num=num+1
            if('iyr:' in line):
                if(int(line.partition('iyr:')[2][:4])>=2010 and int(line.partition('iyr:')[2][:4])<=2020):
                    num=num+1
            if('eyr:' in line):
                if(int(line.partition('eyr:')[2][:4])>=2020 and int(line.partition('eyr:')[2][:4])<=2030):
                    num=num+1
            if('hgt:' in line):
                if(line.partition('hgt:')[2][3:5]=='cm' and int(line.partition('hgt:')[2][:3])>=150 and int(line.partition('hgt:')[2][:3])<=193):
                    num=num+1
                elif(line.partition('hgt:')[2][2:4]=='in' and int(line.partition('hgt:')[2][:2])>=59 and int(line.partition('hgt:')[2][:2])<=76):
                    num=num+1
            if('hcl:' in line):
                if(line.partition('hcl:')[2][0]=='#'):
                    trigger=0
                    for letter in line.partition('hcl:')[2][1:7]:
                        if(letter not in ('a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9')):
                           trigger=1
                    if trigger==0:
                        num=num+1
            if('ecl:' in line):
                if(line.partition('ecl:')[2][:3] in ('amb','blu','brn','gry','grn','hzl','oth')):
                    num=num+1
            if('pid:' in line):
                if(line.partition('pid:')[2][:9].isdigit() and not line.partition('pid:')[2][:10].isdigit()):
                    print(line.partition('pid:')[2][:10])
                    num=num+1
            #password.append(re.split('[\' : -]', line))
    file1.close()
    if(num==7):
        valid=valid+1
    print(valid)
    #168 too big

def day5():
    file = open('day5.txt', 'r')
    Lines = file.readlines()
    id=0
    seatid=[]
    for passport in Lines:
        min=0
        max=127
        seatmin=0
        seatmax=7
        for letter in passport:
            rowdiff=round((max-min)/2+0.5)
            seatdiff=round((seatmax-seatmin)/2+0.5)
            if(letter=='F'):
                max=max-rowdiff
            elif(letter=='B'):
                min=rowdiff+min
            elif(letter=='L'):
                seatmax=seatmax-seatdiff
            else:
                seatmin=seatmin+seatdiff
        newid=min*8+seatmin
        seatid.append(newid)
        if(newid>id):
            id=newid
    print("The highest seat id is ", id)
    sortedid=sorted(seatid)
    for id in range(len(sortedid)-1):
        if(sortedid[id]+1!=sortedid[id+1]):
            print("The missing seat id is ", sortedid[id]+1)

def day6():
    file = open('day6.txt', 'r')
    answer = file.readlines()
    allAnswerYes=[]
    anyAnswerYes=[]
    sumAny=0
    sumAll=0
    for person in answer:
        if person !='\n':
            for letter in person:
                if(letter not in anyAnswerYes and letter!='\n'):
                    anyAnswerYes.append(letter)
            if(allAnswerYes==[]):
                allAnswerYes=person.strip('\n')
            else:
                allAnswerYes=set(allAnswerYes).intersection(person)
            
        else:
            sumAny=sumAny+len(anyAnswerYes)
            sumAll=sumAll+len(allAnswerYes)
            anyAnswerYes=[]
            allAnswerYes=[]
    sumAny=sumAny+len(anyAnswerYes)
    sumAll=sumAll+len(allAnswerYes)
    print(sumAny)
    print(sumAll)

def day7a():
    bagofholding=0
    file = open('day7.txt', 'r')
    rules = file.readlines()
    ruleList=[]
    for rule in rules:
        newrule=[]
        divide=rule.partition(' bags contain ')
        splitting=rule.split(' ')
        newrule.append(splitting[0]+ " " + splitting[1])
        for contained in range(rule.count(',')+1):
            if(splitting[5+4*contained]!="other"):
                newrule.append(splitting[5+4*contained]+ " " + splitting[6+4*contained])
        ruleList.append(newrule)
    bags=ruleList
    for bag in bags:
        print(len(bag))
        print("test",bag.count('shiny gold'))
        while not(len(bag)==1 or bag.count('shiny gold')>=1):

            for check in ruleList:
                if(len(bag)==1):
                    break
                for i in range(len(bag)-1):
            
                    if(check[0]==bag[i+1] and bag[i+1]!='shiny gold'):
                        del bag[i+1]
                        for j in range(len(check)-1):
                            bag.append(check[j+1])
                    break
        print(bag)
        if(len(bag)>1):
            bagofholding=bagofholding+1
    print(bags)
    print(bagofholding)
    #subtract 1 from this because the shiny bag is already here and can't hold itself

def day8():
    import copy
    file = open('day8.txt', 'r')
    instructions=file.readlines()
    allInstructions=[]
    for instruction in instructions:
        instruct=instruction.split()
        instruct.append(0)
        allInstructions.append(instruct)
    originalInstructions=copy.deepcopy(allInstructions)
    fixing=0
    starting=0
    line=starting
    while (line!=641):
        line=starting
        acc=0
        while(line==641 or allInstructions[line][2]==0):
            if(line==641):
                break
            allInstructions[line][2]=1
            if(allInstructions[line][0]=='nop'):
                line=line+1
            elif(allInstructions[line][0]=='acc'):
                acc=acc+int(allInstructions[line][1])
                line=line+1
            else:
                line=line+int(allInstructions[line][1])
        print(fixing," ",line)
        if(line!=641):
            changed=0
            allInstructions=copy.deepcopy(originalInstructions)
            while(changed!=1):
                if(allInstructions[fixing][0]=='nop'):
                    allInstructions[fixing][0]='jmp'
                    changed=1
                elif(allInstructions[fixing][0]=='jmp'):
                    allInstructions[fixing][0]='nop'
                    changed=1
                fixing=fixing+1
    print(acc)
    print(line)  

def day9():
    file = open('day9.txt', 'r')
    data=file.read().splitlines()
    preamble=25
    numbers=[]
    check=[]
    for number in data:
        numbers.append(int(number))

    for x in range(preamble):
        for y in range(preamble):
            if(x!=y):
                check.append(numbers[x]+numbers[y])
            #check.append(x+y+1)

    for checking in range(preamble,len(numbers)):
        if(numbers[checking] not in check):
            #print(numbers[checking],' pass')
        #else:
            print(numbers[checking],' fail')
        #print(check)
        check=check[preamble-1:]
        for x in range(1,preamble):
            check.append(numbers[checking]+numbers[checking-x])

    value=1639024365
    for test in range(len(numbers)):
        sum=0
        number=test
        inc=0
        while(sum<value):
            sum=sum+numbers[number]
            number=number+1
            inc=inc+1
            if(sum==value):
                print(test," ",number," ",numbers[test:number])
                #print("test",numbers[test]," ",numbers[number]," ",sum," ",number)
                print(min(numbers[test:number])," ", max(numbers[test:number])," ",min(numbers[test:number])+max(numbers[test:number]))

def day10():
    file= open('day10.txt', 'r')
    data=file.read().splitlines()
    numbers=[]
    needed=[1]
    step1=0
    step3=0
    optional=0
    permut=1
    for number in data:
        numbers.append(int(number))
    numbers.append(0)
    numbers.append(max(numbers)+3)
    numbers=sorted(numbers)
    for step in range(len(numbers)-1):
        if(numbers[step+1]-numbers[step]==3):
            step3=step3+1
            needed.append(1)
            permut=permut*(2**(optional)-int(optional/3))
            optional=0
        else:
            step1=step1+1
            if(numbers.count(numbers[step]+3)==1 or numbers.count(numbers[step]+2)==1):
                needed.append(0)
                optional=optional+1
            else:
                needed.append(1)
                test=2**(optional)-int(optional/3)
                permut=permut*(2**(optional)-int(optional/3))
                optional=0
    print(needed)
    print(numbers)
    print(step1," ", step3+1, " ",step1*(step3))
    print(permut)

def day11():
    file = open('day11.txt', 'r')
    data=file.read().splitlines()
    seats=[]
    for rows in data:
        seats.append(list(rows))
    newseating=seats
    height=len(seats)
    width=len(seats[0])
    print(height)

day11()