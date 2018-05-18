class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path == "/../":
            return "/"
        stack = []
        tokens = path.split("/")
        for token in tokens:
            if token == ".." and stack:
                stack.pop()
            elif token != ".." and token != "." and token:
                stack.append(token)
        return "/" + "/".join(stack)
