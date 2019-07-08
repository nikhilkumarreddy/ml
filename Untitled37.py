
# coding: utf-8

# In[16]:


aa=int(input())
n,p,r=input().split()
n=int(n)
p=int(p)
r=int(r)
import itertools
b='a'*4
k=len(list(itertools.combinations(b,3)))
print(2*k)

