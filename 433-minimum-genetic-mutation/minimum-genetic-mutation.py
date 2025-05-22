class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque()
        bank = set(bank)
        queue.append(startGene)
        visited = set()
        visited.add(startGene)

        steps = 0

        while queue:

            for _ in range(len(queue)):

                gene = queue.popleft()

                if gene == endGene:
                    return steps
                

                for ch in ['A','C','G','T']:

                    for i in range(len(gene)):
                        new_gene = gene[:i] + ch + gene[i + 1:]

                        if new_gene in bank and new_gene not in visited:

                            queue.append(new_gene)
                            visited.add(new_gene)

            
            steps += 1

        
        return -1

                


        