//1040
#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    float n1, n2, n3, n4, media, exame;

    cin >> n1 >> n2 >> n3 >> n4;
    media = (n1*2+n2*3+n3*4+n4) / 10;
    
    cout << fixed << setprecision(1);
     
    if (media >= 7.0) {
        cout << "Media: " << media << "\nAluno aprovado." << endl;
    }
    else if (media < 5.0) {
        cout << "Media: " << media << "\nAluno reprovado." << endl;
    }
    else {
        cout << "Media: " << media << "\nAluno em exame." << endl;
        cin >> exame;
        cout << "Nota do exame: " << exame << endl;

        if (exame > 5) {
            media = (media + exame) / 2;
            cout << "Media: " << media << "\nAluno aprovado." << endl;
        }
        else {
            cout << "Media: " << media << "\nAluno reprovado." << endl;
        }
    }
    return 0;
}