"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def helper(root):
            if root == None:
                return ''
            ret = str(root.val) + ' '
            if root.children:
                ret += '[ '
                for c in root.children:
                    ret += helper(c)
                ret += '] '
            return ret
        ret = helper(root)
        return ret.rstrip(' ')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """     
        def helper(idx, data):
            root, i = None, idx
            if i >= len(data):
                return root, i
            
            if data[i].isdigit():
                root = Node(int(data[i]), [])
                if i+1 < len(data) and data[i+1] != '[':
                    return root, i
                i = i + 2
                while i < len(data):
                    if data[i] == ']':
                        return root, i
                    child, i = helper(i, data)
                    root.children.append(child)
                    i += 1
            return root, i
  
        data = data.split(' ')
        root, _ = helper(0, data)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
