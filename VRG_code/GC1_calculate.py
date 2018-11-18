#!/usr/bin/python

import os
import numpy as np

filename=input("Please input the filename(Enclosed in symbol ''):")
f=open(filename,'r')
chrom=[]
pos=[]

for line in f:
    temp=line.split("\t")
    chrom.append(temp[0])
    pos.append(temp[1])


for i in range(len(chrom)):
    string='samtools faidx ../data/hs37d5.fa '
    string+=chrom[i]
    string+=':'
    string+=str(int(pos[i])-49)
    string+='-'
    string+=str(int(pos[i])+50)
    string+=' > ../newVARSCAN_result/calculate_result/Num'
    string+=str(i+1)
    string+='.fa'
    os.system(string)

#samtools faidx data/hs37d5.fa 1:100-200 > calculate_result/Num1.fa


f.close()
