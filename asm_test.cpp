#include <ctime>
#include <iostream>
#include <iomanip>
#include <unistd.h>

using namespace std;
uint64_t n;
uint64_t m;

uint64_t count(){
        for(;;)
        {
                m++;
                if (n == m)
                        break;
        }
return m;

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

uint64_t count_asm(){
	__asm__ __volatile__ (
			"mov %1, %%rax;"
			"mov %2, %%rbx;"
			"loop:\n"
			"inc %%rbx;"
			"cmp %%rax , %%rbx;"
			"jne loop;"
			:"=r"(m)
			:"r"(n) , "r"(m));

return m;

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


