import sys


def main():
  if len(sys.argv) < 2:
    print("Usage: python task_additional02.py <number_of_rows> [output.html]", file=sys.stderr)
    sys.exit(1)

  try:
    n = int(sys.argv[1])
  except ValueError:
    print("Error: provide an integer number of rows.", file=sys.stderr)
    sys.exit(1)

  if n < 1:
    print("Error: number of rows must be at least 1.", file=sys.stderr)
    sys.exit(1)

  out_path = sys.argv[2] if len(sys.argv) > 2 else "table.html"

  parts = []
  parts.append("<!DOCTYPE html>")
  parts.append("<html><head><meta charset='utf-8'><title>Table</title></head><body>")
  parts.append("<table border='0' cellpadding='8' cellspacing='0' style='border-collapse: collapse; width: 100%;'>")

  for i in range(n):
    if n == 1:
      gray = 128
    else:
      gray = int(255 * (n - 1 - i) / (n - 1))
    color = f"rgb({gray},{gray},{gray})"
    text_color = "white" if gray < 128 else "black"
    parts.append(f"  <tr style='background-color: {color}; color: {text_color};'>")
    parts.append(f"    <td>Row {i + 1}</td>")
    parts.append("  </tr>")

  parts.append("</table>")
  parts.append("</body></html>")

  html = "\n".join(parts)
  with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)
  print(f"Created file: {out_path}", file=sys.stderr)


if __name__ == "__main__":
  main()
