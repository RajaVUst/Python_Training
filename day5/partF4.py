def fizz_buzz(n):
    result={}
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            result[i]="FIZZBUZZ"
        elif i%3==0:
            result[i]="FIZZ"
        elif i%5==0:
            result[i]="BUZZ"

    print(result)
    
fizz_buzz(20)

# OUTPUT

# {3: 'FIZZ', 5: 'BUZZ', 6: 'FIZZ',
#        9: 'FIZZ', 10:'BUZZ', 12: 'FIZZ', 
#        15: 'FIZZBUZZ', 18: 'FIZZ', 20: 'BUZZ'}