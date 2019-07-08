
# coding: utf-8

# In[20]:


n=int(input())
total=int(input())
hun=int(input())
two_hun=int(input())
five_hun=int(input())
thous=int(input())
arr=[]
for i in range(0,hun+1):
    
    for j in range(0,two_hun+1):
        
        for k in range(0,five_hun+1):
            
            for l in range(0,thous+1):
                
                if i*100+j*200+k*500+l*1000 ==total:
                    if i+j+k+l <=n:
                        arr.append(i+j+k+l)
                        
                
                
if len(arr)<=0:
    print('0')
else:
    print(max(arr))

