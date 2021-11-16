from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter
from ...bs_reference.child import BSReferenceChild

class Cost(BSNode):
    _tag_name = 'cost'

    # References
    costs = BSReferenceChild('Costs')

    # Fields
    name = BSNodeField('name')
    value = BSNodeField('value')
    type_id = BSNodeField('typeId')


class Costs(BSNodeIterable):
    _tag_name = 'costs'

    _iter_child_class = BSReferenceIter('Cost')

