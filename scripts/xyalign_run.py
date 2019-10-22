# to run xyalign on bams

import os
import subprocess

bamfile=[]

t=[]

bam_folder=raw_input("Please enter folder name for BAM files: ")
output_folder=raw_input("Please enter output folder:")

for path, subdirs, files in os.walk(bam_folder):  #to get the names of each sample 
	for filename in files:
		if (filename.endswith('.bam')):
			bamfile.append(filename)
			t=filename.strip().split('.')

			t=[]

for i in range(0, len(bamfile)):
	subprocess.Popen('xyalign --CHROM_STATS --use_counts --bam %s/%s --ref /home/dnanexus/hs37d5/hs37d5.fa --output_dir %s/xyalign-chrom-stats/ --sample_id %s --chromosomes X Y --target_bed /home/dnanexus/target-bed/20130108.exome.targets.nochr.bed --logfile xyalign_stat.log' %(bam_folder,bamfile[i],output_folder,bamfile[i]), shell=True)

result_file=[]

t1=[]

for path, subdirs, files in os.walk(output_folder+'/xyalign-chrom-stats/results'):
        for filename in files:
                if (filename.endswith('.txt')):
                        result_file.append(output_folder+'/xyalign-chrom-stats/results/'+filename)
                        
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

with open(output_folder+'/gender_ratio.csv', 'w') as gender_ratio_file:
        gender_ratio_file.write('file,reads mapped to chrX(%),reads mapped to chrY(%)\n')
        for a in range(0, len(result_file)):
                gender_ratio_file.write(bamfile[a]+','+"{0:.2f}".format(x_ratio[a])+','+"{0:.2f}".format(y_ratio[a])+'\n')
