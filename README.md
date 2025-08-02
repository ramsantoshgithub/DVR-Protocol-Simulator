
# Distance Vector Routing Protocol Simulator

This project is a Python-based simulator for the **Distance Vector Routing (DVR) protocol**. It uses multithreading to demonstrate the decentralized nature of the algorithm, where each thread represents an individual router in the network. Routers communicate asynchronously using a shared queue system to exchange their distance vector tables and iteratively compute the shortest paths to all other nodes in the network.

-----

## 🚀 Features

  * **Decentralized Simulation**: Each router is simulated as a separate thread, performing computations independently.
  * **Bellman-Ford Algorithm**: Implements the Bellman-Ford equation for routers to update their routing tables based on information from neighbors.
  * **Asynchronous Communication**: Utilizes a shared queue for routers to send and receive distance vectors from their neighbors.
  * **Dynamic Topology Parsing**: The network topology is read from a simple text file, allowing for easy testing with different network structures.
  * **Iterative Updates**: The simulation displays the routing tables for each router at every iteration, clearly marking any updated path costs with an asterisk (\*) to visualize the convergence process.

-----

## 🛠️ How It Works

The simulation starts by reading a network topology from an input file. For each router defined in the topology, a dedicated thread is spawned.

1.  **Initialization**: Initially, each router only knows the direct costs to its immediate neighbors. The routing tables are populated with these costs and `infinity` for all other destinations.
2.  **Information Sharing**: After a 2-second interval, each router sends its current distance vector (its routing table) to all of its adjacent neighbors using a shared queue.
3.  **Table Computation**: Once a router receives distance vectors from all its neighbors, it recalculates its own routing table using the Bellman-Ford equation. It compares its current path cost to a destination with the new paths available through its neighbors.
4.  **Display and Repeat**: The newly updated routing tables are printed to the terminal for the current iteration. Any cost that has changed during this iteration is marked with an asterisk (\*).

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
3.  Run the script from your terminal, passing the input file as a command-line argument:
    ```bash
    python dist_vector_routing.py input.txt
    ```

-----

## 📄 Input File Format

The program takes a text file as input to define the network topology. The file must follow this format:

  * **Line 1**: A single integer representing the total number of routers.
  * **Line 2**: A string containing the names of the routers (e.g., ABC).
  * **Subsequent Lines**: Each line defines a link with its cost, in the format `Node1Node2Cost` (e.g., `AB5` means the cost between A and B is 5).
  * **Last Line**: The file must end with the string `EOF`.

### Example Input was provided in `input.txt`
