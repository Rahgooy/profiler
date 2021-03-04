from profilerpy import profile, Profiler, default_profiler
import time

customProfiler = Profiler()


@profile
def method1():
    time.sleep(.3)

@profile('Named Method')
def method2():
    time.sleep(1)
@profile('Method3', profiler=customProfiler)
def method3():
    time.sleep(2)


default_profiler.start('Code 1')
for i in range(7):
    time.sleep(0.1)
default_profiler.finish('Code 1')

for i in range(3):
  method1()
  method2()
  method3()

default_profiler.print_profile()

print('*' * 85)
customProfiler.print_profile()
