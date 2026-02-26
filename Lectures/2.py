def boolean_matrix_disjunction(first_matrix, second_matrix):
    row_count = len(first_matrix)
    column_count = len(first_matrix[0])
    return [
        [
            int(first_matrix[row_index][column_index] or second_matrix[row_index][column_index])
            for column_index in range(column_count)
        ]
        for row_index in range(row_count)
    ]


def boolean_matrix_transpose(source_matrix):
    row_count = len(source_matrix)
    column_count = len(source_matrix[0])
    return [
        [
            source_matrix[row_index][column_index]
            for row_index in range(row_count)
        ]
        for column_index in range(column_count)
    ]


def boolean_matrix_inversion(source_matrix):
    row_count = len(source_matrix)
    column_count = len(source_matrix[0])
    return [
        [
            1 - source_matrix[row_index][column_index]
            for column_index in range(column_count)
        ]
        for row_index in range(row_count)
    ]


def boolean_matrix_subtraction(first_matrix, second_matrix):
    row_count = len(first_matrix)
    column_count = len(first_matrix[0])
    return [
        [
            int(first_matrix[row_index][column_index] and (1 - second_matrix[row_index][column_index]))
            for column_index in range(column_count)
        ]
        for row_index in range(row_count)
    ]


def boolean_matrix_multiplication(first_matrix, second_matrix):
    row_count = len(first_matrix)
    column_count = len(second_matrix[0])
    common_dimension = len(second_matrix)

    result_matrix = [
        [0 for _ in range(column_count)]
        for _ in range(row_count)
    ]

    for row_index in range(row_count):
        for column_index in range(column_count):
            for common_index in range(common_dimension):
                result_matrix[row_index][column_index] = int(
                    result_matrix[row_index][column_index]
                    or (
                        first_matrix[row_index][common_index]
                        and second_matrix[common_index][column_index]
                    )
                )

    return result_matrix


first_matrix_example = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 0]
]

second_matrix_example = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
]

print(boolean_matrix_disjunction(first_matrix_example, second_matrix_example))
print(boolean_matrix_transpose(first_matrix_example))
print(boolean_matrix_inversion(first_matrix_example))
print(boolean_matrix_subtraction(first_matrix_example, second_matrix_example))
print(boolean_matrix_multiplication(first_matrix_example, second_matrix_example))
