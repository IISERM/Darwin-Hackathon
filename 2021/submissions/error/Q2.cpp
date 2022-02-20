#include <iostream>

using namespace std;

float f(float a, int b) {
    float s = 1.0;
    for (int i = 1; i <= b; i++)
        s *= a;
    return s;
}

int main() {
    int n, k;
    float fc = 1.0;
    cout << "Enter value of k: ";
    cin >> k;
    cout << "Enter value of N:";
    cin >> n; // Can this be done in a safer manner?

    k = f(2, k);              // k = 2^k
    fc = f(0.25, n);          // fc = 0.25^n
    fc = fc * f(0.75, k - n); // 0.25^n * 0.75^(2^k-n) ??

    for (int i = n; i > 0; i--) { // Umm what?
        fc = fc * k / i;
        k--;
    }

    cout << "Probability is:" << fc << "\n";

    return 0;
}
