#include <stdio.h>

unsigned int integer2byte_rep (unsigned char b)
{
  unsigned char mask = 1;
  unsigned int decade = 1;
  unsigned int r = 0;

  for (int i = 0; i < 8; i++) {
    r += (b&mask?1:0)*decade;
    mask <<= 1;
    decade *= 10;
  }

  return r;
}

