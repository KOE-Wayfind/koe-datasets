from PIL import Image
import pathlib as pl

# place = 'oddai'
# place = 'oscent'
# place = 'Main-entrance'
# place = 'conference-a'
# place = 'conference-b'
place = 'enginius-office'

path = pl.Path(f'new/rgb/{place}/')
new = pl.Path(f'new/gray/{place}/')

# Create new directory
new.mkdir(parents=True, exist_ok=True)

for file in path.iterdir():
    if file.is_file():
        im = Image.open(file)
        im = im.convert('L')
        # save to new directory
        file = new / file.name
        print(f'Saving {file}')
        im.save(file)