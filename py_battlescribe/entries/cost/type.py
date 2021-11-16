from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter


class CostType(BSNode):
    _tag_name = 'costType'

    # Fields
    name = BSNodeField('name')
    default_cost_limit = BSNodeField('defaultCostLimit')
    node_id = BSNodeField('id')


class CostTypes(BSNodeIterable):
    _tag_name = 'costTypes'

    _iter_child_class = BSReferenceIter('CostType')
