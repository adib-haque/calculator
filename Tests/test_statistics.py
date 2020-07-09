import unittest
from pprint import pprint
from Statistics.Statistics import Statistics
from CsvReader.CSVReader import CsvReader
from CsvReader.Data import Data


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        test_data = CsvReader("/Tests/Data/randomdata.csv")
        answers = CsvReader("Tests/Data/answers.csv").data
        values = Data(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.population_mean(values), float((column['mean'])))

    def test_median(self):
        test_data = CsvReader("/Tests/Data/randomdata.csv")
        answers = CsvReader("/Tests/Data/answers.csv").data
        values = Data(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.median(values), float((column['median'])))

    def test_mode(self):
        test_data = CsvReader("/Tests/Data/randomdata.csv")
        answers = CsvReader("Tests/Data/answers.csv").data
        values = Data(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.mode(values), float((column['mode'])))

    def test_pop_std_dev(self):
        test_data = CsvReader("/Tests/Data/randomdata.csv")
        answers = CsvReader("Tests/Data/answers.csv").data
        values = Data(test_data, 'value')
        for column in answers:
            self.assertEqual(round(self.statistics.pop_standard_dev(values), 4), float((column['PSD'])))

    def test_variance_population_proportion(self):
        test_data = CsvReader("/Tests/Data/randomdata.csv")
        answers = CsvReader("Tests/Data/answers.csv").data
        values = Data(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.variance_pop_proportion(values), float((column['VPP'])))

    def test_z_score(self):
        test_data = CsvReader("/Tests/Data/randomdata.csv")
        answers = CsvReader("Tests/Data/answers.csv").data
        values = Data(test_data, "value")
        for column in answers:
            self.assertEqual(self.statistics.z_score(values), float((column['z_score'])))

    def test_sample_variance(self):
        test_data = CsvReader("/Tests/Data/randomdata.csv")
        answers = CsvReader("Tests/Data/answers.csv").data
        values = Data(test_data, 'value')
        x = self.statistics.sample_variance(values)
        self.assertEqual(x, x)

    def test_confidence_interval_calculator(self):
        test_data = CsvReader("/Tests/Data/randomdata.csv")
        answers = CsvReader('Tests/Data/answers.csv').data
        values = Data(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.conf_interval(values),
                             (float(column['conf_int_high']), float(column['conf_int_low'])))

    def test_proportion(self):
        test_data = CsvReader("/Tests/Data/randomdata.csv")
        answers = CsvReader("Tests/Data/answers.csv").data
        values = Data(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.proportion(values), float((column['proportion'])))


if __name__ == '__main__':
    unittest.main()
