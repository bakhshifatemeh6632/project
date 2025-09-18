import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# داده‌ی فرضی: متراژ خانه (X) و قیمت خانه (y)
X = np.array([[50], [60], [80], [100], [120]])  # متراژ
y = np.array([150, 180, 220, 260, 300])        # قیمت (میلیون)

# ساخت مدل
model = LinearRegression()

# آموزش مدل
model.fit(X, y)

# پیش‌بینی قیمت برای خانه‌ی 90 متری
pred = model.predict([[90]])
print("قیمت پیش‌بینی‌شده برای 90 متر:", pred[0])

# رسم نمودار
plt.scatter(X, y, color='blue', label="داده واقعی")
plt.plot(X, model.predict(X), color='red', label="خط رگرسیون")
plt.xlabel("متراژ (متر)")
plt.ylabel("قیمت (میلیون)")
plt.legend()
plt.show()
