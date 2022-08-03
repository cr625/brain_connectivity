#!/bin/bash
# sample: ./runMe.sh 

experimentPath=.
samplePath=$experimentPath/src/pnc_subjects.txt
measuresList=$experimentPath/src/featureList.txt
connectomesFolder=$experimentPath/pnc_fmri_connectomes

systemMaps=$experimentPath/src/Schaefer220.txt
hemisphereMaps=$experimentPath/src/Yeo_7system_in_Schaefer218_functionalOrder.txt
numNodes=218


bct_features_py=./scripts/bct_features.py


if [[ ! -e $measuresList ]]; then
	python $bct_features_py --printFullMeasureList > $measuresList
	echo "Features list file is not found!! A full features lits is generated in $measuresList . Check the file and rerun this script to generate features for connectomes. Exiting..."
	exit 1
fi

mkdir -p $experimentPath/features

python $bct_features_py --measuresList $measuresList --connectomesFolder $connectomesFolder/ --subjectsList $samplePath --systemMaps $systemMaps --hemisphereMaps $hemisphereMaps --outputFolder $experimentPath/features/ --numNodes $numNodes --verbose --normalizeConnectomes none


