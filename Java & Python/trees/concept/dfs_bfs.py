def depthFirst(startingNode, soughtValue):
   visitedNodes = set()
   stack = [startingNode]
 
   while len(stack) > 0:
      node = stack.pop()
      if node in visitedNodes:
         continue
 
      visitedNodes.add(node)
      if node.value == soughtValue:
         return True
 
      for n in node.adjacentNodes:
         if n not in visitedNodes:
            stack.append(n)
   return False

""""""""""""""""""""""""""""""""""""""""""

from collections import deque
 
def breadthFirst(startingNode, soughtValue):
   visitedNodes = set()
   queue = deque([startingNode])
 
   while len(queue) > 0:
      node = queue.pop()
      if node in visitedNodes:
         continue
 
      visitedNodes.add(node)
      if node.value == soughtValue:
         return True
 
      for n in node.adjacentNodes:
         if n not in visitedNodes:
            queue.appendleft(n)
           # 
   return False