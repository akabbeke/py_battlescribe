from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter
from ...bs_reference.link import BSReferenceLink
from ...bs_reference.child import BSReferenceChild
from ...bs_node.field import BSNodeField
from ...bs_node import BSNode

class CategoryEntry(BSNode):
    _tag_name = 'categoryEntry'

    # Links
    info_links = BSReferenceChild('InfoLinks')

    # References
    constraints = BSReferenceChild('Constraints')
    modifiers = BSReferenceChild('Modifiers')

    # Fields
    name = BSNodeField('name')
    node_id = BSNodeField('id')
    publication_id = BSNodeField('publicationId')
    hidden = BSNodeField('hidden')
    page = BSNodeField('page')

class CategoryEntries(BSNodeIterable):
    _tag_name = 'categoryEntries'

    _iter_child_class = BSReferenceIter('CategoryEntry')
    _link_type = BSReferenceLink('CategoryLinks')