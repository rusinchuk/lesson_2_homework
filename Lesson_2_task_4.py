d = {'title': 'cooking', 'price': 258, 'ingredients': 'apple'}
print(d)
d['description'] = "Apple juice"
print(d)
d['price'] =  d['price'] + 100
print(d)
d['ingredients'] = d['ingredients'] + ' , juice'
print(d['ingredients'])
d.pop('description')
print(d)
