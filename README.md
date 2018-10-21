# Bloom-Filter
Programs are written in python2.7

Directory Structure
===================
```
	1. bloom_filter.py
	2. main_bf.py
	3. count_bloom_filter.py
	4. main_cbf.py
	5. testset1-input.txt
	6. run.sh
	7. README.md
	8. trace.txt
```
File details
====================
```
- 'main_bf.py' contains the bloom filter implementation which uses class defined in 'bloom_filter.py'
- 'main_cbf.py' contains the counting bloom filter implementation which uses class defined in 'count_bloom_filter.py'
- 'testset1-input.txt' is the input to both bloom and counting bloom filters which contains 100 news reports covering terrorist activities in Latin America from Message Understanding Conference (MUC-3).
- 'run.sh' is the shell script to run the code.
- 'trace.txt' contains the sample output.
```
Dependencies
=====
```
Need to install mmh3 and bitVector packages which has been taken care in the script file.
```
How to run
=====
```
Please run the program as,

	./run.sh

This will invoke both bloom filter and counting bloom filter one after another.
```
