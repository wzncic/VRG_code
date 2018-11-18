#!/usr/bin/python

output_hi=[]
#output_lo=[]

fr=open('../data/new_GATK/output.postCGP.Gfiltered.deNovos.vcf','r')
for line in fr:
    if 'hiConfDeNovo' in line:
        output_hi.append(line)
    #elif 'loConfDeNovo' in line:
        #output_lo.append(line)


fw1=open('../data/new_GATK/hiDenovo.vcf','w')
fw1.writelines(output_hi)
#fw2=open('../data/loDenovo.vcf','w')
#fw2.writelines(output_lo)

fr.close()
fw1.close()
#fw2.close()
