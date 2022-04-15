#include "beaufort.h"

int main(){
    string text, key, out;
    cout<<"Text: ";
    cin>>text;
    cout<<"Key: ";
    cin>>key;
    out=beaufort(text, key);
    cout<<out<<"\n";
    
}
