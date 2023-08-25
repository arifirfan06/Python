# 1. At least 8 character long
# 2. contain any short letter, numbers $%#@
# 3. has to end with number

import re
user_input = 'voltiezzza%8'
pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
re_validation = pattern.fullmatch(user_input)
print(re_validation)