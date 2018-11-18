#!/usr/bin/python

import pandas as pd


index=[]
value1=[]
value2=[]
value3=[]
output=[]


fr=open('../data/loDenovo.vcf','r')
for line in fr:
    temp=line.split("\t")
    index.append(temp[8])
    value1.append(temp[9])
    value2.append(temp[10])
    value3.append(temp[11])


n=len(index)      #create a string array that with n rows and m lines
m=3
output=[None]*n
for i in range(len(output)):
    output[i]=[""]*m


for i in range(len(index)):
    temp=index[i].split(":")
    j=0
    while(temp[j]!="AD"):
        j+=1
    tempdata1=value1[i].split(":")
    data1=tempdata1[j]
    output[i][0]=data1
    tempdata2=value2[i].split(":")
    data2=tempdata2[j]
    output[i][1]=data2
    tempdata3=value3[i].split(":")
    data3=tempdata3[j]
    output[i][2]=data3


fr.close()

output_df=pd.DataFrame(output)
output_df.columns=['son','father','mother']
output_df.to_csv('../GATK_loresult/coverageResult.csv',index=False)
