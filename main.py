import sys
import argparse
import time
from container import Container

args = sys.argv


def main():
    """ Точка входа """
    print("Homework №3\nKulyakhtina Alyona, BSE 204:\nTask 12 - Animals, func 10\n")
    print("COMMANDS:")
    print("-i: Working with data from a file")
    print("-r: Random data generation")
    print()
    start = time.time()
    try:
        if len(sys.argv) != 3:
            print("Incorrect parameters!")
            sys.exit(0)

        parser = argparse.ArgumentParser(description="animal ....")
        parser.add_argument('-i', '--input_file',
                            help='specify path/filename',
                            type=str)
        parser.add_argument('-r', '--number_of_animals',
                            help='generates random input',
                            type=int)

        args = parser.parse_args()
        container = Container()
    except:
        print("ERROR!")
        sys.exit(0)

    if args.input_file is not None:
        container.read_from_file(args.input_file)
    else:
        container.generate_random(args.number_of_animals)
    container.straight_sort()
    with open("test/output.txt", 'w') as f:
        f.write(str(container))
    end = time.time()
    print(end - start)
    return 0

if __name__ == '__main__':
    main()