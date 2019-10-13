# ScanCNV

Creating an awesome tool to perform ScanCNV on WES data independent of callers/platform that focuses on confidence and reportability of CNV calls, particularly in clinical data.
ScanCNV creates a unified independent set of metrics for Quality Control on CNV calls to identify false positive calls and enable cross caller comparisons.
We use fastqc to evaluate overall library metrics, focusing on whether or not the overall library passes basecall qualities.
### Motivation:
* CNV callers based on WES frequently produce noisy/false positive calls
* Validating these calls involves MPLA/external tools: time + memory 
### Solution: 
* Unified independent set of metrics for QCing CNV calls
* Identify false positive calls 
* Enable cross callers comparison 
# Workflow:
![](https://github.com/NCBI-Codeathons/CNV_QC/raw/master/workflow_new.png)

# Inputs
* Bam files
* CNV calls in VCF format
# Outputs

# Usage
```
python parse_fastqc.py <fastqc> 
```
### Parameters

# Datasets:
* Simulated CNV 6 samples (males and females) fastq data (truthset: https://docs.google.com/spreadsheets/d/1TcpIsANN-rxTqyr-k5E9MS0ijj_5GxyNBR-4wFGaJUw/edit#gid=0)
* 1000Genomes 10 random samples (males and females) mapped data

# QC metrics:
* Read quality in SV - python to pull from vcf
* Outliers 
* Read quality (just use a subset: 2nd 10k)
* Sex identification - XYAlign
* Relatedness of samples - PLINK
* Noisiness of read depth - python to pull from vcf
* Distribution of calls - python to pull from vcf
* Mappability
* GC content - DangerTrack
* Stability - DangerTrack
* SD of read depth across samples - python to pull from vcf


# Dependencies
* Plink 
```
wget http://math.uic.edu/t3m/plink/PLink.dmg
tar xfz plink.tar.gz
cd plink
python -m plink.app
```
* DangerTrack
* Miniconda
```
wget https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh
sh Miniconda2-latest-Linux-x86_64.sh
```
* Samtools v 1.9
```
conda install -c conda-forge -c bioconda samtools
```
* Pyvcf
```
conda install -c bioconda pyvcf
```
* FastQC v0.11.8
```
conda install -c bioconda fastqc
```
* XYalign v1.1.6
```
conda install -c bioconda xyalign
```
* Pysam v >0.13
```
Condo install -c bioconda pysam=0.13
```
* Bedtools v2.29.0
```
conda install -c bioconda bedtools
```
* BWA
```
conda install -c bioconda bwa
```
* hs37d5 human genome reference
* Targeted capture regions bed file

