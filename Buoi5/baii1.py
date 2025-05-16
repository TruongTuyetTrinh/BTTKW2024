import numpy as np
import pandas as pd
import statsmodels.api as sm

X = np.array([0.5, 0.75, 1.00, 1.25, 1.5, 1.75, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.5, 4.00, 4.25, 4.50, 4.75, 5.00, 5.00])
y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

df = pd.DataFrame({'Giờ_ôn_thi': X, 'Kết_quả_thi': y})

# Thêm hằng số (intercept)
X = sm.add_constant(df['Giờ_ôn_thi'])  # X là biến độc lập
y = df['Kết_quả_thi']  # y là biến phụ thuộc

# Xây dựng mô hình hồi quy logistic
model = sm.Logit(y, X)
result = model.fit()

# Hiển thị kết quả mô hình
print(result.summary())

# Lấy và in ra các hệ số beta
beta_0, beta_1 = result.params
print(f"Beta 0 (Intercept): {beta_0}")
print(f"Beta 1 (Slope): {beta_1}")

#

# Tính xác suất cho từng giá trị giờ ôn thi
df['Xác_suất_đậu'] = result.predict(X)

# In ra kết quả
print(df[['Giờ_ôn_thi', 'Xác_suất_đậu']])
