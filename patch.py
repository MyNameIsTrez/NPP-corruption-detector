#!/usr/bin/env python3

import struct
import sys

# A patch is (name, offset, size, expected change)
# These are from nprofile.txt
patches = (
    ("Killcount", 0x1244, 8, 0x2),
    ("Killcount (mines)", 0x124C, 8, 0x2),
    ("Amount of gold collected", 0x12BC, 8, 0x24),
    ("Number of keypresses (jump)", 0x12DC, 8, 0x21),
    ("Number of keypresses (left)", 0x12E4, 8, 0xD),
    ("Number of keypresses (right)", 0x12EC, 8, 0x16),
    ("Number of attempts (episodes)", 0x130C, 8, 0x3),
    ("Number of victories (episodes)", 0x1314, 8, 0x1),
)


def main():
    previous_filename = sys.argv[1]
    current_filename = sys.argv[2]

    with open(previous_filename, "r+b") as previous_file, open(
        current_filename, "r+b"
    ) as current_file:
        for index, (name, offset, size, expected_change) in enumerate(patches):
            print(f"\npatch name: {name}")

            previous_file.seek(offset)
            previous_value_bytes = previous_file.read(8)
            print(f"previous_value_bytes: {previous_value_bytes}")
            current_file.seek(offset)
            current_value_bytes = current_file.read(8)
            print(f"current_value_bytes: {current_value_bytes}")

            previous_value = struct.unpack_from("<Q", previous_value_bytes)[0]
            print(f"previous_value: {previous_value}")
            current_value = struct.unpack_from("<Q", current_value_bytes)[0]
            print(f"current_value: {current_value}")

            change = current_value - previous_value
            print(f"change: {change}")
            print(f"expected_change: {expected_change}")

            assert change == expected_change

            new_value = bytes.fromhex("42" * size)
            previous_file.seek(offset)
            previous_file.write(new_value)
            current_file.seek(offset)
            current_file.write(new_value)


if __name__ == "__main__":
    main()
