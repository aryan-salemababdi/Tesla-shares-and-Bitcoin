import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
btc_data = pd.read_csv("/content/btc.csv")
tesla_data = pd.read_csv("/content/tesla.csv")
date = btc_data["date"].values
open = btc_data["1. open"].values
high = btc_data["2. high"].values
low = btc_data["3. low"].values
close = btc_data["4. close"].values
volume = btc_data["5. volume"].values
date , open , high , low , close , volume = date[::-1] , open[::-1] , high[::-1] , low[::-1] , close[::-1] , volume[::-1]
_a ={"open" : open,"high": high,"low":low,"close":close,"volume":volume}
new_btc_data = pd.DataFrame(_a , index = date , columns=["open" , "high" , "low" , "close" , "volume"] )
open = new_btc_data["open"].values[3600:]
high = new_btc_data["high"].values[3600:]
low = new_btc_data["low"].values[3600:]
close = new_btc_data["close"].values[3600:]
plt.figure(figsize=(15,7),dpi=80)
plt.title("BTC Open Price")
plt.xlabel("date")
plt.ylabel("price")
# plt.xticks([0,3704],["2011-08-19","2021-11-11"])
plt.plot(open , label = " open ")
plt.plot(high , label = " high ")
plt.plot(low , label = " low ")
plt.plot(close , label = " close ")
plt.legend()
plt.grid()
plt.show()
date = tesla_data["date"].values
open = tesla_data["1. open"].values
high = tesla_data["2. high"].values
low = tesla_data["3. low"].values
close = tesla_data["4. close"].values
volume = tesla_data["5. volume"].values
date , open , high , low , close , volume = date[::-1] , open[::-1] , high[::-1] , low[::-1] , close[::-1] , volume[::-1]
_b ={"open" : open,"high": high,"low":low,"close":close,"volume":volume}
new_tesla_data = pd.DataFrame(_b , index = date , columns=["open" , "high" , "low" , "close" , "volume"] )
open = new_tesla_data["open"].values[2000:]
high = new_tesla_data["high"].values[2000:]
low = new_tesla_data["low"].values[2000:]
close = new_tesla_data["close"].values[2000:]
plt.figure(figsize=(20,10),dpi=80)
plt.title("Tesla Open Price")
plt.xlabel("date")
plt.ylabel("price")
# plt.xticks([0,3704],["2011-08-19","2021-11-11"])
plt.plot(open , label = " open ")
plt.plot(high , label = " high ")
plt.plot(low , label = " low ")
plt.plot(close , label = " close ")
plt.legend()
plt.grid()
plt.show()
print("for last 165 days we have for open high :")
plt.hist(open)
plt.show()
btc = new_btc_data["open"].values[3605:]
tessla = new_tesla_data["open"].values[2765:]
print(f"Covariance is {np.cov(tessla,btc)} (matrix)")
p_coeef , p_value = pearsonr(btc,tessla)
print(f" Correlation Coefficients is  {p_coeef}")
print(f" p-value is {p_value}")
print("According to the data, the obtained Pearson correlation coefficient indicates a strong direct relationship between the shares of Bitcoin and Tesla in the last 100 days.")
