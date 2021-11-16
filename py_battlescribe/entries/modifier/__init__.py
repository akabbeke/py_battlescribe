from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter
from ...bs_reference.child import BSReferenceChild


class Modifier(BSNode):
    _tag_name = 'modifier'

    # References
    conditions = BSReferenceChild('Conditions')
    repeats = BSReferenceChild('Repeats')
    condition_groups = BSReferenceChild('ConditionGroups')

    # Fields
    field = BSNodeField('field')
    value = BSNodeField('value')
    node_type = BSNodeField('type')

class Modifiers(BSNodeIterable):
    _tag_name = 'modifiers'

    _iter_child_class = BSReferenceIter('Modifier')
