"""
UMass ECE 241 - Advanced Programming
Project 2 - Fall 2023
"""
import sys
from graph import Graph, Vertex
from priority_queue import PriorityQueue

class DeliveryService:
    def __init__(self) -> None:
        """
        Constructor of the Delivery Service class
        """
        self.city_map = Graph()
        self.MST = Graph()

    def buildMap(self, filename):
        """
        :param filename : str
        :return:
        """
        
        #looks through file
        with open(filename, "r") as file:
            lines = file.readlines()
            for item in lines:
                # splits all of the items in the line on your txt file
                connect = item.split("|")

                #add vertex and edge: vertex 1, vertex 2, cost: 
                self.city_map.addEdge(int(connect[0]), int(connect[1]), int(connect[2]))
                   

    def isWithinServiceRange(self, restaurant, user, threshold) -> bool:
        """
        :param restaurant
        :param user:
        :param threshold:
        :return:
        """
        print("vertList", self.city_map.vertList[0])
        user_vertex = self.city_map.getVertex(user)
        resturant_vertex = self.city_map.getVertex(restaurant)


        #checks to see if user/restaurant information is valid
        #check if user vertex exists 
        if user_vertex == None:
            return False

        #check if user node is an island
        if user_vertex.getConnections() == None: 
            return False

        #why does getVertex(restaurant) work in dijkstra but not Prims
        dist, path = self.dijkstra(self.city_map, resturant_vertex, user_vertex)
        print("distance and path", dist, path)

        if dist > threshold: 
            return False
        else: 
            return True





    def dijkstra(self, aGraph,start,destination):
        """
        :param aGraph: Graph 
        :param user: int
        :param threshold: int
        :return: destination.getDistance(), path 
        """
        #added later
        for V in aGraph:
            V.setDistance(sys.maxsize)
            V.setPred(None) 
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
    

        #find path: all added by me 
        path = [] 

        current = destination

        #travels back through predecessors until it returns to start vertex 
        while current != start:
            path.append(int(current.id)) 
            current = current.getPred()

        if current == start: 
            path.append(start.id)
            path.reverse()

        return destination.getDistance(), path 




    def buildMST(self, restaurant):
        """
        :param restaurant: int
        :return: 
        """
        self.MST = self.prim(self.city_map, self.city_map.getVertex(restaurant))
        
    #make it return an mst graph
    def prim(self,G,start):
        """
        :param restaurant: int
        :param G : Graph
        :param start : int
        :return: mst : graph 
        """
        pq = PriorityQueue()
        for v in G:
            v.setDistance(sys.maxsize)
            v.setPred(None)
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(),v) for v in G])
        mst = Graph() #added
        while not pq.isEmpty():
            currentVert = pq.delMin()
            #adds vertex to graph 
            mst.addVertex(currentVert.getId()) #added
            #adds edge of two current.vert and pred.vert to graph 
            if currentVert.getPred() != None: #added
                weight = currentVert.getWeight(currentVert.getPred()) #added
                mst.addEdge(currentVert.getId(), currentVert.getPred().getId(), weight) #added
            for nextVert in currentVert.getConnections():
                newCost = currentVert.getWeight(nextVert)
                if nextVert in pq and newCost<nextVert.getDistance():
                    nextVert.setPred(currentVert)
                    nextVert.setDistance(newCost)
                    pq.decreaseKey(nextVert,newCost)
        return mst #added

    def minimalDeliveryTime(self, restaurant: int, user: int) -> int:
        """
        :param restaurant: int 
        :param user: int 
        :return: dist : int
        """

        user_vertex = self.MST.getVertex(user)
        resturant_vertex = self.MST.getVertex(restaurant)
        
        #checks to see if user/restaurant information is valid
        #check if user vertex exists 
        if user_vertex == None:
            return -1
        
        if restaurant not in self.MST.vertList.keys():
            return -1 
        
        if user not in self.MST.vertList.keys():
            return -1 

        #check if user node is an island
        if user_vertex.getConnections() == None: 
            return -1

        #why does getVertex(restaurant) work in dijkstra but not Prims
        dist, path = self.dijkstra(self.MST, resturant_vertex, user_vertex)

        return dist
        

    def findDeliveryPath(self, restaurant: int, user: int) -> str:
        """
        :param restaurant: int
        :param user: int
        :return: directions : str
        """

        user_vertex = self.city_map.getVertex(user)
        resturant_vertex = self.city_map.getVertex(restaurant)

        #checks to see if user/restaurant information is valid
        if user_vertex == None:
            return "INVALID"
        
        if restaurant not in self.city_map.vertList.keys():
            return "INVALID" 
        
        if user not in self.city_map.vertList.keys():
            return "INVALID"

        #check if user node is an island
        if user_vertex.getConnections() == None: 
            return "INVALID"

        dist, path = self.dijkstra(self.city_map, resturant_vertex, user_vertex)

        #turns path and dist into correct looking str 
        directions = ""
        for i in range(len(path)-1): 
            directions += f"{path[i]}->"
        directions += f"{path[i+1]} ({dist})"
        return directions 
       

    def findDeliveryPathWithDelay(self, restaurant, user, delay_info):
        """
        :param restaurant:
        :param user:
        :param delay_info:
        :return:
        """
        
        #updates map for traffic jam: 
        self.Traffic(restaurant, user, delay_info)
        
        user_vertex = self.city_map.getVertex(user)
        resturant_vertex = self.city_map.getVertex(restaurant)

        dist, path = self.dijkstra(self.city_map, resturant_vertex, user_vertex)

        directions = ""
        for i in range(len(path)-1): 
            directions += f"{path[i]}->"
        directions += f"{path[i+1]} ({dist})"
        return directions 
    
    
    
    
    def Traffic(self, restaurant, user, delay_info):
        """
        :param restaurant:
        :param user:
        :param delay_info:
        :return: 
        """

        print("graph orig", self.city_map.vertList)

        #add weight to graph
        #pull key values from graph and delay_info and use double for loop to compare them
        # item = int
        # key = int
        for item in self.city_map.vertList:
            for key in delay_info: 
                print("item", item)
                print("key", key)
                
                #for each item that appears in both dictionaries increase all weights by delay_info[]
                if item == key:

                    #get vertex object equivalent to item from city_map
                    # main_vertex = vertex  
                    main_vertex = self.city_map.getVertex(item)

                    #grabs vertex objects that are connected to main_vertex
                    #connections = dict
                    connections = main_vertex.getConnections()
                    print("connections", connections)

                    
                    #node = vertex 
                    #node.id = int
                    for node in connections: 
                        print("node", node.id)
                        print("main_vertex", main_vertex)
                        
                        #retrieves weight value 
                        weight = main_vertex.connectedTo[node]
                        print("weight", weight)

                        #retrieves traffic delay
                        print("delay", delay_info[key])
                        delay = delay_info[key]

                        #adds edge to graph with updated weight 
                        self.city_map.addEdge(item, node.id, weight+delay)
                        print("graph updated", self.city_map.vertList)

    


        


    ## DO NOT MODIFY CODE BELOW!
    @staticmethod
    def nodeEdgeWeight(v):
        return sum([w for w in v.connectedTo.values()])

    @staticmethod
    def totalEdgeWeight(g):
        return sum([DeliveryService.nodeEdgeWeight(v) for v in g]) // 2

    @staticmethod
    def checkMST(g):
        for v in g:
            v.color = 'white'

        for v in g:
            if v.color == 'white' and not DeliveryService.DFS(g, v):
                return 'Your MST contains circles'
        return 'MST'

    @staticmethod
    def DFS(g, v):
        v.color = 'gray'
        for nextVertex in v.getConnections():
            if nextVertex.color == 'white':
                if not DeliveryService.DFS(g, nextVertex):
                    return False
            elif nextVertex.color == 'black':
                return False
        v.color = 'black'

        return True

# NO MORE TESTING CODE BELOW!
# TO TEST YOUR CODE, MODIFY test_delivery_service.py
