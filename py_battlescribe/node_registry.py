from collections import defaultdict

from .bs_node import BSNode



class NodeRegistry:
    """Acts as a registry of nodes and provides a mapping of node ids to nodes.

    Nodes mush be registered using the register method to be available.
    """
    def __init__(self):
        self._registry = {}
        self._type_registry = defaultdict(dict)
        self._category_registry = defaultdict(dict)

    def __getitem__(self, node_id: str) -> BSNode:
        return self._registry.get(node_id)

    def __setitem__(self, node_id: str, item: BSNode):
        self._registry[node_id] = item

    def get(self, node_id: str) -> BSNode:
        """Returns the BSNode with id, node_id. raises a KeyError
        if there is no match.

        Parameters
        ----------
        node_id : str
            The node_id for the target

        Returns
        -------
        BSNode
            The corresponding target
        """
        return self[node_id]

    def register(self, bs_node: BSNode):
        """Register the node with the registry
        if there is no match.

        Parameters
        ----------
        bs_node : BSNode
            The node to register
        """
        node_id = bs_node.attr.get('id')
        if node_id and node_id not in self._registry:
            self._registry[node_id] = bs_node
            self._type_registry[bs_node.__class__.__name__][node_id] = bs_node

            category_entries = getattr(bs_node, 'category_entries', None)
            if category_entries:
                for category in category_entries:
                    self._category_registry[category.node_id][node_id] = bs_node
