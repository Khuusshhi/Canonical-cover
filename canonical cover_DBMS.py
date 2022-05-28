

domain=list(input("Enter the schema : "))
fd=input("Enter the Functional Dependences : ")
s=[]


def step0(domain,fd):
    s1=fd.split(",")
    s2=[]
    a=[]
    #s2=s1.split("->")
    for i in s1:
        s2.append(i.split("->"))
    for i in range(len(s2)):
        if len(s2[i][1])!=1:
            
            a=list(s2[i][1])
            s2[i][1]=a
    dom=list(domain)
    print(s2)
    print(dom)
    return s2 ,dom       
arr0,dom=step0(domain,fd)

def step1(arr0):
    s2=arr0
    c=[]
    for i in range(len(s2)):
        #print(i)
        if len(s2[i][1])!=1:
            x=i
            for a in range(len(s2[i][1])):
                #print(len(s2[i][1]))
                b=([s2[i][0],s2[i][1][a]])
                c.append(b)
            del s2[i]
        else :
            pass 
    for i in range(len(c)):
        s2.append(c[i])
            

    print(s2)    
    return s2 
print("step1")       
arr1=step1(arr0)

def closure(closure,arr1,x):
    s2=arr1
    x=x
    b,c,d,s3=[],[],[],[]
    s3+=closure
    

    for i in range(len(s3)):
    
        b+=s3[i]
    #a.append(b) 
   
    flag=1 
    #print("s3",s3,"i",x)
            
    while flag==1:
        # if len(s3)>1:
        #     s3=s3[1]
        #     print("s3",s3)

        for i in range(len(s2)):
            # if len(s3[x])>1:
            #     s3=s3[1]
            
            if s3[1] == s2[i][0]:

                    c+=s2[i]
                    s3=s2[i]
                    #print(c)
                    flag=1

        flag=0    
    
    #print(c)
    d=c+b
    #,a=b,c
    #a.append(d)
    res = []
    for i in d:
        if i not in res:
            res.append(i)
    res.sort()
    return b,res

def closure_without(arr1):
    s3=arr1
    s2=arr1
    s3=s3[0][0]
    a=s2.pop(0)
    c=[]
    c+=s3
    sum=0
    j=0
    x=[]
    for i in range(len(s2)):
        sum+=1
        if s3 == s2[i][0]:
            c+=s2[i]
           #print(s2[i][1])
           #s3=s2[i][1]
            x.append(i)       
     
    for i in range(len(s2)):
        if s3 == s2[i][0]:
            c+=s2[i]
            #print(s2[i][1])
            s3=s2[i][1]
            

        #print(sum,i,j)
    s2.append(a) 
    res = []
    for i in c:
        if i not in res:
            res.append(i)
    res.sort()
    return res           







def step2(arr1):
    s2=arr1
    s3=arr1
    w,wo=[],[]
    print("with")
    for i in range(len(s2)):
        c,d=closure(s3[i],s2,i)
        w.append(d)
        print(c,d)

    print("without")
    for i in range(len(s2)):
        #print("s3",s3)
        a=closure_without(s2)
        wo.append(a)
        print(a)
    for i in range(len(w)):
        if w[i]==wo[i]:
            pass
        else:
            s.append(s2[i])
    
    # print("w",len(w))    
    # print("wo",len(wo))  
    return w,wo
  



print("step2")
arr21,arr22=step2(arr1)

def step3(arr1):
    s2=arr1
    s4,w31,w32=[],[],[]
    for i in range(len(s2)):
        if len(s2[i][0])>1:
            c,d=closure(s2[i],s2,i)
            w31.append(d)
            s4=list(s2[i][0])
            print(s4,"s4")
            for i in range(len(s4)):
                s5=[]
                s5.append("")
                s5+=s4[i]
                a=closure(s5,s2,i)
                w32.append(a)
                #print(a)  
            print("w31",w31)
            print("w32",w32)  
            for i in range(len(s4)):
                if w31[0]==w32[i][1]:
                   pass
                    

    
    return a            
print("step3")
arr3=step3(arr1)


print("\n cannonical cover",s)

candy=[]
def candidate_key(arr1,arr21,dom):
    s2=arr1
    s3=arr21
    dom=dom
    #print("s2",s2,"s3",s3,"d0m",dom)
    for i in range(len(s2)):
        if s3[i]==dom:
            candy.append(arr1[i])
    res = []
    for i in candy:
        if i not in res:
            res.append(i)
    res.sort()
    
    print(res)        
    return res

print("candidate_key")
can=candidate_key(arr1,arr21,dom)                







#a->b,b->c,c->da->b,b->c,c->d
#a->b,b->c,c->d,ab->c,a->abcd
