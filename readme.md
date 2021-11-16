# py_battlescribe

I wrote this to parse the raw data used by the BattleScribe app into a python friendly data structure. This was written with the Warhammer 40k repo (https://github.com/BSData/wh40k) in mind but it should be generic enough to work with other repos.

This also de-references all the link objects so you don't have to. I also plan to publish this as a package.

## Example
Clone the data repository of your choice to your local machine. Then run the below.


```python
from py_battlescribe.battlescribe import BattlescribeRepo

repo = BattlescribeRepo('path_to_repository')
games_system = repo.game_systems[0]

for catalogue in repo.catalogues:
    for selection_entry in catalogue.selection_entries:
        print(f'- {selection_entry} -- {selection_entry.node_type}')
        for profile in selection_entry.profiles:
            print(f'-- {profile} -- {prof.type_name}')

```