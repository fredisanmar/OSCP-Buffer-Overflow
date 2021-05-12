
from constants import *
### Aplication fuzzer

payload = "A"

counter = 1

for i in range(1, 100):
    print("fuzzing %s bytes" % counter)
    send_payload(payload * counter + "\n")
    counter = counter + 50
