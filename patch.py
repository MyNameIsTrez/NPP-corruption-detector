#!/usr/bin/env python3

import sys

# A patch is (offset, bytes to write in hex)
patches = ((0, "4142"),)


def main():
    filename = sys.argv[1]

    with open(filename, "r+b") as f:
        for index, (offset, byte_string) in enumerate(patches):
            f.seek(offset)
            f.write(bytes.fromhex(byte_string))


if __name__ == "__main__":
    main()
