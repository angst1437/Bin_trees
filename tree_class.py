from node_class import *

class Tree:
    def __init__(self):
        """
        При создании дерева у него есть:
            Указатель на корень
        """
        self.root = None

    def add_vertex(self, key) -> None:
        """Добавление вершины(ноды) в дерево"""

        # случай, когда дерево пустое (вершина добавляется как корень)
        if self.root is None:
            self.root = Node(key)

        #случай, когда дерево непустое
        else:
            is_node_added = False
            curr_node = self.root
            # циклом обходим дерево, пока не найдем подходящее место
            while not is_node_added:
                if key < curr_node.get_key(): # спускаемся влево

                    if not curr_node.is_child_exsist()[0]: # если у ноды нет левого ребенка, задаем его
                        curr_node.set_child(Node(key), is_greater=False)
                        is_node_added = True # выходим из цикла

                    else: # если у ноды есть левый ребенок, то идем дальше
                        curr_node = curr_node.get_child(is_greater=False)

                else: # спускаемся вправо

                    if not curr_node.is_child_exsist()[1]: # если у ноды нет правого ребенка, задаем его
                        curr_node.set_child(Node(key), is_greater=True)
                        is_node_added = True

                    else: # если у ноды есть правый ребенок, то идем дальше
                        curr_node = curr_node.get_child(is_greater=True)

    def find_key(self, key) -> Node or None:
        """
        Функция по поиску ноды по ключу.
        Возвращает ноду, если такой ключ есть.
        Возвращает None, если такого ключа в дереве нету.
        """
        is_key_found = False
        curr_node = self.root

        while not is_key_found:
            if curr_node.get_key() == key:
                return curr_node

            else:
                if key > curr_node.get_key():
                    curr_node = curr_node.get_child(is_greater=True)
                    if curr_node is None:
                        return None
                elif key < curr_node.get_key():
                    curr_node = curr_node.get_child(is_greater=False)
                    if curr_node is None:
                        return None
        return None


    def find_next(self, key) -> Node or None:
        """
        Ищет ближайшую большую по ЗНАЧЕНИЮ вершину.
        Возвращает None, если такого значения нету.
        """
        is_next_found = False
        counter = 1
        # Counter означает то, насколько больше мы ищем значение.
        # Если ноды с key + 1 не были найдены, то ищем key + 2
        # и так пока не найдем ближайшую вершину,
        # либо key + counter не станет выше максимального значения в дереве
        while not is_next_found:
            if (key + counter) > self.max().get_key():
                return None

            res = self.find_key(key + counter)
            # если find_keye возвратило None, поиск продолжается,
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

    def delete(self, key) -> None:
        """
        Функция удаляет ноду из дерева по ЗНАЧЕНИЮ
        Всего есть 3 случая:
            1. У ноды нет детей => нода просто удаляется(у родителя удаляется ссылка на эту ноду, удаляется ключ)
            2. У ноды один ребенок => нода удаляется, наследник(вместе со своим "хвостом") встает на её место
            3. У ноды 2 ребенка => ищем find_next(), удаляем ноду, подставляя значение find_next() вместо нее.
                Если у ноды, найденной find_next() есть наследники, то рекурсивно применяем delete
        """
        node = self.find_key(key)

        if node is None:
            return None

        parent = node.get_parent()

        # случай 1 ---------------------------------------------------------------------------
        if not all(node.is_child_exsist()):
            if node.get_key() >= parent.get_key():
                parent.set_child(None, is_greater=True)
            else:
                parent.set_child(None, is_greater=False)
            return

        # случай 2 ----------------------------------------------------------------------------
        elif node.is_child_exsist()[0] != node.is_child_exsist()[1]:
            # существует только правый наследник
            if node.is_child_exsist()[1]:
                if node.get_key() >= parent.get_key():
                    parent.set_child(node.get_child(is_greater=True), is_greater=True)
                    node.set_child(None, is_greater=True)
                    self.delete(node.get_key())
                else:
                    parent.set_child(node.get_child(is_greater=True), is_greater=False)
                    node.set_child(None, is_greater=True)
                    self.delete(node.get_key())

            # существует только левый наследник
            elif node.is_child_exsist()[0]:
                if node.get_key() >= parent.get_key():
                    parent.set_child(node.get_child(is_greater=False), is_greater=True)
                    node.set_child(None, is_greater=True)
                    self.delete(node.get_key())
                else:
                    parent.set_child(node.get_child(is_greater=False), is_greater=False)
                    node.set_child(None, is_greater=True)
                    self.delete(node.get_key())

        # случай 3 --------------------------------------------------------------------
        elif all(node.is_child_exsist()):
            nxt = self.find_next(key)
            self.delete(nxt.get_key())
            node.set_key(nxt.get_key())
            node.set_key(nxt.get_key())


    def sorting(self) -> list:
        pass

    def get_height(self, node=None):  # node указывает на узел дерева, высоту которого надо найти
        if node is None:  # если node = None, то начинаем с root
            if self.root is None:
                return -1
            else:
                node = self.root

        # Здесь определяются левые и правые дочерние узлы текущего узла
        left_child = node.get_child(is_greater=False)
        right_child = node.get_child(is_greater=True)

        '''
        -1 вместо 0 учитывает, что в случае отсутствия дочернего узла высота текущего поддерева должна быть на единицу 
        меньше, чем если бы узел был (так как в бинарных деревьях высота пустого поддерева обычно считается -1)
        '''

        if left_child is not None:
            left_height = self.get_height(left_child)
        else:
            left_height = -1

        if right_child is not None:
            right_height = self.get_height(right_child)
        else:
            right_height = -1

        # Прибавляем 1, чтобы учесть текущий узел
        return max(left_height, right_height) + 1
