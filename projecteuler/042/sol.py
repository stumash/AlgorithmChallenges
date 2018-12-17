from typing import Iterator
from math import sqrt, ceil, floor

def main():
    words = get_words()
    print(sum(1 for w in words if is_triangle_word(w)))

def is_triangle_word(s: str) -> bool:
    return is_triangle_number(word_value(s))

def is_triangle_number(n: int) -> bool:
    double = int(2 * n)
    sqrt_double = sqrt(double)
    low, high = floor(sqrt_double), ceil(sqrt_double)
    return low != high and low*high == double

def word_value(s: str) -> int:
    return sum(char_value(c) for c in s)

def char_value(c: str) -> int:
    return ord(c) - ord('A') + 1

def get_words() -> Iterator[str]:
    with open('words.txt', 'r') as f:
        text = f.read()
    quoted_words = text.split(',')
    return (s.strip('\"') for s in quoted_words)

if __name__ == "__main__":
    main()
