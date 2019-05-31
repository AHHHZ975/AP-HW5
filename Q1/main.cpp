#include <iostream>
#include <vector>
#include <numeric> //for std::iota
#include <algorithm>
#include <iterator>
// #include <execution>

using std::vector;
using std::cout;
using std::endl;

bool isOdd(int x) { 
   return x%2 == 1; 
} 

int main(){
	vector<int> vec1(100);
	vector<int> vec2(10);	
	iota(begin(vec1), end(vec1), 1);	
	iota(begin(vec2), end(vec2), 1);
	std::ostream_iterator<int> out_it (std::cout," ");
	//////////////////////////////////////////////
	// vec1.insert(vec1.end(), vec2.begin(), vec2.end());
	// std::copy(vec1.begin(), vec1.end(), out_it);
	// cout << endl;
	//////////////////////////////////////////
	// auto odd_vec = find_if(vec1.begin(), vec1.end(), isOdd);    	
	// while(odd_vec != vec1.end()){
    	// cout << *odd_vec << ' '; 
    	// odd_vec = find_if(odd_vec+1, vec1.end(), isOdd);
	// }
	// cout << endl;
	////////////////////////////////////////
	// vector<int> reverse_vec;
	// std::reverse_copy(vec1.begin(), vec1.end(), std::back_inserter(reverse_vec));
	// reverse_vec.insert(reverse_vec.begin(), vec1.rbegin(), vec1.rend());
	// std::copy(reverse_vec.begin(), reverse_vec.end(), out_it);
	// cout << endl;
	//////////////////////////////////////	
	// sort(vec2.begin(), vec2.end());	
	// sort(std::execution::par, vec2.begin(), vec2.end());	
	// std::copy(vec2.begin(), vec2.end(), out_it);
	// cout << endl;
	return 0;
}