from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.child import BSReferenceChild
from ...bs_reference.iter import BSReferenceIter


class ProfileType(BSNode):
    _tag_name = 'profileType'

    # References
    Characteristic_types = BSReferenceChild('CharacteristicTypes')

    # Fields
    node_id = BSNodeField('id')
    name = BSNodeField('name')


class ProfileTypes(BSNodeIterable):
    _tag_name = 'profileTypes'

    _iter_child_class = BSReferenceIter('ProfileType')
