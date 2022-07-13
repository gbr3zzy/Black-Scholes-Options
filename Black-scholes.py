def _get_option_value(series):
""" Return the option value given the OptionType
    :param series: row of the dataframe, accessible by label
    :return: Black-Scholes option value
"""
option_type = series["OptionType"] S = series["UnderlyingPrice"]
K = series["Strike"]
r = series["InterestRate"]
t = series["TimeUntilExpiration"] vol = series["ImpliedVolatilityMid"]
meth_name = "black_scholes_{0}_value".format(option_type) return float(globals().get(meth_name)(S, K, r, t, vol))
def _get_delta(series):
""" Return the option delta given the OptionType
    :param series: row of the dataframe, accessible by label
    :return: option delta
"""
option_type = series["OptionType"] S = series["UnderlyingPrice"]
K = series["Strike"]
r = series["InterestRate"]
t = series["TimeUntilExpiration"] vol = series["ImpliedVolatilityMid"]
meth_name = "{0}_delta".format(option_type)
return float(globals().get(meth_name)(S, K, r, t, vol))
def _get_gamma(series):
""" Return the option gamma
    :param series: row of the dataframe, accessible by label
    :return: option gamma
"""
S = series["UnderlyingPrice"]
K = series["Strike"]
r = series["InterestRate"]
t = series["TimeUntilExpiration"] vol = series["ImpliedVolatilityMid"]
return float(gamma(S, K, r, t, vol))

def _get_vega(series):
""" Return the option vega
    :param series: row of the dataframe, accessible by label
    :return: option vega
"""
S = series["UnderlyingPrice"]
K = series["Strike"]
r = series["InterestRate"]
t = series["TimeUntilExpiration"] vol = series["ImpliedVolatilityMid"]
return float(vega(S, K, r, t, vol)) def _get_theta(series):
    """ Return the option theta given the OptionType
    :param series: row of the dataframe, accessible by label
    :return: option theta
"""
option_type = series["OptionType"] S = series["UnderlyingPrice"]
K = series["Strike"]
r = series["InterestRate"]
t = series["TimeUntilExpiration"] vol = series["ImpliedVolatilityMid"]
meth_name = "{0}_theta".format(option_type)
return float(globals().get(meth_name)(S, K, r, t, vol))
def _get_rho(series):
""" Return the option rho given the OptionType
    :param series: row of the dataframe, accessible by label
    :return: option rho
"""
option_type = series["OptionType"] S = series["UnderlyingPrice"]
K = series["Strike"]
r = series["InterestRate"]
t = series["TimeUntilExpiration"] vol = series["ImpliedVolatilityMid"]
meth_name = "{0}_rho".format(option_type)
return float(globals().get(meth_name)(S, K, r, t, vol))

