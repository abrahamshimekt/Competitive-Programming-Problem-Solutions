class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        reps = {}
        sizes = {}
        names = {}

        for account in accounts:
            name = account[0]
            for index in range(1,len(account)):
                reps[account[index]] = account[index]
                sizes[account[index]] = 1
                names[account[index]] = name

        def find(email):
            while email != reps[email]:
                email = reps[email]
            return email

        def union(email1,email2):
            rep1 = find(email1)
            rep2 = find(email2)
            if rep1 != rep2:
                if sizes[rep1] < sizes[rep2]:
                    reps[rep1] = rep2
                elif sizes[rep2] < sizes[rep1]:
                    reps[rep2] = rep1
                else:
                    reps[rep1] = rep2
                    sizes[rep2] +=1

        for account in accounts:
            for index in range(1,len(account)-1):
                union(account[index],account[index+1])

        repsToEmail = defaultdict(set)
        for account in accounts:
            for index in range(1,len(account)):
                rep = find(account[index])
                repsToEmail[rep].add(account[index])
        ans = []
        for rep,emails in repsToEmail.items():
            account = [names[rep]]
            account += sorted(emails)
            ans.append(account)
        return ans

