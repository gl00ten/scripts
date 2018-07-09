from difflib import SequenceMatcher
import os

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

os.chdir('/media/ssarah/ext4_scratch/')

l = os.listdir()

i = 0
f = 0
for i in range(len(l)):
    for f in range(i+1,len(l)):
        if similar(l[i],l[f]) > 0.9:
            print(l[i],'|||',l[f])
