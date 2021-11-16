from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter


class Repeat(BSNode):
    _tag_name = 'repeat'

    # Fields
    child_id = BSNodeField('childId')
    field = BSNodeField('field')
    include_child_forces = BSNodeField('includeChildForces')
    include_child_selections = BSNodeField('includeChildSelections')
    percent_value = BSNodeField('percentValue')
    repeats = BSNodeField('repeats')
    round_up = BSNodeField('roundUp')
    scope = BSNodeField('scope')
    shared = BSNodeField('shared')
    value = BSNodeField('value')


class Repeats(BSNodeIterable):
    _tag_name = 'repeats'

    _iter_child_class = BSReferenceIter('Repeat')
