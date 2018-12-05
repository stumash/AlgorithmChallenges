#include <map>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <chrono>
#include <ctime>

/**
 * Compile with
 *
 *      g++ -std=c++11 -O3    92.cpp -o 92.out
 *
 * for best performance results. Or even use
 *
 *      g++ -std=c++11 -Ofast 92.cpp -o 92.out
 *
 * for even more speed.
 */

// compute sum of square of digits less than 10M
int step(int n) {
    int sum = 0;
    for (int i = 0; i < 6; ++i) {
        int digit = (n / (int) pow(10.0, (double(i)))) % 10;
        sum += digit * digit;
    }
    return sum;
}

std::map<int, int> known;

int terminator(int n) {
    std::map<int,int>::iterator it = known.find(n);

    if (it != known.end()) {
        return it->second;
    }

    std::vector<int> chain;
    chain.push_back(n);
    while (true) {
        int next = step(chain.back());

        it = known.find(next);
        if (it != known.end()) {
            int result = it->second;

            for(std::vector<int>::iterator it = chain.begin(); it != chain.end(); ++it) {
                known[*it] = result;
            }

            return result;
        }

        chain.push_back(next);
    }
}

int main(int argc, char** argv) {
    using namespace std::chrono;
    long start_time = duration_cast<milliseconds>(
        high_resolution_clock::now().time_since_epoch()
    ).count();

    known[89] = 89;
    known[1] = 1;

    int count = 0;
    for (int i = 1; i < 1000000; ++i) {
        if (terminator(i) == 89) {
            ++count;
        }
    }

    long end_time = duration_cast<milliseconds>(
        high_resolution_clock::now().time_since_epoch()
    ).count();

    printf("%d\n", count);
    printf("duration (ms): %ld", end_time-start_time);
}
