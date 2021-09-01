acronyms = {'LOL': 'laugh out load',
'IDK': "I don't know", 
'TBH': 'to be honest'}

Sentence = 'IDK' + ' What happened ' + 'TBH'

Translation = acronyms.get('IDK') +' What happened ' + acronyms.get('TBH')

print ('Sentence:', Sentence)
print ('Translation:', Translation)