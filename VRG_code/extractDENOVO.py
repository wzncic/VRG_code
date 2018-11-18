#!/usr/bin/python

output=[]
fr=open('../data/new_VARSCAN/trio.mpileup.output.snp.vcf','r')
for line in fr:
    if 'DENOVO' in line:
        output.append(line)

fw=open('../data/new_VARSCAN/denovo.vcf','w')
fw.writelines(output)

fr.close()
fw.close()
