import heapq

class Node:
    
    def __init__(self,data,freq):
        self.data=data
        self.freq=freq
        self.left=None
        self.right=None
        
    def __lt__(self,other):
        return self.freq < other.freq
    
class Huffman:
    
    def print_codes(self,root,code):
        if root is None:
            return
        if (root.data) != "$":
            print(f"{root.data} : {code}")
            
        self.print_codes(root.left,code+"0")
        self.print_codes(root.right,code+"1")
        
    def build(self,data,freq):
        min_heap=[]
        for i in range(len(data)):
            heapq.heappush(min_heap,Node(data[i],freq[i]))
            
        while (len(min_heap)>1):
            left=heapq.heappop(min_heap)
            right=heapq.heappop(min_heap)
            temp=Node("$",left.freq+right.freq)
            temp.left=left
            temp.right=right
            heapq.heappush(min_heap,temp)
            
        self.print_codes(min_heap[0],"")
        
#data=["A","B","C","D","E","F"]
data=input("Enter the data with spaces : ").split()
#freq=[5,9,12,13,16,45]
freq=list(map(int,input("Enter the frequencies with spaces : ").split()))
huff=Huffman()
huff.build(data,freq)