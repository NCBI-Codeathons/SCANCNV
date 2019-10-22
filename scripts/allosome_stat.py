# to get allosome read ratio from XYAlign output

import math
import os
import subprocess

result_file=[]
sample=[]
t1=[]

for path, subdirs, files in os.walk(r'/home/dnanexus/xyalign-chrom-stats/results'):  #to get the names of each sample
        for filename in files:
                if (filename.endswith('.txt')):
                        result_file.append('/home/dnanexus/xyalign-chrom-stats/results/'+filename)
			sample.append(filename.replace('_chrom_stats_count.txt',''))		                        
x_reads=[]
y_reads=[]

t2=[]

for i in range(0, len(result_file)):
	with open(result_file[i], 'r') as input_file:
		for line in input_file.readlines():
			if line.startswith('chrom'):
				continue
			t2=line.strip().split("\t")
			if(t2[0] == 'X'):
				x_reads.append(float(t2[1]))
			if(t2[0] == 'Y'):
				y_reads.append(float(t2[1]))
			t2=[]

x_ratio=[0]*len(result_file)
y_ratio=[0]*len(result_file)
total_reads=[0]*len(result_file)

for j in range(0, len(x_reads)):
	total_reads[j]=(x_reads[j]+y_reads[j])
	x_ratio[j]=(100*(x_reads[j]/total_reads[j]))
	y_ratio[j]=(100*(y_reads[j]/total_reads[j]))

with open('/home/dnanexus/gender_ratio.csv', 'w') as gender_ratio_file:
	gender_ratio_file.write('file,reads mapped to chrX(%),reads mapped to chrY(%)\n')
	for a in range(0, len(result_file)):
		gender_ratio_file.write(sample[a]+','+"{0:.2f}".format(x_ratio[a])+','+"{0:.2f}".format(y_ratio[a])+'\n')		
