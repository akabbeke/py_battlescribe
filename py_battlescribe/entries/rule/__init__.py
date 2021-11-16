from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter
from ...bs_reference.child import BSReferenceChild
from ...bs_reference.link import BSReferenceLink



class Rule(BSNode):
    _tag_name = 'rule'

    description = BSReferenceChild('Description')
    modifiers = BSReferenceChild('Modifiers')

    # Fields
    name = BSNodeField('name')
    node_id = BSNodeField('id')
    publication_id = BSNodeField('publicationId')
    hidden = BSNodeField('hidden')
    page = BSNodeField('page')


class Rules(BSNodeIterable):
    _tag_name = 'rules'

    _link_type = BSReferenceLink('InfoLinks')

    _iter_child_class = BSReferenceIter('Rule')
