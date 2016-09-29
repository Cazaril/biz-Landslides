#!/bin/bash


for i in $(ls *.html);
do
    #    sed -i -r 's| Business API ecosystem|Business API ecosystem|g' ./$i
    #    sed -i -r 's|(src=".*") (title="=1x1")|\1 width="1200" height="410"|g' ./$i
    sed -i -r 's|Application Mashup \(WireCloud\) course \@ http\:\/\/edu\.fiware\.org|Business API Ecosystem \(WireCloud\) course \@ http\:\/\/edu\.fiware\.org|g' ./$i
    #    sed -i -r 's| (=1x1)|\1|g' ./$i
#     echo "

# ---

# .fx: back-cover

# Thanks!

# FIWARE                                FIWARE Lab
# OPEN APIs FOR OPEN MINDS              Spark your imagination

#          www.fiware.org               FIWARE Ops
# twitter: @Fiware                      Easing your operations" >> $i
#    sed -i -r 's_=[[:digit:]]+x[[:digit:]]+_ _g' ./$i
done
    
