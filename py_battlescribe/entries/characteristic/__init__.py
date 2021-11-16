from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter

class Characteristic(BSNode):
    _tag_name = 'characteristic'

    # Fields
    name = BSNodeField('name')
    type_id = BSNodeField('typeId')

    def to_dict(self):
        return {
            **super().to_dict(),
            'value': self._xml_node.text if self._xml_node is not None else None,
        }

    @property
    def value(self):
        return self._xml_node.text if self._xml_node is not None else None

class Characteristics(BSNodeIterable):
    _tag_name = 'characteristics'

    _iter_child_class = BSReferenceIter('Characteristic')
