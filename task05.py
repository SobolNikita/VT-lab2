import sys

def main():
  words = sys.argv[1:]
  if not words:
    print("Usage: python task05.py <word1> <word2> <word3> ...")
    sys.exit(1)
  longest_word = max(words, key=len)
  print(longest_word)

if __name__ == "__main__":
  main()