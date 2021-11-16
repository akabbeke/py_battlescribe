
import os
import xml.etree.ElementTree as ET

from .node_registry import NodeRegistry
from .entries.catalogue import Catalogue
from .entries.game_system import GameSystem

DEFAULT_GAME_SYSTEM_PREFIX = 'gst'
DEFAULT_CATALOGUE_PREFIX = 'cat'

DEFAULT_NAMESPACES = {
    DEFAULT_GAME_SYSTEM_PREFIX: 'http://www.battlescribe.net/schema/gameSystemSchema',
    DEFAULT_CATALOGUE_PREFIX: 'http://www.battlescribe.net/schema/catalogueSchema',
}


class BattlescribeRepo:
    def __init__(self, dir_path: str, namespaces: dict=None, game_system_prefix: str=None, catalogue_prefix: str=None):
        self.dir_path = dir_path
        self.namespaces = namespaces or DEFAULT_NAMESPACES
        self.game_system_prefix = game_system_prefix or DEFAULT_GAME_SYSTEM_PREFIX
        self.catalogue_prefix = catalogue_prefix or DEFAULT_CATALOGUE_PREFIX
        self.node_registry = NodeRegistry()

        self.game_systems = self._load_game_systems()
        self.catalogues = self._load_catalogues()

    def _library_files(self):
        return sorted([os.path.join(self.dir_path, p) for p in os.listdir(self.dir_path) if os.path.isfile(os.path.join(self.dir_path, p))])

    def _game_system_files(self):
        return [p for p in self._library_files() if p.endswith('.gst')]

    def _catalouge_files(self):
        return [p for p in self._library_files() if p.endswith('.cat')]

    def _load_game_systems(self):
        game_systems = []
        for xml_path in self._game_system_files():
            print(xml_path)
            game_systems.append(
                GameSystem(
                    ET.parse(xml_path).getroot(),
                    self.namespaces,
                    self.game_system_prefix,
                    self.node_registry
                )
            )
        return game_systems

    def _load_catalogues(self):
        catalogues = []
        for xml_path in self._catalouge_files():
            print(xml_path)
            catalogues.append(
                Catalogue(
                    ET.parse(xml_path).getroot(),
                    self.namespaces,
                    self.catalogue_prefix,
                    self.node_registry
                )
            )
        return catalogues


class BattlescribeRoster:
    def __init__(self, battlescribe):
        self._battlescribe = battlescribe

    def available_catalogues(self):
        return self._battlescribe.catalogues

    def available_force_entries(self, catalogue):
        pass


class BattlescribeForceEntry:
    def __init__(self, catalogue, force_entry):
        self._catalogue = catalogue
        self._force_entry = force_entry


