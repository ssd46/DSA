class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False

        st=[]
        for i in range(len(s)):
            if(s[i] in '({['):
                st.append(s[i])
            elif (st and ((st[-1] == '(' and s[i] == ')') or
             (st[-1] == '{' and s[i] == '}') or
              (st[-1] == '[' and s[i] == ']'))):
                st.pop()
            else:
                return False
        if(not st):
            return True
        else:
            return False


        