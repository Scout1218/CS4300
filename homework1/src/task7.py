import numpy as np

def summarize(values: list[float]) -> dict[str, float]:
    """
    Calculate basic summary statistics (mean, median, standard deviation) for a list of values.

    Args:
        values (list[float]): A list of numeric values.

    Returns:
        dict[str, float]: A dictionary containing:
            - "mean": The arithmetic mean of the values.
            - "median": The median of the values.
            - "std": The population standard deviation of the values.
    """
    arr = np.asarray(values, dtype=float)
    return {
        "mean": float(np.mean(arr)),
        "median": float(np.median(arr)),
        "std": float(np.std(arr, ddof=0)),  # population std dev
    }