import sys
sys.path.append(".")

from src.alu import ALU

alu = ALU()

print(alu.execute("TEST", 300, 0))
print(alu.execute("TEST", 2**31, 0))
