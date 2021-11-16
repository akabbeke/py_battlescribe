from py_battlescribe.battlescribe import BattlescribeRepo

repo = BattlescribeRepo('/Users/adam/src/wh40k')

games_system = repo.game_systems[0]

for catalogue in repo.catalogues:
    for selection_entry in catalogue.selection_entries:
        print(f'--- {selection_entry} -- {selection_entry.node_type}')
        for prof in selection_entry.profiles:
            print(f'------ {prof} -- {prof.type_name}')
