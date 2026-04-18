def long_messy_function(data):
    x = 0
    y = 1
    z = 2
    result = []
    for item in data:
        if item is None:
            if y > 0:
                if z > 1:
                    result.append("missing")
                else:
                    result.append("unknown")
            else:
                result.append("none")
        else:
            if isinstance(item, int):
                if item % 2 == 0:
                    result.append(item * x)
                else:
                    result.append(item + y)
            elif isinstance(item, str):
                if item.strip() == "":
                    result.append("empty")
                else:
                    result.append(item.upper())
            else:
                result.append(item)
        x += 1
        y += 2
        z += 3
    total = 0
    for value in result:
        if isinstance(value, int):
            total += value
    return total


def helper(values):
    a = 0
    for v in values:
        a += 1
    return a
