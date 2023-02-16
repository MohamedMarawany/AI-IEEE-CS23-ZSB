def examples():
    """
    Creates User_manual Text Document which guides the user to entering the correct data format in equations.txt
    """

    # Create a mapping table to translate numbers to subscripts
    subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    # Ask and Store number of equations
    while True:
        num_of_equation = int(input("Number of equations: ").strip())
        if num_of_equation <= 9:
            break
        else:
            print("Please enter a value less than 9")

    # Write several guidance statements for the user
    with open(__file__.replace("getting_info.py", "user_manual.txt"), "w", encoding='utf-8') as file:
        file.write("This file is your catalogue to use this program.\n\n\n")
        file.write("First, Store your equations in a text file named 'equations.txt'.\n")
        file.write(f"If you have {num_of_equation} equations, Your text file should be like this:\n")
        file.write(f"Number of equations: {num_of_equation}\n")

        # Write different equations with specific subscripts by translating using mapping table
        for i in range(num_of_equation):
            file.write(f"eq{i + 1}: ".translate(subscript))
            for j in range(num_of_equation):
                file.write(f"a{i + 1}{j + 1}x{j + 1} ".translate(subscript))
                if j == num_of_equation - 1:
                    file.write(f"= a{i + 1}{0}".translate(subscript))
                else:
                    file.write("+ ")
            file.write("\n")

    # Print for the user the user_manual.txt path
    print(__file__.replace("getting_info.py", "user_manual.txt"))


def getting_equations():
    try:
        """
        Returns an augmented matrix ready for Gauss Elimination
        """

        x = 0  # Sign Controller
        main_lst = []  # Returned Nested List that act as an augmented matrix
        solution_lst = []
        f = open('equations.txt', encoding='utf-8')  # File being read
        temp = int(f.readline().strip('\n')[-1])  # Read number of equations

        for line in f:

            lst = []
            # Prepare temporary list to hold rows of augmented matrix
            for i in range(temp + 1):
                lst.append(0)

            key = line.strip('\n').split()

            # 1st Item
            # Necessary Check in case of shuffled equations
            for i in range(temp):
                if key[1][-1] == chr(8321 + i):
                    lst[i] = (int(key[1].strip('x' + chr(8321 + i))))

            # Rest of items
            # Used to modify parameters sign
            for i in range(2, len(key) - 2):
                if key[i - 1] == '-':
                    x = -1
                elif key[i - 1] == '+':
                    x = 1
                for j in range(temp):
                    if key[i][-1] == chr(8321 + j):
                        lst[j] = (x * int(key[i].strip('x' + chr(8321 + j))))

            # Extra Last Column
            lst[-1] = int(key[-1])
            main_lst.append(lst)
        f.close()
        for i in main_lst:
            solution_lst.append(i.pop(len(i) - 1))
        return main_lst, solution_lst

    except FileNotFoundError:
        print("File Not Found")
    except (ValueError, IndexError):
        print("You have probably entered the text document equations wrong")
