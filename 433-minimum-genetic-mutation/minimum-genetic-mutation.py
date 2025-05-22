class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        #Bidirectional BFS

        if endGene not in bank:
            return -1
        
        startSet = set()
        startSet.add(startGene)
        endSet = set()
        endSet.add(endGene)

        visited = set()
        visited.add(startGene)
        gene_set = ['A','C','G','T']

        steps = 0

        while startSet and endSet:

            if len(startSet) > len(endSet):
                startSet , endSet = endSet , startSet

            next_level = set()
            

            for gene in startSet:
                for i in range(len(gene)):
                    for ch in gene_set:
                        if gene[i] == ch:
                            continue
                        new_gene = gene[:i] + ch + gene[i + 1:]

                        if new_gene in endSet:
                            return steps + 1
                        if new_gene in bank and new_gene not in visited:
                            visited.add(new_gene)
                            next_level.add(new_gene)


            startSet = next_level
            steps += 1

        

        return -1

