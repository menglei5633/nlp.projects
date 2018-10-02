#include <stdio.h>

int main(int argc,  char* atgv[]) {
    char* filename = atgv[1];
    FILE* fp = fopen(filename, "r");
    char buffer[100];
    for (int i = 0; i < 20; ++i) {
        fscanf(fp, "%s", buffer);
        printf("%s\n", buffer);
    }
    return 1;
}
