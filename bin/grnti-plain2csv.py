#!python3

import re
import sys

FILENAME = sys.argv[1]
SEPARATOR = ','
columns_count = 6
current_row = [''] * columns_count

column_group_tpl = 'level_{0}_code' + SEPARATOR + 'level_{0}_title'
print(SEPARATOR.join([column_group_tpl.format(x) for x in range(round(columns_count / 2))]))

with open(FILENAME, 'r') as f:
    lst = f.readlines()

    for i, line in enumerate(lst):
        current_code = re.match(r'(\d{2})\.?(\d{2})?\.?(\d{2})?', line.strip()).group(0)
        current_title = '"' + line.replace(current_code, '').strip() + '"'
        current_level = len(current_code.split('.')) - 1
        idx = current_level * 2
        current_row[idx], current_row[idx + 1] = current_code, current_title
        current_row[idx + 2:] = [''] * (columns_count - idx - 2)

        if i == len(lst) - 1:
            print(SEPARATOR.join(current_row))
        else:
            next_code = re.match(r'(\d{2})\.?(\d{2})?\.?(\d{2})?', lst[i + 1].strip()).group(0)
            next_level = len(next_code.split('.')) - 1

            if next_level <= current_level:
                print(SEPARATOR.join(current_row))
