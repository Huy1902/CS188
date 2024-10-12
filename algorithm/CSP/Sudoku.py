from os import remove
from queue import Queue

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 0, 0]
          ]


def print_sudoku(puzzle):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(puzzle[i][j], end=" ")
        print()


print_sudoku(puzzle)


class CSP:

    def __init__(self, variables, domains, constrains):
        self.variables = variables
        self.domains = domains
        self.constraints = constrains
        self.count_assignment = 0
        self.filtering()

    def solve(self):
        assignments = {}
        solution = self.backtracking(assignments)
        return solution

    def backtracking(self, assignments):
        if len(assignments) == len(self.variables):
            return assignments
        variable = self.get_most_constrained_variable(assignments)
        consistent_value = [value for value in self.domains[variable] if
                            self.is_consistent(variable, value, assignments)]

        while consistent_value:
            self.count_assignment += 1
            assignments[variable] = self.get_least_constraining_value(variable, consistent_value, assignments)
            next_assignments = self.backtracking(assignments)
            if next_assignments is not None:
                return next_assignments
            del consistent_value[consistent_value.index(assignments[variable])]
            del assignments[variable]

        # for value in consistent_value:
        #     self.count_assignment += 1
        #     assignments[variable] = value
        #     next_assignments = self.backtracking(assignments)
        #     if next_assignments is not None:
        #         return next_assignments
        #     del assignments[variable]
        return None

    # Optimization: Filtering: Forward checking & Arc consistency
    def filtering(self) -> None:
        queue = Queue()
        for i in range(9):
            for j in range(9):
                for constraint in self.constraints[(i, j)]:
                    queue.put((constraint, (i, j)))
        while not queue.empty():
            constraint = queue.get()
            head = constraint[0]
            tail = constraint[1]
            if self.remove_inconsistent_value(tail, head):
                for constraint in self.constraints[tail]:
                    queue.put((tail, constraint))


    def remove_inconsistent_value(self, tail, head):
        removed = False
        for x in self.domains[tail]:
            exist_y_satisfy_constraint = False
            for y in self.domains[head]:
                if y != x:
                    exist_y_satisfy_constraint = True
                    break
            if not exist_y_satisfy_constraint:
                self.domains[tail].remove(x)
                removed = True
        return removed


    # Optimization: Ordering: The Minimum Remaining Values
    def get_most_constrained_variable(self, assignments):
        unassigned_var = [var for var in self.variables if var not in assignments.keys()]
        return min(unassigned_var, key=lambda var: len(self.domains[var]))


    def count_constrain_of_value(self, remaining_var, value):
        count = 0
        for var in remaining_var:
            if value in self.domains[var]:
                count += 1
        return count

    # Optimization: Ordering: The Least Constraining Value
    def get_least_constraining_value(self, variable, domain, assignments):
        remaining_var = [var for var in self.constraints[variable] if var not in assignments.keys()]
        return min(domain, key=lambda value: self.count_constrain_of_value(remaining_var, value))


    def is_consistent(self, variable, value, assignments: dict):
        for constraint in self.constraints[variable]:
            if constraint in assignments.keys() and assignments[constraint] == value:
                return False
        return True


# Add constrain to var, with sudoku constrains consist of:
# column constraint, row constraint, subgrid constraint
def add_constrain(var: tuple, constraints: dict):
    constraints[var] = []
    # column constraint
    for i in range(9):
        if i != var[0]:
            constraints[var].append((i, var[1]))

    # row constraint
    for j in range(9):
        if j != var[1]:
            constraints[var].append((var[0], j))

    # subgrid constraint
    for i in range(var[0] // 3 * 3, var[0] // 3 * 3 + 3):
        for j in range(var[1] // 3 * 3, var[1] // 3 * 3 + 3):
            if i != var[0] or j != var[1]:
                constraints[var].append((i, j))
    return constraints


variables = [(i, j) for i in range(9) for j in range(9)]

domains = {var: list(range(1, 10)) if puzzle[var[0]][var[1]] == 0
else [puzzle[var[0]][var[1]]] for var in variables}

constraints = {}
for i in range(9):
    for j in range(9):
        constraints = add_constrain((i, j), constraints)

CSP_problem = CSP(variables, domains, constraints)
solution = CSP_problem.solve()
puzzle_solution = [[0 for j in range(9)] for i in range(9)]
for i in range(9):
    for j in range(9):
        puzzle_solution[i][j] = solution[(i, j)]
print(CSP_problem.count_assignment)
print_sudoku(puzzle_solution)
