D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }

union = D1|D2  #insertion 
print(union)

insertion = set(D1)&set(D2) # intersection
intersection_result = {key:D1[key] for key in insertion}
print(intersection_result)

difference={key:D1[key] for key in set(D1) - set(D2)}  #difference 
print(difference)

merge=D1.copy()      #same keys merge their values
for key,value in D2.items():
    if key in merge:
        merge[key]=merge[key]+value
    else:
        merge[key]=value
print(merge)