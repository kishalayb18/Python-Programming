def solution(queries):
    value=[1,2,3,4]
    retString=[]
    for q in queries:
        if q[0]=="ADD":
            value.append(int(q[1]))
            retString.append("")
        elif q[0]=="EXISTS":
            if int(q[1]) in value:
                retString.append("true")
            elif int(q[1]) not in value:
                retString.append("false")
        elif q[0]=="REMOVE":
            if int(q[1]) in value:
                value.remove(int(q[1]))
                retString.append("true")
            else:
                retString.append("false")
        elif q[0]=="GET_NEXT":
            if int(q[1]) in value:
                print(q[1])
                
                # for i in value:
                #     if i > q[1]:
                        
                #         print(i)
            elif int(q[1]) not in value:
                print(q[1])
                value.append("")

    return retString


result=solution( [
["EXISTS", "1"],
["REMOVE", "1"],
["GET_NEXT", "2"]
])

print(result)