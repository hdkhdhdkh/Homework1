
def getBondDuration(y, face, couponRate, m, ppy = 1):
 pvcfsum =0 
 cf=0
 pvcf=0
 t=1
 wt=0  
 while t<=m:
    if t<m:
        cf = face * couponRate
    elif t == m:
        cf = face + (face * couponRate)
     
    wt=wt+t*((1 + y)**(-t)) * cf
    pvcfsum = pvcfsum + ((1 + y )**(-t)) * cf
    t+=1
    
    #bondDuration = wt/pvcfsum

 return(wt/pvcfsum)
   
    
  
