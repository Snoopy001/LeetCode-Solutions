# Time: O(|V| + |E| + 4^(maxTime/min(times))) = O(|V| + |E| + 4^10)
# Time: O(|V| + |E|) = O(|V| + |E|)

class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :type values: List[int]
        :type edges: List[List[int]]
        :type maxTime: int
        :rtype: int
        """
        def iter_dfs(adj):
            lookup, lookup2 = [0]*len(adj), set()
            result = 0
            stk = [(1, (0, maxTime, 0))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, time, total = args
                    lookup[u] += 1
                    if lookup[u] == 1:
                        total += values[u]
                    if not u:
                        result = max(result, total)
                    stk.append((4, (u,)))
                    for v, t in reversed(adj[u]):
                        if (u, v) in lookup2 or time < t:
                            continue
                        stk.append((3, (u, v)))
                        stk.append((1, (v, time-t, total)))
                        stk.append((2, (u, v)))
                elif step == 2:
                    u, v = args
                    lookup2.add((u, v))
                elif step == 3:
                    u, v = args
                    lookup2.remove((u, v))
                elif step == 4:
                    u = args[0]
                    lookup[u] -= 1
            return result

        adj = [[] for _ in xrange(len(values))]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        return iter_dfs(adj)


# Time: O(|V| + |E| + 4^(maxTime/min(times))) = O(|V| + |E| + 4^10)
# Time: O(|V| + |E|) = O(|V| + |E|)
class Solution2(object):
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :type values: List[int]
        :type edges: List[List[int]]
        :type maxTime: int
        :rtype: int
        """
        def dfs(values, adj, u, time, total, lookup, lookup2, result):
            lookup[u] += 1
            if lookup[u] == 1:
                total += values[u]
            if not u:
                result[0] = max(result[0], total)
            for v, t in adj[u]:
                if (u, v) in lookup2 or time < t:
                    continue
                lookup2.add((u, v))
                dfs(values, adj, v, time-t, total, lookup, lookup2, result)
                lookup2.remove((u, v))
            lookup[u] -= 1

        adj = [[] for _ in xrange(len(values))]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        result = [0]
        dfs(values, adj, 0, maxTime, 0, [0]*len(adj), set(), result)
        return result[0]