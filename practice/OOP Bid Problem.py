class Property:
    def __init__(self, pType, pVal, pMaxBid):
        self.property_type = pType
        self.property_value = pVal
        self.max_bid_price = pMaxBid


class Tender:
    def __init__(self, buyer, pType, bPrice):
        self.buyerName = buyer
        self.propertyType = pType
        self.bidPrice = bPrice


if __name__ == "__main__":

    def bidProperty(pL, tL):
        p_list = pL
        t_list = tL
        mBid = 0
        temp = []
        result = []
        for i in p_list:
            s1=i.property_type.upper
            print(s1)
            for j in t_list:
                s2=j.propertyType
                if i.property_type == j.propertyType:
                    if i.property_value <= j.bidPrice <= i.max_bid_price:
                        if mBid < j.bidPrice:
                            mBid = j.bidPrice
                            temp.clear()
                            temp.append(j)

            if len(temp) != 0:
                result.append(temp[0].buyerName)
                p_list.remove(i)

        if len(result) == 0:
            print('Property not found')
        else:
            for i in result:
                print(i)
            for i in p_list:
                print(i.property_type)


    n = int(input())
    liP = []
    for i in range(n):
        ptype = input()
        pvalue = int(input())
        pmaxbid = int(input())
        liP.append(Property(ptype, pvalue, pmaxbid))

    n = int(input())
    liB = []
    for i in range(n):
        bname = input()
        btype = input()
        bprice = int(input())
        liB.append(Tender(bname, btype, bprice))

    bidProperty(liP, liB)
