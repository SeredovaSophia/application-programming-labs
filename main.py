import argparse

from data_frame import create_data_frame, add_columns, compute_stat_info, filter_h_w, add_area_col, sort_area, create_hist


def parse() -> tuple[str, int, int]:
    """
    Получает аргументы командной строки.
    :return: Кортеж с путём к аннотации, значения максимальных высоты и длины изображения
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('annotation_path', type=str, help='Input path to the annotation file')
    parser.add_argument('max_height', type=int, help='Input max height of image:')
    parser.add_argument('max_width', type=int, help='Input max width of image:')
    arguments = parser.parse_args()
    return arguments.annotation_path, arguments.max_height, arguments.max_width


def main():
    annotation_path, max_height, max_width = parse()

    try:
        data_frame = create_data_frame(annotation_path)
        print("DataFrame после создания:")
        print(data_frame)

        add_columns(data_frame)
        print("DataFrame после добавления столбцов:")
        print(data_frame)

        compute_stat_info(data_frame)

        add_area_col(data_frame)
        print("DataFrame после добавления столбца площади:")
        print(data_frame)

        filtered_data_frame = filter_h_w(data_frame, max_height, max_width)
        print("Отфильтрованный DataFrame:")
        print(filtered_data_frame)

        sorted_data_frame = sort_area(filtered_data_frame)
        print("Отсортированный DataFrame по площади:")
        print(sorted_data_frame)
        create_hist(data_frame)
        print("Гистограмма успешно создана.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__=="__main__":
    main()