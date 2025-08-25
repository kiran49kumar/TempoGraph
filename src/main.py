import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def main():
    # Sample dataset (songs as nodes, similarity edges)
    songs = ["SongA", "SongB", "SongC"]
    edges = [("SongA", "SongB"), ("SongB", "SongC")]

    # Create a simple graph
    G = nx.Graph()
    G.add_nodes_from(songs)
    G.add_edges_from(edges)

    # Print graph info
    print("Nodes:", G.nodes())
    print("Edges:", G.edges())

    # Draw graph
    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()
