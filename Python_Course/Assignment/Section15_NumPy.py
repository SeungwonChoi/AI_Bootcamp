import numpy as np

m_tables = [(np.arange(1,10) * i).tolist() for i in range(1,10)]

print(str(m_tables).replace("[","\n[").replace("]]","]\n]"))