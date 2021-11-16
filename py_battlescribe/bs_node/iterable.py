from typing import Dict, List, Type, TypeVar

from . import BSNode
from ..bs_reference.iter import BSReferenceIter


class BSNodeIterable(BSNode):
    """A representation of an iterable node in the battlescribe XML tree.

    Parameters
    ----------
    xml_node : xml.etree.ElementTree.Element
        The exml node

    namespaces : Dict[str, str]
        The namespaces mapping for the XML element

    prefix : str
        The namespace prefix for the XML element

    node_registry : NodeRegistry
        The node registry being used to track the nodes ID

    parent : BSNode
        The parent to this node. If it is none then this is the root

    link_field_name : str
        The name of the field on the parent class to search for linked nodes in

    Attributes
    ----------
    _tag_name : str
        The name of the XML node tag for the class

    _link_type : BSReferenceLink
        The itterable link type that contains links to this node type

    _iter_child_class: BSReferenceIter
        The type class of the iterable children
    """

    _tag_name = 'bsNodeIterable'

    _link_type = None

    _iter_child_class = BSReferenceIter('BSNode')

    def __init__(self, *args, **kwargs):
        self._iter_items = []
        self._link_target_items = None
        super().__init__(*args, **kwargs)

    def __iter__(self):
        return iter(self._iter_items + self._link_targets)

    @property
    def _link_targets(self):
        if not self._link_target_items:
            self._link_target_items = self._fetch_links()
        return self._link_target_items

    def _fetch_links(self):
        # Check if a link type is specified
        if self._link_type is None:
            return []
        # Check if the parent has the matching link type
        link_iter = self._parent.get_child_by_type(self._link_type.type_class())
        if link_iter is None:
            return []
        # If there is a match then fetch all links of the correct type
        raw_targets = link_iter.get_links_of_type(self._iter_child_class.type_class())
        return [x for x in raw_targets]

    def __getitem__(self, item_index: int):
        return self._iter_items[item_index]

    def __len__(self):
        return len(self._iter_items + self._link_targets)

    def _init_children(self):
        super()._init_children()
        iter_child_class = self._iter_child_class.type_class()
        if self._xml_node is not None:
            for child_node in self.findall(iter_child_class.tag_name()):
                self._iter_items.append(iter_child_class(
                    xml_node=child_node,
                    namespaces=self._namespaces,
                    prefix=self._prefix,
                    node_registry=self._node_registry,
                    parent=self,
                ))

    def to_dict(self) -> List[dict]:
        """Return a list of dictionary representations of the child nodes"""
        return [x.to_dict() for x in self]

    def concatenate(self, other):
        """Concatenate the list of items

        Parameters
        ----------
        other : list
            The list of other items
        """
        for item in other:
            if isinstance(item, self._iter_child_class.type_class()):
                self._iter_items.append(item)
            else:
                raise ValueError(f'{item} is not {self._iter_child_class.type_class()}')

