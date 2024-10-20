class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        operation = []
        elements = []

        ops = set(['!', '&', '|'])

        for c in expression:
            if c in ops:
                operation.append(c)
                elements.append([])
            elif c == 't' or c == 'f':
                elements[-1].append(c)
            elif c == ')':
                op = operation.pop()
                el = elements.pop()
                res = self.evaluate(op, el)
                if elements:
                    elements[-1].append('t' if res else 'f')
                else:
                    return res

        return False    # shouldn't happen
    

    def evaluate(self, op: str, el: list[str]) -> bool:
        if op == '|':
            for e in el:
                if e == 't':
                    return True
            return False
        elif op == '&':
            for e in el:
                if e == 'f':
                    return False
            return True
        else:   # op == '!'
            return el[0] == 'f'
