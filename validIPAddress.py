class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        delimter = ""
        if "." in queryIP:
            delimter = "."
        else:
             delimter = ":"

        query = queryIP.split(delimter)

        if "" in query:
            return "Neither" 

        if delimter == ".":
            if len(query) != 4:
                return  "Neither"
            for ip in query:
                if not ip.isdigit() or len(ip) > 1 and ip[0] == "0" or int(ip) < 0 or  int(ip) > 255:

                    return "Neither"
            return "IPv4"
        else:
            if len(query) != 8:
                return  "Neither"
            for ip in query:
                if len(ip) > 4 :
                    return "Neither"
                for char in ip:
                    if not char.isdigit() and char.lower() not in 'abcdef':
                        return "Neither"
            return  "IPv6"

