"""
This module will create a linear regression using scikit learn
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt


class Regression():

    def __init__(self):

        self._model = None
        self._pred_line = None
        self._y_name = None
        self._x_name = None
        self._independent_value = None
        self._target_value = None

    def make_model(self, data: pd.DataFrame, input_col: str, output_col: str):
        """
        This function creates a linear regression model.

        Parameters:
            data (pandas DataFrame): data used for the regression.
            input-col (str): feature variable.
            output_col (str): target variable.
        """

        # set the variable names for our model
        self._x_name = input_col
        self._y_name = output_col

        # set the target and feature values
        self._independent_value = data[[input_col]]
        self._target_value = data[output_col]

        # create and fit the model
        r_model = LinearRegression()
        r_model.fit(self._independent_value, self._target_value)
        y_pred = r_model.predict(X=self._independent_value)

        # asign the model to the class variables
        self._model = r_model
        self._pred_line = y_pred

    def get_regression_line(self):
        """
        This function returns the regression line definition as a string.

        Returns:
            model_line (str): string containing the regression model line
        """
        slope = self._model.coef_[0]
        intercept = self._model.intercept_

        model_line = f'{self._y_name} = {slope:.2f} * {self._x_name} + {intercept:.2f}'

        return model_line

    def get_r_squared(self):
        """
        This funciton returns the R² measure of our regression model.

        Returns:
            r_squared
        """
        r2 = r2_score(self._target_value, self._pred_line)
        return r2

    def get_MSE(self):
        """
        This funciton returns the mean squared error (MSE) measure of our regression model.

        Returns:
            MSE
        """
        MSE = mean_squared_error(self._target_value, self._pred_line)
        return MSE

    def get_plot(self):

        """
        This function creates a graph for the linear regression it has made.
        """

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(self._independent_value, self._target_value, color='blue', label='Actual Data')
        ax.plot(self._independent_value, self._pred_line, color='red', label='Regression Line')
        
        # Display formula, R^2, and MSE on the plot
        formula_text = self.get_regression_line()
        r2 = self.get_r_squared()
        mse = self.get_MSE()

        ax.text(0.05, 0.95, f"Prediction Formula: {formula_text}", transform=ax.transAxes, fontsize=12, verticalalignment='top')
        ax.text(0.05, 0.90, f"R^2: {r2:.2f}", transform=ax.transAxes, fontsize=12, verticalalignment='top')
        ax.text(0.05, 0.85, f"MSE: {mse:.2f}", transform=ax.transAxes, fontsize=12, verticalalignment='top')
        
        # Labels and title
        ax.set_xlabel(self._x_name)
        ax.set_ylabel(self._y_name)
        ax.set_title("Linear Regression Plot")
        ax.legend()
        ax.grid(True)
        
        return fig  # Return the figure object
    