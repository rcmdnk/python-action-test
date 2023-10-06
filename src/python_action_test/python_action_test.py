import sys


def main() -> None:
    n_arg = len(sys.argv)
    if n_arg == 1:
        print("Hello World!")
    elif n_arg == 2:
        print(f"Hello {sys.argv[1]}!")
    else:
        print(f"Hello {', '.join(sys.argv[1:])}!")


if __name__ == "__main__":
    main()
