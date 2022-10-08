# This is a simple shell code for running experients
#!/bin/bash
# readonly FOLDER2="results"  way to create a constant variable in shell script

# function to run experiments
readonly sample_ratio=0.75

RunExperiments() {

flag=0

cd data/test

for FILE in *;
do
	if [ $flag -eq 0 ]
	then
		cd ../../results;
		mkdir "$FILE";
		flag=1;	
	else
		mkdir "$FILE";
	fi
done

pwd #sample-proj/results
cd ../
for FILE in data/test/*;
do
	echo "$FILE"
	python src/test.py "$FILE" "$sample_ratio"
done

}

# function to generate in/out-degree distribution files
GetDistributions() {

flag=0

cd data/test

for FILE in *;
do
	if [ $flag -eq 0 ]
	then
		cd ../../results;
		flag=1;	
	fi
	cd "$FILE"
	cwd=$(pwd)
	echo $cwd
	python ../../src/cal-fre.py $cwd/sampled_"$sample_ratio"_degree_sequence.txt "$FILE" $sample_ratio 
	cd ..
done

echo "Distribution Generation finished!"
echo "Current directory is: $(pwd)"

}

###

for arg in "$@"; do
  if [[ "$arg" = -re ]] || [[ "$arg" = --run-experiments ]]; then
    ARG_RUN_EXPERIMENTS=true
  fi
  if [[ "$arg" = -gd ]] || [[ "$arg" = --get-distributions ]]; then
    ARG_GET_DISTRIBUTIONS=true
  fi
  if [[ "$arg" = -a ]] || [[ "$arg" = --aws-copy ]]; then
    ARG_AWS_COPY=true
  fi
done

###

if [[ "$ARG_RUN_EXPERIMENTS" = true ]]; then
  RunExperiments
fi

if [[ "$ARG_GET_DISTRIBUTIONS" = true ]]; then
  GetDistributions
fi

if [[ "$ARG_AWS_COPY" = true ]]; then
  AwsCopy
fi



