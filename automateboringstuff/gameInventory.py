# Idea is to use dictionaries to represent a player's inventory in a rpg like game. First version prints the amount of items as a total and also the items in the inventory per challenge.

char = {'gold': 1, 'craftingmats': 13, 'sword': 2, 'armor': 5, 'shield': 1, 'ranged': 3}
chest = ['gold', 'gold', 'gold', 'gold', 'gold', 'gold', 'craftingmats', 'craftingmats', 'craftingmats', 'shield']

def displayInventory(inventory): 
  print('Your inventory includes:')
  item_total = 0
  for k in inventory.keys(): 
    print(k, ': ', inventory[k])
    item_total = item_total + inventory.get(k, 0)
  print('The total number of items in your inventory ' + str(item_total))

# Adding new functionality of encountering loot and adding it to inventory.
def addToInventory(inventory, loot):
  for i in loot:
      if inventory.get(i, 0) != 0: # Current bug if any items are intially value 0!
          inventory[i] += 1
  return inventory
      
displayInventory(char)
char = addToInventory(char, chest)
displayInventory(char)
