from cx_Freeze import setup, Executable 

setup(name ='test',
      version=1,
      executables = [Executable("main.py")])

