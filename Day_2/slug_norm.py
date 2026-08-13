title1 = '  My First Python Project!!'
 #strip the white space 
step1 = title1.strip()
#remove !!
step2 = step1.replace('!!', ".")
#convert to lower case
step3 = step2.lower()
final = step3.replace(" ", "_")
print(final)