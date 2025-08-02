
-----

# Distance Vector Routing Protocol Simulator

[cite\_start]This project is a Python-based simulator for the **Distance Vector Routing (DVR) protocol**[cite: 2, 3]. [cite\_start]It uses multithreading to demonstrate the decentralized nature of the algorithm, where each thread represents an individual router in the network[cite: 4, 5]. [cite\_start]Routers communicate asynchronously using a shared queue system to exchange their distance vector tables and iteratively compute the shortest paths to all other nodes in the network[cite: 5, 26].

-----

## 🚀 Features

  * [cite\_start]**Decentralized Simulation**: Each router is simulated as a separate thread, performing computations independently[cite: 4, 34].
  * [cite\_start]**Bellman-Ford Algorithm**: Implements the Bellman-Ford equation for routers to update their routing tables based on information from neighbors[cite: 27].
  * [cite\_start]**Asynchronous Communication**: Utilizes a shared queue for routers to send and receive distance vectors from their neighbors[cite: 5, 26].
  * [cite\_start]**Dynamic Topology Parsing**: The network topology is read from a simple text file, allowing for easy testing with different network structures[cite: 12, 41].
  * [cite\_start]**Iterative Updates**: The simulation displays the routing tables for each router at every iteration, clearly marking any updated path costs with an asterisk (\*) to visualize the convergence process[cite: 28, 29, 30].

-----

## 🛠️ How It Works

The simulation starts by reading a network topology from an input file. For each router defined in the topology, a dedicated thread is spawned.

1.  **Initialization**: Initially, each router only knows the direct costs to its immediate neighbors. [cite\_start]The routing tables are populated with these costs, and `infinity` for all other destinations[cite: 25].
2.  [cite\_start]**Information Sharing**: After a 2-second interval, each router sends its current distance vector (its routing table) to all of its adjacent neighbors using a shared queue[cite: 26, 31].
3.  [cite\_start]**Table Computation**: Once a router receives distance vectors from all its neighbors, it recalculates its own routing table using the Bellman-Ford equation[cite: 27, 32]. It compares its current path cost to a destination with the new paths available through its neighbors.
4.  [cite\_start]**Display and Repeat**: The newly updated routing tables are printed to the terminal for the current iteration[cite: 28, 29]. [cite\_start]Any cost that has changed during this iteration is marked with an asterisk (\*)[cite: 30].

This cycle of sharing, computing, and updating repeats, allowing the network to converge towards the optimal shortest paths.

-----

## 📋 Prerequisites

Make sure you have the following installed:

  * Python 3.x
  * NumPy library

-----

## ▶️ How to Run

1.  Clone the repository:
    ```bash
    git clone <your-repo-link>
    ```
2.  Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```
3.  [cite\_start]Run the script from your terminal, passing the input file as a command-line argument[cite: 39]:
    ```bash
    python dist_vector_routing.py input.txt
    ```

-----

## 📄 Input File Format

The program takes a text file as input to define the network topology. The file must follow this format:

  * [cite\_start]**Line 1**: A single integer representing the total number of routers[cite: 19].
  * [cite\_start]**Line 2**: A string containing the names of the routers (e.g., ABC)[cite: 20].
  * [cite\_start]**Subsequent Lines**: Each line defines a link with its cost, in the format `Node1Node2Cost` (e.g., `AB5` means the cost between A and B is 5)[cite: 21].
  * [cite\_start]**Last Line**: The file must end with the string `EOF`[cite: 23].

A sample file input.txt is also provided.
