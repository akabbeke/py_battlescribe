from ..bs_node import BSNode


class BSReference:
    """A schema definition for a reference to a child node type
    Mostly used to get around import issues.

    Parameters
    ----------
    child_class_name : str
        The name of the child node type node
    """
    def __init__(self, child_class_name):
        self._child_class = child_class_name

    def type_class(self) -> BSNode:
        from ..entries.catalogue.link import CatalogueLink, CatalogueLinks
        from ..entries.category.entry import CategoryEntry, CategoryEntries
        from ..entries.category.link import CategoryLink, CategoryLinks
        from ..entries.constraint import Constraint, Constraints
        from ..entries.condition import Condition, Conditions
        from ..entries.condition.group import ConditionGroup, ConditionGroups
        from ..entries.characteristic.type import CharacteristicType, CharacteristicTypes
        from ..entries.characteristic import Characteristic, Characteristics
        from ..entries.cost.type import CostType, CostTypes
        from ..entries.cost import Cost, Costs
        from ..entries.description import Description
        from ..entries.modifier import Modifier, Modifiers
        from ..entries.modifier.group import ModifierGroup, ModifierGroups
        from ..entries.force_entry import ForceEntry, ForceEntries
        from ..entries.info_group import InfoGroup
        from ..entries.profile.type import ProfileType, ProfileTypes
        from ..entries.profile import Profile, Profiles
        from ..entries.publication import Publication, Publications
        from ..entries.repeat import Repeat, Repeats
        from ..entries.rule import Rule, Rules
        from ..entries.selection_entry import SelectionEntry, SelectionEntries
        from ..entries.selection_entry.group import SelectionEntryGroup, SelectionEntryGroups

        from ..links.entry_link import EntryLink, EntryLinks
        from ..links.info_link import InfoLink, InfoLinks

        from ..shared.info_groups import SharedInfoGroups
        from ..shared.profiles import SharedProfiles
        from ..shared.rules import SharedRules
        from ..shared.selection_entries import SharedSelectionEntries
        from ..shared.entry_groups import SharedSelectionEntryGroups

        
        return {
            'CatalogueLinks': CatalogueLinks,
            'CatalogueLink': CatalogueLink,
            'CategoryEntries': CategoryEntries,
            'CategoryEntry':CategoryEntry,
            'CategoryLinks': CategoryLinks,
            'CategoryLink': CategoryLink,
            'Constraints': Constraints,
            'Constraint': Constraint,
            'Conditions': Conditions,
            'Condition': Condition,
            'ConditionGroups': ConditionGroups,
            'ConditionGroup': ConditionGroup,
            'CharacteristicTypes': CharacteristicTypes,
            'CharacteristicType': CharacteristicType,
            'Characteristics': Characteristics,
            'Characteristic': Characteristic,
            'CostTypes': CostTypes,
            'CostType': CostType,
            'Costs': Costs,
            'Cost': Cost,
            'Description': Description,
            'Modifiers': Modifiers,
            'Modifier': Modifier,
            'ModifierGroups': ModifierGroups,
            'ModifierGroup': ModifierGroup,
            'EntryLinks': EntryLinks,
            'EntryLink': EntryLink,
            'ForceEntries': ForceEntries,
            'ForceEntry': ForceEntry,
            'InfoLinks': InfoLinks,
            'InfoLink': InfoLink,
            'InfoGroup': InfoGroup,
            'ProfileTypes': ProfileTypes,
            'ProfileType': ProfileType,
            'Profiles': Profiles,
            'Profile': Profile,
            'Publications': Publications,
            'Publication': Publication,
            'Repeats': Repeats,
            'Repeat': Repeat,
            'Rules': Rules,
            'Rule': Rule,
            'SelectionEntries': SelectionEntries,
            'SelectionEntry': SelectionEntry,
            'SelectionEntryGroups': SelectionEntryGroups,
            'SelectionEntryGroup': SelectionEntryGroup,
            'SharedInfoGroups': SharedInfoGroups,
            'SharedProfiles': SharedProfiles,
            'SharedRules': SharedRules,
            'SharedSelectionEntries': SharedSelectionEntries,
            'SharedSelectionEntryGroups': SharedSelectionEntryGroups,
        }[self._child_class]
