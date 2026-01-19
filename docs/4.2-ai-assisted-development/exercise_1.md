# Exercise 1: Code Understanding with AI
Open a web browser and choose an AI chat (ChatGPT, Claude, Le Chat) and try the
prompt templates below with the `main.py` of the pkoffee project.

### PROMPT 1
```
Explain the code below to an engineer discovering it.
CODE:
```

### PROMPT 2
```
Explain what this code is doing conceptually, how the main
components interact, and what problem it is solving.
Assume the reader is technically competent but unfamiliar
with the codebase. 
CODE:
```

### PROMPT 3
```
Explain this code at a high level for an engineer who didn’t
write it. Focus on intent, data flow, and design choices
rather than line-by-line mechanics.
CODE:
```

## Original `main.py` script
```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from pathlib import Path
import seaborn as sns

data = pd.read_csv("coffee_productivity.csv")
X = data["cups"].values
Y = data["productivity"].values

fig = plt.figure(figsize=(10, 6))
ax = plt.gca()
ax.set_xlabel("Cups of Coffee")
ax.set_ylabel("Productivity")
ax.set_title("Productivity vs Coffee")
ax.grid(True, alpha=0.3)

sns.violinplot(
    data=data,
    x="cups",
    y="productivity",
    hue="cups",
    ax=ax,
    inner="quartile",
    cut=0,
    density_norm="width",
    palette="Greens",
    linewidth=0.8,
    legend=False,
)

x_min, x_max = float(np.min(X)), float(np.max(X))
y_min, y_max = float(np.min(Y)), float(np.max(Y))
dy = max(1e-8, y_max - y_min)

MODELS = [
    {
        "name": "quadratic",
        "p0": [y_min, 0.0, 0.01],
        "bounds": (-np.inf, np.inf),
        "f": lambda xx, a0, a1, a2: a0 + a1 * xx + a2 * xx**2,
    },
    {
        "name": "saturating",
        "p0": [dy, max(1.0, 0.2 * (x_min + x_max)), y_min],
        "bounds": ([-np.inf, 0.0, -np.inf], [np.inf, np.inf, np.inf]),
        "f": lambda xx, Vmax, K, y0: y0 + Vmax * (xx / np.maximum(K + xx, 1e-9)),
    },
    {
        "name": "logistic",
        "p0": [dy, 0.5, 0.5 * (x_min + x_max), y_min],
        "bounds": ([-np.inf, 0.0, -np.inf, -np.inf], [np.inf, np.inf, np.inf, np.inf]),
        "f": lambda xx, L, k, x0, y0: y0 + L / (1.0 + np.exp(-k * (xx - x0))),
    },
    {
        "name": "peak",
        "p0": [max(y_min, y_max), max(1.0, 0.5 * (x_min + x_max))],
        "bounds": ([-np.inf, 0.0], [np.inf, np.inf]),
        "f": lambda xx, a, b: a * xx * np.exp(-xx / np.maximum(b, 1e-9)),
    },
    {
        "name": "peak2",
        "p0": [max(1e-6, y_max / max(1.0, x_max**2)), max(1.0, 0.5 * (x_min + x_max))],
        "bounds": ([-np.inf, 0.0], [np.inf, np.inf]),
        "f": lambda xx, a, b: a * (xx**2) * np.exp(-xx / np.maximum(b, 1e-9)),
    },
]

fits = []
for m in MODELS:
    popt, _ = curve_fit(m["f"], X, Y, p0=m["p0"], bounds=m["bounds"], maxfev=20000)
    yhat = m["f"](X, *popt)
    ss_res = float(np.sum((Y - yhat) ** 2))
    ss_tot = float(np.sum((Y - np.mean(Y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
    fits.append({"name": m["name"], "func": m["f"], "params": popt, "r2": r2})


fits.sort(key=lambda d: (d["r2"] if np.isfinite(d["r2"]) else -np.inf), reverse=True)

x_smooth = np.linspace(np.min(X), np.max(X), 300)
for idx, res in enumerate(fits):
    y_s = res["func"](x_smooth, *res["params"])
    label = f"{res['name']} (R²={res['r2']:.3f})"
    ax.plot(x_smooth, y_s, lw=2, label=label)


ax.legend()
ax.set_ylim(-0.2, 8)
out_path = Path(__file__).with_name("fit_plot.png")
plt.tight_layout()
plt.savefig(out_path, dpi=150)
plt.show()
```