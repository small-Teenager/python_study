class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu1 = CPU
cpu2 = cpu1

print(cpu1, id(cpu1))
print(cpu2, id(cpu2))


disk = Disk()

computer = Computer(cpu1, disk)

