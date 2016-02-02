

from time import *
import serial


tp=bitearray(81312)
def toutblanc():
for i in xrange(0,len(tp), ):
tp[i]=chr(00)
tp[i+1]=chr(00)
tp[i+2]=chr(00)
tp[i+3]=chr(255)

ser.write(tp)



