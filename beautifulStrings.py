# Problem:
# String s is called unique if all the characters of s are different.
# String s2 is producible from string s1 if we can remove some characters of s1
# to obtain s2.
# String s1 is more beautiful than string s2 if s1 is longer than s2 or
# they have equal length and s1 is lexicographically greater than s2.
# Given a string s find the most beautiful unique string producible from s.

# Solution:
# Obvioulsy we want exactly one representative of each character in the input.
# Suppose for concreteness that the alphabet is a-z.  We must pick the last 'a'
# in the string.  If there is a 'b' before the 'a' that we pick, we must pick
# the last such.  Otherwise, pick the last 'b' in the string.  Having chosen k
# letters, they divide the original string into k+1 subtrings.  For the (k+1)st
# letter, choose the last occurrence in the first substring it appears in.
#

# We will take the non-whitespace printable ASCII characters as the alphabet.
# These are ! (hex 21) through ~ (hex 7E).

from collections import defaultdict

def beaut(input):
    index = defaultdict(list)
    for idx, char in enumerate(input):
        index[char].append(idx)
    found = [len(input)]
    for seek in map(chr, range(0x21, 0x7f)):
        if not index[seek]: continue
        r = [f for f in found if f > index[seek][0]][0]

        # r is right-hand endpoint of first substring containing seek,
        # so we want the largest element of index[seek] that is less than r

        p = [x for x in index[seek] if x < r][-1]
        found.append(p)
        found.sort()

    return ''.join([input[k] for k in found[:-1]])

def main():
    with open("beauts.txt", 'w') as fout:
        with open("strings.txt") as fin:
            for line in fin:
                fout.write(beaut(line))

if __name__ == '__main__':
    main()