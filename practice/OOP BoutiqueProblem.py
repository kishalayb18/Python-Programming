class Boutique:
    def __init__(self,boutiqueId,boutiqueName,boutiqueType,boutiqueRating,boutiquePoints):
        self.id=boutiqueId
        self.name=boutiqueName
        self.type=boutiqueType
        self.rating=boutiqueRating
        self.points=boutiquePoints

#boutiqueDict={} # boutique

class OnlineBoutique:
    def __init__(self,bDict):
        self.boutiqueDict=bDict

    def getBoutique(self,lower,upper,extra,type):
        self.lower=lower
        self.upper=upper
        self.extra=extra
        self.type=type

        listBType=self.boutiqueDict[type]

        if len(listBType)==0:
            print('No boutique found')

        for i in listBType:
            if self.lower <= i.rating <= self.upper:
                i.points=i.points+self.extra



if __name__=="__main__":
    n=int(input('Enter No. of Boutique: '))
    li=[]
    typeList=[]
    boutiqueDict = {}

    for i in range(n):
        id=int(input('id: '))
        name=input('name: ')
        type=input('type: ')
        rating=float(input('rating: '))
        points=int(input('points: '))
        li.append(Boutique(id,name,type,rating,points)) #creating Boutique objects and append it to li, li is an array of objects

    for i in li:
        if i.type not in typeList:
            typeList.append(i.type) #typeList has all the unique types of the Boutique objects
    print('typeList==',typeList)

    for i in typeList:
        boutiqueDict[i] = []    #making the dict key as the type of Boutique objects, and value is a list
        for j in li:
            if i==j.type:
                boutiqueDict[i].append(j)   #the list contains the object of same type

    OB_Obj= OnlineBoutique(boutiqueDict)
    lowerLim = float(input('lowerLim: '))
    upperLim=float(input('upperLim: '))
    extraPoint=int(input('extraPoint: '))
    boutiqueType=input('boutiqueType: ')
    OB_Obj.getBoutique(lowerLim,upperLim,extraPoint,boutiqueType)
    