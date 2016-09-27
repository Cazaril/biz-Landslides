#!/bin/bash


for i in $(ls *.html);
do
    sed -i 's_\(src=".\+.png" \)title="=\([[:digit:]]\+\)x\([[:digit:]]\+\)"_\1 width="\2" height="\3" _g' ./$i
done
    
