#include <iostream>
#include <vector>
#include <numeric> //for std::iota
#include <algorithm>
#include <iterator>
// #include <execution>

using std::vector;
using std::cout;
using std::endl;

int main(){
	////////////////////// A ///////////////////
	vector<int> vec1(100);
	vector<int> vec2(10);	
	iota(begin(vec1), end(vec1), 1);	
	iota(begin(vec2), end(vec2), 1);
	std::ostream_iterator<int> out_it (std::cout," ");
	//////////////////// B ///////////////////
	cout << "/////////////// The vec1 is extended by  vec2: ///////////////" << endl;
	vec1.insert(vec1.end(), vec2.begin(), vec2.end());
	std::copy(vec1.begin(), vec1.end(), out_it);
	cout << endl;
	//////////////////// C ///////////////////
	cout << "/////////////// The odd_vec is: ///////////////" << endl;
	vector<int> odd_vec(vec1.size()/2);
	copy_if(vec1.begin(), vec1.end(), odd_vec.begin(), [](int i){return i%2==1;}); 
	std::copy(odd_vec.begin(), odd_vec.end(), out_it);	
	cout << endl;
	//////////////////// D ///////////////////
	cout << "/////////////// The reverse_vec is: ///////////////" << endl;
	vector<int> reverse_vec;
	std::reverse_copy(vec1.begin(), vec1.end(), std::back_inserter(reverse_vec)); // First solution
	// reverse_vec.insert(reverse_vec.begin(), vec1.rbegin(), vec1.rend()); // Second solution
	std::copy(reverse_vec.begin(), reverse_vec.end(), out_it);
	cout << endl;
	//////////////////// E ///////////////////
	cout << "/////////////// The sorted vec2 is: ///////////////" << endl;
	// sort(std::execution::par, vec2.begin(), vec2.end());	 // Error
	sort(vec2.begin(), vec2.end());	
	std::copy(vec2.begin(), vec2.end(), out_it);
	cout << endl;
	return 0;
}