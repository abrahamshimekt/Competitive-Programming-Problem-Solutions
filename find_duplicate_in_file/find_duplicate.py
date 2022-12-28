def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        length = len(paths)
        content_duplicate = {}

        # Each time chope the ith source by white space 
        # and find the root path
        for index in range(length):
            path = paths[index].split()
            root = path[0]
            path_length = len(path)

            # then concatenate the ith file path to the root path
            # and parse the content of the file by spliting the file using '('
            # add the content of the file as a key and add the paths in a list as a value 
            # inorder to check the duplication of content

            for indexx in range(1,path_length):
                curr_path = f'{root}/{path[indexx]}'.split('(')
                content = curr_path[-1]
                if content not in content_duplicate:
                    content_duplicate[content] =[curr_path[0]]
                else:
                     content_duplicate[content].append(curr_path[0])

        

        # for each content if the contents is duplicated, add it the duplicate files list 

        duplicate_files =[]
        for content in content_duplicate:
            if len(content_duplicate[content]) >1:
                duplicate_files.append(content_duplicate[content])
        return duplicate_files