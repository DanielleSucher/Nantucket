## On the structure of a limerick

Limericks have a fairly loose form. The rhyme scheme and syllable count is typically something like this:

> A (7, 8 or 9 syllables*)  
> A (7, 8 or 9)  
> B (5 or 6)  
> B (5 or 6)  
> A (7, 8 or 9)

And as if that weren't loosey-goosey enough, they can have either anapaestic meter (duh-duh-DUM, duh-duh-DUM) or amphibrachic meter (duh-DUM-duh, duh-DUM-duh)!

So, I chose the following as the canonical example to work from when building this limerick detector:

> There was a young student from Crew  
> Who learned how to count in base two.  
> His sums were all done  
> With zero and one,  
> And he found it much simpler to do.

Going by the canonical example above, Nantucket is set to look for limericks with the following structure:
  
> A (8)  
> A (8)  
> B (5)  
> B (5)   
> A (9)  
  
> duh DUM duh duh DUM duh duh DUM  
> duh DUM duh duh DUM duh duh DUM  
> duh DUM duh duh DUM   
> duh DUM duh duh DUM  
> duh duh DUM duh duh DUM duh duh DUM

## Example results

From *Swann's Way* by Proust:

> would be saying What can he be  
> doing just now I do hope he  
> doing a little  
> work It too dreadful  
> that a fellow with such gifts as he  

> bad conduct should deserve Was I  
> then not yet aware that what I  
> felt myself for her  
> depended neither  
> upon her actions nor upon my  

> was wonderful to another  
> How I should have loved to We were  
> unfortunate to  
> a third Yes if you  
> like I must just keep in the line for

From Genesis:

> in the iniquity of the  
> city And while he lingered the  
> men laid hold upon  
> his hand and upon  
> the hand of his wife and upon the


## TODO

stop the tokenizer regex from screwing up output  
handle words not found in cmudict  
take meter into account  
make it more generally usable  
maybe make it worth with different limerick formats qua different strategies one can choose
make the search algorithm faster/more efficient (perhaps by not starting from scratch for each go-round)


## How to use

Written with Python 2.7.2, using the awesome nltk library and the CMU pronunciation dictionary. 

pip install numpy  
pip install nltk  
  
To get the CMU dictionary (which is critical):  
python  
import nltk  
nltk.download()  
d  
cmudict  
  
Once you have all that... well, I'll tell you what to do once there's something to do. For the moment, it's just set to search through Swann's Way, which contains at least the three delightful accidental limericks quoted above. This is in-progress for now, sorry!