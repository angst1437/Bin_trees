from node_class import *

class Tree:
    def __init__(self):
        """
        При создании дерева у него есть:
            Указатель на корень
            список ключей
        """
        self.root = None
        self.keylist = []

    def add_vertex(self, value) -> None:
        """Добавление вершины(ноды) в дерево"""

        # случай, когда дерево пустое (вершина добавляется как корень)
        if self.root is None:
            self.root = Node(value, key=1)
            self.keylist.append(1)

        #случай, когда дерево непустое
        else:
            is_node_added = False
            curr_node = self.root
            # циклом обходим дерево, пока не найдем подходящее место
            while not is_node_added:
                if value < curr_node.get_value(): # спускаемся влево

                    if not curr_node.is_child_exsist()[0]: # если у ноды нет левого ребенка, задаем его
                        # ниже мы задаем ключ новой вершины как максимальный ключ из дерева + 1
                        key = max(self.keylist) + 1
                        curr_node.set_child(Node(value, key), is_greater=False)
                        self.keylist.append(key)
                        is_node_added = True # выходим из цикла

                    else: # если у ноды есть левый ребенок, то идем дальше
                        curr_node = curr_node.get_child(is_greater=False)

                else: # спускаемся вправо

                    if not curr_node.is_child_exsist()[1]: # если у ноды нет правого ребенка, задаем его
                        key = max(self.keylist) + 1
                        curr_node.set_child(Node(value, key), is_greater=True)
                        self.keylist.append(key)
                        is_node_added = True

                    else: # если у ноды есть правый ребенок, то идем дальше
                        curr_node = curr_node.get_child(is_greater=True)

    def find_key(self, key) -> Node or None:
        """
        Функция по поиску ноды по ключу.
        Возвращает ноду, если такой ключ есть.
        Возвращает None, если такого ключа в дереве нету.
        """

        if key not in self.keylist:
            return None

        is_key_found = False
        curr_node = self.root

        while not is_key_found:
            if curr_node.get_key() == key:
                return curr_node

            else:
                if key > curr_node.get_key():
                    curr_node = curr_node.get_child(is_greater=True)
                elif key < curr_node.get_key():
                    curr_node = curr_node.get_child(is_greater=False)
        return None

    def find_value(self, value) -> Node or None:
        """
        Функция по поиску ноды по значению.
        Возвращает ноду, если нода с таким значением есть.
        Возвращает None, если нода с таким значением нету.
        Если таких значений несколько, то возвращает самое близкое к корню.
        """

        is_node_found = False
        curr_node = self.root

        while not is_node_found:
            if curr_node.get_value() == value:
                return curr_node
            else:
                if value > curr_node.get_value():
                    curr_node = curr_node.get_child(is_greater=True)
                    if curr_node is None:
                        return None

                elif value < curr_node.get_value():
                    curr_node = curr_node.get_child(is_greater=False)
                    if curr_node is None:
                        return None


    def find_next(self, value) -> Node or None:
        """
        Ищет ближайшую большую по ЗНАЧЕНИЮ вершину.
        Возвращает None, если такого значения нету.
        """
        is_next_found = False
        counter = 1
        # Counter означает то, насколько больше мы ищем значение.
        # Если ноды с value + 1 не были найдены, то ищем value + 2
        # и так пока не найдем ближайшую вершину,
        # либо value + counter не станет выше максимального значения в дереве
        while not is_next_found:
            if (value + counter) > self.max().get_value():
                return None

            res = self.find_value(value + counter)
            # если find_value возвратило None, поиск продолжается,
            # в обратном же случае возвращаем ноду
            if res is not None:
                return res
            else:
                counter += 1




    def min(self) -> Node:
        """Возвращает минимальную по значению ноду в дереве"""
        curr_node = self.root

        while True:
            if curr_node.is_child_exsist()[0]:
                curr_node = curr_node.get_child(is_greater=False)
            else:
                minimum = curr_node
                return minimum

    def max(self) -> Node:
        """Возвращает максимальную по значению ноду в дереве"""
        curr_node = self.root

        while True:
            if curr_node.is_child_exsist()[1]:
                curr_node = curr_node.get_child(is_greater=True)
            else:
                maximum = curr_node
                return maximum

    def delete_value(self, value) -> None:
        """
        Функция удаляет ноду из дерева по ЗНАЧЕНИЮ
        Всего есть 3 случая:
            1. У ноды нет детей => нода просто удаляется(у родителя удаляется ссылка на эту ноду, удаляется ключ)
            2. У ноды один ребенок => нода удаляется, наследник(вместе со своим "хвостом") встает на её место
            3. У ноды 2 ребенка => ищем find_next(), удаляем ноду, подставляя значение find_next() вместо нее.
                Если у ноды, найденной find_next() есть наследники, то рекурсивно применяем delete
        """
        node = self.find_value(value)

        if node is None:
            return None

        parent = node.get_parent()

        # случай 1 ---------------------------------------------------------------------------
        if not all(node.is_child_exsist()):
            if node.get_value() >= parent.get_value():
                parent.set_child(None, is_greater=True)
                self.keylist.remove(node.get_key())
            else:
                parent.set_child(None, is_greater=False)
                self.keylist.remove(node.get_key())
            return

        # случай 2 ----------------------------------------------------------------------------
        elif node.is_child_exsist()[0] != node.is_child_exsist()[1]:
            # существует только правый наследник
            if node.is_child_exsist()[1]:
                if node.get_value() >= parent.get_value():
                    parent.set_child(node.get_child(is_greater=True), is_greater=True)
                    node.set_child(None, is_greater=True)
                    self.delete_value(node.get_value())
                    self.keylist.remove(node.get_key())
                else:
                    parent.set_child(node.get_child(is_greater=True), is_greater=False)
                    node.set_child(None, is_greater=True)
                    self.delete_value(node.get_value())

            # существует только левый наследник
            elif node.is_child_exsist()[0]:
                if node.get_value() >= parent.get_value():
                    parent.set_child(node.get_child(is_greater=False), is_greater=True)
                    node.set_child(None, is_greater=True)
                    self.delete_value(node.get_value())
                else:
                    parent.set_child(node.get_child(is_greater=False), is_greater=False)
                    node.set_child(None, is_greater=True)
                    self.delete_value(node.get_value())

        # случай 3 --------------------------------------------------------------------
        elif all(node.is_child_exsist()):
            nxt = self.find_next(value)
            self.delete_value(nxt.get_key())
            node.set_key(nxt.get_key())
            node.set_value(nxt.get_value())
            self.keylist.remove(node.get_key())
