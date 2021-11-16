from ...bs_link import BSLink
from ...bs_node.field import BSNodeField
from ...bs_node.iterable_links import BSNodeIterableLinks
from ...bs_reference.iter import BSReferenceIter
from ...bs_reference.child import BSReferenceChild

class EntryLink(BSLink):
    _tag_name = 'entryLink'

    # Links:
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
    selection_entry_groups = BSReferenceChild('SelectionEntryGroups')

    # Fields
    target_id = BSNodeField('targetId')
    collective = BSNodeField('collective')
    hidden = BSNodeField('hidden')
    node_id = BSNodeField('id')
    is_import = BSNodeField('import')
    name = BSNodeField('name')
    page = BSNodeField('page')
    publication_id = BSNodeField('publicationId')
    node_type = BSNodeField('type')

    @property
    def target(self):
        target = super().target
        if target is not None:
            target.category_entries.concatenate([x for x in self.category_entries])
            target.constraints.concatenate([x for x in self.constraints])
            target.costs.concatenate([x for x in self.costs])
            target.modifier_groups.concatenate([x for x in self.modifier_groups])
            target.modifiers.concatenate([x for x in self.modifiers])
            target.profiles.concatenate([x for x in self.profiles])
            target.selection_entry_groups.concatenate([x for x in self.selection_entry_groups])
        return target


class EntryLinks(BSNodeIterableLinks):
    _tag_name = 'entryLinks'

    _iter_child_class = BSReferenceIter('EntryLink')

