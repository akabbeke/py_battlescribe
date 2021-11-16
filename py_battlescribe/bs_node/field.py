class BSNodeField:
    """A schema definition for a field on the object

    Parameters
    ----------
    field_name : str
        The name of the field on the node

    field_type : str, optional
        The field type to cast the value into
    """
    def __init__(self, field_name: str, field_type: str=None):
        self._field_name = field_name
        self._field_type = field_type

    def __call__(self, bs_node):
        return bs_node.attr.get(self._field_name)
