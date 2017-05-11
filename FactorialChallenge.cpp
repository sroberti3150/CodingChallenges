/*
This program will prompt a user for an integer input, then find the number of trailing zeroes on the resultant factorial.
It will accomplish this by creating a linked list of all of the factors of the inputted number, then checking each factor to see if it divides 2 or 5.
The number of trailing zeroes in a number will be equal to the number of times 2 and 5 are multiplied together.  Thus, the number of trailing zeroes will be equal to
either the number of 2 factors or the number of 5 factors, whichever is lower.
*/

#include <iostream>


using namespace std;

struct node { // This struct contains the data for each factor in the factorial.
	node *next;
	public:
		int factor, twos, fives ;
};

int getUserInput() {// Get the number from the user.
	int input;
	cout << "Please enter a number:" << endl;
	cin >> input;
	return input;
}

node *factorize(int num) { //Break the factorial into its sequential factors, placing each one into a node on the linked list.
	node *head;
	node *item;
	head = new node;
	item = head;
	for(int i = 1; i <= num; i++){
		item->next = new node;
		item = item->next;
		item->factor = i;	
	}
	item->next = NULL;
	return head;
}

int checkTwos(int factor) {
	int count;
	count = 0;
	while((factor % 2) == 0) {
		count += 1;
		factor = factor / 2;
	}
	return count;
}

int checkFives(int factor) {
	int count;
	count = 0;
	while ((factor % 5) == 0) {
		count += 1;
		factor = factor / 5;
	}
	return count;
}


void checkFactors(node *head) {//Check every factor in the link list individually, checking how many times it divides two and/or five.
	node *item;
	item = head;
	int factor;
	while(item->next != NULL) {
		item = item->next;
		factor = item->factor;
		item->twos = checkTwos(factor);
		item->fives = checkFives(factor);
	}
}

void calculateZeroes(node *head) {// Run through the list and add up the total number of twos and fives in the factorial, find the lesser of the two counts, and print the result.
	node *item;
	int twosCount=0, fivesCount=0, zeroes;
	item = head;
	string end;
	while(item->next != NULL) {
		item = item->next;
		twosCount += item->twos;
		fivesCount += item->fives;	
	}
	
	if (twosCount <= fivesCount) {
		zeroes = twosCount;
	}
	else {
		zeroes = fivesCount; 
	}

	cout << endl << "In the factorial of that number, there are " << zeroes << " trailing zeroes." << endl;
	system("pause");
 }


int main() {
	node *head;
	int input = getUserInput();
	head = factorize(input);
	checkFactors(head);
	calculateZeroes(head);
	
	return 0;
}




