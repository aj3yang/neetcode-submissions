class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        in_degrees = [0] * numCourses
        for i in prerequisites:
            pre, crs = i[1], i[0]
            adj_list[pre].append(crs)
            in_degrees[crs] += 1

        q = deque()

        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                q.append(i)
        ans = 0
        while q:
            node = q.popleft()
            ans += 1
            for i in adj_list[node]:
                in_degrees[i] -= 1
                if in_degrees[i] == 0:
                    q.append(i)

        if ans != numCourses:
            return False
        else:
            return True

            
        

  
