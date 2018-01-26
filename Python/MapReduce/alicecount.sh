#! /bin/bash 

cat ../data/aliceInwonderland.txt | python word_count_mapper.py | sort | python word_count_reducer.py 