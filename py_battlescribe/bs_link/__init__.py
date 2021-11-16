from ..bs_node import BSNode

class BSLink(BSNode):
    """A representation of a link

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

    target_id : str
        The id of the link target
    """

    target_id = None

    @property
    def target(self) -> BSNode:
        """The target node"""
        return self._node_registry.get(self.target_id).copy()
