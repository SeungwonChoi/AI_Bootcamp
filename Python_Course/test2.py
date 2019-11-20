import numpy as np
sigma = 3.5
mu = 65

data = sigma * np.random.randn(200) + mu

x = float(input("score?"))
t_score = 10*(x -data.mean())/data.std() + 50
print("mean", round(data.mean(),1))
print("std", round(data.std(),1))
print("std value", round(t_score,1))