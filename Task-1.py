def find_starting_index(food, people):
    tf = sum(food)
    tp = sum(people)
    if tf != tp:
        return -1
    n = len(food)
    cf = 0
    st = 0
    for i in range(n):
        cf += food[i] - people[i]
        if cf < 0:
            st = i + 1
            cf = 0
    return st if cf >= 0 else -1
food_input = input()
food = [int(x) for x in food_input.split()]
people_input = input()
people = [int(x) for x in people_input.split()]
print(find_starting_index(food, people))


