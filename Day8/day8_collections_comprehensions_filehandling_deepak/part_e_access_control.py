team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}

def access_report(a, b):
    return {"common": a & b, "unique_to_a": a - b, "combined": a | b, "symmetric_difference": a ^ b}

print(team_a & team_b)
print(team_a - team_b)
print(team_a | team_b)
print(team_a ^ team_b)
print(access_report(team_a, team_b))
# Output:
# {'slack', 'jira'}
# {'github', 'figma'}
# {'github', 'notion', 'slack', 'vscode', 'figma', 'jira'}
# {'github', 'notion', 'vscode', 'figma'}
# {'common': {'slack', 'jira'}, 'unique_to_a': {'github', 'figma'}, 'combined': {'github', 'notion', 'slack', 'vscode', 'figma', 'jira'}, 'symmetric_difference': {'github', 'notion', 'vscode', 'figma'}}
# Symmetric difference answers: "which tools does only one team have?"