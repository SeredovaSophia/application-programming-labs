import cv2

import matplotlib.pyplot as plt
import pandas as pd

def create_data_frame(annotation: str) -> pd.DataFrame:
    """
    Создает DataFrame из файла аннотации.
    :param annotation: Путь к файлу аннотации
    :return: DataFrame
    """
    df = pd.read_csv(annotation)
    df.columns=['relative_path', 'absolute_path']
    return df

def add_columns(df: pd.DataFrame) -> None:
    """
    Добавляет столбцы высоты, ширины и количества каналов изображения.
    :param df: DataFrame
    """
    height = []
    width = []
    channels = []

    for i in df['absolute_path']:
        img = cv2.imread(i)
        height.append(img.shape[0])
        width.append(img.shape[1])
        channels.append(img.shape[2])

    df['height'] = height
    df['width'] = width
    df['channels'] = channels


def compute_stat_info(df: pd.DataFrame) -> None:
    """
    Вычисляет и выводит статистическую информацию.
    :param df: DataFrame
    """
    stat = df[['height', 'width', 'channels']].describe()
    print(stat)

def filter_h_w(df: pd.DataFrame, max_h: int, max_w: int) -> pd.DataFrame:
    """
    Фильтрует DataFrame по максимальной высоте и ширине изображения.
    :param df: DataFrame
    :param max_h: максимальная высота
    :param max_w: максимальная ширина
    :return: новый DataFrame
    """
    new_df = df[(df['height'] <= max_h) & (df['width'] <= max_w)]
    return new_df

def add_area_col(df: pd.DataFrame) -> None:
    """
    Добавляет столбец с площадью изображений.
    :param df: DataFrame
    """
    df['area'] = df['height'] * df['width']

def sort_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Сортирует DataFrame по площади изображений (от меньшего к большему).
    :param df: DataFrame
    :return: новый DataFrame
    """
    return df.sort_values('area')

def create_hist(df: pd.DataFrame) -> None:
    """
    Создает гистограмму распределения площадей изображений.
    :param df: DataFrame
    """
    plt.figure()
    df['area'].hist()
    plt.title('Histogram by area')
    plt.xlabel('Area')
    plt.ylabel('Number of images')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()