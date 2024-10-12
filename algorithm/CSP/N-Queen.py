from algorithm.CSP.CSP import CSP


def generate_board(n):
    return [[0] * n for _ in range(n)]

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()

def add_constraint(variable) :
    constraints[variable] = []

    # col constraint
    for i in range(n) :
        if i != variable[0] :
            constraints[variable].append((i, variable[1]))

    # row constraint
    for j in range(n):
        if j != variable[1] :
            constraints[variable].append((variable[0], j))

    # Primary/Major Diagonal constraint
    for i in range(1, n) :
        if variable[0] - i >= 0 and variable[1] - i >= 0 :
            constraints[variable].append((variable[0] - i, variable[1] - i))
        if variable[0] + i < n and variable[1] + i < n :
            constraints[variable].append((variable[0] + i, variable[1] + i))

    # Second/Minor Diagonal constraint
    for i in range(1, n):
        if variable[0] - i >= 0 and variable[1] + i < n :
            constraints[variable].append((variable[0] - i, variable[1] + i))
        if variable[0] + i < n and variable[1] - i >= 0 :
            constraints[variable].append((variable[0] + i, variable[1] - i))


def goal_test(assignments: dict, variables):
    # print(list(assignments.values()).count(1))
    return list(assignments.values()).count(1) == n

# constraint states
constraint_states = {(1, 0), (0, 1), (0, 0)}

n = 12  # Define the size of the board
variables = [(i, j) for i in range(n) for j in range(n)]

domains = {var: [1, 0] for var in variables}

constraints = {}
for i in range(n):
    for j in range(n):
        add_constraint((i, j))
board = generate_board(n)
print_board(board)
CSP_problem = CSP(variables, domains, constraints, goal_test, n, constraint_states)
solution = CSP_problem.solve()
print(CSP_problem.count_assignment)
print_board(
    [[solution[(i, j)] for j in range(n)] for i in range(n)]
)
