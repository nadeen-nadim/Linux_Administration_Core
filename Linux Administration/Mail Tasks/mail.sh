#!/bin/bash

#write all history to file cmds_hist
history >> cmds_hist

# command to send history to my mail
mailx -A cmds_hist -s "cmds_hist" nadeenmnadim@hotmail.com

ln -s /etc/passwd passwd_link

mailx -A passwd_link -s "Passwd file" nadeenmnadim@hotmail.com

find /home/Desktop/my_codes 2> errors.txt
mailx -A errors.txt -s "Errors" nadeenmnadim@hotmail.com


