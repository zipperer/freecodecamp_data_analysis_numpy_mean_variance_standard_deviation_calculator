import numpy as np

def perform_calculation_for_matrix(calculation_function, matrix):
  axis_for_columns = 0
  axis_for_rows = 1
  values_for_columns = calculation_function(matrix, axis=axis_for_columns).tolist()
  values_for_rows = calculation_function(matrix, axis=axis_for_rows).tolist()
  # https://numpy.org/doc/1.26/reference/generated/numpy.mean.html#numpy.mean
  # "The average is taken over the flattened array by default"
  # I take it as given that each of these functions performs the calculation on the flattened matrix when the function receives no argument for paramenter `axis`. 
  # If needed, could first apply https://numpy.org/doc/1.26/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten
  value_for_flattened_matrix = calculation_function(matrix)
  return values_for_columns, values_for_rows, value_for_flattened_matrix

def calculate(list):
  if (len(list) != 9):
    raise ValueError("List must contain nine numbers.")
  
  # use list to make numpy array
  # https://numpy.org/doc/1.26/reference/generated/numpy.array.html#numpy.array
  array = np.array(list)

  # construct 3 x 3 matrix
  # https://numpy.org/doc/1.26/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape
  matrix_intended_height = 3
  matrix_intended_width = 3
  matrix_intended_dimensions = (matrix_intended_height, matrix_intended_width)
  matrix = array.reshape(matrix_intended_dimensions)


  calculations_to_perform_for_rows_columns_and_flattened_matrix = {
    'mean' : np.ndarray.mean,
    'variance' : np.ndarray.var,
    'standard deviation' : np.ndarray.std,
    'max' : np.ndarray.max,
    'min' : np.ndarray.min,
    'sum' : np.ndarray.sum
  }

  calculations = {}
  
  for calculation_type, calculation_function in calculations_to_perform_for_rows_columns_and_flattened_matrix.items():
    values_for_columns, values_for_rows, value_for_flattened_matrix = perform_calculation_for_matrix(calculation_function, matrix)
    calculations[calculation_type] = [values_for_columns, values_for_rows, value_for_flattened_matrix]
  
  return calculations
