import numpy as np


def scale(values: list[float], factor: float) -> list[float]:
    return [v * factor for v in values]


result = scale([1.0, 2.0, 3.0], 2.0)
print(np.array(result).mean())
