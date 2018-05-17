import random
from sklearn import linear_model
from sklearn.externals import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics


def decide_y(a, b, c, d, e, f):
    choice = random.choice([1,2,3,4,5])
    if choice == 1:
        return a + b + c + d + e + f
    if choice == 2:
        return a*b + c + d + e + f
    if choice == 3:
        return a+c
    if choice == 4:
        return a*b*c*d+e
    if choice == 5:
        return d+a


df = pd.DataFrame()
for _ in range(10000):
    a = random.randint(1,100)
    b = random.randint(5,25)
    c = random.randint(25, 1000)
    d = random.randint(15, 27)
    e = random.randint(13, 27)
    f = 42
    y = decide_y(a, b, c, d, e, f)
    df = df.append({
        "A": a,
        "B": b,
        "C": c,
        "D": d,
        "E": e,
        "F": f,
        "Y": y
    }, ignore_index=True)

lin_reg = linear_model.LinearRegression()
X = df[["A", "B", "C", "D", "E", "F"]]
y = df["Y"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)

print("R^2", metrics.r2_score(y_test, y_pred))
print("MSE:", metrics.mean_squared_error(y_test, y_pred))
print("MAE:", metrics.mean_absolute_error(y_test, y_pred))

joblib.dump(lin_reg, 'linear_regression_example.pkl')
