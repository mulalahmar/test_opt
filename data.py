import numpy as np

# Problem description
'''
Max z = 40.x1 + 30.x2  
  st.	2.x1 + 1.x2 <= 100 
      1.x1 + 2.x2 <= 80 
      x1, x2 are positive integers 
'''

# Problem parameters
n_products = 2
n_resources = 2

# Define coeffcients of ojecive function
objective_param = [40, 30]

# define lhs for constraints
lhs_param = [
    [2, 1], # 2.x1 + 1.x2
    [1, 2]  # 1.x1 + 2.x2
]

# Define rhs for constrainst
rhs_bounds = [100,  # ... <= 100
              80]   # ... <= 80

# Define lower and upper bounds for decision variables
var_bounds = [
    [0, 0],
    [np.inf, np.inf]
]

# Define dictionary to store the status
status_dict = {
    '0': 'Optimal solution found.',
    '1': 'Iteration or time limit reached.',
    '2': 'Problem is infeasible.',
    '3': 'Problem is unbounded.',
    '4': 'Other; see message for details.'
}