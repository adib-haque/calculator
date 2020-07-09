import unittest
from CsvReader.CSVReader import CsvReader
from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_CSV(self):
        test_data = CsvReader("Tests/Data/csvtester.csv").data
        for row in test_data:
            self.assertEqual(row["Value 1"], "480")


if __name__ == '__main__':
    unittest.main()
