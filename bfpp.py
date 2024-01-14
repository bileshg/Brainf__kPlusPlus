import sys


class Memory:
    def __init__(self):
        self._cells = [0] * 100
        self._pointer = 0

    def get(self):
        return self._cells[self._pointer]

    def set(self, n):
        self._cells[self._pointer] = n

    def increment(self):
        self._cells[self._pointer] += 1

    def decrement(self):
        if self._cells[self._pointer] > 0:
            self._cells[self._pointer] -= 1

    def right(self):
        self._pointer += 1
        if self._pointer >= len(self._cells):
            self._cells.append(0)

    def left(self):
        if self._pointer > 0:
            self._pointer -= 1


class _Engine:
    _instance = None

    @staticmethod
    def cleanup(code):
        commands = set('><+-.,[]:;#$')
        return ''.join(c for c in code if c in commands)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._memory = Memory()
        self._stack = []
        self._source_code = None
        self._jump_table = None
        self._code_pointer = 0

    def _reset(self):
        self._memory = Memory()
        self._stack = []
        self._source_code = None
        self._jump_table = None
        self._code_pointer = 0

    def _create_jump_table(self):
        jump_table = {}
        stack = []

        for position, command in enumerate(self._source_code):
            if command == '[':
                stack.append(position)

            elif command == ']':
                left = stack.pop()
                right = position
                jump_table[left] = right
                jump_table[right] = left

        return jump_table

    def _execute(self, command):
        if command == '>':
            self._memory.right()
        elif command == '<':
            self._memory.left()
        elif command == '+':
            self._memory.increment()
        elif command == '-':
            self._memory.decrement()
        elif command == '.':
            print(chr(self._memory.get()), end='')
        elif command == ',':
            self._memory.set(ord(input()[0]))
        elif command == '[':
            if self._memory.get() == 0:
                self._code_pointer = self._jump_table[self._code_pointer]
        elif command == ']':
            if self._memory.get() != 0:
                self._code_pointer = self._jump_table[self._code_pointer]
        elif command == ':':
            print(self._memory.get(), end=' ')
        elif command == ';':
            self._memory.set(int(input()))
        elif command == '#':
            self._stack.append(self._memory.get())
        elif command == '$':
            self._memory.set(self._stack.pop())

    def run(self, source_code):
        self._reset()
        self._source_code = _Engine.cleanup(source_code)
        self._jump_table = self._create_jump_table()
        while self._code_pointer < len(source_code):
            self._execute(source_code[self._code_pointer])
            self._code_pointer += 1
        print()


bf = _Engine()


def main():
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r") as f:
            bf.run(f.read())
    else:
        print(f"Usage: {sys.argv[0]} filename")


if __name__ == "__main__":
    main()
