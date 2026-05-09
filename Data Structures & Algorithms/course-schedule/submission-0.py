class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_map = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            pre_map[course].append(prereq)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                # ah ugh: CYCLE!
                return False

            if pre_map[course] == []:
                return True
            
            visiting.add(course)

            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            pre_map[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True