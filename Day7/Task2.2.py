team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}

common_tools = team_a & team_b
team_a_only = team_a - team_b
combined_tools = team_a | team_b
symmetric_difference = team_a ^ team_b

print("Common tools:", common_tools)
print("Only Team A:", team_a_only)
print("Combined tools:", combined_tools)
print("Tools available to only one team:", symmetric_difference)


def access_report(first_team, second_team):
    return {
        "common": first_team & second_team,
        "only_team_a": first_team - second_team,
        "combined": first_team | second_team,
        "only_one_team": first_team ^ second_team
    }


print("Access report:", access_report(team_a, team_b))

#output
'''
Common tools: {'jira', 'slack'}
Only Team A: {'github', 'figma'}
Combined tools: {'jira', 'vscode', 'figma', 'slack', 'github', 'notion'}
Tools available to only one team: {'vscode', 'figma', 'github', 'notion'}
Access report: {'common': {'jira', 'slack'}, 'only_team_a': {'github', 'figma'}, 'combined': {'jira', 'vscode', 'figma', 'slack', 'github', 'notion'}, 'only_one_team': {'vscode', 'figma', 'github', 'notion'}}

'''