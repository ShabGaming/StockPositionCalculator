import streamlit as st
import numpy as np


def calculate_additional_stock_short(short_price, initial_amount, current_price, leverage_multiplier):
    # Calculate the value of the short position
    short_position_value = round(initial_amount * leverage_multiplier, 2)

    # Calculate the additional quantity of stocks needed
    additional_quantity = round(short_position_value / current_price, 2)

    # Calculate the additional value needed
    additional_value_needed = additional_quantity * current_price

    return additional_quantity, additional_value_needed


def calculate_additional_stock_long(long_price, initial_amount, current_price, leverage_multiplier):
    # Calculate the value of the long position
    long_position_value = round(initial_amount * leverage_multiplier, 2)

    # Calculate the additional quantity of stocks needed
    additional_quantity = round(long_position_value / current_price, 2)

    # Calculate the additional value needed
    additional_value_needed = additional_quantity * current_price

    return additional_quantity, additional_value_needed

def main():

    st.title("Additional Stock Calculator 💵📊")

    tabs = st.radio("Select Position:", ("Short", "Long"))

    if tabs == "Short":
        short_price = st.number_input(
            "Short Price", value=0.0000, format="%.4f")
        initial_amount = st.number_input(
            "Initial Amount ($)", value=0.00, format="%.4f")
        leverage_multiplier = st.slider(
            "Leverage Multiplier", min_value=1, max_value=100, value=5)
        current_price = st.number_input(
            "Current Price", value=0.0000, format="%.4f")

        if st.button("Calculate - Short 📉"):
            additional_quantity, additional_value = calculate_additional_stock_short(
                short_price, initial_amount, current_price, leverage_multiplier)
            st.success(
                f"The additional quantity of stock to buy (Short) is approximately: {additional_quantity:.4f}")
            st.success(
                f"The amount to spend (Short) is approximately: ${additional_value:.2f}")

    elif tabs == "Long":
        long_price = st.number_input("Long Price", value=0.0000, format="%.4f")
        initial_amount = st.number_input(
            "Initial Amount ($)", value=0.00, format="%.4f")
        leverage_multiplier = st.slider(
            "Leverage Multiplier", min_value=1, max_value=100, value=5)
        current_price = st.number_input(
            "Current Price", value=0.0000, format="%.4f")

        if st.button("Calculate - Long 📈"):
            additional_quantity, additional_value = calculate_additional_stock_long(
                long_price, initial_amount, current_price, leverage_multiplier)
            st.success(
                f"The additional quantity of stock to buy (Long) is approximately: {additional_quantity:.4f}")
            st.success(
                f"The additional amount to spend (Long) is approximately: ${additional_value:.2f}")

    st.markdown("---")
    st.markdown("<p align='center' style='font-size: 18px;'>Made by Shahab with ❤️</p>",
                unsafe_allow_html=True)
    
    # Add a section for the basic calculator in the sidebar
    st.sidebar.title("Basic Calculator 🧮")

    # Add input fields for basic calculations
    number1 = st.sidebar.number_input("Enter number 1", value=0.0)
    number2 = st.sidebar.number_input("Enter number 2", value=0.0)

    # Add buttons for basic operations
    operation = st.sidebar.selectbox(
        "Select operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Calculate the result based on the selected operation
    if operation == "Add":
        result = number1 + number2
    elif operation == "Subtract":
        result = number1 - number2
    elif operation == "Multiply":
        result = number1 * number2
    elif operation == "Divide":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Cannot divide by zero"

    # Display the result
    st.sidebar.text(f"Result: {result}")

    
if __name__ == "__main__":
    main()
