# How Do We Find Interesting Things in Very Large Simulations?

It's a growing problem in computational astrophysics.  Hydrodynamic simulations (say of giant molecular clouds and star forming regions) are getting very large.  When we want to analyse them and find interesting features to compare to the physical Universe, simply searching them "by eye" is becoming an enormous task.
One simple solution to this is to farm out the problem to citizen scientists, essentially doing the "by eye" hundreds of thousands of times in a few days.  This technique is great if you can break up the simulation into easily viewable chunks for each citizen scientist to look at.  But what if you can't do this, or you don't have access to millions of enthusiastic people?
We must rely on algorithms to solve this problem.  Luckily cosmologists came across similar issues in N-Body simulations of dark matter.  These simulations have slightly less physics inside, and hence grew to large sizes much quicker, which was essential to modelling the growth of structure on cosmic scales.  They used something called tensor classification to analyse the mass distribution.

![dark_matter_millenium_simulation](/images/posts/how-do-we-find-interesting-things-in-very-large-simulations/dark_matter_millenium_simulation.jpg)

*The distribution of dark matter in the Millennium Simulation.  Tensor classification helps cosmologists identify filamentary regions, and the knots where filaments collide to form dense clusters of galaxies*

This is a technique which relies on computing a rank 2 tensor, a matrix, which contains information about how the simulation changes with position over all 3 dimensions.
For example, we can compute a tidal tensor, which is two derivatives of the gravitational potential.  This measures how the gravitational force changes as a function of position.  Manipulation of the tensor (finding its eigenvalues and eigenvectors) allows us to say what shapes and geometries the gravitational force is trying to build.  Is it making pancake-like sheets? Rope-like filaments? Or is it squeezing everything into a sphere? Or, is it doing none of this, creating a void?
This technique gives cosmologists useful information about the filamentary structure of dark matter on very large scales.  In a [recent paper](http://adsabs.harvard.edu/abs/2016MNRAS.457.2501F), I investigated how these N-Body methods (where the only force active is gravity) could be ported into hydrodynamic calculations (where pressure forces, radiation and perhaps magnetic fields also play a role).
As we work with smoothed particle hydrodynamics (SPH), which also simulates a fluid using particles, these methods are easy to apply, with the advantage that there are less free parameters in the calculation.
And it has some stunning uses.  Want to find the spiral arms in a self-gravitating disc? Presto:
![sgdisc](/images/posts/how-do-we-find-interesting-things-in-very-large-simulations/sgdisc.png)
![sgdisc_tidalcluster.png](/images/posts/how-do-we-find-interesting-things-in-very-large-simulations/sgdisc_tidalcluster.png)
Want to trace the blast wave of a supernova as it travels through interstellar gas? Sure:
![SN.png](/images/posts/how-do-we-find-interesting-things-in-very-large-simulations/sn.png)
![SN_filamentsV.png](/images/posts/how-do-we-find-interesting-things-in-very-large-simulations/sn_filamentsv.png)
It is also quite good at detecting filaments in molecular clouds, but the results aren't quite as impressive - yet.  Most recently, we've been using the technique on simulations of entire galaxies, and we're starting to see how material flows in and out of spiral arms, which helps to produce molecular clouds.
We've really only just begun using tensor classification for problems like this, and there are some great possibilities for analysing magnetic field structures in a similar way.
I have some very exciting plans for this technique, so stay tuned for further updates!
