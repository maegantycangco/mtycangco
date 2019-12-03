import pandas as pd
x = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
y = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
z = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
w = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
dfx = pd.DataFrame(x,columns=['Student','Math'])
dfy = pd.DataFrame(y,columns=['Student','Electronics'])
dfz = pd.DataFrame(z,columns=['Student','GEAS'])
dfw = pd.DataFrame(w,columns=['Student','ESAT'])
xy = pd.merge(dfx,dfy,how='outer',on='Student')
zw = pd.merge(dfz,dfw,how='outer',on='Student')
final=pd.merge(xy,zw,how='outer',on='Student')
print (final)