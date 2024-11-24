from downloader_img import download_images
from img_iterator import ImageIterator
from create_annotation import create_annotation
from a_parser import get_args

def main() -> None:
    """
    Функция обрабатывает аргументы и вызывает соответствующие функции для скачивания изображений,
    создания аннотации и итерации по изображениям.
    """
    keyword, number, imgdir, annotation_file = get_args()

    try:
        download_images(keyword, number, imgdir)
        create_annotation(imgdir, annotation_file)

        my_iterator = ImageIterator(annotation_file)
        for item in my_iterator:
            print(item)

    except Exception as e:
        print(f"Что-то пошло не так: {e}")


if __name__ == "__main__":
    main()
