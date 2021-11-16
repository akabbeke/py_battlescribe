from __future__ import annotations

import json
import re
from collections import defaultdict
from copy import deepcopy
from xml.etree.ElementTree import Element

from time import sleep
from typing import Dict, TypeVar, Type, List

from timeit import default_timer as timer



class BSNode:
    """A representation of a node in the battlescribe XML tree.

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
    """

    _tag_name = 'bsNode'
    def __init__(self, xml_node: Element=None, namespaces: Dict[str, str]=None, prefix=None, node_registry=None, \
                 parent=None, link_field_name=None, is_copy=False):
        self._xml_node = xml_node
        self._namespaces = namespaces
        self._prefix = prefix
        self._node_registry = node_registry
        self._parent = parent
        self._link_field_name = link_field_name
        self._is_copy = is_copy

        self._set_attributes()
        self._init_children()
        if not is_copy:
            self._node_registry.register(self)

    def __bool__(self) -> bool:
        return self._xml_node is not None

    def __repr__(self) -> str:
        if self.attr.get('name'):
            return f'<{self.__class__.__name__} - {self.attr.get("name")}>'
        else:
            return f'<{self.__class__.__name__} - no_name>'

    def to_dict(self, include_links=False) -> dict:
        """Return a dictionary depresentaion of this node an all it's child nodes

        Parameters
        ----------
        include_links : bool
            if links should be included in the returned dictionary. By defualt they are
            not as the linked nodes are already included.
        """
        from ..bs_reference.child import BSReferenceChild
        from .iterable_links import BSNodeIterableLinks
        from .field import BSNodeField

        new_dict = {'__type__': self.__class__.__name__}
        for property_name, property_obj in self.__class__.__dict__.items():
            if isinstance(property_obj, BSReferenceChild):
                if self.__dict__.get(property_name) is not None:
                    if isinstance(self.__dict__.get(property_name), BSNodeIterableLinks) and not include_links:
                        continue
                    new_dict[property_name] = self.__dict__.get(property_name).to_dict()
                else:
                    new_dict[property_name] = None
            elif isinstance(property_obj, BSNodeField):
                new_dict[property_name] = self.__dict__.get(property_name)
        return new_dict

    @property
    def attr(self) -> dict:
        """Returns a dictionary representaion of the attributes on the node"""
        if self._xml_node is None:
            return {}
        return self._xml_node.attrib

    def _set_attributes(self):
        from .field import BSNodeField

        if self._xml_node is None:
            return
        for property_name, property_obj in self.__class__.__dict__.items():
            if isinstance(property_obj, BSNodeField):
                self.__dict__[property_name] = property_obj(self)

    def _init_children(self):
        from ..bs_reference.child import BSReferenceChild
        if self._xml_node is None:
            for property_name, property_obj in self.__class__.__dict__.items():
                if isinstance(property_obj, BSReferenceChild):
                    self.__dict__[property_name] = None
        else:
            for property_name, property_obj in self.__class__.__dict__.items():
                if isinstance(property_obj, BSReferenceChild):
                    child_class = property_obj.type_class()
                    self.__dict__[property_name] = child_class(
                        xml_node=self.find(child_class.tag_name()),
                        namespaces=self._namespaces,
                        prefix=self._prefix,
                        node_registry=self._node_registry,
                        parent=self,
                        is_copy=self._is_copy,
                    )

    def get_child_by_type(self, child_type: Type[BSNode]) -> BSNode:
        """Return the child object of type child_type

        Parameters
        ----------
        child_type : Type[BSNode]
            The child type to access
        """
        for property_name, property_obj in self.__dict__.items():
            if isinstance(property_obj, child_type) and not property_name.startswith('_'):
                return property_obj

    def copy(self, new_parent=None) -> BSNode:
        """Return a copy of this node. This can take some time is copying a node with many ancestors"""
        return self.__class__(
            xml_node=self._xml_node,
            namespaces=self._namespaces,
            prefix=self._prefix,
            node_registry=self._node_registry,
            parent= new_parent or self._parent,
            link_field_name=self._link_field_name,
            is_copy=True

        )

    def find(self, tag: str) -> Element:
        """Return the XML child element with matching tag"""
        if self._xml_node is not None:
            return self._xml_node.find(f'{self._prefix}:{tag}', namespaces=self._namespaces)

    def findall(self, tag: str) -> List[Element]:
        """Return a list of the XML child elements with matching tags"""
        if self._xml_node is not None:
            return self._xml_node.findall(f'{self._prefix}:{tag}', namespaces=self._namespaces)
        else:
            return []

    @classmethod
    def tag_name(cls) -> str:
        return cls._tag_name

    def pprint(self, depth=0):
        print(' ' * depth + f'{self}')



