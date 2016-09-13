#!/bin/bash

for i in $( ls *.xmf ); do
    echo '</Grid>  ' >> $i
    echo '</Domain>' >> $i
    echo '</Xdmf>  ' >> $i
done
