import numpy as np
from scipy.stats import t, chi2

def confidence_intervals(data, confidence_level=0.95):
    n = len(data)
    mean_arithmetic = np.mean(data)
    variance = np.var(data, ddof=1)
    sem = np.std(data, ddof=1) / np.sqrt(n)
    alpha = 1 - confidence_level
    ci_mean = t.interval(confidence_level, df=n-1, loc=mean_arithmetic, scale=sem)
    
    chi_l, chi_u = chi2.ppf([alpha / 2, 1 - alpha / 2], df=n - 1)
    ci_variance = ((n - 1) * variance / chi_u, (n - 1) * variance / chi_l)

    return ci_mean, ci_variance

if __name__ == "__main__":
    data = np.random.normal(loc=0, scale=1, size=2040)
    ci_mean, ci_variance = confidence_intervals(data)
    print(f"Доверительный интервал для среднего арифметического при 95%:", ci_mean)
    print(f"Доверительный интервал для дисперсии при 95%:", ci_variance)
