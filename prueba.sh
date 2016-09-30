#!/bin/bash


for i in $(ls *.text);
do
    pandoc -f rst -t commonmark -o ./$i.md ./$i
    #    sed -i -r 's| Business API ecosystem|Business API ecosystem|g' ./$i
    #    sed -i -r 's|(src=".*") (title="=1x1")|\1 width="1200" height="410"|g' ./$i
    #    sed -i -r 's|Application Mashup \(WireCloud\) course \@ http\:\/\/edu\.fiware\.org|Business API Ecosystem \(WireCloud\) course \@ http\:\/\/edu\.fiware\.org|g' ./$i
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

for i in $(ls *.text.md);
do
    rename 's/\.text.md$/\.md/' ./$i
done

for i in $(ls *.md);
do
    sed -i -r 's|(\#+ .*)|---\n\n\1|g' ./$i
    sed -i -r 's|(!\[\w*\]\(.*\))|---\n\n\1|g' ./$i
    sed -i -r '0,/\\\*/ s|\\\*|# Introduction to Business API ecosystem\n\n.fx: cover\n\n@conwet\n\n---\n|g' ./$i
    sed -i -r 's|\\(# .*)|\n\1|g' ./$i
    sed -i -r '0,/\\\*/ s|\\\*||g' ./$i
    echo "

---

.fx: back-cover

Thanks!

FIWARE                                FIWARE Lab
OPEN APIs FOR OPEN MINDS              Spark your imagination

         www.fiware.org               FIWARE Ops
twitter: @Fiware                      Easing your operations" >> $i
done
