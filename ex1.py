def find(s, n):
    hash_map = {}
    
    for i in range(len(s)):
        complement = n - s[i]
        
        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[s[i]] = i
    
    return None
