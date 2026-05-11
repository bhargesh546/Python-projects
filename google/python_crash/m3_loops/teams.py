#teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
teams = input("Enter the name of the teams seperated by ',': ").split(',')

teams = [team.title().strip() for team in teams]

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
    print("-"*30)
