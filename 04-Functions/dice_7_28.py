def f(dice):
    best = ""
    current = ""

    for d in dice:
        if d == current[:1]:
            current += d
        else:
            current = d

        if len(current) > len(best):
            best = current

    return int(best[0])