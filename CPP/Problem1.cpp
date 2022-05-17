
int main()
{
    char A[] = [1, 2, 6, 3, 2, 8] function mystery(A[1...N])
    {
        int i, j, position, temp;
    for
        i = 1 to N
        {
            position = i;
        for
            j = i + 1 to N
            {
                if (A[j] < A[position])
                {
                    position = j
                }
            }
        temp = A[i];
        A[i] = A[position];
        A[position] = tmp;
        }
    }