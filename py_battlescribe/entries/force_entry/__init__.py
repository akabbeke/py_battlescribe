from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter
from ...bs_reference.child import BSReferenceChild


class ForceEntries(BSNodeIterable):
    _tag_name = 'forceEntries'

    _iter_child_class = BSReferenceIter('ForceEntry')


class ForceEntry(BSNode):
    _tag_name = 'forceEntry'

    # Links:
    info_links = BSReferenceChild('InfoLinks')
    category_links = BSReferenceChild('CategoryLinks')

    # References
    category_entries = BSReferenceChild('CategoryEntries')
    constraints = BSReferenceChild('Constraints')
    force_entries = BSReferenceChild('ForceEntries')
    modifiers = BSReferenceChild('Modifiers')
    rules = BSReferenceChild('Rules')

    # Fields
    name = BSNodeField('name')
    node_id = BSNodeField('id')
    publication_id = BSNodeField('publicationId')
    hidden = BSNodeField('hidden')
    page = BSNodeField('page')
