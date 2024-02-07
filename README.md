# Efficient Sampling of Directed Graphs
This repo contains an efficient implementation of the idea proposed in [Constructing and Sampling Directed Graphs with Linearly
Rescaled Degree Matrices](https://www.kdd.org/kdd2022/papers/24_Yunxiang%20Yan.pdf).

The algorithm constructed a small graph from the original graph using Joint Degree Matrix and Degree Correlation Matrix (see paper for more details).

## Dependencies
```sh
python
networkx
numpy
scipy
```

## Usage of Main Algorithm

The main algorithm is implemented in `src/sample.py`

**sample(G, k, file_name)**

Inputs:  **G**: The original graph (nx.DiGraph); **k**: input_sample_ratio (float, within (0,1)); **file_name**: the name of the original graph (defined by user, a folder for storing output files will be created at `results/[file_name]`)

Returns: **time_list**: time used in each step (python list); **number of duplicate edges**: int

Outputs: **edgelist**: stored as `results/[file_name]/sampled_[k]_edge_list.txt` (using `nx.write_edgelist`); **degree_sequence**: stored as `results/[file_name]/sampled_[k]_degree_sequence.txt` formatted as `{ind},{outd}`, each row correponds to one node in the sampled graph

## An Easy Example

```
import networkx as nx
from src import sample

er = nx.fast_gnp_random_graph(1000, 1e-3,directed=True) # create an Erdős-Rényi graph
time_list, duplicate = sample.sample(er, 0.1, 'erdos_renyi_graph') # sample the graph
er_sampled = nx.read_edgelist("results/erdos_renyi_graph/sampled_0.1_edge_list.txt", create_using=nx.DiGraph(), data=False)  # reads back the sampled graph
```

## Advanced Usage

This repo also contains the following content for advanced usage.


- data: folder where 10 synthetic datasets (5 Erdős-Rényi graphs, 5 scale-free graphs) and 8 real-world datasets (from [**The KONECT Project**](http://konect.cc/)) are stored.
- results: folder where sampling results are stored. For the 10 datasets in data folder, the sampled graph (k=0.75) and a range of related files are given
- src: folder where the main algorithm (**sample.py**) and many helper files are stored.
- experiment.sh: shellcode to automatically run all kinds of experiments with arguments (-re: --run-experiments, -gd: --run-experiments, -god: --run-experiments, -pd: --run-experiments, -gfd: --run-experiments, -fpl: --run-experiments). sample_ratio needs to be specified at the top of the shellcode

