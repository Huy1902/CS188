from queue import Queue


class CSP:

    def __init__(self, variables, domains, constrains, goal_test, size, constraint_states):
        self.variables = variables
        self.domains = domains
        self.constraints = constrains
        self.count_assignment = 0
        self.size = size
        self.goal_test = goal_test
        self.constraint_states = constraint_states
        self.filtering()

    def solve(self):
        assignments = {}
        solution = self.backtracking(assignments)
        return solution

    def backtracking(self, assignments):
        if len(assignments) == len(self.variables):
            if self.goal_test(assignments, self.variables):
                # print(assignments, self.count_assignment)
                return assignments
            return None
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
        for i in range(self.size):
            for j in range(self.size):
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
                if (y, x) in self.constraint_states:
                    exist_y_satisfy_constraint = True
                    break
            if not exist_y_satisfy_constraint:
                self.domains[tail].remove(x)
                removed = True
        return removed


    # Optimization: Ordering: The Minimum Remaining Values
    def get_most_constrained_variable(self, assignments):
        unassigned_var = [var for var in self.variables if var not in assignments.keys()]
        if not unassigned_var:
            return None
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
            if constraint in assignments.keys() and (assignments[constraint], value) not in self.constraint_states:
                return False
        return True