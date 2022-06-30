#!/usr/bin/python3

import sys
import re

def major2idx(num):
    if num == 8:
        return 0
    elif num > 64 and num < 72:
        return (num - 64) << 4
    elif num > 127 and num < 136:
        return (num - 120) << 4
    sys.exit(f"invalid scsi major")

if len(sys.argv) != 2:
    sys.exit(f"Usage: {sys.argv[0]} <scsi_major>:<scsi_minor>")

pattern = re.compile(r'^(\d+):(\d+)$')

result = pattern.match(sys.argv[1])
if result == None:
    sys.exit('argument must be "<scsi_major>:<scsi_minor"')
major = int(result.group(1))
minor = int(result.group(2))

index = (minor & 0xfff00) | major2idx(major) | ((minor >> 4) & 0xf)

name = ""
while True:
    name = chr((index % 26) + ord('a')) + name
    index = (index // 26) - 1
    if (index < 0):
        break
name = "sd" + name

print(name)
