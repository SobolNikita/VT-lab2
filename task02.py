import sys


def main():
  if len(sys.argv) < 2:
    print("Использование: python task02.py <количество_строк>")
    sys.exit(1)

  try:
    rows = int(sys.argv[1])
  except ValueError:
    print("Ошибка: количество строк должно быть целым числом.")
    sys.exit(1)

  if rows < 1:
    print("Ошибка: количество строк должно быть не меньше 1.")
    sys.exit(1)

    print("<table border=\"1\">")
    print("  <thead>")
    print("    <tr><th>№ строки</th></tr>")
    print("  </thead>")
    print("  <tbody>")
    for i in range(1, rows + 1):
      print(f"    <tr><td>{i}</td></tr>")
    print("  </tbody>")
    print("</table>")


if __name__ == "__main__":
  main()
