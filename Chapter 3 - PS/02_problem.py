# WRITE A PROGRAM TO FILL IN A LETTER TEMPLATE GIVEN BELOW WITH NAME AND DATE

letter = '''
 Dear <|NAME|>,
THIS TOO SHALL PASS!
<|DATE|>            
''' 
print(letter.replace("<|NAME|>","FUTURE ARTIST").replace("<|DATE|>","5 JUNE'26 " ) )