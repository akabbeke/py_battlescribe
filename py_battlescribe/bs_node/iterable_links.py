from typing import Dict, List, Type, TypeVar

from .iterable import BSNodeIterable

class BSNodeIterableLinks(BSNodeIterable):
    """A representation of an iterable list of links

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
    def get_links_of_type(self, type_class):
        """Return the child object of type child_type

        Parameters
        ----------
        type_class : Type[BSNode]
            The link type to access
        """
        linked_targets = []
        for link in self._iter_items:
            target = link.target
            if isinstance(target, type_class):
                linked_targets.append(target)
        return linked_targets
