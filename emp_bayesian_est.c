#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define k 4

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Enter file name as command line Argument\nAborting\n");
        return 0;
    }

    const char* fileName = argv[1];
    FILE *fp = fopen(fileName, "r");
    if (fp == NULL) {
        printf("Could not open file\n");
        return 0;
    }

    return 0;
}