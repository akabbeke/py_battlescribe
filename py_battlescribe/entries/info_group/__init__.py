from ...bs_node import BSNode
from ...bs_node.field import BSNodeField
from ...bs_reference.child import BSReferenceChild


class InfoGroup(BSNode):
    _tag_name = 'infoGroup'

    # References
    rules = BSReferenceChild('Rules')
    info_links = BSReferenceChild('InfoLinks')
    modifiers = BSReferenceChild('Modifiers')
    profiles = BSReferenceChild('Profiles')

    # Fields
    name = BSNodeField('name')
    hidden = BSNodeField('hidden')
    node_id = BSNodeField('id')
