def calculate_max_joltage():
  total_max_joltage = 0
  with open('input/batteries.txt', 'r') as file:
    for line in file:
      line = line.strip()
      highest_left_pos = 0
      max_left_value = 0
      for i in range(0, len(line) - 1):
        candidate = int(line[i])
        if candidate > max_left_value:
          max_left_value = candidate
          highest_left_pos = i

      max_right_value = 0
      for i in range(highest_left_pos + 1, len(line)):
        candidate = int(line[i])
        if candidate > max_right_value:
          max_right_value = candidate

      total_max_joltage += max_left_value * 10 + max_right_value

  print(total_max_joltage)

def calculate_max_joltage_2(num_digits=2):
  total_max_joltage = 0
  with open('input/batteries.txt', 'r') as file:
    for line in file:
      line = line.strip()

      selected = []
      start_pos = 0

      for digit_index in range(num_digits):
        remaining_digits = num_digits - digit_index - 1
        search_end = len(line) - remaining_digits

        max_value = -1
        max_pos = start_pos

        for i in range(start_pos, search_end):
          candidate = int(line[i])
          if candidate > max_value:
            max_value = candidate
            max_pos = i

        selected.append(max_value)
        start_pos = max_pos + 1

      joltage = int(''.join(map(str, selected)))
      total_max_joltage += joltage

  print(total_max_joltage)

calculate_max_joltage_2(12)
