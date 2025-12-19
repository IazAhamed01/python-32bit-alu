# Day 2: 32-bit helpers for ALU simulation

BIT_WIDTH = 32

def mask_32(value):
    return value & 0xFFFFFFFF

def to_signed_32(value):
    if value & 0x80000000:
        return value - 0x100000000
    return value


# Day 3: Core ALU operations

def add_32(a, b):
    return mask_32(a + b)

def sub_32(a, b):
    return mask_32(a - b)

def and_32(a, b):
    return mask_32(a & b)

def or_32(a, b):
    return mask_32(a | b)

def xor_32(a, b):
    return mask_32(a ^ b)
