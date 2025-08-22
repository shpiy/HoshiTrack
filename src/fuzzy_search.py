def calculate_distance(s1, s2):
    '''Calculates the Levenshtein distance between two strings.'''
    m, n = len(s1), len(s2)

    # Initializes a matrix (list of lists) to store distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initializes the first row and column
    # The distance from an empty string to a string of length i is i
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1

            # The value of each cell is the minimum of the three operations
            # (deletion, insertion, substitution) plus the cost
            dp[i][j] = min(dp[i - 1][j] + 1, # Deletion
                           dp[i][j - 1] + 1, # Insertion
                           dp[i - 1][j - 1] + cost) # Substitution
            
            # The final value in the bottom-right cell is the Levenshtein distance
            return dp[m][n]
        
def find_best_matches(query, df_column, tolerance=2):
    '''
    Finds all items in a DataFrame column that are within the
    Levenshtein distance tolerance for a given query.
    '''
    matches = []
    # Make sure we don't search an empty or invalid column
    if df_column.empty or not hasattr(df_column, 'str'):
        return matches
    
    for index, title in df_column.items():
        # Compare in lowercase for case-insensitive search
        distance = calculate_distance(query.lower(), str(title).lower())

        if distance <= tolerance:
            matches.append({
                'index': index,
                'title': title,
                'distance': distance
            })

        # Sort matches by distance, so the closest ones are first
        return sorted(matches, key=lambda x: x['distance'])