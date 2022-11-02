# This is a simple shell code for running experients
#!/bin/bash
# readonly FOLDER2="results"  way to create a constant variable in shell script

# function to run experiments
readonly sample_ratio=0.75
readonly seperation_line="------------------------------------------------------------------------------------------------------------------------------------------"

RunExperiments() {

data_folder="synthetic"
cd data/"$data_folder"
flag=0
for FILE in *;
do
	if [ $flag -eq 0 ];
	then
		cd ../../results;
		flag=1;	
	fi
	if ! [ -d "$FILE" ]; then
	# Take action if $DIR exists. #
	mkdir "$FILE"
	echo "create folder for $FILE"
	fi
done

pwd #sample-proj/results
cd ../
for FILE in data/"$data_folder"/*;
do
	echo "$FILE"
	python src/test.py "$FILE" "$sample_ratio"
done

}

# function to generate in/out-degree distribution files
GetDistributions() {

flag=0
data_folder="synthetic"

cd data/"$data_folder"

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

# function to get original degree distributions
GetOriginalDistributions() {

flag=0
data_folder="synthetic"
cd data/"$data_folder"

for FILE in sf*;
do
	if [ $flag -eq 0 ]
	then
		cd ../../results;
		flag=1;	
	fi
	if ! [ -d "$FILE" ]; then
	# Take action if $DIR exists. #
	mkdir "$FILE"
	echo "create folder for $FILE"
	fi
	cd "$FILE"
	cwd=$(pwd)
	echo $cwd
	python ../../src/get-original-distr.py ../../data/"$data_folder"/"$FILE" 
	python ../../src/cal-fre.py $cwd/original_degree_sequence.txt "$FILE" original
	cd ..
done

echo "Distribution Generation finished!"
echo "Current directory is: $(pwd)"

}

# function to plot in/out-degree distributions for both sample and originals
PlotDistributions() {
data_folder="synthetic"
flag=0

cd data/"$data_folder"

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
	python ../../src/plot.py "$cwd" "$FILE" $sample_ratio
	cd ..
done

echo "Distribution Generation finished!"
echo "Current directory is: $(pwd)"

}

# function to get in/out-degree frequency distributions from degree distributions
GetFrequencyDistributions() {
data_folder="synthetic"
flag=0

cd data/"$data_folder"

for FILE in *;
do
	if [ $flag -eq 0 ]
	then
		cd ../../results;
		flag=1;	
	fi
	cd "$FILE"
	cwd=$(pwd)
	# echo $cwd
	python ../../src/cal-fre-distr.py "$FILE"_"$sample_ratio"_ind-distr.csv "$FILE" "$sample_ratio" ind
	python ../../src/cal-fre-distr.py "$FILE"_"$sample_ratio"_outd-distr.csv "$FILE" "$sample_ratio" outd
	python ../../src/cal-fre-distr.py "$FILE"_original_ind-distr.csv "$FILE" original ind
	python ../../src/cal-fre-distr.py "$FILE"_original_outd-distr.csv "$FILE" original outd
	echo $seperation_line
	cd ..
done

echo "Frequency Distributions Generation finished!"
echo "Current directory is: $(pwd)"

}

# function to fit power law using frequency distributions
FitPowerLaws() {

flag=0
data_folder="synthetic"
cd data/"$data_folder"

for FILE in *;
do
	if [ $flag -eq 0 ]
	then
		cd ../../results;
		flag=1;	
	fi
	cd "$FILE"
	cwd=$(pwd)
	# echo $cwd
	python ../../src/fit-pl.py "$FILE"_"$sample_ratio"_ind-distr.csv "$FILE" "$sample_ratio" ind
	python ../../src/fit-pl.py "$FILE"_original_ind-distr.csv "$FILE" original ind
	python ../../src/fit-pl.py "$FILE"_"$sample_ratio"_outd-distr.csv "$FILE" "$sample_ratio" outd
	python ../../src/fit-pl.py "$FILE"_original_outd-distr.csv "$FILE" original outd
	echo $seperation_line
	cd ..
done

echo "Power Law fitting finished!"
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
  if [[ "$arg" = -god ]] || [[ "$arg" = --get-original-distributions ]]; then
    ARG_GET_ORIGINAL_DISTRIBUTIONS=true
  fi
  if [[ "$arg" = -pd ]] || [[ "$arg" = --plot-distributions ]]; then
    ARG_PLOT_DISTRIBUTIONS=true
  fi
  if [[ "$arg" = -gfd ]] || [[ "$arg" = --get-frequency-distributions ]]; then
    ARG_GET_FREQUENCY_DISTRIBUTIONS=true
  fi
  if [[ "$arg" = -fpl ]] || [[ "$arg" = --fit-power-laws ]]; then
    ARG_FIT_POWER_LAWS=true
  fi
done

###

if [[ "$ARG_RUN_EXPERIMENTS" = true ]]; then
  RunExperiments
fi

if [[ "$ARG_GET_DISTRIBUTIONS" = true ]]; then
  GetDistributions
fi

if [[ "$ARG_GET_ORIGINAL_DISTRIBUTIONS" = true ]]; then
  GetOriginalDistributions
fi

if [[ "$ARG_PLOT_DISTRIBUTIONS" = true ]]; then
  PlotDistributions
fi

if [[ "$ARG_GET_FREQUENCY_DISTRIBUTIONS" = true ]]; then
  GetFrequencyDistributions
fi
if [[ "$ARG_FIT_POWER_LAWS" = true ]]; then
  FitPowerLaws
fi



