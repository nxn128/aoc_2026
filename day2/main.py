def check_valid_product_id_part1(product_id: str):
  len_id = len(product_id)
  if len_id % 2 != 0:
    return True

  half_id = len_id // 2
  if product_id[:half_id] == product_id[half_id:]:
    return False

  return True

def check_valid_product_id_part2(product_id: str) -> bool:
    return not (product_id in (product_id + product_id)[1:-1])


def calculate_invalid_product_ids_sum() -> int:
  invalid_product_ids_sum = 0

  with open('input/product_ids.txt', 'r') as file:
    for line in file:
      line = line.strip()
      product_id_ranges = line.split(',')
      for product_id_range in product_id_ranges:
        product_id_range_arr = product_id_range.split('-')
        starting_product_id = int(product_id_range_arr[0])
        ending_product_id = int(product_id_range_arr[1])

        for i in range(starting_product_id, ending_product_id + 1):
          if not check_valid_product_id_part2(str(i)):
            invalid_product_ids_sum += i
  return invalid_product_ids_sum

print(calculate_invalid_product_ids_sum())
