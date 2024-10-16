class Node:
    def __init__(self, value, key=None):
        """
            Создание ноды(вершины) дерева. При создании у нее есть:
                Уникальный ключ
                Не уникальное значение
                Указатели на детей, родителя.
            Обязательно при создании указывать только значение
        """
        self.key = key
        self.value = value
        self.parent = None
        self.right_child = None
        self.left_child = None

    def get_child(self, is_greater) -> 'Node' or None:
        """
        Получаем указатель на ребенка. При is_greater=True получаем правого ребенка,
        соответственно для is_greater=False левого.
        Если ребенка нету, то возвращает None.
        """
        if is_greater and self.right_child is not None:
            return self.right_child
        elif not is_greater and self.left_child is not None:
            return self.left_child
        else:
            return None

    def get_parent(self) -> 'Node':
        return self.parent

    def get_key(self) -> int:
        return self.key

    def get_value(self) -> int:
        return self.value


    def set_key(self, key) -> None:
        self.key = key

    def set_value(self, value) -> None:
        self.value = value

    def set_parent(self, parent) -> None:
        self.parent = parent
        if self.value >= parent.value:
            parent.right_child = self
        else:
            parent.left_child = self

    def set_child(self, child, is_greater) -> None:
        """Задаем дочернюю ноду, is_greater работает как в get_child"""
        if is_greater:
            self.right_child = child
            if child is not None:
                child.parent = self
            return

        elif not is_greater:
            self.left_child = child  # связываем родителя и ребенка
            if child is not None:
                child.parent = self
            return

    def is_child_exsist(self) -> list:
        """
        Проверка на наличие детей.
        Возвращает список вида [левый_ребенок не None, правый_ребенок не None]
        """
        return [self.get_child(is_greater=False) is not None,
                self.get_child(is_greater=True) is not None]
