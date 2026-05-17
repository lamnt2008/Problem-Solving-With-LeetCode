class HitCounter:

    def __init__(self):
        self.timestamps = []


    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        l, r = 0, len(self.timestamps)
        while l < r:
            mid = l + (r - l) // 2
            if self.timestamps[mid] <= timestamp - 300: 
                l = mid + 1
            else:
                r = mid
        
        
                
        return len(self.timestamps) - l 

            
        