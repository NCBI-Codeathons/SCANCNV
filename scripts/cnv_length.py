# to flag cnvs based on length

chrom=[]
pos=[]
info=[]
svlen_field=[]
svlen=[]


t1=[]

with open('/home/dnanexus/calls/female.library4.read1_markdup.vcf', 'r') as vcf_file:
	for line in vcf_file.readlines():
		if line.startswith('#'):
			continue
		t1=line.strip().split("\t")
		chrom.append(t1[0])
		pos.append(t1[1])
		info=t1[7].strip().split(";")
		for i in range(0, len(info)):
			if(info[i].startswith("SVLEN")):
				svlen_field=info[i].strip().split('=')
				svlen.append(int(svlen_field[1]))
		info=[]
		svlen_field=[]

with open('/home/dnanexus/calls/cnvlen.csv', 'w') as length_file:
	length_file.write('chrom,pos,cnvlength\n')
	for j in range(0, len(svlen)):
		if((svlen[j] <= -5000000) or (svlen[j] >= 5000000)):
			length_file.write(str(chrom[j])+','+str(pos[j])+','+str(svlen[j])+'\n')						
