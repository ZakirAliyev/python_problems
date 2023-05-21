#include <iostream>

int function(int n) {
    int f = 1;
    int f1 = 2;
    int f2 = 3;

    if (n == 1) {
        return 1;
    }
    else if (n == 2) {
        return 2;
    }
    else {
        for (int i = 3; i < n; i++) {
            f = f1;
            f1 = f2;
            f2 = f + f1;
        }

        return f2;
    }
}

int main() {
    int n;
    std::cin >> n;
    std::cout << function(n) << std::endl;

    return 0;
}
