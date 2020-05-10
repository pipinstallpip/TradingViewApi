import requests


class TradingViewApi:

    REQUEST_URL = 'https://scanner.tradingview.com/crypto/scan'

    T_1_MINUTE = '|1'
    T_5_MINUTES = '|5'
    T_15_MINUTES = '|15'
    T_1_HOUR = '|60'
    T_4_HOURS = '|240'
    T_1_DAY = ''
    T_1_WEEK = '|1W'
    T_1_MONTH = '|1M'

    BUY = 1
    SELL = -1
    NEUTRO = 0

    BINANCE = 'BINANCE'
    BITTREX = 'BITTREX'

    COLUMNS = [
        "Recommend.Other",
        "Recommend.All",
        "Recommend.MA",
        "RSI",
        "RSI[1]",
        "Stoch.K",
        "Stoch.D",
        "Stoch.K[1]",
        "Stoch.D[1]",
        "CCI20",
        "CCI20[1]",
        "ADX",
        "ADX+DI",
        "ADX-DI",
        "ADX+DI[1]",
        "ADX-DI[1]",
        "AO",
        "AO[1]",
        "Mom",
        "Mom[1]",
        "MACD.macd",
        "MACD.signal",
        "Rec.Stoch.RSI",
        "Stoch.RSI.K",
        "Rec.WR",
        "W.R",
        "Rec.BBPower",
        "BBPower",
        "Rec.UO",
        "UO",
        "EMA5",
        "close",
        "SMA5",
        "EMA10",
        "SMA10",
        "EMA20",
        "SMA20",
        "EMA30",
        "SMA30",
        "EMA50",
        "SMA50",
        "EMA100",
        "SMA100",
        "EMA200",
        "SMA200",
        "Rec.Ichimoku",
        "Ichimoku.BLine",
        "Rec.VWMA",
        "VWMA",
        "Rec.HullMA9",
        "HullMA9",
        "Pivot.M.Classic.S3",
        "Pivot.M.Classic.S2",
        "Pivot.M.Classic.S1",
        "Pivot.M.Classic.Middle",
        "Pivot.M.Classic.R1",
        "Pivot.M.Classic.R2",
        "Pivot.M.Classic.R3",
        "Pivot.M.Fibonacci.S3",
        "Pivot.M.Fibonacci.S2",
        "Pivot.M.Fibonacci.S1",
        "Pivot.M.Fibonacci.Middle",
        "Pivot.M.Fibonacci.R1",
        "Pivot.M.Fibonacci.R2",
        "Pivot.M.Fibonacci.R3",
        "Pivot.M.Camarilla.S3",
        "Pivot.M.Camarilla.S2",
        "Pivot.M.Camarilla.S1",
        "Pivot.M.Camarilla.Middle",
        "Pivot.M.Camarilla.R1",
        "Pivot.M.Camarilla.R2",
        "Pivot.M.Camarilla.R3",
        "Pivot.M.Woodie.S3",
        "Pivot.M.Woodie.S2",
        "Pivot.M.Woodie.S1",
        "Pivot.M.Woodie.Middle",
        "Pivot.M.Woodie.R1",
        "Pivot.M.Woodie.R2",
        "Pivot.M.Woodie.R3",
        "Pivot.M.Demark.S1",
        "Pivot.M.Demark.Middle",
        "Pivot.M.Demark.R1"
    ]

    def __init__(self, exchange: str, crypto: str, type_v=''):
        self.exchange = exchange
        self.crypto = crypto
        self.type_v = type_v
        response = self.__request().json()['data'][0]['d']

        self.__dict__ = dict(zip(self.COLUMNS, response))
        del response

    def __request(self):
        return requests.\
            post(self.REQUEST_URL,
                 data='{"symbols":{"tickers":["%s:%s"],'
                      '"query":{"types":[]}},"columns":%s}' % (self.exchange, self.crypto,
                                                               str([f"{x}{self.type_v}" for x in self.COLUMNS])
                                                               .replace('\'', '"')))

    '''
        OSCILLATORS BEGIN
    '''
    def get_relative_strength_index_14(self):
        return self.__dict__['RSI']

    def get_stochastic_k_14_3_3(self):
        return self.__dict__['Stoch.K']

    def get_commodity_channel_index_20(self):
        return self.__dict__['CCI20']

    def get_awesome_oscillators(self):
        return self.__dict__['AO']

    def get_momentum_10(self):
        return self.__dict__['Mom']

    def get_macd_level_12_26(self):
        return self.__dict__['MACD.macd']

    def get_stochastic_rsi_fast_3_3_14_14(self):
        return self.__dict__['Stoch.RSI.K']

    def get_stochastic_rsi_fast_3_3_14_14_rec(self):
        return self.__dict__['Rec.Stoch.RSI']

    def get_williams_percent_range_14(self):
        return self.__dict__['W.R']

    def get_williams_percent_range_14_rec(self):
        return self.__dict__['Rec.WR']

    def get_bull_bear_power(self):
        return self.__dict__['BBPower']

    def get_bull_bear_power_rec(self):
        return self.__dict__['Rec.BBPower']

    def get_ultimate_oscillator_7_14_28(self):
        return self.__dict__['UO']

    def get_ultimate_oscillator_7_14_28_rec(self):
        return self.__dict__['Rec.UO']

    '''
        OSCILLATORS END
    '''

    '''
        AVERAGE BEGIN
    '''
    def get_exponential_moving_average_5(self):
        return self.__dict__['EMA5']

    def get_simple_moving_average_5(self):
        return self.__dict__['SMA5']

    def get_exponential_moving_average_10(self):
        return self.__dict__['EMA10']

    def get_simple_moving_average_10(self):
        return self.__dict__['SMA10']

    def get_exponential_moving_average_20(self):
        return self.__dict__['EMA20']

    def get_simple_moving_average_20(self):
        return self.__dict__['SMA20']

    def get_exponential_moving_average_30(self):
        return self.__dict__['EMA30']

    def get_simple_moving_average_30(self):
        return self.__dict__['SMA30']

    def get_exponential_moving_average_50(self):
        return self.__dict__['EMA50']

    def get_simple_moving_average_50(self):
        return self.__dict__['SMA50']

    def get_exponential_moving_average_100(self):
        return self.__dict__['EMA100']

    def get_simple_moving_average_100(self):
        return self.__dict__['SMA100']

    def get_exponential_moving_average_200(self):
        return self.__dict__['EMA200']

    def get_simple_moving_average_200(self):
        return self.__dict__['SMA200']

    def get_ichimoku_cloud_base_line_9_26_52_26(self):
        return self.__dict__['Ichimoku.BLine']

    def get_ichimoku_cloud_base_line_9_26_52_26_rec(self):
        return self.__dict__['Rec.Ichimoku']

    def get_volume_weighted_moving_average_20(self):
        return self.__dict__['VWMA']

    def get_volume_weighted_moving_average_20_rec(self):
        return self.__dict__['Rec.VWMA']

    def get_hull_moving_average_9(self):
        return self.__dict__['HullMA9']

    def get_hull_moving_average_9_rec(self):
        return self.__dict__['Rec.HullMA9']

    '''
        AVERAGE END
    '''

    '''
        PIVOT BEGIN
    '''

    def get_pivot_classic_s1(self):
        return self.__dict__['Pivot.M.Classic.S1']

    def get_pivot_classic_s2(self):
        return self.__dict__['Pivot.M.Classic.S2']

    def get_pivot_classic_s3(self):
        return self.__dict__['Pivot.M.Classic.S3']

    def get_pivot_classic_r1(self):
        return self.__dict__['Pivot.M.Classic.R1']

    def get_pivot_classic_r2(self):
        return self.__dict__['Pivot.M.Classic.R2']

    def get_pivot_classic_r3(self):
        return self.__dict__['Pivot.M.Classic.R3']

    def get_pivot_classic_middle(self):
        return self.__dict__['Pivot.M.Classic.Middle']

    def get_pivot_fibonacci_s1(self):
        return self.__dict__['Pivot.M.Fibonacci.S1']

    def get_pivot_fibonacci_s2(self):
        return self.__dict__['Pivot.M.Fibonacci.S2']

    def get_pivot_fibonacci_s3(self):
        return self.__dict__['Pivot.M.Fibonacci.S3']

    def get_pivot_fibonacci_r1(self):
        return self.__dict__['Pivot.M.Fibonacci.R1']

    def get_pivot_fibonacci_r2(self):
        return self.__dict__['Pivot.M.Fibonacci.R2']

    def get_pivot_fibonacci_r3(self):
        return self.__dict__['Pivot.M.Fibonacci.R3']

    def get_pivot_fibonacci_middle(self):
        return self.__dict__['Pivot.M.Fibonacci.Middle']

    def get_pivot_camarilla_s1(self):
        return self.__dict__['Pivot.M.Camarilla.S1']

    def get_pivot_camarilla_s2(self):
        return self.__dict__['Pivot.M.Camarilla.S2']

    def get_pivot_camarilla_s3(self):
        return self.__dict__['Pivot.M.Camarilla.S3']

    def get_pivot_camarilla_r1(self):
        return self.__dict__['Pivot.M.Camarilla.R1']

    def get_pivot_camarilla_r2(self):
        return self.__dict__['Pivot.M.Camarilla.R2']

    def get_pivot_camarilla_r3(self):
        return self.__dict__['Pivot.M.Camarilla.R3']

    def get_pivot_camarilla_middle(self):
        return self.__dict__['Pivot.M.Camarilla.Middle']

    def get_pivot_woodie_s1(self):
        return self.__dict__['Pivot.M.Woodie.S1']

    def get_pivot_woodie_s2(self):
        return self.__dict__['Pivot.M.Woodie.S2']

    def get_pivot_woodie_s3(self):
        return self.__dict__['Pivot.M.Woodie.S3']

    def get_pivot_woodie_r1(self):
        return self.__dict__['Pivot.M.Woodie.R1']

    def get_pivot_woodie_r2(self):
        return self.__dict__['Pivot.M.Woodie.R2']

    def get_pivot_woodie_r3(self):
        return self.__dict__['Pivot.M.Woodie.R3']

    def get_pivot_woodie_middle(self):
        return self.__dict__['Pivot.M.Woodie.Middle']

    def get_pivot_demark_s1(self):
        return self.__dict__['Pivot.M.Demark.S1']

    def get_pivot_demark_r1(self):
        return self.__dict__['Pivot.M.Demark.R1']

    def get_pivot_demark_middle(self):
        return self.__dict__['Pivot.M.Demark.Middle']

    '''
        PIVOT END
    '''
