#include<stdio.h>
#include<stdlib.h>

void insertion(int rint[10]) {
	int i, j;
	int n;

	for (i = 1; i < 10; i++) {
		n = rint[i];
		for (j = i - 1; j >= 0; j--) {
			if (rint[j] < n)
				rint[j + 1] = rint[j];
			else
				break;
		}
		rint[j + 1] = n;
	}
}

int Heap[10];
int nH;

void push(int n) {
	int cur, parent;

	Heap[nH] = n;
	cur = nH++;

	while ((parent = (cur + 1) / 2 - 1) >= 0) {
		if (Heap[parent] < n)
			Heap[cur] = Heap[parent];
		else break;
		cur = parent;
	}
	Heap[cur] = n;
}

int pop() {
	int cur, child, left;
	int ret, n;

	ret = Heap[0];
	n = Heap[0] = Heap[--nH];
	cur = 0;
	while ((left = (cur * 2 + 1)) < nH) {
		if (left == nH - 1)
			child = left;
		else {
			if (Heap[left] < Heap[left + 1])
				child = left + 1;
			else
				child = left;
		}
		if (Heap[child] > n)
			Heap[cur] = Heap[child];
		else
			break;
		cur = child;
	}
	Heap[cur] = n;
	return ret;
}

#define MVBIT 6

int main() {
	int rint[10], tint[10];
	int i, t;
	srand(1234);

	unsigned long long ll = 0L;
	unsigned long long tll = 0L;
	unsigned char *tc;

	tc = (unsigned char*)&tll;
//	tc += 7;

	*tc = 1;
	tll <<= (MVBIT * 9);
	ll |= tll;

	*tc = 2;
	tll <<= (MVBIT * 8);
	ll |= tll;

	tll = 0;

	for (i = 0; i < 10; i++)
		tint[i] = 0;
	for (i = 0; i < 10; ) {
		t = rand() % 10;
		if (tint[t] == 0) {
			tint[t] = 1;
			rint[i] = t;
			printf("%d ", rint[i]);
			i++;
		}
	}
	
	printf("\n");
//	insertion(rint);
//	for (i = 0; i < 10; i++)
//		printf("%d ", rint[i]);

	for (i = 0; i < 10; i++)
		push(rint[i]);
	for (i = 0; i < 10; i++)
		printf("%d ",pop());

	printf("\n");

	return 0;
}