import streamlit as st

import openai import OpenAI
from prompts import parsing_prompt
import json
import os

from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint
from scipy.optimize import NonlinearConstraint
from scipy.optimize import BFGS
from scipy.optimize import milp

import pandas as pd
import numpy as np

from prompts import (
    parsing_prompt
)

from utils import (
    objective_function,
    constraint1,
    constraint2,
    generate_constraints,
    generate_var_bounds,
    initial_var_values,
    optimize_problem
)

import data

import numpy as np
from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint
from scipy.optimize import NonlinearConstraint
from scipy.optimize import BFGS
from scipy.optimize import milp

openai.api_key = os.getenv("OPENAI_API_KEY")

# Show title and description.
st.title(":teapot: Teapot.. ")
st.title("Solving Your Most Complex Optimization Problems")
st.write(
    "This is your Optimization Assistant, a chatbot that uses Artificial Intelligence to understand, model and solve optimization problems. This particular example solves for a simple inear program End-to-End. "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
    "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key", type="password")

# Define decision variables bounds
bounds = generate_var_bounds(data.var_bounds)

# Define constraint
cons = generate_constraints(constraint1, constraint2)

# Initial guess for the decision variables
x0 = initial_var_values(data.n_products)

# Optimize problem
res = optimize_problem(objective_function, x0, bounds, cons)

# Print the results
st.write("Optimal solution:", res.x)
st.write("Optimal value:", data.status_dict[str(res.status)])
st.write("Optimal value:", round(-res.fun,2))

'''
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("How can I help you?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
'''