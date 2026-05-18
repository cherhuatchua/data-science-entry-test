def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """

    # Check if lst is a list
    If not isinstance(lst, list):
        return -1

    # Replace matching values
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

numbers = [1, 2, 3, 4, 2, 2, 2, 5]
result1 = find_and_replace(numbers, 2, 9)
print(result1)

fruits = ["apple", "banana", "apple", "apple", "orange"]
result2 = find_and_replace(fruits, "apple", "durian")
print(result2)

# Expected output
[1, 9, 3, 4, 9, 9, 9, 5]
['durian', 'banana', 'durian', 'durian', 'orange']