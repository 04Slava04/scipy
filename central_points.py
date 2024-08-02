import numpy as np
from scipy import stats

def central_points(data):
    mean_arithmetic = np.mean(data)
    mean_geometric = stats.gmean(data[data > 0])  # Геометрическое среднее, только для положительных значений
    mean_harmonic = stats.hmean(data[data > 0])   # Гармоническое среднее, только для положительных значений
    median = np.median(data)
    mode_result = stats.mode(data)

    # Проверка, является ли mode_result.mode массивом и имеет ли он элементы
    if isinstance(mode_result.mode, np.ndarray) and mode_result.mode.size > 0:
        mode = mode_result.mode[0]
    else:
        mode = None  # Если нет элементов, устанавливаем mode в None

    return mean_arithmetic, mean_geometric, mean_harmonic, median, mode

if __name__ == "__main__":
    data = np.random.normal(loc=0, scale=1, size=2040)
    mean_arithmetic, mean_geometric, mean_harmonic, median, mode = central_points(data)
    print("Среднее арифметическое:", mean_arithmetic)
    print("Среднее геометрическое:", mean_geometric)
    print("Среднее гармоническое:", mean_harmonic)
    print("Медиана:", median)
    print("Мода:", mode)
