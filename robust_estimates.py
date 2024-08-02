import numpy as np
from scipy.stats import trim_mean, mstats

def robust_estimates(data, iqr_factor=1.5):
    n = len(data)
    mean_arithmetic = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data, ddof=1)
    iqr = np.percentile(data, 75) - np.percentile(data, 25)

    trimmed_mean = trim_mean(data, proportiontocut=0.1)
    winsorized_mean = mstats.winsorize(data, limits=0.1).mean()
    outlier_bounds_iqr = (median - iqr_factor * iqr, median + iqr_factor * iqr)
    outlier_bounds_sd = (mean_arithmetic - iqr_factor * std_dev, mean_arithmetic + iqr_factor * std_dev)

    filtered_data_iqr = data[(data >= outlier_bounds_iqr[0]) & (data <= outlier_bounds_iqr[1])]
    mean_without_outliers_iqr = np.mean(filtered_data_iqr)

    filtered_data_sd = data[(data >= outlier_bounds_sd[0]) & (data <= outlier_bounds_sd[1])]
    mean_without_outliers_sd = np.mean(filtered_data_sd)

    return trimmed_mean, winsorized_mean, outlier_bounds_iqr, outlier_bounds_sd, mean_without_outliers_iqr, mean_without_outliers_sd

if __name__ == "__main__":
    data = np.random.normal(loc=0, scale=1, size=2040)
    results = robust_estimates(data)
    print("Усеченное среднее:", results[0])
    print("Винсоризированное среднее:", results[1])
    print("Границы выбросов (медиана +/- IQR):", results[2])
    print("Границы выбросов (среднее +/- стандартное отклонение):", results[3])
    print("Среднее без выбросов (IQR):", results[4])
    print("Среднее без выбросов (стандартное отклонение):", results[5])
