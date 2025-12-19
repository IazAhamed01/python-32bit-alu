import sys
sys.path.append(".")

from src.alu import ALU

alu = ALU()

print("ADD :", alu.execute("ADD", 10, 5))
print("SUB :", alu.execute("SUB", 10, 5))
print("SHL :", alu.execute("SHL", 1, 2))   # 1 << 2
print("SHR :", alu.execute("SHR", 8, 2))   # 8 >> 2
print("ZERO:", alu.execute("SUB", 5, 5))
