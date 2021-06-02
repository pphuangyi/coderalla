# Shortest Path Problem
## Dijkstra
1. Dijkstra algorithm algorithm can be generalized to use any labels that ar partially ordered, provided the subsequent labels are monotonically non-decreasing. The generalization is called _generic Dijkstra shortest path algorithm_.
### Run time
1. with min-priority queue: $\Theta\left((|V| + |E|)\log|V|\right)$;
2. with array $\Theta\left(|V|^2\right)$ (Leyzorek et al. 1957?);
3. with Fibonacci heap min-priority queue $\Theta\left(|E| + |V|\log|V|\right)$ (Fredman & Tarjan 1984);