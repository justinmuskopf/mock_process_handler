from random import randint
from sys import argv

KB = 1024
PID = 0
FOOTPRINT = 1
CPU_CYCLES = 2

DEFAULT_NUM_PROCS = 10


class ProcessGenerator():
    MINIMUM_MEMORY_FOOTPRINT = KB
    MAXIMUM_MEMORY_FOOTPRINT = 100 * KB
    WANTED_FOOTPRINT_MEAN = 20 * KB

    MINIMUM_CPU_CYCLES = 1000
    MAXIMUM_CPU_CYCLES = 11000
    WANTED_MEAN_CYCLES = 6000

    MIN_PID = 1
    MAX_PID = pow(2, 15)

    DESC_STRINGS = ["PID", "Memory Footprint", "CPU Cycles"]

    def __init__(self):
        self.generated_processes = []

    def _get_mean(self, idx):
        items = [p[idx] for p in self.generated_processes]

        mean = int(sum(items) / len(self.generated_processes))

        return mean

    def get_mean_footprint(self):
        return self._get_mean(FOOTPRINT)

    def get_mean_cpu_cycles(self):
        return self._get_mean(CPU_CYCLES)

    def _get_random(self, min_val, wanted_val, max_val, idx):
        if len(self.generated_processes) == 0:
            return randint(min_val, max_val)

        print_string = "| {} mean is {} and want {}, generating {} wanted value..."

        mean = self._get_mean(idx)

        if mean < wanted_val:
            value_string = "above"
            random_val = randint(wanted_val, max_val)
        elif mean > wanted_val:
            value_string = "below"
            random_val = randint(min_val, wanted_val)
        else:
            value_string = "around"
            random_val = randint(min_val, max_val)

        print(print_string.format(self.DESC_STRINGS[idx], mean, wanted_val, value_string))

        return random_val

    def _get_random_memory_footprint(self):
        return self._get_random(self.MINIMUM_MEMORY_FOOTPRINT,
                                self.WANTED_FOOTPRINT_MEAN,
                                self.MAXIMUM_MEMORY_FOOTPRINT,
                                FOOTPRINT)

    def _get_random_number_cpu_cycles(self):
        return self._get_random(self.MINIMUM_CPU_CYCLES,
                                self.WANTED_MEAN_CYCLES,
                                self.MAXIMUM_CPU_CYCLES,
                                CPU_CYCLES)

    def _get_random_pid(self):
        generated_pids = [p[PID] for p in self.generated_processes]

        pid = randint(self.MIN_PID, self.MAX_PID)
        while pid in generated_pids:
            pid = randint(self.MIN_PID, self.MAX_PID)

        return pid

    def get_new_process(self):
        pid = self._get_random_pid()
        memory_footprint = self._get_random_memory_footprint()
        cpu_cycles = self._get_random_number_cpu_cycles()

        process = (pid, memory_footprint, cpu_cycles)

        self.generated_processes.append(process)

        return process


class ProcessHandler():
    def __init__(self, num_processes=DEFAULT_NUM_PROCS):
        self.num_processes = num_processes
        self.processes = []

        self.pg = ProcessGenerator()

    def _print_process(self, process):
        print("| PID: {}".format(process[0]))
        print("| CPU Cycles: {}".format(process[2]))
        print("| Memory Footprint (KB): {}".format(self._bytes_to_kilobytes(process[1])))

    def print_processes(self):
        for process in self.processes:
            self._print_process(process)

    def _generate_processes(self):
        for i in range(self.num_processes):
            print("|----------------------------------")
            print("|-- Process {}".format(i + 1))
            print("|----------------------------------")
            process = self.pg.get_new_process()
            print("|----------------------------------")
            self._print_process(process)
            print("|----------------------------------\n")

    def get_mean_footprint(self):
        return self.pg.get_mean_footprint()

    def _bytes_to_kilobytes(self, nbytes):
        return round(nbytes / KB, 2)

    def get_mean_footprint_kb(self):
        nbytes = self.get_mean_footprint()

        return int(self._bytes_to_kilobytes(nbytes))

    def get_mean_cpu_cycles(self):
        return self.pg.get_mean_cpu_cycles()

    def get_processes(self):
        return self.pg.generated_processes

    def start(self):
        self._generate_processes()


def main():
    num_processes = DEFAULT_NUM_PROCS

    if len(argv) == 1:
        print("To define the number of processes to generate, provide this script an argument!")
    else:
        num_processes = int(argv[1])

    ph = ProcessHandler(num_processes)

    ph.start()


if __name__ == "__main__":
    main()
