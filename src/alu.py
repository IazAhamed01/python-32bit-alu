from .operations import (
    mask_32, to_signed_32,
    add_32, sub_32, and_32, or_32, xor_32
)

class ALU:
    def __init__(self):
        self.bit_width = 32

    def execute(self, opcode, a, b=0):
        a = mask_32(a)
        b = mask_32(b)

        if opcode == "ADD":
            result = add_32(a, b)
        elif opcode == "SUB":
            result = sub_32(a, b)
        elif opcode == "AND":
            result = and_32(a, b)
        elif opcode == "OR":
            result = or_32(a, b)
        elif opcode == "XOR":
            result = xor_32(a, b)
        else:
            raise ValueError("Invalid opcode")

        return to_signed_32(result)
