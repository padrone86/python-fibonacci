def fibonacci(i: int) -> int:
    if i == 1:
        return 0
    elif i == 2:
        return 1
    elif i >= 3:
        return fibonacci(i - 2) + fibonacci(i - 1)
    else:
        raise Exception(f"不正な数です: {i}")


if __name__ == "__main__":
    input_number = input("数値を入力: ")
    print([fibonacci(i) for i in range(1, int(input_number))])
