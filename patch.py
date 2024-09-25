#!/usr/bin/env python3

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
    ("?", 0x1354, 4, None),  # The change is normally 5, but it was 6 one time
    ("?", 0x135C, 4, 0x5),  # TODO: Its size might not be 4
    ("Time? (days)", 0x1377, 1, None),
    ("Time? (hours)", 0x1378, 1, None),
    ("Time? (minutes)", 0x1379, 1, None),
    ("Time? (seconds)", 0x137A, 1, None),
    ("Game time (days)", 0x1381, 1, None),
    ("Game time (hours)", 0x1382, 1, None),
    ("Game time (minutes)", 0x1383, 1, None),
    ("Game time (seconds)", 0x1384, 1, None),
    ("Menu time (days)", 0x138B, 1, None),
    ("Menu time (hours)", 0x138C, 1, None),
    ("Menu time (minutes)", 0x138D, 1, None),
    ("Menu time (seconds)", 0x138E, 1, None),
    ("Some time (days)", 0x139F, 1, None),
    ("Some time (hours)", 0x13A0, 1, None),
    ("Some time (minutes)", 0x13A1, 1, None),
    ("Some time (seconds)", 0x13A2, 1, None),
    ("Other time (days)", 0x13A9, 1, None),
    ("Other time (hours)", 0x13AA, 1, None),
    ("Other time (minutes)", 0x13AB, 1, None),
    ("Other time (seconds)", 0x13AC, 1, None),
    ("?", 0xAFFF, 1, None),  # TODO: Its size might not be 1
    ("?", 0xB000, 1, None),  # TODO: Its size might not be 1
    ("?", 0xB022, 1, None),  # TODO: Its size might not be 1
    ("?", 0xB02A, 1, None),  # TODO: Its size might not be 1
    ("?", 0xB02E, 1, None),  # TODO: Its size might not be 1
    ("?", 0xB032, 1, None),  # TODO: Its size might not be 1
    ("?", 0xB03E, 1, None),  # TODO: Its size might not be 1
    ("Palette usage time for Vasquez", 0xB277, 10, None),
    ("Level 1: Attempts", 0x80D324, 4, 0x1),
    ("Level 1: Successes (episode mode)", 0x80D330, 4, 0x1),
    ("Level 2: Attempts", 0x80D354, 4, 0x1),
    ("Level 2: Successes (episode mode)", 0x80D360, 4, 0x1),
    ("Level 3: Attempts", 0x80D384, 4, 0x1),
    ("Level 3: Successes (episode mode)", 0x80D390, 4, 0x1),
    ("Level 4: Attempts", 0x80D3B4, 4, 0x1),
    ("Level 4: Successes (episode mode)", 0x80D3C0, 4, 0x1),
    ("Level 5: Attempts", 0x80D3E4, 4, 0x2),
    ("Level 5: Failures", 0x80D3E8, 4, 0x1),
    ("Level 5: Successes (episode mode)", 0x80D3F0, 4, 0x1),
    ("Level 601: Attempts", 0x8143A4, 4, 0x1),
    ("Level 601: Failures", 0x8143A8, 4, 0x1),
    ("Episode 1: Attempts", 0x8F7924, 4, 0x2),
    ("Episode 1: Failures", 0x8F7928, 4, 0x1),
    ("Episode 1: Successes", 0x8F792C, 4, 0x1),
    ("Episode 121: Attempts", 0x8F8FA4, 4, 0x1),
    ("Episode 121: Failures", 0x8F8FA8, 4, 0x1),
    ("?", 0x3A30134, 4, 0x2),  # TODO: Its size might be smaller than 4
    ("?", 0x3A3013C, 4, 0x1),  # TODO: Its size might not be 4
    ("?", 0x3B30138, 4, None),  # A seemingly random integer, whose value always equals that of the value at 0x3B30140
    ("?", 0x3B30140, 4, None),  # A seemingly random integer, whose value always equals that of the value at 0x3B30138
)


def main():
    previous_filename = sys.argv[1]
    current_filename = sys.argv[2]

    with open(previous_filename, "r+b") as previous_file, open(
        current_filename, "r+b"
    ) as current_file:
        for index, (name, offset, size, expected_change) in enumerate(patches):
            print(f"\npatch name: {name}")

            print(f"offset: {hex(offset)}")

            previous_file.seek(offset)
            previous_value_bytes = previous_file.read(size)
            previous_value = int.from_bytes(previous_value_bytes, "little")
            print(f"previous_value: {previous_value} ({hex(previous_value)})")
            current_file.seek(offset)
            current_value_bytes = current_file.read(size)
            current_value = int.from_bytes(current_value_bytes, "little")
            print(f"current_value: {current_value} ({hex(current_value)})")

            if expected_change == None:
                print("no expected change")
            else:
                change = current_value - previous_value
                print(f"change: {change} ({hex(change)})")
                print(f"expected_change: {expected_change} ({hex(expected_change)})")

                assert change == expected_change

            new_value = bytes.fromhex("42" * size)
            previous_file.seek(offset)
            previous_file.write(new_value)
            current_file.seek(offset)
            current_file.write(new_value)


if __name__ == "__main__":
    main()
