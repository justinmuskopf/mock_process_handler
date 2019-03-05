from process_generator import ProcessGenerator

KB = 1024
PID = 0
FOOTPRINT = 1
CPU_CYCLES = 2


class ProcessHandler():
    def __init__(self, num_processes=1):
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

    def print_statistics(self):
        mean_cycles = self.get_mean_cpu_cycles()
        mean_footprint = self.get_mean_footprint_kb()

        print()
        print("--- Mean CPU cycles: {}".format(mean_cycles))
        print("--- Mean Memory Footprint: {} KB".format(mean_footprint))
        print()

    def start(self):
        self._generate_processes()
