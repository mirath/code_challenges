#!/bin/bash

for case in $(ls -1 cases/*-input.txt);
    do
	echo Running $case
	cat $case | python3 subset_component2.py
	cat ${case%%-input.txt}-output.txt
    done
