from process_handler import ProcessHandler
from sys import argv

DEFAULT_NUM_PROCS = 10


def main():
    num_processes = DEFAULT_NUM_PROCS

    if len(argv) == 1:
        print("To define the number of processes to generate, provide this script an argument!")
    else:
        num_processes = int(argv[1])

    if (num_processes <= 0):
        print("ERROR: Invalid number of processes provided.")
        exit(1)

    ph = ProcessHandler(num_processes)

    ph.start()

    ph.print_statistics()


if __name__ == "__main__":
    main()
