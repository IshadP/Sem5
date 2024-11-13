#include <iostream>
using namespace std;

// class DSU {
//     int* parent;
//     int* rank;

//     public:
//         DSU(int n){
//             parent = new int[n];
//             rank = new int[n];

//             for(int i =0; i<n; i++){
//                 parent[i] = -1;
//                 rank[i] = 1;
//             }
//         }
        
// }

#include<bits/stdc++.h>   
using namespace std;   

typedef pair<int, int> iPair;   
  
 
struct Graph   
{   
    int V, E;   
    vector< pair<int, iPair> > edges;   
   
    Graph(int V, int E)   
    {   
        this->V = V;   
        this->E = E;   
    }   
   
    void addEdge(int u, int v, int w){   
        edges.push_back({w, {u, v}});   
    }   

    int kruskalMST();   
}; 

struct DisjointSets   
{   
    int *parent, *rnk;   
    int n;   
  
    DisjointSets(int n){   
 
        this->n = n;   
        parent = new int[n+1];   
        rnk = new int[n+1];   
        for (int i = 0; i <= n; i++){   
            rnk[i] = 0;    
            parent[i] = i;   
        }   
    }   
  
      int find(int u){   

        if (u != parent[u])   
            parent[u] = find(parent[u]);   
        return parent[u];   
    }   
    void merge(int x, int y)   
    {   
        x = find(x), y = find(y);   
        if (rnk[x] > rnk[y])   
            parent[y] = x;   
        else  
            parent[x] = y;   
  
        if (rnk[x] == rnk[y])   
            rnk[y]++;   
    }   
}; 

int main() 
{ 
    Graph g(4); 
    g.addEdge(0, 1, 10); 
    g.addEdge(1, 3, 15); 
    g.addEdge(2, 3, 4); 
    g.addEdge(2, 0, 6); 
    g.addEdge(0, 3, 5); 
  
    // Function call 
    g.kruskals_mst(); 
  
    return 0; 
}