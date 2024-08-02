import numpy as np
from scipy.stats import skew, kurtosis

def statistical_moments(data):
    n = len(data)
    std_dev = np.std(data, ddof=1)
    variance = np.var(data, ddof=1)
    coefficient_variation = std_dev / np.mean(data)
    sem = np.std(data, ddof=1) / np.sqrt(n)
    skewness = skew(data)
    se_skewness = np.sqrt(6 / n)
    excess_kurtosis = kurtosis(data)
    se_kurtosis = np.sqrt(24 / n)

    return std_dev, variance, coefficient_variation, sem, skewness, se_skewness, excess_kurtosis, se_kurtosis

if __name__ == "__main__":
    data = np.random.normal(loc=0, scale=1, size=2040)
    results = statistical_moments(data)
    print("Стандартное отклонение:", results[0])
    print("Дисперсия:", results[1])
    print("Коэффициент вариации:", results[2])
    print("Стандартная ошибка среднего:", results[3])
    print("Асимметрия:", results[4])
    print("Стандартная ошибка асимметрии:", results[5])
    print("Эксцесс:", results[6])
    print("Стандартная ошибка эксцесса:", results[7])
