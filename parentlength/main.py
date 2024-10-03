 #!python3

import random
from line_profiler import LineProfiler

class Solution:
    def count_max_pairs_osstack(self, instr, balanced):
        if len(instr) == 0:
            return 0, "", balanced
        pairs = 0
        while instr[0] != ")":
            sub_pairs, left, sub_balanced = self.count_max_pairs(instr[1:], False)
            if sub_balanced:
                pairs += sub_pairs
            else:
                pairs = max(pairs, sub_pairs)
            instr = left

            if len(instr) == 0:
                break

        if len(instr) == 0:
            return pairs, instr, balanced

        if instr[0] == ")":
            if balanced:
                sub_pairs, left, sub_balanced = self.count_max_pairs(instr[1:], True)
                return max(pairs, sub_pairs), left, sub_balanced
            else:
                return pairs+1, instr[1:], True

    def count_max_pairs_nostack(self, instr):
        heights = {}
        floor = 0
        sz = len(instr)
        i = 0
        stack = 0
        run = 0
        max_run = 0
        while i < sz:
            if instr[i] == '(':
                stack += 1
                heights[stack] = i
            if instr[i] == ')':
                stack -= 1

            if stack >= floor:
                run += 1

            if stack < floor:
                max_run = max(run, max_run)
                stack = 0
                run = 0
                floor = stack

            i += 1

        if stack > 0:
            end = sz-1
            max_subrun = 0
            while stack > 0:
                stair_start = heights[stack]
                subrun = end-stair_start
                #print(f"s:{stack}, end:{end}, start:{stair_start}, sub:{subrun}, max:{max_subrun}, run:{run}")
                if subrun == 0:
                    run -= 1
                else:
                    max_subrun = max(max_subrun, subrun)
                    run -= subrun+1
                stack -= 1
                end = stair_start-1
                #print(f"s:{stack}, end:{end}, start:{stair_start}, sub:{subrun}, max:{max_subrun}, run:{run}", "asdfasdfasf")
            run = max(run,max_subrun)
        return max(max_run, run)

    def count_max_pairs_osstack_simple(self, instr, stack_sz):
        if instr[0] == ')':
            if stack_sz > 0:
                return 0, instr, stack_sz
            else:
                return self.count_max_pairs_osstack_simple(instr[1:], 0)
        else:
            sz_b4 = len(instr)
            subrun, left, stack_sz_new = count_max_pairs_osstack_simple(instr, stack_sz+1)
            if left[0] == ')':
                return sz_b4-len(left), left[1:], stack_sz_new-1
            else:
                return subrun, left, stack_sz_new

    def count_max_pairs_fwdbck(self, instr):
        floor = 0
        sz = len(instr)
        stack = 0
        run = 0
        max_run = 0
        for i in range(0,sz):
            if instr[i] == '(':
                stack += 1
            else:
                stack -= 1

            if stack >= floor:
                run += 1

            if stack <= floor:
                max_run = max(run, max_run)

            if stack < floor:
                stack = 0
                run = 0
                floor = stack

        run = 0
        stack = 0
        floor = 0
        for i in range(sz-1,0,-1):
            if instr[i] == ')':
                stack += 1
            else:
                stack -= 1

            if stack >= floor:
                run += 1

            if stack <= floor:
                max_run = max(run, max_run)

            if stack < floor:
                stack = 0
                run = 0
                floor = stack
            i -= 1

        return max_run

    def count_max_pairs_stack(self, instr):
        stack = []
        stack.append(-1)
        sz = len(instr)
        answer = 0
        i = 0
        while i < sz:
            #print(f"star ans: {answer}, s: {stack}, i:{i}, str: {instr[i:]}")
            if instr[i] == '(':
                stack.append(i)
                #print(f"open ans: {answer}, s: {stack}, i:{i}")
            else:
                stack.pop();
                #print(f"clos ans: {answer}, s: {stack}, i:{i}")
                if len(stack) == 0:
                    stack.append(i)
                    #print(f"szer ans: {answer}, s: {stack}, i: {i}")
                else:
                    answer = max(answer, i - stack[-1])
                    #print(f"spos ans: {answer}, s: {stack}, i: {i}, top: {stack[-1]}")
            i += 1
        return answer

    def count_max_pairs_smallstack(self, instr):
        stack = 0
        runs = [(0,0)]
        max_run = 0
        sz = len(instr)
        for p in instr:
            if p == "(":
                stack += 1
            else:
                stack -= 1

                if stack < 0:
                    for r in runs:
                        max_run = max(r[1], max_run)
                    stack = 0
                    runs = [(0,0)]
                    continue

                top_depth = runs[-1][0]
                if stack > top_depth: #add new run
                    runs.append((stack,1))

                elif stack == top_depth: #add to run
                    runs[-1] = (runs[-1][0], runs[-1][1]+1)


                else: #collapse run
                    runs[-1] = (stack, runs[-1][1]+1)
                    while top_depth-1 == stack:
                        try:
                            if runs[-2][0] == runs[-1][0]:
                                runs[-2] = (runs[-1][0], runs[-2][1]+runs[-1][1])
                                runs.pop()
                                top_depth = runs[-1][0]
                            else:
                                break
                        except IndexError:
                            break

        for r in runs:
            max_run = max(r[1], max_run)

        return max_run

    def count_max_pairs_matching_fwdback(self, s):
        left = right = ans = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, left+right)
            if right > left:
                right = left = 0
        left = right = 0
        for c in s[::-1]:
            if c == ')':
                right += 1
            else:
                left += 1
            if left == right:
                ans = max(ans, left + right)
            if left > right:
                right = left = 0
        return ans

    def count_max_pairs_fwdbck(self, instr):
        floor = 0
        sz = len(instr)
        stack = 0
        run = 0
        max_run = 0
        for c in instr:
            if c == '(':
                stack += 1
            else:
                stack -= 1

            if stack >= floor:
                run += 1

            if stack <= floor:
                max_run = max(run, max_run)

            if stack < floor:
                stack = 0
                run = 0
                floor = stack

        run = 0
        stack = 0
        floor = 0
        for c in instr[::-1]:
            if c == ')':
                stack += 1
            else:
                stack -= 1

            if stack >= floor:
                run += 1

            if stack <= floor:
                max_run = max(run, max_run)

            if stack < floor:
                stack = 0
                run = 0
                floor = stack

        return max_run

    def count_max_pairs_fasteststack(self, s):
        stack = [-1]
        res = 0
        for index,char in enumerate(s):
            if char == '(':
                stack.append(index)
            else:
                last_index = stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    res = max(res, index - stack[-1])
        return res

    def explained(self, s: str) -> int:
        #each valid region is seperated by invalid regions, so we just have to compare the lengths of all the valid regions
        #the valid regions are defined as those whose graph of "(" - ")" is greater than or equal to zero
        #the zero points define the regions we need to actually compare.

        maxlength = 0
        l_count = 0
        leng = 0
        for i,p in enumerate(s):
            if p == "(":
                l_count += 1
                leng += 1
            if p == ")":
                l_count -= 1
                leng += 1
            if l_count == 0:
                maxlength = max(maxlength, leng)
            if l_count <0:
                leng = 0
                l_count = 0

        #now need to run it backwards from the end!
        backmaxlength = 0
        l_count = 0
        leng = 0

        for i in range(len(s)-1,-1, -1):
            p = s[i]
            if p == ")": #reverse which one matters
                l_count += 1
                leng += 1
            if p == "(":
                l_count -= 1
                leng += 1
            if l_count <0:
                backmaxlength = max(backmaxlength, leng-1) #subtract one cause we went under
                leng = 0
                l_count = 0

        return max(maxlength,backmaxlength)

    count_max_pairs = count_max_pairs_fwdbck
    def longestValidParentheses(self, s: str) -> int:
        ret = self.count_max_pairs(s)
        return ret/2


sol = Solution()

def main():
    instrs = [
        ('', 0),
        ('(', 0),
        (')', 0),
        ('()', 1),
        ('((', 0),
        ('))', 0),
        ('()()()', 3),
        ('(((((())))))', 6),
        ('(())', 2),
        ('(()', 1),
        (')()())', 2),
        ('())()()', 2),
        (')())()()()', 3),
        (')()()())()', 3),
        ('())', 1),
        ('((()', 1),
        ('((())', 2),
        ('()(()', 1),
        ('()(()()', 2),
        ('()()(()', 2),
        ('()()(()()()', 3),
        ('()(()()(()()()', 3),
        ('()()(()(()()()', 3),
        ('()()(()()()(()', 3),
        ('()()(((()))(()', 3),
        ('()(()()))()()()()()', 5),
        ('()(()()))()()', 4),
        ('(())(', 2)
    ]

    for instr in instrs:
        print(f"processing: '{instr[0]}'")
        pairs = sol.longestValidParentheses(instr[0])
        print(pairs, instr[1], pairs==instr[1])
        if pairs != instr[1]:
            print("ERRORERRORERRORERROR")
        else:
            print(f"########################")

par = ('(', ')')
rand_tests = []
for i in range(0,100):
    test = ""
    for j in range(0,3000):
        test += par[random.randrange(0,2)]
    rand_tests.append(test)

def profile():
    print("PROFILING")
    lp = LineProfiler()
    lp_wrapper = lp(sol.count_max_pairs)
    for instr in rand_tests:
        lp_wrapper(instr)
    lp.print_stats()

def bench():
    print("BENCHING")
    for instr in rand_tests:
        sol.longestValidParentheses(instr)
