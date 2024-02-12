#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

char* solution(const char* myString) {
    int size = strlen(myString);
    char* answer = (char*)malloc(size * sizeof(char)); 
    
    for (int i = 0; i < size; i++) {
        answer[i] = tolower(myString[i]);
    }
    
    answer[size] = '\0'; 

    return answer;
} 