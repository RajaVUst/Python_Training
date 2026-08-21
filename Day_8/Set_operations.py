team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}
common_tools = team_a & team_b
print("Common Tools:", common_tools)
unique_to_a = team_a - team_b
print("Unique to Team A:", unique_to_a)
combined_tools = team_a | team_b
print("Combined Toolset:", combined_tools)
symmetric_difference = team_a ^ team_b
print("Symmetric Difference:", symmetric_difference)
def access_report(team_a, team_b):
    return {
        "common": team_a & team_b,
        "unique_to_a": team_a - team_b,
        "combined": team_a | team_b,
        "symmetric_difference": team_a ^ team_b
    }
print("Access Report:", access_report(team_a, team_b))

# output:
# Common Tools: {'slack', 'jira'}
# Unique to Team A: {'figma', 'github'}
# Combined Toolset: {'figma', 'notion', 'slack', 'vscode', 'jira', 'github'}
# Symmetric Difference: {'figma', 'notion', 'github', 'vscode'}
# Access Report: {'common': {'slack', 'jira'}, 'unique_to_a': {'figma', 'github'}, 'combined': {'figma', 'notion', 'slack', 'vscode', 'jira', 'github'}, 'symmetric_difference': {'figma', 'notion', 'github', 'vscode'}}