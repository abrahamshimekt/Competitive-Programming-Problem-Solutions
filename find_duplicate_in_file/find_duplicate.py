def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        length = len(paths)
        content_duplicate = {}
        for index in range(length):
            path = paths[index].split()
            root = path[0]
            path_length = len(path)
            for indexx in range(1,path_length):
                curr_path = f'{root}/{path[indexx]}'.split('(')
                content = curr_path[-1]
                if content not in content_duplicate:
                    content_duplicate[content] =[curr_path[0]]
                else:
                     content_duplicate[content].append(curr_path[0])
        duplicate_files =[]
        print(content_duplicate)
        for content in content_duplicate:
            if len(content_duplicate[content]) >1:
                duplicate_files.append(content_duplicate[content])
        return duplicate_files