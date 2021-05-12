# OSCP-Buffer-Overflow

Python3 Scripts for OSCP buffer overflow exploitation

## Usage

This repository is a compilation of 4 scripts used in the different steps of the OSCP buffer overflow exercise, and a little library used for storing the variables wich its value doesn't change along the exploitation. This variables are the Host IP, the Port in wich the app is running and the offset value. The library also contains a function to make the requests to the app, which is called every time we need to send any string to the server.

The order in wich the scripts are used is:

1. `fuzz.py`: This script fuzzes the app in order to determine approximately how many bytes are needed for the app to crash.
2. `pattern.py`: This script make use of a file created by the user by redirecting the output of the pattern_create.rb tool. More details in the scrpit.
3. `badchars.py`: This script defines a variable in wich all characters are present. It is orientated to make the badchar check without using mona or any other tool, just the debuger.
4. `exploit.py`: This script is the one that embeeds the shellcode in the payload. Also, we ned to set the ESP JUMP. This can be done by using mona and the badchars we found(usually \x00 and \x0A are badchars).


