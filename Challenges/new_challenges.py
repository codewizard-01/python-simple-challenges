"""
You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment, so you decided to take the
opportunity to go for a short walk. The city provides its citizens with a Walk
Generating App on their phones -- everytime you press the button it sends you an
array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
You always walk only a single block for each letter (direction) and you know it takes
you one minute to traverse one city block, so create a function that will return true
if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!)
and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters
('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

"""


def is_valid_walk(walk):
    # determine if walk is valid
    s = 0
    n = 0
    w = 0
    e = 0

    for i in walk:
        print(i)
        if i == "s":
            s += 1
        elif i == "n":
            n += 1
        elif i == "w":
            w += 1
        elif i == "e":
            e += 1

    if len(walk) == 10 and n == s and w == e:
        return True
    else:
        return False


# is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), False, 'should return False'
# is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), True, 'should return True'
