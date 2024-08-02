import numpy as np

def ranges_percentiles(data):
    min_val = np.min(data)
    max_val = np.max(data)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    percentiles = np.percentile(data, [10, 50, 90])
    range_val = max_val - min_val
    iqr = q3 - q1

    return min_val, max_val, q1, q3, percentiles, range_val, iqr

if __name__ == "__main__":
    data = np.random.normal(loc=0, scale=1, size=2040)
    results = ranges_percentiles(data)
    print("Минимум:", results[0])
    print("Максимум:", results[1])
    print("Нижний квартиль (Q1):", results[2])
    print("Верхний квартиль (Q3):", results[3])
    print("Процентили (10%, 50%, 90%):", results[4])
    print("Размах (максимум - минимум):", results[5])
    print("Межквартильный размах (IQR):", results[6])
