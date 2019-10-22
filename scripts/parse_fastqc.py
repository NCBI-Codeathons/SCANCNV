#!/usr/bin/env python2.7

import collections
import os
import sys

fastqc_files_list = sys.argv[1]

metrics = collections.defaultdict(set)

# get fastqc/*_fastqc/fastqc_data.txt
# extract all metrics that failed and report them
with open(fastqc_files_list) as f:
    for raw_line in f:
        fastqc_filepath = raw_line.rstrip()
        with open(fastqc_filepath) as ff:
            for ffraw_line in ff:
                line = ffraw_line.rstrip()
                if 'fail' in line:
                    key, value = line.replace('>>','').replace(' ', '_').split('\t')
                    metrics[fastqc_filepath].add("%s\t%s" %(key, value))


# output failed metrics into a file                        
with open('fastqc_combined.metrics', 'w') as fout:
    for key, values in metrics.iteritems():
        fout.write(key + '\n')
        for value in values:
            fout.write(value + '\n')
