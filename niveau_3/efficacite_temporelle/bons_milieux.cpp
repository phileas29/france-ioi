#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

void getMiddle(int mm[], int p1[], int p2[])
{
    double *m = new double[2];
    m[0] = ((double)p1[0]+(double)p2[0])/2;
    m[1] = ((double)p1[1]+(double)p2[1])/2;
    if( std::floor(m[0]) == m[0] && std::floor(m[1]) == m[1] ) {
        mm[0] = (int)m[0];
        mm[1] = (int)m[1];
    } else {
        mm[0] = -1;
        mm[1] = -1;
    }
}

int main()
{
    int n, i, j;
    cin >> n;
    int map[101][101];
    for(i=0;i<101;i++)
        for(j=0;j<101;j++)
            map[i][j] = 0;

    int points[n][2];

    for(i=0;i<n;i++) {
        cin >> points[i][0];
        cin >> points[i][1];
        map[points[i][0]][points[i][1]] = 1;
    }

    int nbMedianPoints = 0;
    int m[2];

    for(i=1;i<n;i++) {
        for(j=0;j<i;j++) {
            getMiddle(m,points[i],points[j]);
            if( m[0]!=-1 and m[1]!=-1 && map[m[0]][m[1]] == 1 ) {
                nbMedianPoints++;
                map[m[0]][m[1]] = 2;
            }
        }
    }

    cout << nbMedianPoints << endl;
}