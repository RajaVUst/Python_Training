team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}

common = team_a & team_b
only_a = team_a - team_b
combined = team_a | team_b
different = team_a ^ team_b

print("Common:", common)
print("Only Team A:", only_a)
print("Combined:", combined)
print("Only one team has:", different)

# Output:
# Common: {'jira', 'slack'}
# Only Team A: {'figma', 'github'}
# Combined: {'jira', 'slack', 'notion', 'github', 'figma', 'vscode'}
# Only one team has: {'notion', 'github', 'figma', 'vscode'}

# Bonus Function
def access_report(team_a, team_b):
    report = {
        "common": team_a & team_b,
        "only_a": team_a - team_b,
        "combined": team_a | team_b,
        "different": team_a ^ team_b
    }

    return report

result = access_report(team_a, team_b)
print(result)

# Output:
# {'common': {'jira', 'slack'}, 'only_a': {'github', 'figma'}, 'combined': {'jira', 'vscode', 'github', 'figma', 'slack', 'notion'}, 'different': {'vscode', 'github', 'figma', 'notion'}}