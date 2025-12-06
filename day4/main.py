def get_accessible_rolls(floor):
  count = 0
  for i in range(len(floor)):
      for j in range(len(floor[i])):
        if floor[i][j] == '.':
          continue

        left = floor[i][j-1] if j > 0 else '.'
        right = floor[i][j+1] if j < len(floor[i]) - 1 else '.'
        top = floor[i-1][j] if i > 0 else '.'
        bottom = floor[i+1][j] if i < len(floor) - 1 else '.'
        top_left = floor[i-1][j-1] if i > 0 and j > 0 else '.'
        top_right = floor[i-1][j+1] if i > 0 and j < len(floor[i]) - 1 else '.'
        bottom_left = floor[i+1][j-1] if i < len(floor) - 1 and j > 0 else '.'
        bottom_right = floor[i+1][j+1] if i < len(floor) - 1 and j < len(floor[i]) - 1 else '.'

        free_sides = 0
        if left == '.':
          free_sides += 1
        if right == '.':
          free_sides += 1
        if top == '.':
          free_sides += 1
        if bottom == '.':
          free_sides += 1
        if top_left == '.':
          free_sides += 1
        if top_right == '.':
          free_sides += 1
        if bottom_left == '.':
          free_sides += 1
        if bottom_right == '.':
          free_sides += 1

        if free_sides > 4:
          count += 1
  return count

def get_accessible_rolls_v2(floor):
  count = 0

  for i in range(len(floor)):
    for j in range(len(floor[i])):
      if floor[i][j] == '.':
        continue

      left = floor[i][j-1] if j > 0 else '.'
      right = floor[i][j+1] if j < len(floor[i]) - 1 else '.'
      top = floor[i-1][j] if i > 0 else '.'
      bottom = floor[i+1][j] if i < len(floor) - 1 else '.'
      top_left = floor[i-1][j-1] if i > 0 and j > 0 else '.'
      top_right = floor[i-1][j+1] if i > 0 and j < len(floor[i]) - 1 else '.'
      bottom_left = floor[i+1][j-1] if i < len(floor) - 1 and j > 0 else '.'
      bottom_right = floor[i+1][j+1] if i < len(floor) - 1 and j < len(floor[i]) - 1 else '.'

      free_sides = 0
      if left == '.':
        free_sides += 1
      if right == '.':
        free_sides += 1
      if top == '.':
        free_sides += 1
      if bottom == '.':
        free_sides += 1
      if top_left == '.':
        free_sides += 1
      if top_right == '.':
        free_sides += 1
      if bottom_left == '.':
        free_sides += 1
      if bottom_right == '.':
        free_sides += 1

      if free_sides > 4:
        count += 1
        floor[i][j] = '.'

  # If we removed anything, check again for newly exposed rolls
  if count > 0:
    count += get_accessible_rolls_v2(floor)

  return count


def calculate_accessible_rolls_of_paper():
  floor = []
  count = 0
  with open('input/paper.txt', 'r') as file:
    for i, line in enumerate(file):
      line = line.strip()
      floor.append(line)

  count = get_accessible_rolls(floor)

  print(count)

def calculate_accessible_rolls_of_paper_v2():
  floor = []
  count = 0
  with open('input/paper.txt', 'r') as file:
    for i, line in enumerate(file):
      line = line.strip()
      floor.append(list(line))

  count = get_accessible_rolls_v2(floor)

  print(count)

calculate_accessible_rolls_of_paper_v2()
