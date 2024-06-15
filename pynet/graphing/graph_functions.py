#!/usr/bin/env python3

# Python code for graphing and analyzing the network
import csv
import time
import networkx as nx
import matplotlib.pyplot as plt

# Receive a list of ip pairs
def directed_graph(csv_path):

    G = nx.DiGraph();

    with open(csv_path, 'r') as file:
        #reader = csv.DictReader(file)
        reader = csv.reader(file)
        for row in reader:
            #print(row)
            src = row[0]
            dst = row[1]

            G.add_edge(src,dst)

    return G

def draw_graph(G):
    start_time = time.time()

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)  # Position nodes using spring layout
    nx.draw(G, pos, with_labels=False, node_size=30, 
            node_color='skyblue', font_size=10, font_color='black', 
            font_weight='bold', arrowsize=5)
    plt.title('Directed IP Network Graph')

    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken to render: {duration:.4f} seconds")
    
    plt.show()



def draw_graph2(G):
    plt.figure(figsize=(10, 8))

    # Use a different layout algorithm for better visualization
    pos = nx.circular_layout(G)  # Position nodes using circular layout

    # Customize node and edge styles
    nx.draw_networkx_nodes(G, pos, node_size=10, node_color='skyblue', alpha=0.7)
    nx.draw_networkx_edges(G, pos, edge_color='black', width=1.0, arrowsize=5)

    plt.title('Directed IP Network Graph')
    plt.axis('off')  # Hide axis
    plt.show()
