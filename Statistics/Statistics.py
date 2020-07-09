from Calculator.Calculator import Calculator
from CsvReader.CSVReader import CsvReader
from Statistics.confidenceinterval import confidence_interval
from Statistics.median import median
from Statistics.mode import mode
from Statistics.popcorrelationcoefficient import pop_correlation_coefficient
from Statistics.populationmean import population_mean
from Statistics.populationstandarddeviation import pop_stand_dev
from Statistics.populationvariance import population_variance
from Statistics.Proportion import proportion
from Statistics.pvalue import p_value
from Statistics.samplemean import sample_mean
from Statistics.samplestandarddeviation import sample_std_dev
from Statistics.samplevariance import var_sample_proportion
from Statistics.variancepopulationproportion import var_pop_proportion
from Statistics.zscore import z_score



    def conf_interval(self, a):
        self.result = confidence_interval(a)
        return self.result

    def median(self, a):
        self.result = median(a)
        return self.result

    def mode(self, a):
        self.result = mode(a)
        return self.result

    def pop_correlation_coefficient(self, a, b):
        self.result = pop_correlation_coefficient(a, b)
        return self.result

    def population_mean(self, a):
        self.result = population_mean(a)
        return self.result

    def pop_standard_dev(self, a):
        self.result = pop_stand_dev(a)
        return self.result

    def pop_variance(self, a):
        self.result = population_variance(a)
        return self.result

    def proportion(self, a):
        self.result = proportion(a)
        return self.result

    def p_value(self, a):
        self.result = p_value(a)
        return self.result

    def sample_mean(self, a):
        self.result = sample_mean(a)
        return self.result

    def sample_std_dev(self, a):
        self.result = sample_std_dev(a)
        return self.result

    def sample_variance(self, a):
        self.result = var_sample_proportion(a)
        return self.result

    def variance_pop_proportion(self, a):
        self.result = var_pop_proportion(a)
        return self.result

    def z_score(self, a):
        self.result = z_score(a)
        return self.result
