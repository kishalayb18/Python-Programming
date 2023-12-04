def solution(queries):
    value=[]
    file={}
    retString=[]

    for q in queries:
        if q[0]=="ADD_FILE":
            if q[1] in file:
                file[q[1]]=q[2]
                retString.append("overwritten")
            elif q[1] not in file:
                file[q[1]]=q[2]
                retString.append("created")

        elif q[0]=="GET_FILE_SIZE":
            if q[1] in file:
                size=file[q[1]]
                retString.append(size)
            elif q[1] not in file:
                retString.append("")

        elif q[0]=="MOVE_FILE":
            if q[1]==q[2]:
                retString.append("false")
            if q[2] in file:
                retString.append("false")
            elif q[1] not in file:
                retString.append("false")
            else:
                file[q[2]]=file[q[1]]
                del file[q[1]]
                retString.append("true")

        elif q[0]=="GET_N_LARGEST":
            sortedDict = sorted(file)
            n=int(q[3]):
            i=0
            while(i<3):
                retString.append


    return retString


result=solution( [
["ADD_FILE","c:",4],
["ADD_FILE","c:",8],
["ADD_FILE","d:",32],
["GET_FILE_SIZE","d:"],
["GET_FILE_SIZE","c:"],
["MOVE_FILE","d:","e:"],
["GET_FILE_SIZE","d:"]
])

print(result)