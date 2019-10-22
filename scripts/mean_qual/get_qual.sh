#!/bin/bash
samtools view ${4} ${1}:${2}-${3} | awk '{sum+=$5} END { if(NR!=0) {print sum/NR} else {print 0}}'
