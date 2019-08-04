#!/bin/bash

mkdir build
mkdir build/libsc build/p4est build/mangll build/maoi build/dgea
SRC=$(pwd)
BLD=$SRC/build
SC=$BLD/libsc/local
P4EST=$BLD/p4est/local
MANGLL=$BLD/mangll/local
MAOI=$BLD/maoi/local

export CFLAGS="-g -O0"
export CXXFLAGS="-g -O0"
export CC=mpicc
export CXX=mpicxx
export FC=mpif77

# this has to be uncommented in case of using MKL 
#export LIBS="-lmkl_intel_lp64 -lmkl_core -lmkl_sequential -lpthread "

# this is reuired if it's not already defined 
TRILINOS_DIR=/home/hossein/codes/builds/trilinos

# clonning from the source
git clone -b works_w_maoi git@gitlab.com:haghakhani/dgea.git
git clone -b bc/sc4dgea git@gitlab.com:haghakhani/libsc.git
git clone -b p4est4dgea git@gitlab.com:haghakhani/p4est.git
git clone -b works_w_maoi git@gitlab.com:haghakhani/mangll.git
git clone -b works_w_maoi git@gitlab.com:haghakhani/maoi.git

# creating bootstrap files
cd $SRC/libsc && ./bootstrap 
cd $SRC/p4est && ./bootstrap $SRC/libsc/config 
cd $SRC/mangll && ./bootstrap $SRC/libsc/config $SRC/p4est/config  
cd $SRC/maoi  && ./bootstrap $SRC/libsc/config
cd $SRC/dgea && ./bootstrap $SRC/libsc/config 

# installing libsc
echo "installing libsc"
cd $BLD/libsc
$SRC/libsc/configure --enable-mpi\
    && make -j4 && make install


# installing p4est
echo "installing p4est"
cd $BLD/p4est 
$SRC/p4est/configure --enable-mpi --with-sc=$SC\
    && make -j4 && make install

# installing mangll
echo "installing mangll"
cd $BLD/mangll
$SRC/mangll/configure \
    --enable-mpi --with-sc=$BLD/libsc/local --with-p4est=$P4EST\
    && make -j4 && make install

# installing maoi
echo "installing maoi"
cd $BLD/maoi
export CFLAGS="-I${TRILINOS_DIR}/include $CFLAGS"
export CXXFLAGS="-I${TRILINOS_DIR}/include $CXXFLAGS"
export LDFLAGS="-L${TRILINOS_DIR}/lib"
export LIBS="$LIBS -lml -lepetra"
$SRC/maoi/configure --enable-mpi\
    --with-sc=$SC --with-p4est=$P4EST --with-trilinos=$TRILINOS_DIR\
    && make -j4 && make install 

# installing dgea
echo "installing dgea"
cd $BLD/dgea
export CXXFLAGS="-std=c++11 $CXXFLAGS"
$SRC/dgea/configure --enable-mpi\
    --with-sc=$SC --with-p4est=$P4EST --with-mangll=$MANGLL\
    --with-maoi=$MAOI --with-trilinos=$TRILINOS_DIR\
    && make -j4 && make install
