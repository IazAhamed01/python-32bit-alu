from .operations import mask_32, to_signed_32

class ALU:
    def __init__(self):
        self.bit_width = 32

    def execute(self, opcode, a, b=0):
        a = mask_32(a)
        b = mask_32(b)
        return to_signed_32(a), to_signed_32(b)
