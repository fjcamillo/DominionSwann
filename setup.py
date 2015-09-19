from cx_Freeze import setup, Executable

setup(name = 'Dominion',
      version='0.1',
      description='something swanny',
      executables = [Executable('login_user.py')])
