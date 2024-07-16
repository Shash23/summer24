def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        return nums[len(nums) // 2]
    
    

def build_hierarchy(pairs):
    
    hierarchy = defaultdict(list)
    for employee, manager in pairs:
        hierarchy[manager].append(employee)
    return hierarchy

def find_levels(hierarchy, start, end):
    from collections import deque
    
    # BFS to find the shortest path between start and end
    queue = deque([(start, 0)])
    visited = set()
    
    while queue:
        current, level = queue.popleft()
        
        if current == end:
            return level
        
        visited.add(current)
        
        for subordinate in hierarchy[current]:
            if subordinate not in visited:
                queue.append((subordinate, level + 1))
    
    return -1  # In case there is no connection

def main():
    
    data = input().strip().split('\n')
    to_compare = data[0].split('/')
    pairs = [tuple(line.split('/')) for line in data[1:]]
    
    tree = build_tree(pairs)
    start, end = to_compare
    levels = find_levels(tree, end, start)
    
    print(levels)

if __name__ == "__main__":
    main()