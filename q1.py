"""
Q1: Stable Character

You are given a string `s`.

In this string, some characters may appear multiple times.

A character is called **stable** if all of its occurrences appear **together as
one continuous group**, without being interrupted by other characters.

Your task is to identify the **first stable character** you encounter when
reading the string from left to right.

If the string does not contain any stable character, return `None`.

Examples:
---------
Input: "aaabccddde"  → Output: 'a'
Input: "abccba"      → Output: 'c'
Input: "aabbcc"      → Output: 'a'
Input: "abc"         → Output: None
Input: "a"           → Output: None

Explanation:
- In "abccba", 'c' appears at positions 2,3 (continuous), while 'a' and 'b'
  are interrupted
- Single character occurrences are not considered stable (must appear at least
  twice)
"""


def first_stable_character(s):
    """
    Find the first stable character in the string.

    A character is stable if:
    1. It appears at least twice
    2. All occurrences are in one continuous group

    Args:
        s (str): Input string

    Returns:
        str or None: First stable character, or None if no stable character exists

    Examples:
        >>> first_stable_character("abccba")
        'c'
        >>> first_stable_character("abc")
        None
        >>> first_stable_character("a")
        None
    """
    # TODO: Implement your solution here
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    char_positions = {}
    for i, char in enumerate(s):
        if char not in char_positions:
            char_positions[char] = [i, i]
        else:
            char_positions[char][1] = i
    
    for i, char in enumerate(s):
        if char_count[char] >= 2: 
            first_pos, last_pos = char_positions[char]
          
            if i == first_pos:
            
                if last_pos - first_pos + 1 == char_count[char]:
                    return char
    
    return None
    

if __name__ == "__main__":
    # Test your solution here
    print(first_stable_character("abccba"))  # Should print: c
    print(first_stable_character("abc"))     # Should print: None
    print(first_stable_character("a"))       # Should print: None
