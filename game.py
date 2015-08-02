import numpy as np
import random as rd
temp=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
mean=np.mean(temp)
new=[]
final=[]
 
def step_one():
        a=rd.choice(temp)
        b=rd.choice(temp)
        c=rd.choice(temp)
        d=rd.choice(temp)
 
        if (a !=b) and (a !=c) and (a !=d) and (b !=c) and (b!=d) and (c !=d):
                if ( a + b +c +d == mean*4):
                        new.append([a, b, c, d])
                        temp.remove(a)
                        temp.remove(b)
                        temp.remove(c)
                        temp.remove(d)
                else:
                        step_one()
 
        else:
                step_one()
 
def step_two():
        a=rd.choice(new[0])
        b=rd.choice(new[1])
        c=rd.choice(new[2])
        d=rd.choice(new[3])
 
        if (a+b+c+d == mean*4):
                final.append([a,b,c,d])
                new[0].remove(a)
                new[1].remove(b)
                new[2].remove(c)
                new[3].remove(d)
        else:
                step_two()
 
def helper():
        try:
                for i in xrange(4):
                        step_one()
                for j in xrange(4):
                        step_two()
        except RuntimeError:
#                print "Try again"
                global temp, mean, new, final
                temp=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
                mean=np.mean(temp)
                new=[]
                final=[]
                helper()
 
if __name__ == "__main__":
        helper()
 #       print final
 
        print "-------------------"
        print "|",final[0][0],'|', final[1][0], '|', final[2][0],'|',  final[3][0], '|'
        print "-------------------"
        print "|",final[0][1],'|', final[1][1], '|', final[2][1],'|',  final[3][1], '|'
        print "-------------------"
        print "|",final[0][2],'|', final[1][2], '|', final[2][2],'|',  final[3][2], '|'
        print "-------------------"
        print "|",final[0][3],'|', final[1][3], '|', final[2][3],'|',  final[3][3], '|'
