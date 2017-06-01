# Lex of Anagrams

Solve puzzles of anagrams (Python 3.6.0)


## Usage

These program runs on your console.  

### Manual
```
$ python anagram_finder.py
```
You can enter word to want to find anagram in an interactive way.  

### Automatic
```
$ python webdriver.py
```
[ Caution ]  
Error when anagram is not found.  
If an error occurs interrupt program and try again.  

## About Idea

### 1. Rewrite dictionary for anagram  
This work is done by ``anagram_maker.py``.  
Output is in ``dict/``.  

### 2. Build Trie based on anagram dictionary  
The structure of Trie is made by node and edges of characters of words in the dictionary.  

**Trie field**  
- matched_words --- collect word of passing node
- thread --- record the number of node and remaining characters for pseudo parallel processing, when failing to move
- node --- list of node

**Node field**
- id --- node number  
- next --- character and number of the next node  
- output --- word in the dictionary that made with characters until it reached node  
- failture --- number of the returning node when failing to move  
- footpoint --- threads record to avoid loop  

### 3. Find words by following nodes
Following nodes will all the words in dictionary, but return the highest score word.  


## Help me!!!
I have a troubled part.  
When failing to move, that is, moving according to ``failture``, I wrote the following code in ``def fond(), anagram_finder.py`` .

``` python
while self.goto(id, query[i]) is None:
  if len(query[i:]) > 1:
    if query[i+1:] not in self.node[id].footprint.get(id, ""):
      if id not in self.node[id].footprint:
        self.node[id].footprint[id] = [query[i+1:]]
      else:
        self.node[id].footprint[id].append(query[i+1:])
      self.thread[id] = query[i+1:]
  id = self.node[id].failure
```

I cannot judge whether creating threads condition is correct.  
I made ``footprint`` variable to avoid loop.  


## Figure of Trie  
![anagram](https://raw.githubusercontent.com/d0iasm/images/master/anagram-lex/anagram.jpg)  


