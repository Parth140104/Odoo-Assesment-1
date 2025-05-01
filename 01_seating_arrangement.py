from itertools import permutations

def find_circular_seating(guests):
    names = list(guests.keys())
    n = len(names)

    for seating in permutations(names):
        valid = True
        for i in range(n):
            person = seating[i]
            left = seating[(i - 1) % n]
            right = seating[(i + 1) % n]
            preferred_neighbors = set(guests[person])
            actual_neighbors = {left, right}
            if preferred_neighbors != actual_neighbors:
                valid = False
                break
        if valid:
            return list(seating)
    
    return "No valid seating arrangement possible."

guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

result = find_circular_seating(guests)
print(result)
