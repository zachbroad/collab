from util import *

def metric_to_std(fluid_amt):
    us_fluid_oz = fluid_amt * METRIC_TO_STANDARD
    print(build_string(us_fluid_oz, 'oz', 'Standard System'))


def metric_to_imp(fluid_amt):
    imperial_fluid_oz = fluid_amt * METRIC_TO_IMPERIAL
    print(build_string(imperial_fluid_oz, 'oz', 'Imperial System'))


def std_to_metric(fluid_amt):
    standard_fluid_oz = fluid_amt * STANDARD_TO_METRIC
    print(build_string(standard_fluid_oz, 'mL', 'Metric System'))


def std_to_imp(fluid_amt):
    standard_fluid_oz = fluid_amt * STANDARD_TO_IMPERIAL
    print(build_string(standard_fluid_oz, 'oz', 'Standard System'))


def imp_to_metric(fluid_amt):
    imperial_fluid_oz = fluid_amt * IMPERIAL_TO_METRIC
    print(build_string(imperial_fluid_oz, 'mL', 'Metric System'))


def imp_to_std(fluid_amt):
    imperial_fluid_oz = fluid_amt * IMPERIAL_TO_STANDARD
    print(build_string(imperial_fluid_oz, 'oz', 'Imperial System'))
