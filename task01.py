import sys


def get_param_type(value):
  try:
    int(value)
    return "integer"
  except ValueError:
    pass

  try:
    float(value)
    return "float"
  except ValueError:
    pass

  return "string"


def main():
  params = sys.argv[1:]

  if not params:
    print("No parameters provided")
    return

  for i, param in enumerate(params, start=1):
    param_type = get_param_type(param)
    print(f"{i}. '{param}' - {param_type}")


if __name__ == "__main__":
  main()
