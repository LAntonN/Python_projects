text = """
On June 1, 1865, Senator Charles Sumner referred to the most famous speech ever given by President Abraham Lincoln. In his eulogy on the slain president, he called the Gettysburg Address a "monumental act." He said Lincoln was mistaken that "the world will little note, nor long remember what we say here." Rather, the Bostonian remarked, "The world noted at once what he said, and will never cease to remember it. The battle itself was less important than the speech."

There are five known copies of the speech in Lincoln's handwriting, each with a slightly different text, and named for the people who first received them: Nicolay, Hay, Everett, Bancroft and Bliss. Two copies apparently were written before delivering the speech, one of which probably was the reading copy. The remaining ones were produced months later for soldier benefit events. Despite widely-circulated stories to the contrary, the president did not dash off a copy aboard a train to Gettysburg. Lincoln carefully prepared his major speeches in advance; his steady, even script in every manuscript is consistent with a firm writing surface, not the notoriously bumpy Civil War-era trains. Additional versions of the speech appeared in newspapers of the era, feeding modern-day confusion about the authoritative text.


Bliss Copy

Ever since Lincoln wrote it in 1864, this version has been the most often reproduced, notably on the walls of the Lincoln Memorial in Washington. It is named after Colonel Alexander Bliss, stepson of historian George Bancroft. Bancroft asked President Lincoln for a copy to use as a fundraiser for soldiers (see "Bancroft Copy" below). However, because Lincoln wrote on both sides of the paper, the speech could not be reprinted, so Lincoln made another copy at Bliss's request. It is the last known copy written by Lincoln and the only one signed and dated by him. Today it is on display at the Lincoln Room of the White House.

Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.


"""
print(len(text.split()))

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)