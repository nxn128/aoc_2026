def calculate_password():
  position = 50
  rollover_position = 100
  direction = 1
  zero_count = 0

  with open('input/rotations.txt', 'r') as file:
    for line in file:
      line = line.strip()
      rotations = int(line[1:])
      if line.startswith('R'):
        direction = 1
      elif line.startswith('L'):
        direction = -1

      position = (position + (direction * rotations)) % rollover_position

      if position == 0:
        zero_count += 1


    print(zero_count)

def calculate_password_2():
  position = 50
  rollover_position = 100
  direction = 1
  zero_count = 0

  with open('input/rotations.txt', 'r') as file:
    for line in file:
      line = line.strip()
      rotations = int(line[1:])
      if line.startswith('R'):
        direction = 1
      elif line.startswith('L'):
        direction = -1

      for i in range(rotations):
        position = (position + (direction * 1)) % rollover_position
        if position == 0:
          zero_count += 1

    print(zero_count)


calculate_password_2()
