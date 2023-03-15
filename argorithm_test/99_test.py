def nine_math():
    for i in range(1, 10):
        # print(f"{i}x1={i*1}")
        for j in range(1, i + 1):
            print(f"{i}x{j}={i * j}", end=" ")
        print()


if __name__ == '__main__':
    nine_math()
