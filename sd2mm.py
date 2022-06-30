#!/usr/bin/python3

import sys

def sd_major(major_idx):
    if major_idx == 0:
        return 8
    elif major_idx < 8:
        return 65 + major_idx - 1
    else:
        return 128 + major_idx - 8


if len(sys.argv) != 2:
    sys.exit(f"Usage: {sys.argv[0]} <scsi_name>")

sd_name = sys.argv[1].lower()

if sd_name[0:2] != "sd":
    sys.exit("Err: scsi_name must start with 'sd'")

if len(sd_name) == 2:
    sys.exit("Err: scsi_name too short")

index = ord(sd_name[2]) - ord('a')
for c in sd_name[3:]:
    index = (index + 1) * 26 + ord(c) - ord('a')

major = sd_major((index & 0xf0) >> 4)
minor = ((index & 0xf) << 4) | (index & 0xfff00)

print(f"{major}:{minor}")
