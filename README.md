# TradingViewApi

Trading view is a http client to get technical analisys from tradingview website.

### Prerequisites

```
pip3 install requests 
```

### Running tests

```
if __name__ == '__main__':
    exchange = TradingViewApi.BITTREX
    crypto = 'BTCUSDT'
    t = TradingViewApi(exchange, crypto)
    demark_pivot = t.get_pivot_demark_r1()
```

## Class methods
### Oscillators

- get_relative_strength_index_14
- get_stochastic_k_14_3_3
- get_commodity_channel_index_20
- get_awesome_oscillators
- get_momentum_10
- get_macd_level_12_26
- get_stochastic_rsi_fast_3_3_14_14
- get_stochastic_rsi_fast_3_3_14_14_rec
- get_williams_percent_range_14
- get_williams_percent_range_14_rec
- get_bull_bear_power
- get_bull_bear_power_rec
- get_ultimate_oscillator_7_14_28
- get_ultimate_oscillator_7_14_28_rec

### Avergages
- get_exponential_moving_average_5
- get_simple_moving_average_5
- get_exponential_moving_average_10
- get_simple_moving_average_10
- get_exponential_moving_average_20
- get_simple_moving_average_20
- get_exponential_moving_average_30
- get_simple_moving_average_30
- get_exponential_moving_average_50
- get_simple_moving_average_50
- get_exponential_moving_average_100
- get_simple_moving_average_100
- get_exponential_moving_average_200
- get_simple_moving_average_200
- get_ichimoku_cloud_base_line_9_26_52_26
- get_ichimoku_cloud_base_line_9_26_52_26_rec
- get_volume_weighted_moving_average_20
- get_volume_weighted_moving_average_20_rec
- get_hull_moving_average_9
- get_hull_moving_average_9_rec

### Pivot
- get_pivot_classic_s1
- get_pivot_classic_s2
- get_pivot_classic_s3
- get_pivot_classic_r1
- get_pivot_classic_r2
- get_pivot_classic_r3
- get_pivot_classic_middle
- get_pivot_fibonacci_s1
- get_pivot_fibonacci_s2
- get_pivot_fibonacci_s3
- get_pivot_fibonacci_r1
- get_pivot_fibonacci_r2
- get_pivot_fibonacci_r3
- get_pivot_fibonacci_middle
- get_pivot_camarilla_s1
- get_pivot_camarilla_s2
- get_pivot_camarilla_s3
- get_pivot_camarilla_r1
- get_pivot_camarilla_r2
- get_pivot_camarilla_r3
- get_pivot_camarilla_middle
- get_pivot_woodie_s1
- get_pivot_woodie_s2
- get_pivot_woodie_s3
- get_pivot_woodie_r1
- get_pivot_woodie_r2
- get_pivot_woodie_r3
- get_pivot_woodie_middle
- get_pivot_demark_s1
- get_pivot_demark_r1
- get_pivot_demark_middle

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
