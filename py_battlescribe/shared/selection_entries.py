from ..bs_node.iterable import BSNodeIterable
from ..bs_reference.iter import BSReferenceIter


class SharedSelectionEntries(BSNodeIterable):
    _tag_name = 'sharedSelectionEntries'

    _iter_child_class = BSReferenceIter('SelectionEntry')