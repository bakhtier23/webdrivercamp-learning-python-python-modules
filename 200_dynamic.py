#/usr/bin/python3

import sys


if __name__ == '__main__':
  num_args = len(sys.argv)

  if num_args == 0:
    print("0 arguments.")
  else:
    print(f"{num_args} arguments:")
    for i in range(1, num_args + 1):
      try:
        print(f"{i}: {sys.argv[i]}")
      except IndexError:
        print(f"Argument at index {i} does not exist.")
