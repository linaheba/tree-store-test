# Стартовый файл для запуска программы
import logging

from app import TreeStore, items

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        ts = TreeStore(items)
        all_ = ts.get_all()
        print(all_)
        get_item_ = ts.get_item(7)
        print(get_item_)
        get_children_ = ts.get_children(4)
        print(get_children_)
        get_children_ = ts.get_children(5)
        print(get_children_)
        get_all_parents_ = ts.get_all_parents(7)
        print(get_all_parents_)
    except Exception as error:
        logging.info(f'Произошла ошибка - {error}')
