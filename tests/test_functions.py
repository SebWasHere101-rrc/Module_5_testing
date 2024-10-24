"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: ACE Faculty
Date: {current date}
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""

import unittest
from unittest.mock import patch

from src.functions import greet_name_age, math_operation, prompt_name_greeting, grade_outcome

class TestFunctions(unittest.TestCase):
    def test_greet_name_age_valid_arguements_expected_string(self):
        # Arrange
        name = "Sebastian"
        age = 19
        expected = "Hello Sebastian, you are 19 years old!"


        # Act
        actual = greet_name_age(name, age)

        #Assert
        self.assertEqual(expected, actual)

    def test_math_operations_addition_return_sum(self):
        # Arrange
        operand1 = 10
        operand2 = 5
        operation = "+"

        expected = 15.0
        # Act
        actual = math_operation(operand1, operand2, operation)

        #Assert
        self.assertEqual(expected, actual)

        # Arrange, Act, and Assert.
        # self.assertEqual(15.0, math_operation(10, 5, "+"))


    def test_math_operations_subtraction_return_difference(self):
        # Arrange
        operand1 = 10
        operand2 = 5
        operation = "-"

        expected = 5.0
        # Act
        actual = math_operation(operand1, operand2, operation)

        #Assert
        self.assertEqual(expected, actual)

        # Arrange, Act, and Assert.
        # self.assertEqual(5.0, math_operation(10, 5, "-"))

    def test_math_operation_invalid_operator_ValueError(self):
        # Arrange
        operator1 = 4
        operator2 = 15

        # use an invalid operator
        operation = "*"
        expected = "Invalid operation."
        
        
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            math_operation(operator1, operator2, operation)
        
        self.assertEqual(expected, str(context.exception))

    def test_prompt_name_greeting_valid_inputs_greetings_returned(self):
        # builtins.input: allows us to mock input behaviour

        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["Oliver", "Winnipeg"]
            expected = "Your name is Oliver and your current city is Winnipeg."

            # Act
            actual = prompt_name_greeting()

        # Assert
        self.assertEqual(expected, actual)
    
    """
    def test_prompt_name_greeting_no_mocking_pauses_program(self):
        # Arrange
        expected = "Your name is Oliver and your current city is Winnipeg."

        # Act
        actual = prompt_name_greeting()

        # Assert
        self.assertEqual(expected, actual)
    """

    def test_grade_outcome_high_grade_a_plus(self):
        # Arrange
        grade = 100
        expected = "A+"

        low_edge = 91
        # Act
        actual = grade_outcome(grade)
        edge_actual = grade_outcome(low_edge)


        # Assert
        self.assertEqual(expected, actual)
        self.assertEqual(expected, edge_actual)

    def test_grade_outcome_medium_grade_pass(self):
        # Arrange
        grade = 75
        expected = "Pass"

        low_edge = 50
        high_edge = 90

        # Act
        actual = grade_outcome(grade)
        low_actual = grade_outcome(low_edge)
        high_actual = grade_outcome(high_edge)

        # Assert
        self.assertEqual(expected, actual)
        self.assertEqual(expected, low_actual)
        self.assertEqual(expected, high_actual)

    def test_grade_outcome_low_grade_fail(self):
        # Arrange
        grade = 40
        expected = "Fail"
        high_grade = 49

        # Act
        actual = grade_outcome(grade)
        high_actual = grade_outcome(high_grade)

        # Assert
        self.assertEqual(expected, actual)
        self.assertEqual(expected, high_actual)
