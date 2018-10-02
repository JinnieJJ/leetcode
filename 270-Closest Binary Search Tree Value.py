gap = float("inf")
        closest = float("inf")
        while root:
            if abs(root.val - target) < gap:
                gap = abs(root.val - target)
                closest = root
            if target == root.val:
                break
            elif target < root.val:
                root = root.left
            else:
                root = root.right
        return closest.val
