# Profiler

A python package providing simple profiling tools and reports.

## Installation

Run

```bash
pip install profilerpy
```

or

```bash
pip install git+https://github.com/Rahgooy/profiler.git@master
```

## Usage

### Methods

Profiler can be used as a wrapper for the files. For example:

```python
from profilerpy import profile
@profile
def add(a, b):
  return a + b
```

### Code blocks

Another usage is for profiling a block of code:

```python
from profilerpy import default_profiler
# Some line of code
default_profiler.start('Price calculator')
# Price calculator codes
default_profiler.finish('Price calculator')
```

### Print summary

Finally you can print the profiling summary

```python
default_profiler.print_profile()
```

### Multiple profilers

This package uses `dafult_profiler` by default. However, you can use multiple instances of the profiler class.
For example:

```python
from profilerpy import Profiler, profile
priceProfiler = Profiler() # Profile the codes related to calculating price
userProfiler = Profiler() # Profile the codes related to the user management

# Some lines of code
userProfiler.start('Find user')
# Find user codes
userProfile.finish('Find user')

# ...
default_profiler.start('Price calculator')
# Price calculator codes
default_profiler.finish('Price calculator')

@profile('update_user', profiler=userProfiler)
def update_user(user):
  pass
```

### Functions with custom names

```python
@profile('FancyName')
def method1():
  pass
```
