class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        # create a tree, if there is already a root, append it to the tree
        # if root does not exist, then create a new root

        folder_set = set(folder)
        result = []

        for f in folder:

            result.append(f)

            for i in range(len(f)):

                if f[i] == "/" and f[:i] in folder_set:

                    result.pop()
                    break

        return result
                





        
        