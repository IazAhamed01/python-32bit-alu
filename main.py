from src.alu import ALU

def main():
    alu = ALU()

    while True:
        print("\n====== 32-BIT ALU SIMULATOR ======")
        print("1 - ADD")
        print("2 - SUB")
        print("3 - AND")
        print("4 - OR")
        print("5 - XOR")
        print("6 - SHL")
        print("7 - SHR")
        print("0 - EXIT")

        choice = input("Enter choice (number only): ").strip()

        if choice == "0":
            print("Exiting...")
            break

        opcode_map = {
            "1": "ADD",
            "2": "SUB",
            "3": "AND",
            "4": "OR",
            "5": "XOR",
            "6": "SHL",
            "7": "SHR"
        }

        if choice not in opcode_map:
            print("Invalid choice. Try again.")
            continue

        try:
            a = int(input("Enter operand A: "))
            b = int(input("Enter operand B: "))
        except ValueError:
            print("Operands must be integers.")
            continue

        result, flags = alu.execute(opcode_map[choice], a, b)

        print("\nResult:", result)
        print("Flags :", flags)

if __name__ == "__main__":
    main()
