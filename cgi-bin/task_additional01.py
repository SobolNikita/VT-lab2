import sys
import urllib.parse
import os

def detect_type(s):
  try:
    int(s)
    return "integer"
  except ValueError:
    pass

  try:
    float(s)
    return "float"
  except ValueError:
    pass

  return "string"

def main():
  query_string = os.environ.get("QUERY_STRING", "")
  
  form = urllib.parse.parse_qs(query_string)
  
  print("Content-Type: text/html; charset=utf-8")
  print()

  print("<!DOCTYPE html>")
  print("<html><head><meta charset='utf-8'><title>Types</title></head><body>")
  print("<h1>GET parameters types</h1>")
  print("<table border='1'><tr><th>Name</th><th>Value</th><th>Type</th></tr>")

  for key, values in form.items():
    for v in values:
      t = detect_type(v)
      print(f"<tr><td>{key}</td><td>{v}</td><td>{t}</td></tr>")

  print("</table></body></html>")

if __name__ == "__main__":
    main()
