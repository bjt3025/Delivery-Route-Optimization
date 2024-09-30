ECE241 PROJECT 2: Thinking in Graphs
------------------------------------

#### Due: Nov 9th, 2023, 11:59 PM on Gradescope

#### **INTRODUCTION:** 

Food delivery services have rapidly evolved to be an indispensable segment of contemporary life, intertwining technology and logistics to deliver convenience to consumers’ doorsteps. A pivotal aspect of these services is the routing strategy, which determines the path a delivery takes from a restaurant to a customer's location. To optimize the efficiency and reliability of deliveries, it’s essential to determine the best routes amidst varying cityscapes and traffic conditions. In this scenario, Shortest Path First (SPF) algorithm or a variant thereof can be instrumental. Each segment of the street in the city can be represented as a weighted edge in a graph, where the vertices represent intersections or key landmarks.

In this project, you’ll utilize graph theory to model a city's street network, concentrating on the delivery paths of food delivery services. An edge exists between two vertices if a direct street connects them. Weights assigned to the edges are the time it takes to travel along the street, influencing the route chosen for delivery. Using this graph model, you will devise algorithms to determine the most time effective delivery routes, aiming to minimize time and enhance customer satisfaction.

* * *

#### **RESOURCES:**

1.  **City map information**: In this project, we will be utilizing a specially curated fake city map dataset to simulate and analyze food delivery routes and logistics. This dataset has been thoughtfully crafted to represent the intricate network of streets and intersections, providing a realistic framework for our investigations. You can access the dataset we have provided in the starter code. 
2.  **File Format**: This dataset encompasses multiple text files. Within each text file lies a series of records, structured line by line, where each line signifies an edge, described in a standardized format: `NODE1|NODE2|COST`. `NODE1` and `NODE2` represent the connecting nodes, while the `COST` indicates the associated cost in traversing the path between the nodes (i.e., time). Each of these edges symbolizes a bi-directional pathway between two critical points, such as intersections or notable landmarks, represented by nodes/vertices.

* * *

#### **PROJECT START KIT**

Begin your project with the provided starter kit. You can [download the starter code for this project here](https://github.com/chenzibin2019/ECE241_Project2_Fall2023). Familiarize yourself with the following structure of the project folder:

**Files and Their Descriptions:**

1\. **city\_map\_{5,10,20,100}.txt**:  
   - Contains the city map informations. The number after the last underline is the size of the graph (i.e., number of nodes). We suggest you start with small one and test your code with larger ones once you fell confident with your code. 

2\. **delivery\_service.py:**  
   - Features an unfinished \`DeliveryService\` class.  
   - Majority of the class methods still need to be implemented as part of this project.

3\. **graph.py:**  
   - Contains the \`Graph\` and \`Vertex\` class.  
   - Utilize this classes to devise a Graph as required for your tasks.

4\. **test\_delivery\_service.py:**  
   - Contains an array of testing functions tailored for your \`DeliveryService\` class.  
   - Once you've fleshed out the class, run this file to assess the functionality of your code.  
   - Be cautious: Even if you pass all tests in this file, the autograder may still detect issues. This file isn't the final checkpoint for grading.

* * *

#### **PROJECT TASKS**

Suppose you are the SDE in a large food delivery service provider company. In this project, you will be executing the specific tasks and provide various services to restaurants, end users, and delivery persons. Restaurant and user are modeled as vertex in the graph. Unless specified by a specific function, a node can be either restaurant or user. Finish implementing the **DeliveryService** class in delivery\_service.py, which stores the city map and implements a set of useful methods to provide delivery services at the city. 

1.  \[10 pts\] Implement a `buildMap(self, filename: str)` method in the **DeliveryService** class. The method takes a filename (e.g., _city\_map\_5.txt_, as string) as the input and loads the city map from the graph specification in that file. Your code should parse the city map (i.e., edge informations) and store it into a Graph object.  
    *   You don't need to return anything but store the weighted graph in a member variable self.city\_map.
    *   Graph and Vertex class provided in class (also included in the starter code) are imported for you. You should use the Graph and Vertex to represent the graph. You can add variables or functions to help you finish the project. But you must NOT change any existing functions/variables. 
    *   You should never hard code the file path (i.e., if you are working at disk E on Windows, do not start with E:\\ECE241\\xxx, instead, write the _relative path_ to the current python file). 
    *   Links are bi-directional and you can assume the link weights are integer. 
    *   When you read anything from the file, it is ALWAYS a string, you should convert particular items into float or integer, when necessary. 
2.  \[15 pts\] Check if the user is within the service range. Suppose restaurants set a policy that if the user lives outside the range where the delivery person can deliver the food within certain time, the user is NOT within the service range of the restaurant. You are going to implement a function that determines whether a specific user is within the service range of a specific restaurant. 
    *   Implement a method called  `isWithinServiceRange(self, restaurant, user, threshold)` on **DeliveryService** class. This method returns a boolean variable (True or False) to indicate whether a the user (represented as a node ID) is within the service range of a restaurant (represented as a node ID) given the threshold. 
    *   The user is considered as NOT within the service range if the user node does not exist. 
    *   You can assume the restaurant node always exists. 
    *   Hint, consider use DFS to help you finish the task. You might need to modify the DFS algorithm if needed.
3.  \[15 pts\] Restaurants what to have a visualized view of what are the best paths to deliver food. Build a sub-graph by generating a minimum spanning tree (based on the cost) from a particular restaurant to any other node in the graph. 
    *   Implement a method called  `buildMST(self, restaurant)` on **DeliveryService** class to build the MST. 
    *   You don't need to return anything, but store the sub-graph in a class variable self.MST. 
    *   You can assume the restaurant node always exists. 
4.  \[15 pts\] Check the minimal delivery time for the user.   
    *   Implement a method called  `minimalDeliveryTime(self, restaurant, user)` on **DeliveryService** class. This method returns the _fastest_ delivery time from a particular restaurant and the user's home. The method returns the smallest delivery time as an integer.
    *   Your function should return -1 if either node does not exist. 
    *   You have to do this from the MST you built in the previous task. 
5.  \[15 pts\] Find the delivery path for the delivery person.   
    *   Implement a method called  `findDeliveryPath(self, restaurant, user)` on **DeliveryService** class. 
    *   The implemented method should return a string indicating the delivery path. 
    *   We define a path should as a sequence of node IDs connected by arrows (i.e., "->"). Example path: "1->3->7->9" where 1, 3, 7, and 9 are IDs of nodes. 
    *   The output should be a path followed by a bracket with the delivery time in it. Example of output "1->3->7->9 (24)" where node 1 is the restaurant and 9 is the user's delivery address. 24 is the total time spent if the delivery person were to follow the path 1->3->7->9. 
    *   Return "INVALID" if either the restaurant node or the user node does not exist. 
    *   Note, you should find the path from the original graph. You must NOT use the MST. 
6.  \[15 pts\] Suppose there is large sport event happening in the city where there are certain intersections (represented by node) are incurring huge traffic delays. Any delivery person trying to entering those node will incur extra traffic delays. Design an algorithm to find the fastest delivery path given the delay information. 
    *   Implement a method called  `findDeliveryPathWithDelay(self, restaurant, user, delay_info)` on **DeliveryService** class to handle traffic jam. 
    *   Traffic delay information will be given to the function with the last parameter delay\_info. delay\_info is a dictionary where the key is the node ID and the value is extra delay time. For example, if the delay\_info is {3: 10, 5: 20} means any delivery person entering node 3 is going to have extra 10 mins delay and any delivery person entering 5 is going to have extra 20 mins delay. 
    *   Your return should follow the same pattern as defined in the previous task. 

* * *

#### **HINTS AND SUGGESTIONS**

Start early and try to get portions of the program to work step-by-step. Debug your program using a small cities. Only use the complete file once you feel confident when your program works.

* * *

#### **WHAT TO SUBMIT**

You should implement the required code within the corresponding code template from the starter code. After implementing all the code, you should submit **all** files in the folder. **Do NOT rename any file!**

Note that your code will be evaluated at the end of the first week (11/02/2023 11:59) and anyone who gets any points from the autograder will be issued 5 points for submitting code early. 

Reminder: The course honesty policy requires you to write all code yourself, except for the code that we give to you. Your submitted code will be compared with all other submitted codes and code from AI-generated solutions for the course to identify similarities. Note that our checking program is not confused by changed variables or method names. 

* * *

#### **GRADING**

*   Code works on Gradescope (85%)
*   Pre-submission checkpoint for anyone who get any (non-zero) points from the autograder on or before 11/02/2023 11:59 pm Eastern Time. (5%)
*   Program structure and comments (10%)
