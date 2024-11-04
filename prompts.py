
description = """
Problem: A manufacturing company produces two products: Product A and Product B. Each product requires specific amounts of two resources, Resource 1 and Resource 2, both of which have limited availability. The company aims to determine the optimal production quantities of each product to maximize total profit, while adhering to the resource constraints. Here are more details:

Product A:

Profit per unit: $40
Resource 1 required per unit: 2 units
Resource 2 required per unit: 1 unit
Product B:

Profit per unit: $30
Resource 1 required per unit: 1 unit
Resource 2 required per unit: 2 units
Resource Availability:

Resource 1: 100 units
Resource 2: 80 units
The objective is to determine the number of units of Product A and Product B to produce in order to maximize profit, without exceeding the available amounts of Resource 1 and Resource 2.
"""

prompt = f"""
    Convert the following optimization problem statement into a mathematical linear program:

    {description}

    Represent the linear program using the following format:

    **Decision Variables:** [List of decision variables with descriptions]

    **Objective Function:** [Mathematical expression of the objective function]

    **Constraints:** [List of constraints as mathematical inequalities]

    **Non-negativity Constraints:** [List of non-negativity constraints on the variables]
    """

parsing_prompt = (
    f"You are an optimization expert with a focus on mathematical and operational problems. Your task is to exract coefficients from a structured standard form of a linear program and store their values in JSON format. Make sure to name the parameters as instructed."
    f"Return all the parameters in a JSON format. Do not add the word 'json' to the data output.\n"
    f"Extract the decision variable coefficients from the objective function of following linear program {agent_response}."
    f'{{"obj_coeff_1": "example", "obj_coeff_2": "example",.. , "obj_coeff_n": "example"}}'
    f"Extract the lower bound of the decision variables."
    f'{{"lb_coeff_1": "example", "lb_coeff_2": "example",.. , "lb_coeff_n": "example"}}'
    f"Extract the upper bound of the decision variables."
    f'{{"ub_coeff_1": "example", "ub_coeff_2": "example",.. , "ub_coeff_n": "example"}}'
    f"If the upper bound on the decision variable is not stated, assume it unbounded and return 'inf'"
    f"Make sure to extract as many coefficients as the number of decision variables. If there is no coefficient for the decision variable, assign it a zero value. \n"
)

parsing_prompt = (
    f"You are an optimization expert with a focus on mathematical and operational problems. Your task is to exract coefficients from a structured standard form of a linear program and store their values in JSON format. Make sure to name the parameters as instructed."
    f"Return all the parameters in a JSON format. Do not add the word 'json' to the data output.\n"
    f"Extract the coefficients from the constraints of following linear program {agent_response}."
    f"Extract the coefficients of the first constraints and return it as follows:"
    f'{{"const_1_lhs_1": "example", "const_1_lhs_2": "example",.. , "const_1_lhs_n": "example"}}'
    f"Extract the right hand side bound of the first constraint and return it as follows:"
    f'{{"const_1_rhs": "example"}}'
    f"Extract the coefficients of the second constraints and return it as follows:"
    f'{{"const_2_lhs_1": "example", "const_2_lhs_2": "example",.. , "const_2_lhs_n": "example"}}'
    f"Extract the right hand side bound of the first constraint and return it as follows:"
    f'{{"const_2_rhs": "example"}}'
    f"Extract the coefficients of all other constraints following the same pattern."
    f"For each constraint, make sure to extract as many coefficients as the number of decision variables. If there is no coefficient for the decision variable, assign it a zero value. \n"
)