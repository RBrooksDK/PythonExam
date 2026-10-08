# %%
import numpy as np
import pandas as pd
import scipy
from scipy.stats import norm
import matplotlib
import matplotlib.pyplot as plt
import sympy as sp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import sklearn
from sklearn.linear_model import LinearRegression
import openpyxl
import plotly.graph_objects as go

x = sp.symbols("x")
assert sp.integrate(x**2, (x, 0, 2)) == sp.Rational(8, 3)
assert np.isclose(norm.cdf(0), 0.5)
assert pd.DataFrame({"x": [1, 2]}).x.sum() == 3
assert np.isclose(sm.OLS([1, 3, 5], sm.add_constant([0, 1, 2])).fit().params[1], 2)
assert np.isclose(LinearRegression().fit([[0], [1], [2]], [1, 3, 5]).coef_[0], 2)
assert isinstance(openpyxl.Workbook().active.title, str)
assert len(go.Figure().data) == 0
fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])
plt.close(fig)

try:
    import openai
except ModuleNotFoundError:
    pass
else:
    raise AssertionError("openai must not be preinstalled")

print("Exam packages passed the offline runtime check")
