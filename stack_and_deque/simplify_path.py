# https://leetcode.com/problems/simplify-path/description/?envType=problem-list-v2&envId=stack&
# 71. Simplify Path

def simplifyPath(path):
        """
        :type path: str
        :rtype: str
        """

        path = path.split('/')

        correct_path = []

        for dir in path:

            if dir in ('..', '.', ''):
                if dir == '..' and correct_path:
                    correct_path.pop()
            else:
                correct_path.append(dir)

        return '/' + '/'.join(correct_path) if correct_path else '/'


path = input()
print(simplifyPath(path))