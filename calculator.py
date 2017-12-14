#!/usr/bin/python3
import sys
if len(sys.argv)==2:
    try:
        w=sys.argv[1]
        s=int(w)-3500
        if s<=0 :
            print ("0")
        elif (s<=1500 and s>0):
            print (format(s*0.03,".2f"))
        elif (s>1500 and s<=4500):
            print (format(s*0.1-105,".2f"))
        elif (s>4500 and s<=9000) :
            print (format(s*0.2-555,".2f"))
        elif (s>9000 and s<=35000) :
            print (format(s*0.25-1005,".2f"))
        elif (s>35000 and s<=55000) :
            print (format(s*0.3-2755,".2f"))
        elif (s>55000 and s<=80000) :
            print (format(s*0.35-5505,".2f"))
        else:
            print (format(s*0.45-13505,".2f"))
    except:
        print ("Parameter Error")
else:
    print ("error")



