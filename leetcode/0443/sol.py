from typing import List

class Solution():
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 0:
            return 0

        write_i = 0
        curr = chars[0]
        curr_count = 1

        def write():
            nonlocal write_i, curr, curr_count
            chars[write_i] = curr
            write_i += 1

            if curr_count > 1:
                digits = [digit for digit in str(curr_count)]
                chars[write_i : write_i + len(digits)] = digits
                write_i += len(digits)

            curr = c
            curr_count = 1

        for read_i in range(1, n):
            c = chars[read_i]

            if c == curr:
                curr_count += 1
            else:
                write()
        write()

        return write_i

lets = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
print('letters: {}'.format(lets))

print(Solution().compress(lets))
print('letters: {}'.format(lets))
