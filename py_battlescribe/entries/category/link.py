from ...bs_reference.child import BSReferenceChild
from ...bs_node.field import BSNodeField
from ...bs_link import BSLink
from ...bs_node.iterable_links import BSNodeIterableLinks
from ...bs_reference.iter import BSReferenceIter


class CategoryLink(BSLink):
    _tag_name = 'categoryLink'

    # References
    constraints = BSReferenceChild('Constraints')
    modifiers = BSReferenceChild('Modifiers')

    # Fields
    target_id = BSNodeField('targetId')
    hidden = BSNodeField('hidden')
    node_id = BSNodeField('id')
    name = BSNodeField('name')
    primary = BSNodeField('primary')
    publication_id = BSNodeField('publicationId')

    @property
    def target(self):
        target = super().target
        if target is not None:
            target.constraints.concatenate([x for x in self.constraints])
            target.modifiers.concatenate([x for x in self.modifiers])
        return target



class CategoryLinks(BSNodeIterableLinks):
    _tag_name = 'categoryLinks'

    # Links:
    _iter_child_class = BSReferenceIter('CategoryLink')
