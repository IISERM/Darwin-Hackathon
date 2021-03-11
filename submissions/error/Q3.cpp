#include <fstream>
#include <iostream>
using namespace std;

int f(int a, int b) { // a^b
    int s = 1;
    for (int i = 1; i <= b; i++) {
        s *= a;
    }
    return s;
}
int main() {
    int n, i;
    cin >> n;

    int b;
    b = f(2, n); // 2^n

    char a[b][2];           // 2^n X 2
    for (i = 0; i < b; i++) // take input
        cin >> a[i][0] >> a[i][1];

    float c = 0.0, C = 0.0;
    for (i = 0; i < b; i++) { // Count C and c
        if (a[i][0] == 'c')   // AAGH! 0 indexing!
            c++;
        else
            C++;
        if (a[i][1] == 'C')
            C++;
        else
            c++;
    }
    cout << c << " " << C << "\n";
    float p;
    p = C / (C + c); // p(C)

    cout << p * p << ' ' << (1 - p) * (1 - p) << ' ' << p * (1 - p) * 2 << endl;
    // p^2, (1-p)^2, p*(1-p)*2
    return 0;
}
