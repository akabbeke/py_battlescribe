from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_reference.child import BSReferenceChild
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter
from ...bs_reference.link import BSReferenceLink


class SelectionEntryGroup(BSNode):
    _tag_name = 'selectionEntryGroup'

    # Links:
    category_links = BSReferenceChild('CategoryLinks')
    costs = BSReferenceChild('Costs')
    entry_links = BSReferenceChild('EntryLinks')

    # References:
    category_entries = BSReferenceChild('CategoryEntries')
    constraints = BSReferenceChild('Constraints')
    modifier_groups = BSReferenceChild('ModifierGroups')
    modifiers = BSReferenceChild('Modifiers')
    profiles = BSReferenceChild('Profiles')
    rules = BSReferenceChild('Rules')
    selection_entries = BSReferenceChild('SelectionEntries')
    selection_entry_groups = BSReferenceChild('SelectionEntryGroups')

    # Fields:
    collective = BSNodeField('collective')
    default_selection_entry_id = BSNodeField('defaultSelectionEntryId')
    hidden = BSNodeField('hidden')
    node_id = BSNodeField('id')
    is_import = BSNodeField('import')
    name = BSNodeField('name')
    page = BSNodeField('page')
    publication_id = BSNodeField('publicationId')


class SelectionEntryGroups(BSNodeIterable):
    _tag_name = 'selectionEntryGroups'

    _iter_child_class = BSReferenceIter('SelectionEntryGroup')
    _link_type = BSReferenceLink('EntryLinks')