""" Momentum Indicator
"""

import math

import pandas
from talib import abstract

from analyzers.utils import IndicatorUtils


class Momentum(IndicatorUtils):
    def analyze(self, historical_data, period_count=10,
                signal=['momentum'], hot_thresh=None, cold_thresh=None):
        """Performs momentum analysis on the historical data

        Args:
            historical_data (list): A matrix of historical OHCLV data.
            period_count (int, optional): Defaults to 10. The number of data points to consider for
                our momentum.
            signal (list, optional): Defaults to momentum. The indicator line to check hot/cold
                against.
            hot_thresh (float, optional): Defaults to None. The threshold at which this might be
                good to purchase.
            cold_thresh (float, optional): Defaults to None. The threshold at which this might be
                good to sell.

        Returns:
            pandas.DataFrame: A dataframe containing the indicators and hot/cold values.
        """

        dataframe = self.convert_to_dataframe(historical_data)
        mom_values = abstract.MOM(dataframe, period_count).to_frame()
        mom_values.dropna(how='all', inplace=True)
        mom_values.rename(
            columns={mom_values.columns[0]: 'momentum'}, inplace=True)

        if len(mom_values) and signal[0] in mom_values.columns:
            if hot_thresh is not None:
                mom_values['is_hot'] = mom_values.loc[:,
                                                      signal[0]] > hot_thresh
            if cold_thresh is not None:
                mom_values['is_cold'] = mom_values.loc[:,
                                                       signal[0]] < cold_thresh

        return mom_values
