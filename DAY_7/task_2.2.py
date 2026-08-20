team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}

common = team_a & team_b
only_a = team_a - team_b
combined = team_a | team_b
# Symmetric difference: tools that only ONE team has (not shared)
# Real-world question: "Which tools would need a new license if teams merged?"
sym_diff = team_a ^ team_b

print("Common tools:", common)
print("Only Team A:", only_a)
print("Combined toolset:", combined)
print("Symmetric difference (exclusive to one team):", sym_diff)


def access_report(team_a, team_b):
    return {
        "common": team_a & team_b,
        "only_team_a": team_a - team_b,
        "combined": team_a | team_b,
        "exclusive_to_one_team": team_a ^ team_b,
    }


print("\nAccess report:", access_report(team_a, team_b))
