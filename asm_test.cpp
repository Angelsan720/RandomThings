#include <ctime>
#include <iostream>
#include <iomanip>
#include <unistd.h>


/*

In the words of one of my profesors. A good c/cpp programer knows what the compiler turns the code into.
This is a test of how to make inline asm and to see if I know what the compiler would do with a simple for loop.
Works on linux on normal optimization need to fix to run on windows.

*/
using namespace std;
uint64_t n;
uint64_t m;
void count(){
        for(;;)
        {
                m++;
                if (n == m)
                        break;
        }
};
void printPercent(){
        cout << fixed << setprecision( 3 )<<"Percent:"<< (m/n)*100 << "%";

        for ( ; m  != n ; ){
                cout << "\rPercent:"<< (m/n)*100 << "%";
                usleep(1000);

        }
};

void load(){
	__asm__ __volatile__
		 (	"mov $28, %%rax\n"
			"imulq $60, %%rax\n"
			"imulq $22, %%rax\n"
			"imulq $1080, %%rax\n"
			"imulq $1920, %%rax\n"
			"mov $0, %1\n"
			"mov %%rax, %0"
			:"=r"(n) , "=r"(m));
}
void count_asm(){
	__asm__ __volatile__ (
			"mov %1, %%rax;"
			"mov %2, %%rbx;"
			"loop:\n"
			"inc %%rbx;"
			"cmp %%rax , %%rbx;"
			"jne loop;"
			:"=r"(m)
			:"r"(n) , "r"(m));
}

int main(){


	load();
	clock_t c = clock();
	count();
	cout 	<< "Finished normal in:"<< (clock() - c)/CLOCKS_PER_SEC << ":seconds" << endl;

	load();
	c = clock();
	count_asm();
	cout 	<< "Finished asm in:"<< (clock() - c)/CLOCKS_PER_SEC << ":seconds" << endl;






return(0);
}


