#include <iostream>
#include <math.h>
using namespace std;
 
int main()
{
    int numberOfBulbs = 1000;
    int root = sqrt(numberOfBulbs);
    for (int i = 1; i < root + 1; i++)
    {
        cout << (i * i)<< endl;
    }
    return 0;
}