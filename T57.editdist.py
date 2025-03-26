def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Create a table to store results of sub-problems
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Initialize the table
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,      # Deletion
                               dp[i][j - 1] + 1,      # Insertion
                               dp[i - 1][j - 1] + cost)  # Substitution
    
    return dp[m][n]

# Example usage:
str1 = "kitten"
str2 = "sitting"
print("Edit distance:", edit_distance(str1, str2))
