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
  
And eventually will look for the following meter as well:
  
> duh DUM duh duh DUM duh duh DUM  
> duh DUM duh duh DUM duh duh DUM  
> duh DUM duh duh DUM   
> duh DUM duh duh DUM  
> duh duh DUM duh duh DUM duh duh DUM

## Example results

From *Swann's Way* by Proust:

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

from *Ulysses* by James Joyce:

> grace about you I can give you  
> a rare old wine that'll send you  
> skipping to hell and  
> back Sign a will and  
> leave us any coin you have If you

> then he tipped me just in passing  
> but I never thought hed write making  
> an appointment I  
> had it inside my  
> petticoat bodice all day reading

> meant till he put his tongue in my  
> mouth his mouth was sweetlike young I  
> put my knee up to  
> him a few times to
> learn the way what did I tell him I

From *Genesis*:
 
> in the iniquity of the  
> city And while he lingered the  
> men laid hold upon  
> his hand and upon  
> the hand of his wife and upon the

from *Huckleberry Finn* by Mark Twain:

> and see her setting there by her  
> candle in the window with her  
> eyes towards the road and  
> the tears in them and  
> I wished I could do something for her

from *The Brothers Karamazov* by Fyodor Dostoevsky:

> eyes with a needle I love you  
> I love only you Ill love you  
> in Siberia  
> Why Siberia  
> Never mind Siberia if you  
  
> are children of twelve years old who  
> have a longing to set fire to  
> something and they do  
> set things on fire too  
> Its a sort of disease Thats not true  
  
> and be horror struck How can I  
> endure this mercy How can I  
> endure so much love  
> Am I worthy of  
> it Thats what he will exclaim Oh I


## TODO

implement better last-syllable grapheme-to-phoneme translation
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

To add the CMU-based suffix dictionary, just stick 'cmusuffdict' into a new directory 'cmusuffdict' in your nltk_data/corpora/ directory.
  
Once you have all that, you can search for accidental limericks in any text on the command line with: python nantucket.py --text *filename* (ie ulysses.txt)