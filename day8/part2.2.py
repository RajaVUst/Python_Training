team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}


print(f"UNIQUE:{set(team_a and team_b)}")

print(f"UNIQUE TO A:{set(team_a-team_b)}")
print(f"UNIQUE TO B {set(team_b-team_a)}")

symmetric = team_a ^ team_b

print("Symmetric Difference:", symmetric)

# OUTPUT
# UNIQUE:{'jira', 'notion', 'slack', 'vscode'}
# UNIQUE TO A:{'github', 'figma'}
# UNIQUE TO B {'notion', 'vscode'}
# Symmetric Difference: {'vscode', 'github', 'notion', 'figma'}