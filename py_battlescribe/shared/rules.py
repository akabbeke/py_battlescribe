from ..bs_node.iterable import BSNodeIterable
from ..bs_reference.iter import BSReferenceIter


class SharedRules(BSNodeIterable):
    _tag_name = 'sharedRules'

    _iter_child_class = BSReferenceIter('Rule')