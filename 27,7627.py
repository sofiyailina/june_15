with open('27_A_7627.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    nums = [int(line) for  line in f]
maxsum = 0
for i in range(len(nums)):
    for j in range(i+k, len(nums)):
        s = nums[i] + nums[j]
        maxsum = max(maxsum, s)

print(maxsum)