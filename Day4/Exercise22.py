def password_strength(password):
    length_ok = len(password) >= 8
    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
 
    score = sum([length_ok, has_digit, has_upper])
 
    if score == 3:
        return "Strong"
    elif score == 2:
        return "Medium"
    else:
        return "Weak"
 
print(password_strength("abc"))            
print(password_strength("abcdefgh1"))      
print(password_strength("Abcdefgh1")) 
     
# Output:
# Weak
# Medium
# Strong