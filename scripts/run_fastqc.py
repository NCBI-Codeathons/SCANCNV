#!/usr/bin/env python2.7

import os
import subprocess
import sys

bam_filelist = sys.argv[1]

os.mkdir('fastqc')  # outputdir

# for each bam filepath in the filelist
# run fastqc tool
with open(bam_filelist) as f:
    for raw_line in f:
        bam_filename = raw_line.rstrip()
        assert bam_filename.endswith('bam')
        subprocess.Popen('fastqc --extract -k 7 -o fastqc -f bam --nogroup %s -q' %(bam_filename), shell=True)
