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
Meteor is a cool way to create javascript apps https://www.meteor.com/ & [intro](https://www.youtube.com/watch?v=wBp0Rb-ZJak&t=13777s)
