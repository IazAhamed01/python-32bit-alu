import sys
sys.path.append(".")

from src.alu import ALU

alu = ALU()

print("ADD :", alu.execute("ADD", 10, 5))
print("SUB :", alu.execute("SUB", 10, 5))
print("AND :", alu.execute("AND", 10, 5))
print("OR  :", alu.execute("OR", 10, 5))
print("XOR :", alu.execute("XOR", 10, 5))

# Overflow test
print("ADD overflow:", alu.execute("ADD", 2**31 - 1, 1))
