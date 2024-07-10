import itertools

nums = [10, 7, 11, 2]
target = 9

# Generate all combinations of indices
combinations = itertools.combinations(range(len(nums)), 2)


output = []

for comb in combinations:
    if nums[comb[0]] + nums[comb[1]] == target:
        output.append(comb)

print(output)
