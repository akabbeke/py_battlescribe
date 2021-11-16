from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_reference.child import BSReferenceChild


class Catalogue(BSNode):
    _tag_name = 'catalogue'

    # Links:

    catalogue_links = BSReferenceChild('CatalogueLinks')
    entry_links = BSReferenceChild('EntryLinks')
    info_links = BSReferenceChild('InfoLinks')

    # References:
    category_entries = BSReferenceChild('CategoryEntries')
    force_entries = BSReferenceChild('ForceEntries')
    profile_types = BSReferenceChild('ProfileTypes')
    publications = BSReferenceChild('Publications')
    rules = BSReferenceChild('Rules')
    selection_entries = BSReferenceChild('SelectionEntries')
    selection_entry_groups = BSReferenceChild('SelectionEntryGroups')
    shared_info_groups = BSReferenceChild('SharedInfoGroups')
    shared_profiles = BSReferenceChild('SharedProfiles')
    shared_rules = BSReferenceChild('SharedRules')
    shared_selection_entries = BSReferenceChild('SharedSelectionEntries')
    shared_selection_entry_groups = BSReferenceChild('SharedSelectionEntryGroups')

    # Fields:
    author_contact = BSNodeField('authorContact')
    author_name = BSNodeField('authorName')
    author_url = BSNodeField('authorUrl')
    battle_scribe_version = BSNodeField('battleScribeVersion')
    game_system_id = BSNodeField('gameSystemId')
    game_system_revision = BSNodeField('gameSystemRevision')
    node_id = BSNodeField('id')
    library = BSNodeField('library')
    name = BSNodeField('name')
    revision = BSNodeField('revision')