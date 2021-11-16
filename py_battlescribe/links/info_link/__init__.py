from ...bs_link import BSLink
from ...bs_node.field import BSNodeField
from ...bs_node.iterable_links import BSNodeIterableLinks
from ...bs_reference.iter import BSReferenceIter
from ...bs_reference.child import BSReferenceChild


class InfoLink(BSLink):
    _tag_name = 'infoLink'

    # References
    modifiers = BSReferenceChild('Modifiers')

    # Fields
    target_id = BSNodeField('targetId')
    hidden = BSNodeField('hidden')
    node_id = BSNodeField('id')
    name = BSNodeField('name')
    page = BSNodeField('page')
    publication_id = BSNodeField('publicationId')
    node_type = BSNodeField('type')

    @property
    def target(self):
        target = super().target
        if target is not None:
            target.modifiers.concatenate([x for x in self.modifiers])
        return target


class InfoLinks(BSNodeIterableLinks):
    _tag_name = 'infoLinks'

    _iter_child_class = BSReferenceIter('InfoLink')

