

def getBondPrice_Z(face, couponRate, times, yc):
 pvcfsum =0
 cf = couponRate*face
 for y,t in zip(yc,times):
   pv =(1+y)**(-t)
   pvcf = pv*cf
   pvcfsum += pvcf

 bondprice = pvcfsum + pv*face
 return(bondprice) 

yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04
getBondPrice_Z(face, couponRate, times, yc)
