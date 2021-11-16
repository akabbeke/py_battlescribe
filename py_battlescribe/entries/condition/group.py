from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_reference.child import BSReferenceChild
from ...bs_reference.iter import BSReferenceIter
from ...bs_node.iterable import BSNodeIterable


class ConditionGroup(BSNode):
    _tag_name = 'conditionGroup'

    # References
    constraints = BSReferenceChild('Conditions')
    modifiers = BSReferenceChild('ConditionGroups')

    # Fields
    node_type = BSNodeField('type')


class ConditionGroups(BSNodeIterable):
    _tag_name = 'conditionGroups'

    _iter_child_class = BSReferenceIter('ConditionGroup')
