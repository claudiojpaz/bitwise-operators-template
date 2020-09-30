#include <stdio.h>
#include "timer.h"
#include "print_tools.h"

int main (void)
{
  unsigned int b = 1;

  while (1) {

    printf("%08u\n", integer2byte_rep(b));

    b <<= 1;
    if (b >= 255)
      b = 1;

    msleep(500); // ms
    fflush(stdout); // no borrar
  }

  return 0;
}
