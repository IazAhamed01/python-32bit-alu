from .operations import (
    mask_32, to_signed_32,
    add_32, sub_32, and_32, or_32, xor_32,
    shl_32, shr_32
)

class ALU:
    def __init__(self):
        self.bit_width = 32

    def execute(self, opcode, a, b=0):
        flags = {"Z": 0, "S": 0, "C": 0, "V": 0}

        a = mask_32(a)
        b = mask_32(b)

        if opcode == "ADD":
            result = add_32(a, b)
            flags["V"] = int(((a ^ result) & (b ^ result)) >> 31)

        elif opcode == "SUB":
            result = sub_32(a, b)
            flags["V"] = int(((a ^ b) & (a ^ result)) >> 31)

        elif opcode == "AND":
            result = and_32(a, b)

        elif opcode == "OR":
            result = or_32(a, b)

        elif opcode == "XOR":
            result = xor_32(a, b)

        elif opcode == "SHL":
            result, flags["C"] = shl_32(a, b)

        elif opcode == "SHR":
            result, flags["C"] = shr_32(a, b)

        else:
            raise ValueError("Invalid opcode")

        signed_result = to_signed_32(result)

        flags["Z"] = int(result == 0)
        flags["S"] = int((result >> 31) & 1)

        return signed_result, flags
