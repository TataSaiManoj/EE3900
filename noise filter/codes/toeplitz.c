#include <stdio.h>
#include <stdlib.h>

int m = 6; 
int n = 20; 

double **toeplitz(double x[m], double y[n])
{   
    double **matrix = (double**)malloc((n + m - 1) * sizeof(double*)); 

    for(int i = 0; i < (n + m - 1); i++)
    {
        matrix[i] = (double*)malloc(n * sizeof(double)); 
    }

    for(int i = 0; i < (n + m - 1); i++)
    {
        for(int j = 0; j <  n; j++)
        {
            if(i - j < m)
                matrix[i][j] = x[i - j]; 
            else
                matrix[i][j] = 0; 
        }
    }

    return matrix; 
}

void matmul(double **mat1, double mat2[m], double product[(n + m - 1)])
{

    for(int i = 0; i < (n + m - 1); i++)
    {
        double result = 0.0; 

        for(int j = 0; j < n; j++)
        {
            result += (mat1[i][j] * mat2[j]); 
        }

        product[i] = result; 
    }
}


int main()
{
    double x[] = {1, 2, 3, 4, 2, 1}; 
    double y[n]; 

    FILE* fp; 
    fp = fopen("input.txt", "w"); 

    int k = n; 

    y[0] = x[0]; 
    y[1] = -0.5*x[0] + x[1]; 

    for(int i = 2; i < k - 1; i++)
    {
        if(i < 6)
        {
            y[i] = -0.5*y[i-1]+x[i]+x[i-2];
        }
        else if(i > 5 && i < 8)
        {
            y[i] = -0.5*y[i-1] + x[i-2]; 
        }
        else
        {
            y[i] = -0.5*y[i-1]; 
        }
    }

    // passing y to the python file 

    for(int i = 0; i < n; i++)
    {
        fprintf(fp, "%lf ", y[i]);
    }

    double** result = toeplitz(x, y); 

    double ans[(n + m - 1)]; 

    for(int i = 0; i < (n + m - 1); i++)
    {
        ans[i] = 0; 
    }

    matmul(toeplitz(x, y), x, ans); 

    for(int i = 0; i < n; i++)
    {
        printf("%lf, ", y[i]); 
    }

    fclose(fp); 

    // to print the Toeplitz matrix 

    // for(int i = 0; i < 25; i++)
    // {
    //     for(int j = 0; j < 20; j++)
    //     {
    //         printf("%lf ", result[i][j]); 
    //     }

    //     printf("\n"); 
    // }

    // to print the coefficient matrix for the polynomial

    // for(int i = 0; i < 25; i++)
    // {
    //     printf("%lf ", ans[i]); 
    // }
} 
