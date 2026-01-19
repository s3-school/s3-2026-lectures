#!/usr/bin/env python3

#!/usr/bin/env python3
"""
Show a report:
   python mem.py

Make a graph:
   mprof run python mem.py
   mprof plot
"""

import numpy as np
import time
from memory_profiler import profile


@profile
def main():
    N = 10_000
    X = np.arange(N)
    Y = np.linspace(-5, 5, N)
    time.sleep(0.5)
    A = X + Y
    B = (X**2 + Y) / A
    Z = B + A[..., np.newaxis]
    time.sleep(0.5)
    C = Z**2 + 1
    time.sleep(0.5)


if __name__ == "__main__":
    main()
