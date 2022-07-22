import itertools
from copy import copy
from typing import Tuple, Union, List


def get_pattern(sequence):
    sequence = sequence.replace('0', ' ')
    sequence = sequence.split()
    sequence_pattern = list(map(lambda x: len(x), sequence))
    return sequence_pattern


class Table:
    def __init__(self, size, table=None):
        self.size = size
        if table is None:
            self.one_row = '0' * size
            self.table = [self.one_row for _ in range(self.size)]
        else:
            self.table = table

    def clear_row(self, row_index):
        # for row in range(row_index, self.size):
        self.table[row_index] = self.one_row

    def set_row(self, row_index, new_row):
        self.table[row_index] = new_row

    def get_row_pattern(self, row_index: int) -> List[int]:
        this_row = self.table[row_index]
        return get_pattern(this_row)

    def get_column_pattern(self, column_index: int) -> List[int]:
        this_column = [row[column_index] for row in self.table]
        this_column = ''.join(this_column)
        return get_pattern(this_column)

    def __str__(self):
        result = ''
        for row in self.table:
            result += row
            result += '\n'
        return result


class Nonogram:
    def __init__(self, size, rows_description, columns_description):
        self.size = size
        self.rows_description = rows_description
        self.columns_description = columns_description
        self.solved = False
        self.table = Table(self.size)
        self.begin_solve()

    def convert_combination_to_row(self, combination: Union[Tuple[int], List[int]]):
        new_row = ['1' if i in combination else '0' for i in range(self.size)]
        return ''.join(new_row)

    def begin_solve(self):
        processed_row = 0
        self.solve(processed_row)

    def solve(self, processed_row):
        if processed_row < self.size:
            condition = self.rows_description[processed_row]
            black_square_amount = sum(condition)
            all_combinations = itertools.combinations(range(self.size), black_square_amount)
            for combination in all_combinations:
                if self.is_row_promising(processed_row, combination) and self.is_columns_promising(processed_row, combination):
                    self.table.clear_row(processed_row)
                    new_row = self.convert_combination_to_row(combination)
                    self.table.set_row(processed_row, new_row)
                    self.solve(processed_row + 1)
                    if self.is_solved():
                        self.solved = True
                        return
            self.table.clear_row(processed_row)

    def is_solved(self):
        for index in range(self.size):
            row_pattern = self.table.get_row_pattern(index)
            column_pattern = self.table.get_column_pattern(index)
            row_description = self.rows_description[index]
            column_description = self.columns_description[index]
            if any([row_description != row_pattern, column_description != column_pattern]):
                return False
        return True

    def is_row_promising(self, processed_row, combination):
        description = self.rows_description[processed_row]
        new_row = self.convert_combination_to_row(combination)
        new_row = new_row.replace('0', ' ')
        new_row = new_row.split()
        if len(new_row) != len(description):
            return False
        this_row_list = list(map(lambda x: len(x), new_row))
        if this_row_list != description:
            return False
        return True

    def is_columns_promising(self, processed_row, combination):
        current_table = copy(self.table.table)
        new_table = Table(self.size, current_table)
        new_row = self.convert_combination_to_row(combination)
        new_table.set_row(processed_row, new_row)
        for column_index in range(self.size):
            this_column_pattern = new_table.get_column_pattern(column_index)
            if len(this_column_pattern) > len(self.columns_description[column_index]):
                return False
            for i in range(len(this_column_pattern)):
                item1 = this_column_pattern[i]
                item2 = self.columns_description[column_index][i]
                if column_index in combination:
                    if item1 > item2:
                        return False
                else:
                    if item1 != item2:
                        return False
        return True


if __name__ == '__main__':
    size = 10
    rows_description = [
        [1, 4, 2],
        [3, 5],
        [1, 1, 1, 2],
        [4, 1, 1],
        [1, 6],
        [2, 1, 1],
        [3, 2, 1],
        [1, 2, 1, 3],
        [1, 1, 1],
        [4, 2],
    ]
    columns_description = [
        [4, 2],
        [1, 4],
        [4, 5],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [2, 4, 1],
        [1, 2, 1, 1],
        [1, 1, 1, 1],
        [6, 1, 1],
        [3, 1, 3],
    ]

    nonogram = Nonogram(size=size, columns_description=columns_description, rows_description=rows_description)
    print(nonogram.table)
