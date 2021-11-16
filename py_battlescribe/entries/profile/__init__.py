from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_node.iterable import BSNodeIterable
from ...bs_reference.iter import BSReferenceIter
from ...bs_reference.child import BSReferenceChild
from ...bs_reference.link import BSReferenceLink


class Profile(BSNode):
    _tag_name = 'profile'

    # Refernces
    characteristics = BSReferenceChild('Characteristics')
    modifiers = BSReferenceChild('Modifiers')
    modifier_groups = BSReferenceChild('ModifierGroups')

    # Fields
    hidden = BSNodeField('hidden')
    node_id = BSNodeField('id')
    name = BSNodeField('name')
    page = BSNodeField('page')
    publication_id = BSNodeField('publicationId')
    type_id = BSNodeField('typeId')
    type_name = BSNodeField('typeName')


class Profiles(BSNodeIterable):
    _tag_name = 'profiles'

    _link_type = BSReferenceLink('InfoLinks')

    _iter_child_class = BSReferenceIter('Profile')
