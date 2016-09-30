#!/usr/bin/python

# Read message from file and encrypt using caesar cipher

import sys
import getopt

def main(argv):
  # Local variables
  verbose = 0
  inputfile = ""
  outputfile = ""
  shift = 0
  inputString = ""


  # Try to read cmd line args
  try:
    opts, args = getopt.getopt(argv, "hvi:o:s:I:")
  except getopt.GetoptError:
    print("Usage: caesar.py -h")
    sys.exit(1)

  # Parse args
  for opt, arg in opts:
    if opt == "-h":
      print("Minimum invocation: caesar.py -s [..] -i [..]")
      sys.exit()
    elif opt == "-v":
      verbose = 1
    elif opt == "-i":
      inputfile = arg
    elif opt == "-o":
      outputfile = arg
    elif opt == "-s":
      shift = int(arg)
    elif opt == "-I":
      inputString = arg

  # Check that required args were given
  if ((inputfile == "" and inputString == "") or shift == 0):
    print("Insufficient input arguments")
    sys.exit(1)

  # Chose input data
  if inputfile != "":
    # Read input string from file
    with open(inputfile, 'r') as myfile:
      data=myfile.read().upper().rstrip('\n')
  else:
    # Use string from invocation
    data=inputString.upper()

  result = ""
  for c in data:
    result += shiftChar(c, shift)

  print(result)





def shiftChar(x, s):
  # 'x' is input char
  # 's' is shift value
#  print("x= %c" % x)
#  print("x= %d" % s)

#  return chr((((ord(x) - ord('A')) + (s%25))%25) + 65)

  # Get unicode value of 'x' and shift it to the range 0-24
  orgVal = ord(x) - ord('A')
#  print("orgVal= %d" % orgVal)

  # Apply shift
  tmp = orgVal + (s%25)
#  print("tmp= %d" % tmp)

  # Adjust result to the range A-Z (Unicode 65-90)
  outputVal = 65 + (tmp%25)
#  print("outputVal= %d" % outputVal)

  # Return result
  return chr(outputVal)


if __name__ == "__main__":
   main(sys.argv[1:])
