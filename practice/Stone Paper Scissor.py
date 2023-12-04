import random
computer_counter = 0
user_counter = 0
cnt=0
content = ['stone','paper','scissor']
flag=1

print('STONE-PAPER-SCISSOR GAME RULE')
print('\nIT IS A 5 ROUNDS GAME\nUSER SHOULD ENTER 1 or 2 or 3 AS THEIR CHOICE')

while cnt<5:
    computer= random.choice(content)
    print("\n1. Stone     2. Paper       3. Scissor")
    user= int(input('Enter Your Choice: '))
    if(computer =='stone'and user == 2):
        user_counter+=1
    elif(computer == 'stone'and user == 3):
        computer_counter+=1
    elif(computer =='paper'and user ==1):
        computer_counter+=1
    elif(computer =='paper' and user == 3):
        user_counter+=1
    elif(computer == 'scissor' and user == 2):
        computer_counter+=1
    elif(computer == 'scissor' and user == 1):
        user_counter+=1
    elif(computer == 'stone' and user == 1):
        computer_counter+=0
    elif(computer == 'paper' and user == 2):
        computer_counter+=0
    elif(computer == 'scissor' and user ==3):
        computer_counter+=0
    else:
        print("Invalid Choice")
        continue

    cnt=cnt+1
    print("COMPUTER-" +computer)
    print("USER-" +content[user-1])

print('\n---------------------------------\n\t\t\tSCORE')
print('---------------------------------')
print('\tCOMPUTER: ',computer_counter,'\tUSER: ',user_counter)
print('')
if(computer_counter > user_counter):
    print("\t\tWinner is COMPUTER")
elif(computer_counter < user_counter):
    print("\t\tWinner is USER")
else:
    print("\t\tMatch DRAWN")