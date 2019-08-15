#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n,m = map(int,input().split())
d = {}
for i in range(m):
    u,v = map(int,input().split())
    d.setdefault(u,set()).add(v)
    d.setdefault(v,set()).add(u)
m = []
vis = set()
def dfs(v):
    m.append(v)
    vis.add(v)
    for u in d[v]:
        if u not in vis:
            dfs(u)
            m.append(v)
dfs(1)
print(len(m))
print(*m)

