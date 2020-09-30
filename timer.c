#include <stdio.h>
#define __USE_POSIX199309
#include <time.h>

void msleep(int ms)
{
  struct timespec t;

  t.tv_sec = 0;
  t.tv_nsec = 1000000;

  for (int i = 0; i < ms; i++)
    nanosleep(&t,NULL);
}
