#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string pi_digits(size_t n, const string& key) {
    size_t len = n * 10 / 3 + 1;
    vector<int> a(len, 2);
    string out; out.reserve(n);
    int predigit = 0, nines = 0;
    for (size_t j = 0; j < n + 1; ++j) {
        int q = 0;
        for (size_t i = len; i-- > 0;) {
            int x = 10 * a[i] + q * static_cast<int>(i + 1);
            a[i] = x % (2 * static_cast<int>(i) + 1);
            q = x / (2 * static_cast<int>(i) + 1);
        }
        a[0] = q % 10; q /= 10;
        if (j == 0) { predigit = q; continue; }
        if (q == 9) { ++nines; continue; }
        int emit = predigit;
        if (q == 10) { emit = predigit + 1; predigit = 0; }
        out.push_back(char('0' + emit));
        while (nines--) out.push_back('9');
        nines = 0; predigit = q;
        if (out.size() >= n + 1) break;
    }
    return out.substr(1, n);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string raw; size_t digits = 10000;
    cout << "你的生日在圆周率哪里（C++）\n生日 yyyy/mm/dd："; cin >> raw;
    string key; for (char c : raw) if (c != '/') key += c;
    cout << "搜索位数（默认 10000）："; string s; cin >> s; if (!s.empty()) digits = stoull(s);
    digits = max<size_t>(100, min<size_t>(digits, 100000));
    cout << "计算中：" << digits << " 位...\n";
    string pi = pi_digits(digits, key);
    auto pos = pi.find(key);
    if (pos != string::npos) cout << "找到了！位于 π 小数点后第 " << pos + 1 << " 位。\n";
    else cout << "这次还没找到，但你依然是独一无二的数字。\n";
}
