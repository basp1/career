#include <limits>

int sign(int c)
{
    return ((unsigned int)c) >> 31;
}

int changebit(int c)
{
    return c ^ 1;
}

int getmax(int a, int b)
{
    static int ab[2];
    ab[0] = a; ab[1] = b;

    int ia = sign(a);
    int ib = sign(b);
    int i = sign(a - b);
    
    i = i * changebit(ia ^ ib) + (ia ^ ib) * ia;

    return ab[i];
}