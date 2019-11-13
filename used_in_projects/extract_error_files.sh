#! /bin/bash
for i in `seq 0 64`;
do
  if [ -d "n_sample$i" ]; then
    echo $i
#    mkdir hmax/$i
    cp n_sample$i/hmax* hmax/$i
  fi
done
