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

    def solve(self):
        assignments = {}
        solution = self.backtracking(assignments)
        return solution

    def backtracking(self, assignments):
        if len(assignments) == len(self.variables):
            return assignments
        variable = self.get_most_constrained_variable(assignments)
        for value in self.domains[variable]:
            if self.is_consistent(variable, value, assignments):
                self.count_assignment += 1
                assignments[variable] = value
                next_assignments = self.backtracking(assignments)
                if next_assignments is not None:
                    return next_assignments
                del assignments[variable]
        return None

    def get_most_constrained_variable(self, assignments):
        unassigned_var = [var for var in self.variables if var not in assignments.keys()]
        return min(unassigned_var, key=lambda var: len(self.domains[var]))

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

domains = {var: set(range(1, 10)) if puzzle[var[0]][var[1]] == 0
else {puzzle[var[0]][var[1]]} for var in variables}

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
print_sudoku(puzzle_solution)
print(CSP_problem.count_assignment)
