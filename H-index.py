class Solution:
    def hIndex(self, citations: List[int]) -> int:
        containers = [0] * (len(citations) +1)
        for citation in citations:
            containers [min(citation, len(citations))] +=1
        papers = 0
        for container in range(len(containers)-1,-1,-1):
            papers += containers[container]
            if papers >= container:
                return container