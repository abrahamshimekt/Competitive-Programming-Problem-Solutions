def merge(self, intervals):
        intervals.sort()
        output = []
        for interval in intervals:
            if not output or interval[0] > output[-1][1]:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1],interval[1])
                
        return output 