from html import escape

structure = {
    "level1_a": {
        "level2_a": {
            "level3_a": {
                "level4_a": {
                    "level5_a": "value_5a",
                    "level5_b": "value_5b",
                }
            }
        }
    },
    "level1_b": [
        "leaf1",
        ["nested_list_level2", ["nested_list_level3", ["nested_list_level4", ["nested_list_level5"]]]],
    ],
}

def color_for_level(level: int) -> str:
  colors = {1: "red", 2: "blue", 3: "green", 4: "purple"}
  return colors.get(level, "yellow")

def render(obj, level=1):
  html = []
  color = color_for_level(level)

  if isinstance(obj, dict):
    html.append("<ul>")
    for key, value in obj.items():
      html.append(f"<li><span style='color:{color}'>[{escape(str(key))}]</span>")
      html.append(render(value, level + 1))
      html.append("</li>")
    html.append("</ul>")
    elif isinstance(obj, (list, tuple)):
      html.append("<ul>")
      for item in obj:
        html.append("<li>")
        html.append(render(item, level + 1))
        html.append("</li>")
      html.append("</ul>")
    else:
      html.append(f"<span style='color:{color}'>{escape(str(obj))}</span>")

  return "\n".join(html)

def main():
  print("<!DOCTYPE html>")
  print("<html><head><meta charset='utf-8'><title>Structure</title></head><body>")
  print(render(structure, 1))
  print("</body></html>")

if __name__ == "__main__":
  main()
