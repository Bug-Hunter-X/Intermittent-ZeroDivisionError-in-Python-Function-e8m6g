def function_with_error_handling(x):
    try:
        if x == 0:
            return float('inf')  # Return positive infinity to represent division by zero
        else:
            return x + 1
    except Exception as e:
        return f"An error occurred: {e}"

# Example calls demonstrating that the error is gracefully handled
print(function_with_error_handling(1))
print(function_with_error_handling(0))
print(function_with_error_handling(-1))