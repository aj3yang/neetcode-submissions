class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()

        prereqs = defaultdict(list)

        for course, pre in prerequisites:
            prereqs[course].append(pre)
        print(prereqs)

        def dfs(node):

            if node in path:
                return False
            if prereqs[node] == []:
                return True

            path.add(node)
            for prereq in prereqs[node]:
                if not dfs(prereq):
                    return False

            path.remove(node)
            prereqs[node] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True