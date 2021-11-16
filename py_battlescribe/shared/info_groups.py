from ..bs_node.iterable import BSNodeIterable
from ..bs_reference.iter import BSReferenceIter
from ..bs_reference.link import BSReferenceLink

class SharedInfoGroups(BSNodeIterable):
    _tag_name = 'sharedInfoGroups'

    _link_type = BSReferenceLink('InfoLinks')

    _iter_child_class = BSReferenceIter('InfoGroup')