from collections import defaultdict
import re


def operation_order():
    with open("data/20201218.txt") as f:
        lines = f.readlines()
    expressions = [line.strip().replace("(", "( ").replace(")", " )") for line in lines]
    res = 0
    for expression in expressions:
        res += _evaluate_expression(expression)
    print(f"The sum is: {res}")

    # Part 2
    res = 0
    for expression in expressions:
        res += _evaluate_expression(expression, True)
    print(f"The sum is: {res}")


def _evaluate_expression(expression: str, star_2=False) -> int:
    if star_2:
        tmp = expression.split()
        plus_at = re.finditer("\+", "".join(tmp))
        plus_at = [p.start() for p in plus_at]
        for p in plus_at:
            tmp[p - 1] = "( " + tmp[p - 1]
            tmp[p + 1] = tmp[p + 1] + " )"
        expression = " ".join(tmp)
        expression = expression.replace("( )", "")
        return eval(expression)
    while "(" in expression:
        p_at = _find_parenthesis(expression)
        sorted_levels = sorted(p_at, reverse=True)
        at = p_at[sorted_levels[0]][0]
        part = expression[at[0] + 1 : at[1]]
        res = _evaluate(part)
        expression = expression[: at[0]] + res + expression[at[1] + 1 :]
    return int(_evaluate(expression))


def _evaluate(expression: str):
    expression = expression.split()
    res = 0
    operator = "+"
    for ch in expression:
        if ch.isdigit():
            if operator == "+":
                res += int(ch)
            elif operator == "*":
                res *= int(ch)
            else:
                raise Exception("Invalid operator")
        else:
            operator = ch
    return str(res)


def _find_parenthesis(expression):
    start_idx = []
    p_at = defaultdict(list)  # "Level" as keys, lists of index tuples as values
    for i, c in enumerate(expression):
        if c == "(":
            start_idx.append(i)
        if c == ")":
            try:
                l = len(start_idx)
                p_at[l].append((start_idx.pop(), i))
            except IndexError:
                print("Unmatched")
    return p_at


if __name__ == "__main__":
    operation_order()
