# Exercise 2: Code Debugging
Debug the code snippets below  with Copilot/Continue or Browser-based AI.
## CODE 1 (Reorganization of pkoffee/main.py)
```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from pathlib import Path
import seaborn as sns

def load_data(file_path):
    data = pd.read_csv(file_path)
    X = data["cups"].values()
    Y = data["productivity"].values()
    return data, X, Y

def setup_plot():
    fig = plt.figure(figsize=(10, 6))
    ax = plt.gca()
    ax.set_xlabel("Cups of Coffee")
    ax.set_ylabel("Productivity")
    ax.set_title("Productivity vs Coffee")
    ax.grid(True, alpha=0.3)
    return fig, ax

def plot_violin(data, ax):
    sns.violinplot(data=data, x="cups", y="prductivity", hue="cups", ax=ax, inner="quartile", cut=0, density_norm='width', palette="Greens", linewidth=0.8, legend=False)

def define_models(X, Y):
    x_min, x_max = float(np.min(X)), float(np.max(X))
    y_min, y_max = float(np.min(Y)), float(np.max(X))
    dy = max(1e-8, y_max - y_min)

    MODELS = [
        {"name": "quadratic", "p0": [y_min, 0.0, 0.01], "bounds": (-np.inf, np.inf), "f": lambda xx, a0, a1, a2: a0 + a1 * xx + a2 * xx ** 2},
        {"name": "saturating", "p0": [dy, max(1.0, 0.2 * (x_min + x_max)), y_min], "bounds": ([-np.inf, 0.0, -np.inf], [np.inf, np.inf, np.inf]), "f": lambda xx, Vmax, K, y0: y0 + Vmax * (xx / np.maximum(K + xx, 1e-9))},
        {"name": "logistic", "p0": [dy, 0.5, 0.5 * (x_min + x_max), y_min], "bounds": ([-np.inf, 0.0, -np.inf, -np.inf], [np.inf, np.inf, np.inf, np.inf]), "f": lambda xx, L, k, x0, y0: y0 + L / (1.0 + np.exp(-k * (xx - x0)))},
        {"name": "peak", "p0": [max(y_min, y_max), max(1.0, 0.5 * (x_min + x_max))], "bounds": ([-np.inf, 0.0], [np.inf, np.inf]), "f": lambda xx, a, b: a * xx * np.exp(-xx / np.maximum(b, 1e-9))},
        {"name": "peak2", "p0": [max(1e-6, y_max / max(1.0, x_max ** 2)), max(1.0, 0.5 * (x_min + x_max))], "bounds": ([-np.inf, 0.0], [np.inf, np.inf]), "f": lambda xx, a, b: a * (xx ** 2) * np.exp(-xx / np.maximum(b, 1e-9))},
    ]
    return MODELS

def fit_models(MODELS, X, Y):
    fits = []
    for m in MODELS:
        popt, _ = curve_fit(m["f"], X, Y, p0=m["p0"], bounds=m["bounds"], maxfev=20000)
        yhat = m["f"](X, *popt)
        ss_res = float(np.sum((Y - yhat) ** 2))
        ss_tot = float(np.sum((Y - np.mean(Y)) ** 2))
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
        fits.append({"name": m["name"], "func": m["f"], "params": popt, "r2": r2})
    return fits

def sort_fits(fits):
    fits.sort(key=lambda d: (d["r2"] if np.isfinite(d["r2"]) else -np.inf), reverse=True)
    return fits

def plot_fits(fits, ax, X):
    x_smooth = np.linspace(np.min(X), np.max(X), 300)
    for idx, res in enumerate(fits):
        y_s = res["func"](x_smooth, *res["params"])
        label = f"{res['name']} (R²={res['r2']:.3f})"
        ax.plot(x_smooth, y_s, lw=2, label=label)

def save_plot(fig, out_path):
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.show()

def main():
    data, X, Y = load_data("coffees_productivity.csv")
    fig, ax = setup_plot()
    plot_violin(data, ax)
    MODELS = define_models(X, Y)
    fits = fit_models(MODELS, X, Y)
    fits = sort_fits(fits)
    plot_fits(fits, ax, X)
    ax.legend()
    ax.set_ylim(-0.2, 8)
    out_path = Path(__file__).with_name("fit_plot.png")
    save_plot(fig, out_path)

if __name__ == "__main__":
    main()
```

## CODE 2
```python
import os
import shutil

folder_name = input("Enter the folder name: ")
prefix = input("Enter the string to prepend to the filename: ")
text = toUpperCase(prefix)
if  not os.path.isdir(folder_name):
    print("Folder does not exist.")
    exit(1)
files = os.listdir(folder_name)
for file in files:
      new_filename = f"{text}_{file}"

shutil.move(os.path.join(folder_name, file),
os.path.joi(folder_name, new_file_name))

print("Files renamed successfully.")
```
