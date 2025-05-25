class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        InDegree = defaultdict(int)

        for idx,ingredient_list in enumerate(ingredients):
            for idg in ingredient_list:
                graph[idg].append(recipes[idx])
                InDegree[recipes[idx]] += 1
        
        queue = deque()
        for y in supplies:
            queue.append(y)
        res = []

        while queue:

            node = queue.popleft()
            res.append(node)

            for nei in graph[node]:
                InDegree[nei] -= 1

                if InDegree[nei] == 0:
                    queue.append(nei)

        

        return [x for x in res if x in set(recipes)]




