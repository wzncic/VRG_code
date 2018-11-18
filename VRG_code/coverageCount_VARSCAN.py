#!/usr/bin/python

import pandas as pd


index=[]
value1=[]
value2=[]
value3=[]
output=[]


fr=open('../data/new_VARSCAN/denovo.vcf','r')
for line in fr:
    temp=line.split("\t")
    index.append(temp[8])
    value1.append(temp[9])
    value2.append(temp[10])
    value3.append(temp[11])


n=len(index)      #create a string array that with n rows and m lines
m=6
output=[None]*n
for i in range(len(output)):
    output[i]=[""]*m


for i in range(len(index)):
    temp=index[i].split(":")
    j=0
    while(temp[j]!="RD"):
        j+=1
    k=0
    while(temp[k]!="AD"):
        k+=1
    tempdata1=value1[i].split(":")
    output[i][0]=tempdata1[j]
    output[i][1]=tempdata1[k]
    tempdata2=value2[i].split(":")
    output[i][2]=tempdata2[j]
    output[i][3]=tempdata2[k]
    tempdata3=value3[i].split(":")
    output[i][4]=tempdata3[j]
    output[i][5]=tempdata3[k]


fr.close()

output_df=pd.DataFrame(output)
output_df.columns=['father1','father2','mother1','mother2','son1','son2']
output_df.to_csv('../newVARSCAN_result/coverageResult.csv',index=False)

