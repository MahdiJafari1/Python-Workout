def before_after_dot(float, before, after):
    """Accepts a float, and two integers.

    Returns a float containing before digits preceding the dcimal point,
    and after digits following the decimal point.
    """

    s = str(float)
    i = s.index(".")
    print(f"i : {i}")

    print(f"i : {s[i - before : i + after + 1]}")
    print(f"i : {s[i - before : i + after + 1]}")
    return s[i - before : i + after + 1]


before_after_dot(1234.5678, 2, 3)
