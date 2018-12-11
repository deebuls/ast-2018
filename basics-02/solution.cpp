#include <iostream>


using namespace std;
void  conditionals()
{
    // declaration of variables
    int first_number = 0;
    int second_number = 0;

    //Getting values from user
    std::cout << "first_number : " << first_number << " second_number: " << second_number << std::endl; 
    std::cout << "Input any 2 numbers : " << std::endl;

    
   
    //First task
    std::cin >> first_number >> second_number ;
    std::cout << "first_number : " << first_number << " second_number: " << second_number << std::endl; 

    if (first_number < second_number) {
        std::cout << first_number <<  "is less than " << second_number << std::endl;
    }

    if (first_number == second_number) {
        std::cout << first_number <<  "is equal to " << second_number << std::endl;
    }

    if (first_number > second_number) {
    }


    //second task
    
    //Third task
    if (first_number < second_number) {
        std::cout << first_number <<  "is less than " << second_number << std::endl;
    } else if (first_number == second_number) {
        std::cout << first_number <<  "is equal to " << second_number << std::endl;
    } else {
        std::cout << first_number <<  "is less than " << second_number << std::endl;
    }

} 


int main()
{
    conditionals();
}



