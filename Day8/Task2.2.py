
team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}

common = team_a & team_b

only_a = team_a - team_b

combined = team_a | team_b

symmetric_difference = team_a ^ team_b

print("Common:", common)
print("Only Team A:", only_a)
print("Combined:", combined)
print("Symmetric difference:", symmetric_difference)

# Output:
# Common: {'jira', 'slack'}
# Only Team A: {'figma', 'github'}
# Combined: {'figma', 'jira', 'slack', 'github', 'notion', 'vscode'}
# Symmetric difference: {'figma', 'github', 'notion', 'vscode'}

#Bonus — access_report()
def access_report(team_a, team_b):
    return {
        "common": team_a & team_b,
        "only_team_a": team_a - team_b,
        "combined": team_a | team_b,
        "symmetric_difference": team_a ^ team_b
    }


report = access_report(team_a, team_b)

print(report)

# Output:
# { 'common': {'jira', 'slack'}, 'only_team_a': {'figma', 'github'}, 'combined': {'figma', 'jira', 'slack', 'github', 'notion', 'vscode'}, 'symmetric_difference': {'figma', 'github', 'notion', 'vscode'} }


