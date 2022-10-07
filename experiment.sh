# This is a simple shell code for running experients
#!/bin/bash
readonly FOLDER1="data/test"
readonly FOLDER2="results"
flag=0

cd $FOLDER1

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

pwd
cd ../
for FILE in data/test/*;
do
	echo $FILE
	python src/test.py $FILE 0.75
done

