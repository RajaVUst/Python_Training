team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}

common_tools = team_a & team_b

team_a_only = team_a - team_b

combined_tools = team_a | team_b

symmetric_difference = team_a ^ team_b

print("Common tools:", common_tools)
print("Team A only:", team_a_only)
print("Combined toolset:", combined_tools)
print("Symmetric difference:", symmetric_difference)



def access_report(team_a, team_b):
    return {
        "common": team_a & team_b,
        "team_a_only": team_a - team_b,
        "combined": team_a | team_b,
        "symmetric_difference": team_a ^ team_b
    }


report = access_report(team_a, team_b)

print(report)




# Common tools: {'slack', 'jira'}
# Team A only: {'github', 'figma'}
# Combined toolset: {'github', 'notion', 'figma', 'jira', 'slack', 'vscode'}
# Symmetric difference: {'github', 'notion', 'figma', 'vscode'}
# {'common': {'slack', 'jira'}, 'team_a_only': {'github', 'figma'}, 'combined': {'github', 'notion', 'figma', 'jira', 'slack', 'vscode'}, 'symmetric_difference': {'github', 'notion', 'figma', 'vscode'}}
