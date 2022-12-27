def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        sumdomains = {}
        for subdomain in cpdomains:
            list_subdomain = subdomain.split()
            cp = int(list_subdomain[0])
            list_subdomain = list_subdomain[1].split('.')
            for index in range(len(list_subdomain)):
                if '.'.join(list_subdomain[index:]) not in sumdomains:
                    sumdomains[ '.'.join(list_subdomain[index:])] = cp
                else:
                     sumdomains[ '.'.join(list_subdomain[index:])] += cp
        output = []
        for subd in sumdomains:
            cp_domains = f'{str(sumdomains[subd])} {subd}'
            output.append(cp_domains)
        return output