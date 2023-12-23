def started(msg=""):
    print("-" * 85)
    print(f"Operation started:{msg}...\n")


def completed():
    print("Operation completed.")
    print("-" * 85)


def error(msg):
    print(f"Error! {msg}")


def menu():
    print("Please select one of the following options:")
    print("     [years]      List unique years")
    print("     [tally]      Tally up medals")
    print("     [ctally]     Tally up medals for each team")
    print("     [exit]       Exit the program")
    selection = input("Your selection:")
    return selection.strip().lower()


def display_medal_tally(tally):
    print(f"| Gold   | {tally['Gold']:<8} |")
    print(f"| Silver | {tally['Silver']:<8} |")
    print(f"| Bronze | {tally['Bronze']:<8} |")


def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")


def display_years(years):
    sorted_set = sorted(years, reverse=True)
    for year in sorted_set:
        print(year)
