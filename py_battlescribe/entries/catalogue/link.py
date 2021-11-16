from ...bs_link import BSLink
from ...bs_node.field import BSNodeField
from ...bs_node.iterable_links import BSNodeIterableLinks
from ...bs_reference.iter import BSReferenceIter


class CatalogueLink(BSLink):
    _tag_name = 'catalogueLink'

    # Fields
    target_id = BSNodeField('targetId')
    name = BSNodeField('name')
    node_id = BSNodeField('id')
    import_root_entries = BSNodeField('importRootEntries')
    node_type = BSNodeField('type')


class CatalogueLinks(BSNodeIterableLinks):
    _tag_name = 'catalogueLinks'

    _iter_child_class = BSReferenceIter('CatalogueLink')
