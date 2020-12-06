**run the program, redirect the error and output to file and wont exit if the screen get closed**

```
nohup mpirun -np 4 ./titan > foo.out 2> foo.err < /dev/null &
```
-----------
**nested bash loop in a line to extract some file from a direc., rename and copy it to another directory**

```
for i in `seq 0 63`; do   for j in `seq 0 7`;    do      a=func_var_000$j;      a+=_$i;     cp sample$i/func_var_000$j result/$a;      done; done
```
--------------
**for loop on ls**
```
for dir in $(ls sample*)
do
  <some other code>
done
```
-----------
**to see the directories in a direc.**
```
ls -d */
```
-----------
**killing jobs by name**
```
pkill -f my_pattern
```
-----------
**to print the remote branches in git sorted by date**
```
for branch in `git branch -r | grep -v HEAD`;do echo -e `git show --format="%ci %cr" $branch | head -n 1` \\t$branch; done | sort -r
```
-----------
**to track and pull all of remote branches**
```
for remote in `git branch -r | grep -v /HEAD`; do git checkout --track $remote ; done
```
-----------
**search history by arrow keys add to ~/.inputrc**
```
#arrow up
"\e[A":history-search-backward
#arrow down
"\e[B":history-search-forward
```
-----------
**lists and sort recursively all files in a directory**
```
find -printf "%TY-%Tm-%Td %TT %p\n" | sort -n
```
-----------
**Changing login screen wallpaper in ubuntu**
```
sudo -i
xhost +SI:localuser:lightdm
su lightdm -s /bin/bash
gsettings set com.canonical.unity-greeter draw-user-backgrounds 'true'
gsettings set com.canonical.unity-greeter background 'path-to-image'
exit
```
-----------
**disk usage and sorting based on size**
```
du --max-depth=1 /path/to/directory | sort -n -r
```
-----------
**delete a file pattern in all subdirectories**
```
find . -type f -name '*.o' -delete
```
-----------
**syncing two folder if the server information has been set in /.ssh/config**
```
rsync -avzhe "ssh -p 8704" dgea/example/ dom:~/dgea/example
```
-----------
**Replace a String in Multiple Files in Linux Using Grep and Sed**
```
grep -rl matchstring somedir/ | xargs sed -i 's/string1/string2/g'
```
-----------
**number of lines of .c and .h files in a director sorted ascending**
```
find . -name '*.h' -o -name '*.c' | xargs wc -l|sort -n
```
-----------
**snipet to add colors to bash script**
```
#!/bin/bash
PATH=/bin:/usr/bin:

NONE='\033[00m'
RED='\033[01;31m'
GREEN='\033[01;32m'
YELLOW='\033[01;33m'
PURPLE='\033[01;35m'
CYAN='\033[01;36m'
WHITE='\033[01;37m'
BOLD='\033[1m'
UNDERLINE='\033[4m'

echo -e "This text is ${RED}red${NONE} and ${GREEN}green${NONE} and ${BOLD}bold${NONE} and ${UNDERLINE}underlined${NONE}."

tput sgr0
```
-----------
**handy aliases for git to got the next and previous commits. Need to be added to .git/config**
```
[alias]
    prev = checkout HEAD^1
    next = "!sh -c 'git log --reverse --pretty=%H master | awk \"/$(git rev-parse HEAD)/{getline;print}\" | xargs git checkout'"
```
-----------
**search a for an expression and print the next line**
```
awk '/EXPRESSION/{getline; print}' MYFILE
```
-----------
**download especific file type from a website**
```
wget --accept pdf,jpg --mirror --page-requisites --adjust-extension --convert-links --backup-converted --no-parent http://site/path/
```
-----------
**to find home of tex**
```
kpsewhich -var-value TEXMFHOME
```
-----------
**to find pckage installation location**
```
kpsewhich <package.sty>
```
-----------
**convert multiple png files to a gif file**
```
convert -delay 20 -loop 0 *.png non.gif
```
-----------
**trim a picture and take out the background**
```
convert input.png -trim output.png
pdfcrop [options] <input[.pdf]> [output file] 
```
-----------
**To add new themes and icons:**
   1. Install Unity Tweak
   2. create .icons & .themes directories in home directory 
   3. copy the themse and icons in those directory from everywhere (e.g. https://www.gnome-look.org/)
   4. select them from Unity Tweak panel
-------------
**pgrep** gives the PID based on the name of the application. e.g pgrep chrome

**killall** <application_name> to kill all of the application with that name once

-------------
control a service like elasticsearch or apache:
  1. with **service** command
    sudo service elasticsearch start
    sudo service elasticsearch stop
  2. with **systemctl** command
    sudo systemctl start elasticsearch
    sudo systemctl stop elasticsearch
----------------------
**crontab -e** to edit the file that sets the jobs that you want to run exactly at some time in "m h dom mon dow command"

-------------------
**to organize a folder of pdfs**
we can use pamphlet-max-filesize-kb=20 --pamphlet-max-pdf-pages flags to ignore the files that we think are not ebooks
```
./organize-ebooks.sh -v -km -ocr=true -owi -o=<outputfolder> -ofu=<uncertain_folder> -ofp=<pamphlet_folder> <input_folder> --pamphlet-max-filesize-kb=20 --pamphlet-max-pdf-pages=2
```
-------------------
**lsusb to show the connected usb devices**

-------------------
**somtimes it's needed to realize the connected wifi device**
```
sudo usb_modeswitch -KW -v 0bda -p 1a2b
```
0bda and 1a2b aredetermined from the output of lsusb

-------------------
**getopt example

#!/bin/bash -e

ARGUMENT_LIST=(
    "arg-one"
    "arg-two"
    "arg-three"
)


# read arguments
opts=$(getopt \
    --longoptions "$(printf "%s:," "${ARGUMENT_LIST[@]}")" \
    --name "$(basename "$0")" \
    --options "" \
    -- "$@"
)

eval set --$opts

while [[ $# -gt 0 ]]; do
    case "$1" in
        --arg-one)
            argOne=$2
            shift 2
            ;;

        --arg-two)
            argTwo=$2
            shift 2
            ;;

        --arg-three)
            argThree=$2
            shift 2
            ;;

        *)
            break
            ;;
    esac
done

echo $argOne $argTwo $argThree 
-------------------------------------------
