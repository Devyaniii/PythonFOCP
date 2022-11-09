lab=24
a,b,c=113,175,12
def numned(labgrp,d,e,f):
    sub=0
    sub+=d%labgrp
    sub+=e%labgrp
    sub+=f%labgrp
    print(d//labgrp)
    print(e//labgrp)
    print(f//labgrp)
    print((sub+f)//labgrp)
numned(lab,a,b,c)