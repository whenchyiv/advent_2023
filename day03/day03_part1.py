from input import puzzle_input
from loguru import logger
import re


input_list = puzzle_input.split('\n')


def is_special_char(val: str) -> bool:
    return re.match(r'[^a-zA-Z0-9\s!.]', val) is not None


if __name__ == '__main__':
    part_numbers = []
    # Yuck.
    for i, r in enumerate(input_list[:]):
        numbers = re.findall(r'(\d+)', r)
        for n in numbers:
            num_start = r.index(n)
            search_start = -1 if num_start > 0 else 0
            num_end = num_start + len(n)
            search_end = 1 if num_end + 1 < len(r) else 0
            search_space = r[num_start+search_start:num_end+search_end]
            # Zero out searched number while maintaining string legnth to handle duplicate numbers in one row
            # (.index() only gets the first index).
            r = r.replace(r[num_start:num_end], ''.join('.'*len(n)), 1)
            if i > 0:
                search_space = input_list[i-1][num_start+search_start:num_end+search_end] + search_space
            if i + 1 < len(input_list):
                search_space += input_list[i+1][num_start+search_start:num_end+search_end]
            for c in search_space:
                if is_special_char(c):
                    part_numbers.append(int(n))
                    break
    logger.info(f'⚙️ Part numbers sum: {sum(part_numbers)}')
