METRIC_TO_STANDARD = 0.033814
METRIC_TO_IMPERIAL = 0.035195
STANDARD_TO_METRIC = 29.5735
STANDARD_TO_IMPERIAL = 1.04084
IMPERIAL_TO_METRIC = 28.41306
IMPERIAL_TO_STANDARD = 0.96076

def build_string(fluid_amt, measurement, system):
    return 'You have {} {} using the {}'.format(fluid_amt, measurement, system)
