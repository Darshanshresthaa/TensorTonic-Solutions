import numpy as np

def expected_value_discrete(x, p):
    if not np.allclose(np.sum(p), 1):
        raise ValueError

    x = np.vstack(x)
    p = np.vstack(p)

    expected_value = np.sum(x * p)

    return np.float32(expected_value)