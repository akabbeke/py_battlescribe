from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_reference.child import BSReferenceChild


class GameSystem(BSNode):
    _tag_name = 'gameSystem'

    # References
    entry_links = BSReferenceChild('EntryLinks')

    # References
    cost_types = BSReferenceChild('CostTypes')
    category_entries = BSReferenceChild('CategoryEntries')
    selection_entries = BSReferenceChild('SelectionEntries')
    selection_entry_groups = BSReferenceChild('SelectionEntryGroups')
    force_entries = BSReferenceChild('ForceEntries')
    profile_types = BSReferenceChild('ProfileTypes')
    publications = BSReferenceChild('Publications')
    shared_profiles = BSReferenceChild('SharedProfiles')
    shared_rules = BSReferenceChild('SharedRules')
    shared_selection_entries = BSReferenceChild('SharedSelectionEntries')
    shared_selection_entry_groups = BSReferenceChild('SharedSelectionEntryGroups')

    # Fields
    author_contact = BSNodeField('authorContact')
    author_name = BSNodeField('authorName')
    author_url = BSNodeField('authorUrl')
    battle_scribe_version = BSNodeField('battleScribeVersion')
    node_id = BSNodeField('id')
    name = BSNodeField('name')
    revision = BSNodeField('revision')
