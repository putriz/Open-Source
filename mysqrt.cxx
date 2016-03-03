#include <stdio.h>
#include <stdlib.h>
double absolute(double a)
{
  if (a >= 0) return a;
  else return -a;
}
  
double mysqrt(double x)
{
  double guess;
  if (x < 0) 
    {
      //fprintf(stdout, " The number has to be nonnegative %g \n", 0);
      return 0;
    }
  if (x == 0)
    {
      //fprintf(stdout,"The square root of 0 is 0 \n");
      return 0;
    }
  guess = x/2.0;
  while ( absolute((guess*guess)/x - 1.0 ) >= 0.000001)
    guess  = ((x/guess)+guess)/2;
  return guess;
}
