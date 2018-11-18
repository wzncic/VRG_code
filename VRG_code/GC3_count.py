#!/usr/bin/python

import numpy as np
import pandas as pd

csv=[]

f=open('../GATK_hiresult/combine_result/combineResult.csv','r')
for line in f:
    csv.append(line)
f.close()

csv=np.delete(csv,0,0)

n=len(csv)      #create a string array that with n rows and m lines
m=3
output=[None]*n
for i in range(len(output)):
    output[i]=[""]*m

for i in range(len(csv)):
    temp=csv[i].split(",")   #in order to use the subscripts([i][0]&[i][1]) visit the pos&sequence directly
    output[i][0]=temp[0]
    output[i][1]=temp[1]

for i in range(len(output)):      #count the number of G&C&g&c
    sequence=output[i][1]
    num=0
    j=0
    while(sequence[j]!="\n"):
        if(sequence[j]=="G" or sequence[j]=="C" or sequence[j]=='g' or sequence[j]=='c'):
            num+=1
        j+=1
    output[i][2]='%d%%'%(num)

for i in range(len(output)):
    output[i][1]=output[i][1].replace("\n","")  
print(len(output))

output_df=pd.DataFrame(output)
output_df.columns=['pos','sequence','rate']
output_df.to_csv('../GATK_hiresult/count_result/newcountResult.csv',index=False)
