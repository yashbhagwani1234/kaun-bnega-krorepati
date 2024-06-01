questions = [["in which language the fb was created","java","js","python","c++","none",4],
             ["in which language the insta was created","java",'js','python','c++','none',3],
             ["in which language the fb was created","java",'js','python','c++','none',2],
             ["in which language the fb was created","java",'js','python','c++','none',1],
             ["in which language the fb was created","java",'js','python','c++','none',4],
             ["in which language the fb was created","java",'js','python','c++','none',1],
             ["in which language the fb was created","java",'js','python','c++','none',4],
             ["in which language the fb was created","java",'js','python','c++','none',3],
             ["in which language the fb was created","java",'js','python','c++','none',4],
             ["in which language the fb was created","java",'js','python','c++','none',2],
             ["in which language the fb was created","java",'js','python','c++','none',2]]

levels = [10000000,5000000,2500000,1250000,640000,320000,160000,80000,40000,20000,10000,5000,3000,2000,1000]
levels.reverse()
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f'{question[0]}')
    print(f'a. {question[1]}        b. {question[2]}')
    print(f'c. {question[3]}        d. {question[4]}')
    reply = int(input('enter answer:-'))
    if(reply == question[-1]):
        print('Correct answer :)')
        money = money + levels[i]
        print(f'you won {levels[i]}')
        print(f'total money is {money}')
    else:
        print('Wrong answer')
        
    
