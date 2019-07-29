from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft
# /usr/local/bin

# Relative path

path = Path("ecommerce")
print(path.exists())

path = Path()
print(path.glob('*.py'))
# for file in path.glob('*'):
for file in path.glob('*.py'):
    print(file)