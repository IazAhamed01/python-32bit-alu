32-Bit Arithmetic Logic Unit (ALU) Simulator using Python
Project Overview

This project implements a 32-bit Arithmetic Logic Unit (ALU) using Python.
The ALU simulates core processor-level operations such as arithmetic, logical, and shift operations, along with the generation of status flags similar to those found in real CPUs.
The project is designed to bridge the gap between computer architecture theory and software-based simulation.

**Objectives**
To design and simulate the working of a 32-bit ALU
To implement arithmetic, logical, and shift operations using opcode-based control
To understand bit-level computation and two’s complement arithmetic
To generate processor-style status flags
To develop a menu-driven ALU simulator for demonstration and learning

**Features**
Supports 32-bit signed integer operations

**Arithmetic operations:**
Addition (ADD)
Subtraction (SUB)

**Logical operations:**
AND
OR
XOR

**Shift operations:**
Shift Left (SHL)
Shift Right (SHR)

**Status flags:**
Zero (Z)
Sign (S)
Carry (C)
Overflow (V)
Menu-driven interface for user interaction
Modular and well-organized code structure

**Working of the ALU**

The user selects an operation using a numeric menu.
Two operands (A and B) are provided as input.
An opcode corresponding to the selected operation is generated.
The ALU executes the operation based on the opcode.
The result is masked to 32 bits to simulate real hardware behavior.
Status flags are generated based on the result.
The final output and flags are displayed to the user.

32-Bit Data Handling
Python integers are not limited to a fixed size.

**To simulate a 32-bit processor:**

All results are masked using 0xFFFFFFFF.
This ensures overflow and wrap-around behavior similar to real hardware.
Signed values are interpreted using two’s complement representation, allowing correct handling of negative numbers.

**Status Flags**

Zero Flag (Z)
Set when the result of an operation is zero.

Sign Flag (S)
Set when the most significant bit of the result is one, indicating a negative value.

Carry Flag (C)
Set when a carry occurs during arithmetic or shift operations.

Overflow Flag (V)
Set when signed arithmetic overflow occurs.

**How to Run the Project**

Ensure Python 3 is installed on the system.
Navigate to the project directory.
Run the following command:
python main.py
Follow the on-screen menu to select operations and enter operands.
The result and corresponding status flags will be displayed.

**Testing**

Separate test scripts were created to validate:
Arithmetic operations
Logical operations
Shift operations
Overflow behavior
Status flag generation
Testing ensured correct and consistent ALU behavior under normal and edge-case conditions.

**Learning Outcomes**
Gained a clear understanding of ALU functionality within a CPU
Learned practical bit masking and bitwise manipulation
Understood the difference between signed and unsigned arithmetic
Improved modular programming and debugging skill.
Developed insight into opcode-based execution and control logic

**Future Enhancements**
Addition of multiplication and division operations
Support for floating-point arithmetic
Graphical user interface for visualization
Simulation of pipelined ALU architecture
Conclusion

This project successfully simulates a 32-bit Arithmetic Logic Unit using Python while maintaining hardware-like behavior.
It provides practical insight into processor-level computation and demonstrates how low-level architectural concepts can be modeled using high-level programming.
