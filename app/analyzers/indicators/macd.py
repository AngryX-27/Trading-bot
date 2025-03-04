""" MACD Indicator
"""

import math

import pandas
from talib import abstract

from analyzers.utils import IndicatorUtils


class MACD(IndicatorUtils):
    def analyze(self, historical_data, signal=['macd'], hot_thresh=None, cold_thresh=None):
        """Performs a macd analysis on the historical data

        Args:
            historical_data (list): A matrix of historical OHCLV data.
            signal (list, optional): Defaults to macd. The indicator line to check hot/cold
                against.
            hot_thresh (float, optional): Defaults to None. The threshold at which this might be
                good to purchase.
            cold_thresh (float, optional): Defaults to None. The threshold at which this might be
                good to sell.

        Returns:
            pandas.DataFrame: A dataframe containing the indicators and hot/cold values.
        """

        dataframe = self.convert_to_dataframe(historical_data)
        macd_values = abstract.MACD(dataframe).iloc[:]
        macd_values.dropna(how='all', inplace=True)

        if len(macd_values) and signal[0] in macd_values.columns:
            if hot_thresh is not None:
                macd_values['is_hot'] = macd_values.loc[:,
                                                        signal[0]] > hot_thresh
            if cold_thresh is not None:
                macd_values['is_cold'] = macd_values.loc[:,
                                                         signal[0]] < cold_thresh

        return macd_values
