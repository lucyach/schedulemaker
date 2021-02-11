domains = {}
domains["history"] = [3, 4, 5]
domains["science"] = [3, 4]
domains["math"] = [1, 4, 5]
domains["english"] = [1, 2, 3]
domains["spanish"] = [1, 2, 4, 5]

def isConsistent(assignments):
  if not assignments:
    return False
  # checks if two classes have been scheduled in the same period
  for i in assignments.keys():
    for j in assignments.keys():
      if assignments[j] == assignments[i] and j != i:
        return False
  # checks if history is right after english
  if "history" in assignments and "english" in assignments:  
    if assignments["history"] != assignments["english"] + 1:
      return False
  # checks if math is right after science
  if "math" in assignments and "science" in assignments:  
    if assignments["math"] != assignments["science"] + 1:
      return False
  return True

def selectVar(assignments):
  notAssigned = []
  for var in domains.keys():
    if var not in assignments.keys():
      notAssigned.append(var)
  nextVar = notAssigned[0]
  for var in notAssigned:
    if len(domains[var]) < len(domains[nextVar]):
      nextVar = var
  return nextVar

def recursiveBacktracking(assignments):
  if len(assignments) == len(domains):
    return assignments
  var = selectVar(assignments)
  for value in domains[var]:
    newAssignments = assignments.copy()
    newAssignments[var] = value
    if isConsistent(newAssignments):
      result = recursiveBacktracking(newAssignments)
      if isConsistent(result):
        return result

def backtrackingSearch():
  return recursiveBacktracking({})
  
print backtrackingSearch()