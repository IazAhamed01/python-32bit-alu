# Day 2: 32-bit helpers for ALU simulation

BIT_WIDTH = 32

def mask_32(value):
    """Limit value to 32 bits"""
    return value & 0xFFFFFFFF


def to_signed_32(value):
    """Convert unsigned 32-bit to signed 32-bit"""
    if value & 0x80000000:
        return value - 0x100000000
    return value
