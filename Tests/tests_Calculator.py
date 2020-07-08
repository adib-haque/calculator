import unittest
from Calculator import Calculator
from CsvReader.CSVReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        test_data = CsvReader("Tests/Data/addition.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

    def test_subtract_method_calculator(self):
        test_data = CsvReader("Tests/Data/subtraction.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

    def test_multiply_method_calculator(self):
        test_data = CsvReader("Tests/Data/multiplication.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

    def test_divide_method_calculator(self):
        test_data = CsvReader("Tests/Data/division.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

    def test_square_method_calculator(self):
        test_data = CsvReader("Tests/Data/square.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.sqr(row['Value 1']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

    def test_sqrt_method_calculator(self):
        test_data = CsvReader("Tests/Data/sqrt.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['Value 1']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
