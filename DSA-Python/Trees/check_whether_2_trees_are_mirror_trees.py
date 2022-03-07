# https://practice.geeksforgeeks.org/problems/two-mirror-trees/1/?page=8&category[]=Tree&sortBy=submissions
# https://www.youtube.com/watch?v=9jH2L2Ysxko

class Solution:
    def areMirror(self,root1,root2):
        '''
        :param root1,root2: two root of the given trees.
        :return: True False
        
        '''
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.data == root2.data:
            if (self.areMirror(root1.left,root2.right) and self.areMirror(root1.right,root2.left)):
                return True
        return False