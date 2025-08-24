# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## How to run the code:

### Docker:
This is my preferred method to help you get an idea of what the code does. 

1. Build the image.
   ```
   docker build -t book-bot:latest .
   ```
2. Run the container. This will by default read ```frankenstein.txt```.
   ```
   docker run -rm book-bot
   ```
   ```rm``` will remove the container after it has exited.


### On your bare metal:
Generic Python script that reads through a .txt file or any text formatted book. 

You will need to create a ```books``` directory to store your books in. 

- [Frankenstein](https://www.gutenberg.org/cache/epub/41445/pg41445.txt)
- [Moby Dick]()

Then to run the main program you can type:
```
python3 main.py <path_to_book>
```


