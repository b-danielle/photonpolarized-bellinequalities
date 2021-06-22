import math
from math import sqrt
import numpy as np
import cmath
from cmath import exp
from random import random

parametrobell=open('parametro.txt','w')



c=[0]*17     
s=[0]*1000   
nbe=[0]*17   


pi=math.pi

NI=8000   
NE=100    
im=1j    



th=pi/4 +pi/200  


sp=0   


    
for n in range(1,NE):   
     
    aps=[-pi/4,pi/4,-pi/4,pi/4,-pi/4,pi/4,-pi/4,pi/4,0,pi/2,0,pi/2,0,pi/2,0,pi/2]         
    apt=[-pi/8,3*pi/8,3*pi/8,-pi/8,pi/8,6*pi/8,6*pi/8,pi/8,-pi/8,3*pi/8,3*pi/8,-pi/8,pi/8,6*pi/8,6*pi/8,pi/8]    
   
    
    for nb in range(0,15):    
            r1=random()
            if r1<1/2:                       
                aps[nb]=aps[nb]+pi/200
            else:
                aps[nb]=aps[nb]-pi/200
            
            r2=random()
            if r2<1/2:                    
                apt[nb]=apt[nb]+pi/200
            else:
                apt[nb]=apt[nb]-pi/200
                
            r3=random()
            if r3<1/2:                      
                t=NI+r3*500
                N=int(t)
            else:
                t=NI-r3*500
                N=int(t)
        
            for k in range(1,N):      
                   r4=random()
                   if r4<1/2:
                       phi=pi/4 +r4*5*(2*pi/360)
                   else:
                       phi=pi/4 -r4*5*(2*pi/360)
            
            
                   ap=math.cos(th)*math.cos(aps[nb])*math.cos(apt[nb])+cmath.exp(im*phi)*math.sin(th)*math.sin(aps[nb])*math.sin(apt[nb])                
                   q=ap*(ap.conjugate())
                   g=q.real         
                   c[nb]=c[nb]+g    
              
            
            
                   nbe[nb]=int(c[nb])   
           
         
    sum1=nbe[0]+nbe[1]+nbe[2]+nbe[3]
    sum2=nbe[4]+nbe[5]+nbe[6]+nbe[7]
    sum3=nbe[8]+nbe[9]+nbe[10]+nbe[11]
    sum4=nbe[12]+nbe[13]+nbe[14]+nbe[15]
    
    
    n1=nbe[0]+nbe[1]-nbe[2]-nbe[3]
    n2=nbe[4]+nbe[5]-nbe[6]-nbe[7]
    n3=nbe[8]+nbe[9]-nbe[10]-nbe[11]
    n4=nbe[12]+nbe[13]-nbe[14]-nbe[15]
    
    p1=n1/sum1
    p2=n2/sum2
    p3=n3/sum3
    p4=n4/sum4
    
    s[n]=p1-p2+p3+p4        
    sp=sp+s[n]                   
    parametrobell.write('{0:5.6f} ,\n'.format(s[n]))  
   
    #TERMINA PRUEBA DE BELL



promedio=sp/(NE-1)     




v=0
for k in range(1,NE):
    v=v+((promedio-s[k])**2)/NE
    
estandar=math.sqrt(v)
print (promedio,estandar)




parametrobell.close()














































