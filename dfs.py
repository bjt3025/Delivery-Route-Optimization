def dijkstra(self, aGraph,start,destination):
        #added later 
        for vert in aGraph:
            vert.setDistance(float("inf"))
            vert.setPred(None)
        #creates PriorityQueue object 
        pq = PriorityQueue()
        #sets distance from starting vertex to zero 
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(),v) for v in aGraph])
        while not pq.isEmpty():
            currentVert = pq.delMin()
            for nextVert in currentVert.getConnections():
                newDist = currentVert.getDistance() + int(currentVert.getWeight(nextVert))
                if newDist < nextVert.getDistance():
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert,newDist)
        return destination.getDistance()




