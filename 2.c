/*Create a Structure called BankMgmt with AccNumber, CustName, AvlBalance,
AccType as members. Implement a Bank management Application as menu driven 
program for the above said Structure scenario.
Menu Option:
1. Withdrawal 2. Deposit 3. Display Balance 4. Exit
If option
1 is chosen- Amount can be withdrawn from the account (Withdrawn amount 
should be given as input). For withdrawal the condition is- the AvlBalance must be 
greater than withdrawn amount). 
2 is chosen- Amount can be deposited to the account (the deposited amount 
should be given as input). The deposited amount should be reflected in AvlBalance of 
the account.
3 is chosen- Current available balance (AvlBalance) of the AccNumber should 
be Displayed with other details
4 is chosen- Exit from the application.
 */
#include <stdio.h>
#include <stdlib.h>

// Structure declaration 
typedef struct 
{
    int *array1; // Pointer to the first array
    int *array2; // Pointer to the second array
} Arrays;

int main() {
    int n; // Size of the array
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    // Dynamically allocate memory for the structure
    Arrays *arrays = (Arrays *)malloc(sizeof(Arrays));
    if (arrays == NULL) 
    {
        printf("Memory allocation for structure failed.\n");
        return 1;
    }

    // Dynamically allocate memory for the arrays
    arrays->array1 = (int *)malloc(n * sizeof(int));
    arrays->array2 = (int *)malloc(n * sizeof(int));
    if (arrays->array1 == NULL || arrays->array2 == NULL) 
    {
        printf("Memory allocation for arrays failed.\n");
        free(arrays);
        return 1;
    }

    // Input elements into the first array
    printf("Enter %d elements for the array:\n", n);
    for (int i = 0; i < n; i++) 
    {
        scanf("%d", (arrays->array1 + i)); // Pointer arithmetic to access elements
    }

    // Process and copy elements to the second array
    for (int i = 0; i < n; i++) 
    {
        if (i % 2 == 0) 
        {
            // Even-positioned index (odd-positioned element)
            *(arrays->array2 + i) = *(arrays->array1 + i); // Copy directly
        } 
        else 
        { 
            // Odd-positioned index
            if (i > 0 && i < n - 1) 
            {
                *(arrays->array2 + i) = (*(arrays->array1 + i - 1)) * (*(arrays->array1 + i + 1));
            } 
            else 
            {
                *(arrays->array2 + i) = *(arrays->array1 + i); // Edge cases (first/last element)
            }
        }
    }

    // Display the second array
    printf("The elements of the second array are:\n");
    for (int i = 0; i < n; i++) 
    {
        printf("%d ", *(arrays->array2 + i));
    }
    printf("\n");

    // Free allocated memory
    free(arrays->array1);
    free(arrays->array2);
    free(arrays);

    return 0;
}
