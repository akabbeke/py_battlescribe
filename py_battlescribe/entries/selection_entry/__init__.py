from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter
from ...bs_reference.child import BSReferenceChild
from ...bs_reference.link import BSReferenceLink


class SelectionEntry(BSNode):
    _tag_name = 'selectionEntry'

    #Links:
    category_links = BSReferenceChild('CategoryLinks')
    entry_links = BSReferenceChild('EntryLinks')
    info_links = BSReferenceChild('InfoLinks')

    # References
    category_entries = BSReferenceChild('CategoryEntries')
    constraints = BSReferenceChild('Constraints')
    costs = BSReferenceChild('Costs')
    modifier_groups = BSReferenceChild('ModifierGroups')
    modifiers = BSReferenceChild('Modifiers')
    profiles = BSReferenceChild('Profiles')
    rules = BSReferenceChild('Rules')
    selection_entries = BSReferenceChild('SelectionEntries')
    selection_entry_groups = BSReferenceChild('SelectionEntryGroups')

    # Fields:
    collective = BSNodeField('collective')
    hidden = BSNodeField('hidden')
    node_id = BSNodeField('id')
    is_import = BSNodeField('import')
    name = BSNodeField('name')
    page = BSNodeField('page')
    publication_id = BSNodeField('publicationId')
    node_type = BSNodeField('type')


class SelectionEntries(BSNodeIterable):
    _tag_name = 'selectionEntries'

    _iter_child_class = BSReferenceIter('SelectionEntry')
    _link_type = BSReferenceLink('EntryLinks')
