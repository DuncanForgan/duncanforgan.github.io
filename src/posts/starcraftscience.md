# Starcraft as a Citizen Science Tool

In a similar vein to [last week's post](/blog/galactic-grand-tours-and-strengthening-fermis-paradox "Galactic Grand Tours, and strengthening Fermi’s Paradox"), I'm proud to show you results from an outreach project I've been working on with [Tom Targett](http://www.roe.ac.uk/ifa/people/tat.html) at the ROE for the last few months.  As the result of a rather long-winded discussion of interstellar colonisation at coffee time, we got to thinking about how rigorously we could simulate conflict between competing civilisations.
Of course, we don't have any evidence that other civilisations even exist, let alone fight each other for resources.  All we know is that conflict has been an important part of human history since time immemorial, and that we can see the origins of our penchant for tribalism and warfare [in our primate cousins](http://news.bbc.co.uk/earth/hi/earth_news/newsid_8400000/8400019.stm).

[![](/images/posts/starcraftscience/dday.jpg)](/images/posts/starcraftscience/dday.jpg)

*The D Day landings. Via ww2incolor.com*

As it would be churlish from a scientific standpoint to [assume that our aggressive behaviour is unique](http://en.wikipedia.org/wiki/Copernican_principle) amongst intelligent species, Tom and I felt it was safe to assume in our current ignorance that intelligent species are completely capable of conducting interstellar wars, and would do so to secure resources.
This still left us with a bit of a problem - how can you model interstellar conflict when you know nothing about the combatants? It was then that we hit on the idea of calibrating our simulations by using 'real' data on how alien species fight.  [StarCraft 2](http://en.wikipedia.org/wiki/StarCraft_II:_Wings_of_Liberty), a real time strategy game played throughout the world, has several races of belligerents, who fight each other frequently in the domain of Massively Multiplayer Online gaming.  In a classic example of citizen science, we found that the general public had generated a vast dataset of (admittedly fictional) alien behaviour, which we could use to drive our simulations.
So, we created a population of stars similar to the local Solar neighbourhood, and seeded it with six different races, each representing one of the three civilisations (the Terrans, the insectoid Zerg and the advanced, telepathic Protoss), carrying out one of two strategies.

The "macro" strategy refers to species which build up large amounts of resources before moving against an opponent in an attempt to overwhelm them; the "micro" strategy encourages rapid motion of a smaller military force to quickly eliminate a fledgling opponent. This gives 30 possible combinations of combatants.  As we had access to user data showing the outcome of each combination rehearsed many times in StarCraft 2 games played online, we could soon develop a probability that Race 1 defeats Race 2, and so on and so forth.

This allowed us to do two things: i) we could see if there was a preferred strategy for StarCraft 2 users to adopt, and ii) How does the balance of power change when these alien races are placed in a Galactic context?

We looked at i) by searching for a [Nash Equilibrium](http://en.wikipedia.org/wiki/Nash_equilibrium).  This is a set of strategies (in this case for two players), that if both players agree to adopt, then there is no better solution to be found by changing tack.  When we did the analysis, we found that the best possible solution for both players is to randomly select from the six races.  This is a consequence of the Starcraft developers keeping the six races evenly matched, so that the game would remain interesting to the players.

[![A snapshot of the simulation.  The colours represent the space colonised by each race](/images/posts/starcraftscience/mov_sc2.png)](/images/posts/starcraftscience/mov_sc2.png)

*A snapshot of the simulation. The colours represent the space colonised by each race*

But is this still true if you place the species in interstellar space?  [Almost](www.roe.ac.uk/~tat/StarCraftScience): as the species are all quite evenly matched, the sector ends up in an equilibrium where each species has approximately 1/6th of the available resources (you can see a movie of the simulation, and download the paper at the link above).  But statistically, when watching this sector being colonised many times over, the Terrans have a slight advantage when using the "micro" strategy.  If we make the simulation more "realistic" by allowing the micro strategists to move faster in interstellar space, the micro strategy utterly dominates.  Even if we balance this by allowing the defenders of a star system to have a "defender's advantage" (we calculated this by looking at how Starcraft 2 gamers fared when they selected the map to battle on), the three species that choose a micro strategy rule the sector (and presumably, the Galaxy).

As I said, this is fairly arbitrary - we don't intend to claim the Zerg and Protoss are real! We were interested in seeing how the [video games industry can help scientists understand difficult topics](http://en.wikipedia.org/wiki/Corrupted_Blood_incident) like life in the Galaxy, where actual data is so thin on the ground.

But thankfully, it does seem like Earth has a slight edge when it comes to interstellar dominion...

[![Not included in the simulation...](/images/posts/starcraftscience/st_web01.jpg)](/images/posts/starcraftscience/st_web01.jpg)

*Not a snapshot from the simulation...*

