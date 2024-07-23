def calculate_structure_sum(data_structure):
    total_sum = 0

    def traverse_structure(element):
        nonlocal total_sum

        if isinstance(element, (int, float)):
            total_sum += element
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, (list, tuple, set)):
            for item in element:
                traverse_structure(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                traverse_structure(key)
                traverse_structure(value)

    for item in data_structure:
        traverse_structure(item)

    return total_sum


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
