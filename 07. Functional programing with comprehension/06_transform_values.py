def transform_values(func, dict):
    return {key: func(value) for key, value in dict.items()}


d = {"a": 1, "b": 2, "c": 3}
print(transform_values(lambda x: x * x, d))
