#!/bin/bash


for i in $(ls *.md);
do
    echo "

---

.fx: back-cover

Thanks!

FIWARE                                FIWARE Lab
OPEN APIs FOR OPEN MINDS              Spark your imagination

         www.fiware.org               FIWARE Ops
twitter: @Fiware                      Easing your operations" >> $i
#    sed -i -r 's_=[[:digit:]]+x[[:digit:]]+_ _g' ./$i
done
    
