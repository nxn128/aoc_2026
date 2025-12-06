def calculate_fresh_ingredients():
  fresh_ingredients = []
  available_ingredients = []
  with open('input/ingredients.txt', 'r') as file:
    for line in file:
      line = line.strip()
      if "-" in line:
        fresh_ingredients.append(line)
        continue
      available_ingredients.append(line)

  print("poo")
  print(fresh_ingredients)
  print(available_ingredients)

calculate_fresh_ingredients()
