# Файл с классом TreeStore (некоторые наименования были изменены в соответствии с соглашением PEP8)

class TreeStore:
    """
    Класс для работы с массивом (списком) объектов.
    """
    def __init__(self, items):
        """
        Конструктор класса
        :param items: массив (список) объектов
        """
        self.items = items
        self.mapping_for_id = {item['id']: item for item in items}  # маппинг для объектов по id
        self.children_mapping = {}

        # Маппинг для дочерних элементов
        for item in items:
            parent_id = item['parent']
            if parent_id not in self.children_mapping:
                self.children_mapping[parent_id] = []
            self.children_mapping[parent_id].append(item)

    def get_all(self):
        """
        Метод для получения начального массива (списка)
        :return: начальный массив (список) объектов
        """
        return self.items

    def get_item(self, id_):
        """
        Метод для получения объекта по id
        :param id_: id объекта
        :return: объект
        """
        return self.mapping_for_id.get(id_)

    def get_children(self, id_):
        """
        Метод для получения массива (списка) элементов, для которых является родителем объект с заданным id
        :param id_: id родительского объекта
        :return: массив (списко) объектов, для которых parent_id = id
        """
        return self.children_mapping.get(id_, [])

    def get_all_parents(self, id_):
        """
        Метод для получения цепочки родительских элементов для объекта
        с заданным id (начиная от самого элемента, чей id был передан)
        :param id_: id бъекта
        :return: массив (список) цепочки родительских элементов
        """
        parents = []
        current_id = id_

        # Перебираем объекты, пока не наткнёмся на родителя 'root'
        while current_id != "root":
            item = self.mapping_for_id.get(current_id)
            if item:
                # Добавляем родителя в цепочку
                parents.append(item)
                current_id = item['parent']
            else:
                break

        return parents
