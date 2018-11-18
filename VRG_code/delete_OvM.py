#!/usr/bin/python

output=[]
fr=open('../data/hiDenovo.vcf','r')
for line in fr:
    temp=line.split("\t")
    ref=temp[3]
    alt=temp[4]
    if(len(ref)==1 and len(alt)==1):
        output.append(line)

fw=open('../data/new.hiDenovo.vcf','w')
fw.writelines(output)

fr.close()
fw.close()
