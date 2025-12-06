def calculate_fresh_ingredients():
  fresh_ingredients = []
  available_ingredients = []
  with open('input/ingredients.txt', 'r') as file:
    for line in file:
      line = line.strip()
      if "-" in line:
        fresh_ingredients.append(line)
        continue
      if line is None or line == "":
        continue
      available_ingredients.append(line)

  fresh_count = 0
  for ingredient in available_ingredients:
    for fresh_ingredient in fresh_ingredients:
      fresh_ingredient_parts = fresh_ingredient.split('-')
      if int(ingredient) >= int(fresh_ingredient_parts[0]) and int(ingredient) <= int(fresh_ingredient_parts[1]):
        fresh_count += 1
        break
  print(fresh_count)

def calculate_fresh_ingredients_2():
  ranges = []
  with open('input/ingredients.txt', 'r') as file:
    for line in file:
      line = line.strip()
      if "-" in line:
        parts = line.split('-')
        ranges.append((int(parts[0]), int(parts[1])))

  # Merge overlapping ranges
  ranges.sort()
  merged = []
  for start, end in ranges:
    if merged and start <= merged[-1][1] + 1:
      merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
      merged.append((start, end))

  # Count total numbers in merged ranges
  total = sum(end - start + 1 for start, end in merged)
  print(total)

calculate_fresh_ingredients_2()
