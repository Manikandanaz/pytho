import os
for k,v in os.environ.items():
    if ('AZURE' in k):
         print(f'{k}:{v}')
