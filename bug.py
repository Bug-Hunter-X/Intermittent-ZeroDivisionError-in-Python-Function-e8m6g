def function_with_uncommon_error(x):
    if x == 0:
        return 1 / x  # ZeroDivisionError
    else:
        return x + 1

# Example call demonstrating that the error is not always triggered
print(function_with_uncommon_error(1))

# Example call demonstrating the ZeroDivisionError
print(function_with_uncommon_error(0))