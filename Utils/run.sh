python stanford_extract.py -p pred-challenge.149.json \
	-o output
cd output
zip results_spotting.zip */*/*/results_spotting.json
