import itertools

with open("input.txt") as f:
    data = f.read().strip().split("\n")


def evaluate(equation, operators):
    result = int(equation[0])
    for i, op in enumerate(operators):
        if op == '+':
            result += int(equation[i + 1])
        elif op == '*':
            result *= int(equation[i + 1])
        elif op == '|':
            result = int(str(result) + equation[i + 1])
    return result

def solve(equations, part_two):
    total_sum = 0
    ops = "+*|" if part_two else "+*"

    for line in equations:
        test_value, equation = line.split(":")
        equation = equation.split()
        n = len(equation) - 1

        for p in itertools.product(ops, repeat=n):
            if  evaluate(equation, p) == int(test_value):
                total_sum += int(test_value)
                break
    return total_sum



print(f"Solve part one {solve(data, False)}")
#28730327770375

print(f"Solve part one {solve(data, True)}")
#28730327770375