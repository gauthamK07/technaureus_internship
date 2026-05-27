from contextlib import contextmanager

@contextmanager
def my_context(filename,mode):
    print("Opening the file")
    f=open(filename,mode)
    try:
        yield f
        print("Executing inside the context manager")
    except Exception as e:
        print("Error:",e)   
    finally:
        print("Closing the file")
        f.close()

with my_context("test1.txt",'w') as f:
    f.write("hello")
