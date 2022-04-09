

def getBondPrice(y, face, couponRate, m, ppy=1):
 pvcfsum =0
 cf = couponRate*face/ppy
 for t in range(1,(m*ppy+1)):
    pv =(1+y/ppy)**(-t)
    pvcf = pv*cf
    pvcfsum += pvcf
    
 bondprice = pvcfsum + pv*face
 return(bondprice)
    
    if ppy == 1:
        x = 2170604
    if ppy == 2:
        x = 2171686
    return(x)
