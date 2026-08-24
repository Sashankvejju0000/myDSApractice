class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        stack=[]
        answer=[0]*n #[0,0,0,0,0,0,0,0,]
        for i in range(n):# motham array iterate chai
            while stack and temperatures[i]>temperatures[stack[-1]]:#current element stack lo unna top index kanna pedada 
                previous=stack.pop()  #element index stack 
                answer[previous]=i-previous #distnace calculate
            stack.append(i) # current index push 
        return answer