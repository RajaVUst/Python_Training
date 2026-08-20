team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}
 
common = team_a & team_b
only_a = team_a - team_b
combined = team_a | team_b
symmetric = team_a ^ team_b
 
print(common)
 
print(only_a)
 
print(combined)
 
print(symmetric)
 
# Output:
# {'slack', 'jira'}
# {'figma', 'github'}
# {'figma', 'notion', 'slack', 'vscode', 'jira', 'github'}  
# {'figma', 'notion', 'vscode', 'github'}
 