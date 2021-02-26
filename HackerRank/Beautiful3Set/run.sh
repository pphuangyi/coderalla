#! /bin/bash

for i in {1..100}
do
	result=`./maximumIndependentSet.py $i 3`
	echo $i, $result
done
