from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter


class CharacteristicType(BSNode):
    _tag_name = 'characteristicType'

    # Fields
    name = BSNodeField('name')
    node_id = BSNodeField('id')


class CharacteristicTypes(BSNodeIterable):
    _tag_name = 'characteristicTypes'

    _iter_child_class = BSReferenceIter('CharacteristicType')