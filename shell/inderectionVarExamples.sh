# Variable Indirection
# SRC: https://stackoverflow.com/questions/10820343/how-can-i-generate-new-variable-names-on-the-fly-in-a-shell-script

SIMU_ABC="MonSimuAbc"
SIMU_CDE="MonSimuCde"

PART1="MonSimu"
PART2="ABC CDE"

# Ex1: Create new vars with substring
for P2 in $PART2 ; do
  VAR="SIMU_$P2"
  echo "TEST: ${!VAR}"
done

# Ex2: Print generated variables
SAMPLE1='1-first.with.custom.name'
SAMPLE2='2-second.with.custom.name'
for (( i = 1; i <= 2; i++ ))
do
   var="SAMPLE$i"
   echo ${!var}
done
