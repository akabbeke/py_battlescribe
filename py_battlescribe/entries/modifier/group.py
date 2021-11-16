from ...bs_node import BSNode
from ...bs_reference.child import BSReferenceChild
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter


class ModifierGroup(BSNode):
    _tag_name = 'modifierGroup'

    # References
    conditions = BSReferenceChild('Conditions')
    modifiers = BSReferenceChild('Modifiers')
    condition_groups = BSReferenceChild('ConditionGroups')


class ModifierGroups(BSNodeIterable):
    _tag_name = 'modifierGroups'

    _iter_child_class = BSReferenceIter('ModifierGroup')
