#include <iostream>
using namespace std;

string beaufort(string text, string key) {
    string cipher;
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for(int i=0; i<text.size(); i++) {
        char c0 = text[i];
        char c1 = key[i % key.size()];
