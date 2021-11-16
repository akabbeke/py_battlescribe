from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter


class Publication(BSNode):
    _tag_name = 'publication'

    # Fields
    name = BSNodeField('name')
    publisher = BSNodeField('publisher')
    node_id = BSNodeField('id')
    short_name = BSNodeField('shortName')
    publication_date = BSNodeField('publicationDate')


class Publications(BSNodeIterable):
    _tag_name = 'publications'

    _iter_child_class = BSReferenceIter('Publication')
