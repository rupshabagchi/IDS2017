# Exercise 1 - Titanic v2.0

In this exercise, we'll continue to study the Titanic data set which was used in Exercise 1.1. Now that we have preprocessed it a bit, it's time to do some exploratory data analysis.

1. First consider each feature variable in turn. For categorical variables, find out the most frequent value, i.e., the 
  mode. For numerical variables, calculate the median value.

2. Combining the modes of the categorical variables, and the medians of the numerical variables, construct an imaginary 
  "average Joe" on board of the ship. Also following the same procedure for using subsets of the passengers, construct the 
  "average survivor Jane" and the "average non-survivor Joe".

3. Now study the distributions of the variables in the two groups. How well do the average cases represent the respective 
  groups? Can you find actual passengers that are very similar to the representative of their own group (survivor/non-
  survivor)? Can you find passengers that are very similar to the representative of the _other_ group?

   Note that this task may be hard to complete since it would require that you sift through lots of data. And this is
   quite a small data set! Find ways to explore the data which facilitate this kind of investigation. You are free to
   choose your methods: non-graphical/graphical, static/interactive -- anything goes.

4. To give a more complete picture of the two groups, provide graphical displays of the distribution of the variables in 
  each group whenever appropriate (not, e.g., on the ticket number).

5. One step further is the analysis of pairwise and multivariate relationships between the variables in the two groups. Try 
  to visualize two variables at a time using, e.g., scatter plots and use a different color to display the survival status. 
  Hint: to better show many data points with the same value for a given variable, you can use either transparency or 
  'jitter'.

6. Try to come up with visualizations that best brings forth the differences between the two groups of passengers.

7. Finally, recall the preprocessing that was carried out in last week's exercises. Can you say something about the effect 
  of the choices that were made, in particular, to use the mode or the mean to impute missing values, instead of, for 
  example, ignoring passengers with missing data?

# Exercise 2 - Text data v2.0

This exercise is related to the second exercise last week. Find your self-made `pos.txt` and `neg.txt`, or if you didn't complete the exercise, you can find the model solutions here after Thursday.

1. Find the most common words in each file. What are they? Are some of them clearly general terms relating to the nature of the data, and not just the emotion?

2. Compute a [TF/IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) vector for each of the text files, and make them into a `2 x unique words` matrix.

3. List the words with the highest TF/IDF score in each class, and plot the unique words of each class and their corresponding scores. Note that there will be a lot of words, so find a way to make it clean! If you can't plot them all, plot as much as you can. How do the results differ from those in part 1?

4. Try to make your implementation as efficient as possible. How big of a dataset can you run your programs on? Try out the different sized sets of [Amazon reviews](http://jmcauley.ucsd.edu/data/amazon/). Can build the same plots for the almost 9M book reviews?


# Exercise 3 - Junk Charts

There's a thriving community of chart enthusiasts who keep looking for statistical graphics that they find inappropriate, and which they call "junk charts", and who often also propose fixes to improve them.

1. Find at least three statistical visualizations that you think aren't very good, and identify their problems. Copying 
  examples from various junk chart websites isn't accepted -- you should find your own junk charts. You should be able
  to find good (or rather, bad) examples quite easily since a large fraction of charts have at least some issues. The 
  examples you choose should also have 
  _different_ problems, so don't look for three column or bar charts whose axes don't begin at zero. Try to find as 
  interesting and diverse examples as you can.

2. Try to produce improved versions of the charts you selected. The data is of course often not available, but perhaps you 
  can try to extract it, at least approximately, from the chart. Or perhaps you can simulate data that looks similar enough 
  to make the point.


# Exercise 4 - GIS

To get at least a bit familiar with [GIS](https://en.wikipedia.org/wiki/Geographic_information_system) data and the
concept of map projections, we'll do a simple task of plotting two data sets that are given in different coordinate
systems.

1. Download the [world_m.zip](https://github.com/HY-TKTL/intro-to-data-science-2017/blob/master/world_m.zip) and [cities.zip](https://github.com/HY-TKTL/intro-to-data-science-2017/blob/master/cities.zip) files that each include a set of GIS files. Most notably, the
   `shp` files are [Shapefile](https://en.wikipedia.org/wiki/Shapefile)-files with coordinates (don't look, it's binary!). 
   The `prj` files contain information (in plain text, so okay to look) about the coordinate systems. Open the files
   using your favorite programming environment and packages. We warmly recommend [Geopandas](http://geopandas.org/) for
   pythonistas.

2. The `world_m` file contains borders of almost all countries in the world. Plot the world.

3. On top of the countries that you just plotted, plot another layer of information, namely the capital cities of each
   country from the `cities` data-set. However, depending on how clever your programming environment is, the cities
   will probably all appear to be in the Gulf of Guinea, near the coordinates (0&deg;, 0&deg;).

4. Perform a map projection to bring the two data-sets into a shared coordinate system. (You can choose which one.)
   Now plot the two layers together to make sure the capital cities are where they are supposed to be.



 
  

