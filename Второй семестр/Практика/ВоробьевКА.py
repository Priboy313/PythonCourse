# SimpleAnalysis
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr


def get_series() -> pd.Series:
	"""Создание объекта Series"""
	_series = []
	for i in range(1000):
		_series.append(random.randint(-300, 300))
	
	return pd.Series(_series)


def set_series_graph(series:pd.Series) -> None:
	"""Построение графика объекта series"""
	_line = series.plot(kind="line", title="series_line")


def set_series_histogram(series:pd.Series) -> None:
	"""Построение гистограммы объекта series"""
	_rounded_series = np.ceil(series / 100) * 100
	_hist = _rounded_series.plot(kind="hist", title="series_hist")
	_hist.xaxis.set_major_locator(tkr.MultipleLocator(500))
	_hist.xaxis.set_minor_locator(tkr.MultipleLocator(200))
	_hist.set_xlim([-300, 300])


def get_dataframe(series:pd.Series) -> pd.DataFrame:
	"""Создание объекта dataframe"""
	_dataframe = pd.DataFrame({"Series": series})
	_dataframe["Ascending"] = series.sort_values(ascending=True, ignore_index=True)
	_dataframe["Descending"] = series.sort_values(ascending=False, ignore_index=True)
	
	return _dataframe


def set_dataframe_graph(dataframe:pd.DataFrame) -> None:
	"""Построение графика объекта dataframe"""
	_line = dataframe.drop(["Series"], axis=1).plot(kind="line", title="dataframe_line")


def main():
	# Получение объекта series
	series = get_series()

	# Рассчёт стандартных характеристик объекта series
	series_min = min(series)
	series_max = max(series)
	series_repeats = len(series) - len(series.unique())
	series_sum = sum(series)
	series_rms = np.std(series)
	print(
		f"Минимальное значение series: {series_min}\n"
		f"Максимальное значение series: {series_max}\n"
		f"Повторияющихся значений в series: {series_repeats}\n"
		f"Сумма значений series: {series_sum}\n"
		f"Среднеквадратическое отклонение series: {series_rms}\n"
		)
	
	# Построение графика объекта series
	set_series_graph(series)
	plt.show()

	# Построоение гистограммы объекта series
	set_series_histogram(series)
	plt.show()

	# Формирование объекта dataframe
	dataframe = get_dataframe(series)
	
	# Построение графика dataframe
	set_dataframe_graph(dataframe)
	plt.show()


if __name__ == "__main__":
	main()




