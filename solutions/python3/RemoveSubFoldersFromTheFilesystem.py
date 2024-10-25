class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folders_set = set(folder)
        res = []

        for path in folder:
            names = path.split("/")
            if len(names) == 2: # string in the form of "/name" (one folder only)
                res.append(path)
                continue

            temp = ""
            delete = False
            for i in range(1, len(names) - 1):
                temp += "/" + names[i]
                if temp in folders_set:
                    delete = True
                    break
            
            if not delete:
                res.append(path)

        return res
