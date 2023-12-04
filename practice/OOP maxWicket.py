class Player:
    def __init__(self,name,country,age,run,wicket):
        self.name=name
        self.country=country
        self.age=age
        self.run=run
        self.wicket=wicket

class Team:
    def __init__(self,pList):
        self.playerList=pList

    def minRun(self):
        run=[]

        for i in self.playerList:
            run.append(i.run)

        min1=min(run)
        result=[]

        for i in self.playerList:
            if min1==i.run:
                result.append(i.name)
                result.append(i.run)
                result.append(i.country)

        return result

if __name__=="__main__":
    n=int(input('Enter No. of players'))
    li=[]

    for i in range(n):
        name=input('Name: ')
        coun=input('Country: ')
        age=int(input('Age: '))
        run=int(input('Run: '))
        wckt=int(input('Wicket: '))

        li.append(Player(name,coun,age,run,wckt))


    print('array of ob',li)
    teamObj=Team(li)

    minR=teamObj.minRun()

    for i in minR:
        print(i)
