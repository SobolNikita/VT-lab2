import sys


def main():
  if len(sys.argv) < 2:
    print("Usage: python task02.py <number_of_rows>")
    sys.exit(1)

  try:
    rows = int(sys.argv[1])
  except ValueError:
    print("Error: number of rows must be an integer.")
    sys.exit(1)

  if rows < 1:
    print("Error: number of rows must be at least 1.")
    sys.exit(1)

  print("<table border=\"1\">")
  print("  <thead>")
  print("    <tr><th>Row #</th></tr>")
  print("  </thead>")
  print("  <tbody>")
  for i in range(1, rows + 1):
    print(f"    <tr><td>{i}</td></tr>")
  print("  </tbody>")
  print("</table>")


if __name__ == "__main__":
  main()
