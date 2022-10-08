# This is a simple shell code for running experients
#!/bin/bash
# readonly FOLDER2="results"  way to create a constant variable in shell script


RunExperiments() {

flag=0

cd data/test

for FILE in *;
do
	if [ $flag -eq 0 ]
	then
		cd ../../results;
		mkdir $FILE;
		flag=1;	
	else
		mkdir $FILE;
	fi
done

pwd #sample-proj/results
cd ../
for FILE in data/test/*;
do
	echo $FILE
	python src/test.py $FILE 0.75
done

}

###

for arg in "$@"; do
  if [[ "$arg" = -r ]] || [[ "$arg" = --run-experiments ]]; then
    ARG_RUN_EXPERIMENTS=true
  fi
  if [[ "$arg" = -z ]] || [[ "$arg" = --zip-file ]]; then
    ARG_ZIP_FILE=true
  fi
  if [[ "$arg" = -a ]] || [[ "$arg" = --aws-copy ]]; then
    ARG_AWS_COPY=true
  fi
done

###

if [[ "$ARG_RUN_EXPERIMENTS" = true ]]; then
  RunExperiments
fi

if [[ "$ARG_ZIP_FILE" = true ]]; then
  ZipFile
fi

if [[ "$ARG_AWS_COPY" = true ]]; then
  AwsCopy
fi



