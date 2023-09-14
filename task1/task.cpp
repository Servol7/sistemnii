#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

vector<string> split(const string& s, char delimiter)
{
    vector<string> tokens;
    string token;
    istringstream tokenStream(s);
    while (getline(tokenStream, token, delimiter))
        tokens.push_back(token);
    return tokens;
}

vector<vector<string> > readCSV(string filename)
{
    vector<vector<string> > data;
    ifstream file(filename);
    string line;
    long long i = 0;
    while (getline(file, line)) {
        data.push_back({});
        vector<string> tokens = split(line, ',');
        for (string token : tokens) {
            data[i].push_back(token);
        }
        i++;
    }
    file.close();
    return data;
}

int main()
{
    vector<vector<string> > data = readCSV("example.csv");
    int n, m;
    cin >> n >> m;
    cout << data[n-1][m-1];
    return 0;
}
