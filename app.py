import streamlit as st
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset using st.cache_data
@st.cache_data  # Use st.cache_resource if the data is from a remote resource
def load_data(filename):
    return pd.read_csv(filename)

# Main function to run the app
def main():
    st.title('Home Price Prediction App')

    # Load the dataset
    df = load_data('homeprices.csv')

    # Display the dataset
    st.subheader('Dataset')
    st.write(df)

    # Scatter plot with best-fit line and predicted point
    st.subheader('Scatter plot of Area vs Price with Best-Fit Line and Predicted Point')
    fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure and axis

    # Scatter plot of existing data points
    ax.scatter(df['area'], df['price'], color='red', marker='+', label='Existing Data')

    # Drop the 'price' column to prepare for training
    new_df = df.drop('price', axis='columns')

    # Create linear regression object
    reg = linear_model.LinearRegression()
    reg.fit(new_df, df['price'])

    # Prediction input and output
    area_input = st.number_input('Enter the area (in sq ft)', min_value=0.0, format="%.2f")
    predicted_price = reg.predict([[area_input]])

    # Scatter plot of predicted point
    ax.scatter(area_input, predicted_price, color='blue', marker='o', label='Predicted Point')
    
    # Plot the best-fit line
    x_values = np.array([df['area'].min(), area_input, df['area'].max()])
    y_values = reg.predict(x_values.reshape(-1, 1))
    ax.plot(x_values, y_values, color='green', linestyle='-', linewidth=2, label='Best-Fit Line')

    # Plot settings
    ax.set_xlabel('Area')
    ax.set_ylabel('Price')
    ax.legend()
    st.pyplot(fig)  # Display the plot using st.pyplot()

    # Display the predicted price and equation of the line
    st.subheader('Prediction Details')
    st.write(f'For an area of {area_input} sq ft:')
    st.write(f'- Predicted Price: ${predicted_price[0]:,.2f}')
    st.write(f'- Equation of the Line: y = {reg.coef_[0]:.2f} * x + {reg.intercept_:.2f}')

if __name__ == '__main__':
    main()
