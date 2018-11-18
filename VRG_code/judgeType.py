#!/usr/bin/python

import pandas as pd

filename=input("Please input the filename(Enclosed in symbol ''):")

output=[]

fr=open(filename,'r')
for line in fr:
    temp=line.split("\t")
    if(temp[3]=='A'):    
        if(temp[4]=='T'):
            output.append(2)
        elif(temp[4]=='G'):
            output.append(1)
        elif(temp[4]=='C'):
            output.append(2)
        else:
            output.append(0)
    elif(temp[3]=='T'):        
        if(temp[4]=='A'):
            output.append(2)
        elif(temp[4]=='G'):
            output.append(2)
        elif(temp[4]=='C'):
            output.append(1)
        else:
            output.append(0)
    elif(temp[3]=='G'):         
        if(temp[4]=='A'):
            output.append(1)
        elif(temp[4]=='T'):
            output.append(2)
        elif(temp[4]=='C'):
            output.append(2)
        else:
            output.append(0)
    elif(temp[3]=='C'):         
        if(temp[4]=='A'):
            output.append(2)
        elif(temp[4]=='T'):
            output.append(1)
        elif(temp[4]=='G'):
            output.append(2)
        else:
            output.append(0)
    else:
        output.append(0)

output_df=pd.DataFrame(output)
output_df.columns=['type']
output_df.to_csv('../newVARSCAN_result/judgeType.csv',index=False)

fr.close()
