from random import randint

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
