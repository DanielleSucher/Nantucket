## On the structure of a limerick

Limericks have a fairly loose form. The rhyme scheme and syllable count is typically something like this:

> A (7, 8 or 9 syllables)  
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
  
And eventually will perhaps look for the following meter as well:
  
> duh DUM duh duh DUM duh duh DUM  
> duh DUM duh duh DUM duh duh DUM  
> duh DUM duh duh DUM   
> duh DUM duh duh DUM  
> duh duh DUM duh duh DUM duh duh DUM


## Example results

from *Swann's Way* by Proust:

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

> to abandon the habit of  
> lying Even from the point of  
> view of coquetry  
> pure and simple he  
> had told her can't you see how much of


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

from *Genesis*:
 
> in the iniquity of the  
> city And while he lingered the  
> men laid hold upon  
> his hand and upon  
> the hand of his wife and upon the

> Amorite and the Girgasite  
> And the Hivite and the Arkite  
> and the Sinite And  
> the Arvadite and  
> the Zemarite and the Hamathite

from *Huckleberry Finn* by Mark Twain:

> he suspicion what we're up to  
> Maybe he won't But we got to  
> have it anyway  
> Come along So they  
> got out and went in The door slammed to

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


## TODO (maybe)

take meter into account  
maybe make it worth with different limerick formats qua different strategies one can choose
make the search algorithm faster/more efficient (perhaps by not starting from scratch for each go-round)


## How to use

Written with Python 2.7.2, using the awesome nltk library and the CMU pronunciation dictionary. 

    pip install numpy  
    pip install nltk  
  
To get the CMU dictionary (which is critical):  

    $ python  
    >>> import nltk  
    >>> nltk.download()  
    NLTK Downloader
    ---------------------------------------------------------------------------
        d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
    ---------------------------------------------------------------------------
    Downloader> d

    Download which package (l=list; x=cancel)?
      Identifier> cmudict
        Downloading package 'cmudict' to ~/nltk_data...
          Unzipping corpora/cmudict.zip.

To add my CMU-based suffix dictionary, just stick 'cmusuffdict' into a new directory 'cmusuffdict' in your nltk_data/corpora/ directory.

    $ mkdir ~/nltk_data/corpora/cmusuffdict
    $ mv suffdict_creation/cmusuffdict ~/nltk_data/corpora/cmusuffdict/

IF you're curious about how I handled rhyming words not in the CMU dictionary, check out suffdict.py and test_suffdict.py. I get approximately 90.85% accuracy, according to my tests. Or you can read my ridiculously long blog post about the making of Nantucket - http://www.daniellesucher.com/2012/04/nantucket-an-accidental-limerick-detector/
  
Once you have all that, you can search for accidental limericks in any text (from a directory containing both Nantucket's files and the text) on the command line with: python nantucket.py --text *filename* (ie: *python nantucket.py --text ulysses.txt*).
