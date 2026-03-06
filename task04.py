import sys


def main():
  if len(sys.argv) < 2:
    print("Usage: python task04.py <number>")
    sys.exit(1)

  number_str = sys.argv[1].lstrip("-")
  if not number_str or not number_str.isdigit():
    print("Error: parameter must be an integer (e.g. 123 or -456).")
    sys.exit(1)

  digit_sum = 0
  for digit in number_str:
    digit_sum += int(digit)
  print(digit_sum)


if __name__ == "__main__":
  main()
