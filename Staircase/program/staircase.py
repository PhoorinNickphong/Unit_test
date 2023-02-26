def staircase(n):
    result = ""
    for i in range(1, n + 1):
        result += f'{"#"*i:>{n}}\n'

    return result.rstrip()