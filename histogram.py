import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def calc_histogram(img: np.ndarray) -> tuple:
    """
    Вычисляем гистограммы для трех цветовых каналов изображения.
    :param img: Цветное изображение в формате numpy.ndarray.
    :return: Кортеж из трех гистограмм (для синего, зеленого и красного каналов).
    """
    hist_b = cv.calcHist([img], [0], None, [256], [0, 256])
    hist_g = cv.calcHist([img], [1], None, [256], [0, 256])
    hist_r = cv.calcHist([img], [2], None, [256], [0, 256])
    return hist_b, hist_g, hist_r

def plot_histogram(hists: tuple) -> None:
    """
     Строим графики гистограмм для каждого цветового канала.
    :param hists: Кортеж из трех гистограмм (для синего, зеленого и красного каналов).
    """
    plt.figure()
    plt.plot(hists[0], color='blue', label='Синий канал')
    plt.plot(hists[1], color='green', label='Зеленый канал')
    plt.plot(hists[2], color='red', label='Красный канал')

    plt.title("Гистограммы цветового изображения")
    plt.xlabel("Яркость")
    plt.ylabel("Количество пикселей")
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim([0, 256])
    plt.legend()
    plt.show()