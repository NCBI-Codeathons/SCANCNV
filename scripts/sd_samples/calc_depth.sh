samtools depth -a $1 > $1.depth
awk '{t+=$3}END{print(t/NR)}' $1.depth
