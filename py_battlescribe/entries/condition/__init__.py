from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter


class Condition(BSNode):
    _tag_name = 'condition'

    # Fields
    child_id = BSNodeField('childId')
    field = BSNodeField('field')
    include_child_forces = BSNodeField('includeChildForces')
    include_child_selections = BSNodeField('includeChildSelections')
    percent_value = BSNodeField('percentValue')
    scope = BSNodeField('scope')
    shared = BSNodeField('shared')
    node_type = BSNodeField('type')
    value = BSNodeField('value')


class Conditions(BSNodeIterable):
    _tag_name = 'conditions'

    _iter_child_class = BSReferenceIter('Condition')
