#!/usr/bin/python

import numpy as np
import pandas as pd

vcf=[]

filename=input("Please input the filename(Enclosed in symbol ''):")
f1=open(filename,'r')
for line in f1:
    vcf.append(line)
f1.close()

n=len(vcf)      #create a string array that with n rows and m lines
m=2
output=[None]*n
for i in range(len(output)):
    output[i]=[""]*m

for i in range(len(vcf)):
    temp=vcf[i].split("\t")   #store the pos in output[i][0]
    output[i][0]=temp[1]


for i in range(len(vcf)):
    num='../newVARSCAN_result/calculate_result/Num'+str(i+1)+'.fa'  #open the '.fa' file with the corresponding pos
    f2=open(num,'r')
    temp=[]
    sequence=""
    for line in f2:                  #store the sequence in output[i][1]
        temp.append(line)
    sequence=temp[1].replace("\n","")+temp[2].replace("\n","")
    output[i][1]=sequence
    f2.close()

output_df=pd.DataFrame(output)
output_df.columns=['pos','sequence']
output_df.to_csv('../newVARSCAN_result/combine_result/combineResult.csv',index=False)
