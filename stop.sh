#!/usr/bin/env bash

# build the script name, check for extension
scriptName=$1
# if [[ "$STR" != *".py" ]]; then
#   scriptName+=".py"
# fi

# grep all processes with the script name
proc_str=$(ps aux | grep $scriptName)

# split the string at linebreaks
proc_words=(${proc_str//" "/ })

# now loop through the above array and parse all process ids
# to kill the corresponing processes subsequently
usr="$(whoami)"
delete=0
for i in "${proc_lines[@]}"
do
    if [[ $delete == 1 ]]; then
        delete=0
        #kill -9 $i 
        echo 'hit' $i 
    fi
    if [[ $usr == $i ]]; then
        
        delete=1
    fi
done



# close all pins
#python3 closePins.py