# Creston NVX Automation

Automate Crestron NVX Configuration


## Description

I wrote this program to automate some of the work when setting up multiple Crestron NVX devices. 
The program takes data from a spreadhsheet we get from a client with configuration information and uses the data from it
to automatically open web browser pages and fill in the information needed for configuration of the deivce.
It uses the Sellenium python library for that functionality. Currently it is able to do the initial password setup,
initial IP, Hostname, and other various setting configs. Plus it can upload firmware files from the PC to the devices. 
