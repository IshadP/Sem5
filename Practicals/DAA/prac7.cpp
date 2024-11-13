#include<iostream>
#include <limits.h>
using namespace std;

int minDistance(int dist[], bool Tset[]) {
    int min = INT_MAX, min_index;

    for (int i = 0; i < 6; i++)
        if (Tset[i] == false && dist[i] <= min)
            min = dist[i], min_index = i;
    return min_index;
}


void output(int dist[]) {
    cout << "Vertex \t Distance from the Source\n";
    for (int i = 0; i < 6; i++){
        char ver = 65+i;
        cout << ver << " \t\t " << dist[i] << endl;
    }
}


void dijkstraAlgorithm(int graph[6][6], int src) {
    int dist[6];
    bool Tset[6];

    for (int i = 0; i < 6; i++)
        dist[i] = INT_MAX, Tset[i] = false;
    dist[src] = 0;
    for (int count = 0; count < 6 - 1; count++) {
        int u = minDistance(dist, Tset);
        Tset[u] = true;


        for (int v = 0; v < 6; v++)
            if (!Tset[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v])
                dist[v] = dist[u] + graph[u][v];
    }

    output(dist);
}




int main(){
        int graph[6][6] = { { 0, 1, 2, 0, 0, 0},
                        { 1, 0, 1, 0, 3, 0},
                        { 2, 1, 0, 2, 2, 0},
                        { 0, 0, 2, 0, 1, 1},
                        { 0, 3, 2, 1, 0, 2},
                        { 0, 0, 0, 1, 2, 0},
    };

    dijkstraAlgorithm(graph, 0);

    return 0;
}