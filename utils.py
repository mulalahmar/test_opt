# Define objective function
# Define objective function
def objective_function(x, sign=-1.0):
    return sign * np.dot(objective_param, x)

# Define linear constraints
def constraint1(x, sign=-1.0):
    return sign * (np.dot(lhs_param[0],x) - rhs_bounds[0])

def constraint2(x, sign=-1.0):
    return sign * (np.dot(lhs_param[1],x) - rhs_bounds[1])

def generate_constraints(constraint1, constraint2):
    con1 = {'type': 'ineq', 'fun': constraint1}
    con2 = {'type': 'ineq', 'fun': constraint2}
    cons = [con1, con2]
    return cons

# Define decision variables bounds
def generate_var_bounds(var_bounds):
    bounds = Bounds(var_bounds[0], var_bounds[1])
    return bounds

# Initial guess for the decision variables
def initial_var_values(n_products):
    x0 = [0 for x in range(n_products)]
    return x0

# Solve the optimization problem
def optimize_problem(objective_function, x0, bounds, cons):
  res = minimize(objective_function,
                x0, 
                method='SLSQP',
                constraints=cons,#[linear_constraint],
                #options={'verbose': 1},
                bounds=bounds
                )
  return res