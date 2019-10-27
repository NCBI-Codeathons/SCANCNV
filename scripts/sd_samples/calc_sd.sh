for f in $1/*bam
do
  bash calc_depth.sh $f >> depth.txt
done

awk '{sum+=$1; sumsq+=$1*$1}END{print sqrt(sumsq/NR - (sum/NR)**2)}' depth.txt
