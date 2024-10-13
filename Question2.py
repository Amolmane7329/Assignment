# Function to find the Longest Common Subsequence (LCS)
def lcs(str1, str2, m, n):
    # Create a DP table to store lengths of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

# Function to calculate minimum deletions and insertions
def min_operations(str1, str2):
    m = len(str1)
    n = len(str2)

    # Find LCS of str1 and str2
    lcs_length = lcs(str1, str2, m, n)

    # Minimum deletions = characters in str1 that are not part of LCS
    deletions = m - lcs_length

    # Minimum insertions = characters in str2 that are not part of LCS
    insertions = n - lcs_length

    return deletions, insertions

# Test case
str1 = "heap"
str2 = "pea"

# Get the result
deletions, insertions = min_operations(str1, str2)

# Output the result
print(f"Minimum Deletions = {deletions}")
print(f"Minimum Insertions = {insertions}")

