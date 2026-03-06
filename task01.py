import sys


def get_param_type(value):
  try:
    int(value)
    return "целое число"
  except ValueError:
    pass

  try:
    float(value)
    return "дробное число"
  except ValueError:
    pass

  return "строка"


def main():
  params = sys.argv[1:]

  if not params:
    print("Параметры не заданы")
    return

  for i, param in enumerate(params, start=1):
    param_type = get_param_type(param)
    print(f"{i}. '{param}' — {param_type}")


if __name__ == "__main__":
  main()
