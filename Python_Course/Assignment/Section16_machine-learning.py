import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from sklearn import linear_model

# csvから価格を取得
def importData():
    btc_price = pd.read_csv('../coindesk-bpi-USD-close_data-2018-05-22_2018-06-21.csv')
    btc_price = btc_price[['Close Price']]
    data = np.array(btc_price)
    return data

data = importData()

# ここでは15時間前までを見る
days_ago = 15

Z = np.zeros((len(data), days_ago))

# 時間による推移を見て、そこから偏差を学習させる
for i in range(0, days_ago):
    Z[i:len(data), i] = data[0:len(data) - i, 0]

Y = Z[:,0]
X = Z[:,1:]

# 学習では、15~600行目を使う
train_x = X[15:600,:]
train_y = Y[15:600]

# 残りの全てをテストデータとする(最終値もテストデータにし、その1時間後を予測) 
test_x = Z[599:len(Z),:14]
test_y = Y[600:len(Y)]

# LinearRegression を使用して線形回帰モデルで学習
model = linear_model.LinearRegression()
model.fit(train_x, train_y)

# pred_y に対して、テストデータを使用して学習結果を代入
pred_y = model.predict(test_x)

# 予測結果を出力
result = pd.DataFrame(pred_y) 
result.columns = ['pred_y']
result['test_y'] = np.append(test_y, None)

# 回帰式の係数を表示
print("切片:", model.intercept_)
print("回帰係数:", model.coef_)

# テストデータ区間をPlot
plt.plot(range(0,len(result)-1), test_y, label='Actual price', color='blue')
plt.plot(range(0,len(result)), pred_y, label='Predicted price', color='red')
plt.xlabel('Hours')
plt.ylabel('Price ($)')
plt.title('Bitcoin Price')
plt.grid(True)
plt.legend()
plt.savefig("Bitcoin Price.png")
plt.close()

# テストデータ区間の末端を拡大Plot
plt.plot(range(len(result)-51,len(result)-1), test_y[len(test_y)-50:len(test_y)], label='Actual price', color='blue', marker = 'o')
plt.plot(range(len(result)-51,len(result)), pred_y[len(pred_y)-51:len(pred_y)], label='Predicted price', color='red', marker ='x')
plt.xlabel('Hours')
plt.ylabel('Price ($)')
plt.title('Bitcoin Price')
plt.grid(True)
plt.legend()
plt.savefig("Bitcoin Price Zoom-Up.png")
plt.close()