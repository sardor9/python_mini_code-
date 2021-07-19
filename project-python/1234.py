from alpha_vantage.timeseies. import TimeSeries
import matplotlip.pyplot as plt
import credentials

ts = TimeSeries(
    key(credentials.APY_KEY,
    output_format='pandas'
)

data, meta_data = ts.get_intraday(
    symbol='TSLA',
    interval='30min',
    outputsize='full',
)
data['4. close'].plot()
plt.show()
    
