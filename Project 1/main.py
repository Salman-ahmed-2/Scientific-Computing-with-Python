def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top = []
    bottom = []
    lines = []
    results = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Each problem must contain two operands and one operator."

        first, operator, second = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first), len(second)) + 2
        top.append(first.rjust(width))
        bottom.append(operator + second.rjust(width - 1))
        lines.append('-' * width)

        if show_answers:
            result = str(eval(first + operator + second))
            results.append(result.rjust(width))

    arranged_problems = "    ".join(top) + "\n" + "    ".join(bottom) + "\n" + "    ".join(lines)

    if show_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])