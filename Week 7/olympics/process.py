import tui


def list_years(data):
    tui.started("Listing years")
    years = set()
    for line in data:
        year = line[9]
        years.add(year)
    tui.display_years(years)
    tui.completed()


def tally_medals(data):
    tui.started("Tallying medals")
    medals = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for line in data:
        medal = line[14]
        if medal == "Gold":
            medals["Gold"] += 1
        elif medal == "Silver":
            medals["Silver"] += 1
        elif medal == "Bronze":
            medals["Bronze"] += 1
    tui.display_medal_tally(medals)
    tui.completed()


def tally_team_medals(data):
    tui.started("Tallying Team medals")
    team_medals = {}
    for line in data:
        team = line[6]
        medal = line[14]
        if medal in ("Gold", "Silver", "Bronze"):
            if team in team_medals:
                team_medals[team][medal] += 1
            else:
                team_medals[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
                team_medals[team][medal] += 1
    tui.display_team_medal_tally(team_medals)
    tui.completed()
