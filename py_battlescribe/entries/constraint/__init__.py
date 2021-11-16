from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter

class Constraint(BSNode):
    _tag_name = 'constraint'

    # Fields
    field = BSNodeField('field')
    node_id = BSNodeField('id')
    include_child_forces = BSNodeField('includeChildForces')
    include_child_selections = BSNodeField('includeChildSelections')
    percent_value = BSNodeField('percentValue')
    scope = BSNodeField('scope')
    shared = BSNodeField('shared')
    node_type = BSNodeField('type')
    value = BSNodeField('value')


class Constraints(BSNodeIterable):
    _tag_name = 'constraints'

    _iter_child_class = BSReferenceIter('Constraint')
