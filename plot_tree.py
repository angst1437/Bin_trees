def plot_node(key, parent_key, pos, parent_pos, ax):
    ax.text(pos[0], pos[1], str(key), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))

    if parent_key is not None:
        ax.plot([parent_pos[0], pos[0]], [parent_pos[1], pos[1]], 'k-')

def plot_binary_tree(ax, node, x=0.5, y=1.0, dx=0.25, dy=0.1, parent_pos=None):
    if node:
        plot_node(node.key, None if parent_pos is None else node.key, (x , y), parent_pos, ax)
        if node.left_child:
            plot_binary_tree(ax, node.left_child, x - dx, y - dy, dx / 2, dy, (x, y))
        if node.right_child:
            plot_binary_tree(ax, node.right_child, x + dx, y - dy, dx / 2, dy, (x, y))