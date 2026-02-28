def topological_sort_standard(elements, relation_matrix):
    size = len(elements)
    active = [True] * size
    result = []

    for _ in range(size):
        minimal_index = None

        for col in range(size):
            if not active[col]:
                continue

            is_minimal = True
            for row in range(size):
                if active[row] and relation_matrix[row][col]:
                    is_minimal = False
                    break

            if is_minimal:
                minimal_index = col
                break

        if minimal_index is None:
            raise ValueError()

        result.append(elements[minimal_index])
        active[minimal_index] = False

    return result


elements_example = [1, 2, 3, 4]
relation_matrix_example = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

print("Линейное расширение:", topological_sort_standard(elements_example, relation_matrix_example))