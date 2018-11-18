#!/usr/bin/python

import numpy as np
import pandas as pd

filename1="../data/new_VARSCAN/denovo.vcf"
f1=open(filename1,'r')
filename2="../data/new_VARSCAN/trio.mpileup.output.snp.vcf"
f2=open(filename2,'r')

denovo=[]
pos=[]

for line in f1:
    temp=line.split("\t")
    denovo.append(temp[1])

i=0
for line in f2:
    temp=line.split("\t")
    ref=temp[3]
    alt=temp[4]
    if(len(ref)==1 and len(alt)==1):
        pos.append(temp[1])
    i+=1
    if(i>=151451):
        break

print(len(pos))

n=len(denovo)      #create a string array that with n rows and m lines
m=4
output=[None]*n
for i in range(len(output)):
    output[i]=[""]*m

for i in range(len(denovo)):
    output[i][0]=denovo[i]
    output[i][1]=str(int(denovo[i])-49)
    output[i][2]=str(int(denovo[i])+50)
    num=0
    for j in range(len(pos)):
        if(int(pos[j])>=int(output[i][1]) and int(pos[j])<=int(output[i][2])):
            num+=1
    output[i][3]=str(num)
    print("complete"+str(i))

output_df=pd.DataFrame(output)
output_df.columns=['pos','pos-49','pos+50','num']
output_df.to_csv('../newVARSCAN_result/newcountPOS.csv',index=False) 


f1.close()
f2.close()
