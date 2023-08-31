#https://stackoverflow.com/questions/57854382/some-generator-object-clarification
s=iter(input());print('NYOE S'[all(c in s for c in 'hello')::2])