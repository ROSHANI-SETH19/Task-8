def max_product(nums):
    if not nums:
        return 0

    max_dp = [0] * len(nums)
    min_dp = [0] * len(nums)
    max_dp[0] = min_dp[0] = result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_dp[i] = max(nums[i], min_dp[i-1] * nums[i])
            min_dp[i] = min(nums[i], max_dp[i-1] * nums[i])
        else:
            max_dp[i] = max(nums[i], max_dp[i-1] * nums[i])
            min_dp[i] = min(nums[i], min_dp[i-1] * nums[i])

        result = max(result, max_dp[i])

    return result

# Example usage:
nums = [2, 3, -2, 4]
print("Maximum subarray product:", max_product(nums))  # Output: 6

nums = [-2, 0, -1]
print("Maximum subarray product:", max_product(nums))  # Output: 0
