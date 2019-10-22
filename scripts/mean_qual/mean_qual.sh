#!/bin/bash

awk '$0!~/^#/{split($8,a,";");split(a[1],b,"END=");print $1"\t"$2"\t"b[2]"\t'$2'"}' $1 | awk '{system("bash get_qual.sh "$1" "$2" "$3" "$4)}'
