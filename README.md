# Comparison of Paths using Depth-First Search (DFS) and Breadth-First Search (BFS)

In this analysis, we compared the results of running Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms on a given graph. We examined the different paths found by these two algorithms and explained why these paths were obtained.

### Paths using DFS:

Luke -> Leia -> Han -> Chewbacca -> DarthVader
Luke -> Leia -> Han -> DarthVader
Luke -> Leia -> Chewbacca -> Han -> DarthVader
Luke -> Leia -> Chewbacca -> DarthVader
Luke -> Leia -> DarthVader
Luke -> Han -> Leia -> Chewbacca -> DarthVader
Luke -> Han -> Leia -> DarthVader
Luke -> Han -> Chewbacca -> Leia -> DarthVader
Luke -> Han -> Chewbacca -> DarthVader
Luke -> Han -> DarthVader
Luke -> Chewbacca -> Leia -> Han -> DarthVader
Luke -> Chewbacca -> Leia -> DarthVader
Luke -> Chewbacca -> Han -> Leia -> DarthVader
Luke -> Chewbacca -> Han -> DarthVader
Luke -> Chewbacca -> DarthVader
Luke -> DarthVader

### Paths using BFS:

Luke -> DarthVader
Luke -> Leia -> DarthVader
Luke -> Han -> DarthVader
Luke -> Chewbacca -> DarthVader
Luke -> Leia -> Han -> DarthVader
Luke -> Leia -> Chewbacca -> DarthVader
Luke -> Han -> Leia -> DarthVader
Luke -> Han -> Chewbacca -> DarthVader
Luke -> Chewbacca -> Leia -> DarthVader
Luke -> Chewbacca -> Han -> DarthVader
Luke -> Leia -> Han -> Chewbacca -> DarthVader
Luke -> Leia -> Chewbacca -> Han -> DarthVader
Luke -> Han -> Leia -> Chewbacca -> DarthVader
Luke -> Han -> Chewbacca -> Leia -> DarthVader

In summary, DFS and BFS algorithms found different paths in the given graph. DFS explores each branch as deeply as possible before backtracking, which leads to longer paths in some cases. On the other hand, BFS explores all neighbors of a node before moving to their children, resulting in shorter paths. The choice of algorithm depends on the specific problem and the desired path-finding behavior.
