def spy_game(nums):
    a = []
    checker = [0, 0, 7]
    for i in range(len(nums)):
        nums[i] = int(nums[i])
        if nums[i] == 0:
            if nums[i] not in a:
                a.append(nums[i])
            elif len(a) == 1:
                a.append(nums[i])
        elif nums[i] == 7:
            if nums[i] not in a:
                a.append(nums[i])
    print(True) if a == checker else print(False)              

spy_game([1,2,4,0,0,7,5]) #--> True
spy_game([1,0,2,4,0,5,7]) #--> True
spy_game([1,7,2,0,4,5,0]) #--> False
spy_game(input().split())