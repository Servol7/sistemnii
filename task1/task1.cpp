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
    vector<vector<string> > data = readCSV("task1.csv");
    vector<vector<int> > a(data.size());
    for (int i = 0; i < data.size(); i++){
        for (int j = 0; j < data[i].size(); j++){
            if ((i != j) && (data[i][j] == "1")) a[i].push_back(j+1);
        }
    }
    for (int i = 0; i < a.size(); i++){
        cout << i+1 << ":\n";
        for (int j = 0; j < a[i].size(); j++){
            cout << a[i][j] << " ";
        }
        cout << '\n';
    }
    return 0;
}
