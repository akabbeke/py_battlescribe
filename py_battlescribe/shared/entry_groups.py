from ..bs_node.iterable import BSNodeIterable
from ..bs_reference.iter import BSReferenceIter

class SharedSelectionEntryGroups(BSNodeIterable):
    _tag_name = 'sharedSelectionEntryGroups'

    _iter_child_class = BSReferenceIter('SelectionEntryGroup')