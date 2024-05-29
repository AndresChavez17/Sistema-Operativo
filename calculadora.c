#include <stdio.h>

int main() {
    char operador;
    float num1, num2;

    printf("Ingrese el operador (+, -, *, /): ");
    scanf("%c", &operador);

    printf("Ingrese dos números: ");
    scanf("%f %f", &num1, &num2);

    switch (operador) {
        case '+':
            printf("Resultado: %.2f\n", num1 + num2);
            break;
        case '-':
            printf("Resultado: %.2f\n", num1 - num2);
            break;
        case '*':
            printf("Resultado: %.2f\n", num1 * num2);
            break;
        case '/':
            if (num2 != 0)
                printf("Resultado: %.2f\n", num1 / num2);
            else
                printf("Error: División por cero\n");
            break;
        default:
            printf("Operador no válido.\n");
    }

    return 0;
}