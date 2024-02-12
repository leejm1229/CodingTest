#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int solution(const char* str1, const char* str2) {
    int size1 = strlen(str1);
    int size2 = strlen(str2);

    for (int i = 0; i <= size2 - size1; i++) {
        if (strncmp(&str2[i], str1, size1) == 0) {
            return 1;
        }
    }

    return 0;
}