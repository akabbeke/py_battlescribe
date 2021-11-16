from ..bs_node.iterable import BSNodeIterable
from ..bs_reference.iter import BSReferenceIter


class SharedProfiles(BSNodeIterable):
    _tag_name = 'sharedProfiles'

    _iter_child_class = BSReferenceIter('Profile')
