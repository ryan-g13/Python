def pPicnic(itemDict, leftWidth, rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth, '-'))
    for k, v in itemDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'Beer': 12, 'chicken': 1, 'salsa': 1, 'tortilla chips': 13}
pPicnic(picnicItems, 10, 10)
pPicnic(picnicItems, 20, 5)