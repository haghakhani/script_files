#!/bin/bash

for dir in $(ls sample*)
do
  echo $dir
  cp $dir/pileheightrecord.-00001 pileheights/
  mv pileheights/pileheightrecord.-00001 pileheights/$dir
done
