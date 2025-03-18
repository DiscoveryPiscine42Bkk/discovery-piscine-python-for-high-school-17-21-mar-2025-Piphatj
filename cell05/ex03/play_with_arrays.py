#!/usr/bin/env python3
#  play_with_arrays.py
import numpy as np
ar = np.array([2, 8, 9, 48, 8, 22, -12, 2])
newar = ar[ar>5]
newar1 = np.array(newar +2)
unique_ar = set(newar1)
print(ar.tolist())
print(unique_ar)