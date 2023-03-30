'''Given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.
Return null if there is no such ordering.
For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].'''

def course_ordering(courses):
    # Create a set to store visited courses and a stack to store the ordering
    visited = set()
    ordering = []
    
    # Define a recursive helper function to visit each course and its prerequisites
    def dfs(course):
        # If the course has already been visited, return
        if course in visited:
            return
        
        # Mark the course as visited
        visited.add(course)
        
        # Recursively visit each of the course's prerequisites
        for prereq in courses[course]:
            dfs(prereq)
        
        # Add the course to the ordering
        ordering.append(course)
    
    # Visit each course
    for course in courses:
        dfs(course)
    
    # If the ordering is not the same size as the number of courses, there must be a cycle
    if len(ordering) != len(courses):
        return None
    
    # Return the ordering (since we added courses to the ordering in reverse order)
    return list((ordering))
