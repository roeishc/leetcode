class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        muls = []
        running_mul = 1
        stack = [1]

        idx = len(formula) - 1
        curr_number = ""

        while 0 <= idx:
            if formula[idx].isdigit():      # is a digit
                curr_number += formula[idx]
            elif formula[idx].isalpha():    # not a digit
                curr_number = ""
            elif formula[idx] == ")":
                curr_multiplier = int(curr_number[::-1]) if curr_number else 1
                running_mul *= curr_multiplier
                stack.append(curr_multiplier)
                curr_number = ""
            elif formula[idx] == "(":
                running_mul //= stack.pop()
                curr_number = ""
            
            muls.append(running_mul)
            idx -= 1

        muls = muls[::-1]

        final_map = defaultdict(int)

        idx = 0
        while idx < len(formula):
            if formula[idx].isupper():
                curr_atom = formula[idx]
                curr_count = ""
                idx += 1
                while idx < len(formula) and formula[idx].islower():    # get the atom (lower and upper case)
                    curr_atom += formula[idx]
                    idx += 1
                while idx < len(formula) and formula[idx].isdigit():    # get atom's count
                    curr_count += formula[idx]
                    idx += 1
                if curr_count:
                    final_map[curr_atom] += int(curr_count) * muls[idx - 1]
                else:
                    final_map[curr_atom] += muls[idx - 1]
            else:
                idx += 1

        final_map = dict(sorted(final_map.items()))

        res = ""
        for atom, count in final_map.items():
            res += atom
            if count > 1:
                res += str(count)

        return res
                
