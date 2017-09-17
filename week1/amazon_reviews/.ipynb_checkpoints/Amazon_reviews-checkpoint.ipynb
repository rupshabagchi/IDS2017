{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import json\n",
    "import string\n",
    "\n",
    "# Read json objects into an array\n",
    "data = []\n",
    "with open(\"Automotive_5.json\") as f:\n",
    "    for line in f:\n",
    "        data.append(json.loads(line))\n",
    "\n",
    "# Lowercasing, remove punctuation\n",
    "for entry in data:\n",
    "    edited = entry[\"reviewText\"]\n",
    "    edited = \"\".join(l for l in edited if l not in string.punctuation)\n",
    "    edited = edited.lower()\n",
    "    entry[\"reviewText\"] = edited\n",
    "\n",
    "# Remove stopwords\n",
    "with open(\"stop-word-list.csv\") as f:\n",
    "    stopwords = set(f.read().split(\", \"))\n",
    "    \n",
    "for entry in data:\n",
    "    text = entry[\"reviewText\"]\n",
    "    entry[\"reviewText\"] = \" \".join([word for word in text.split() if word not in stopwords])\n",
    "\n",
    "# Apply stemming\n",
    "from nltk.stem.porter import *\n",
    "ps = PorterStemmer()\n",
    "for entry in data:\n",
    "    entry[\"reviewText\"] = \" \".join([ps.stem(word) for word in entry[\"reviewText\"].split()])\n",
    "\n",
    "# Split into positive and negative\n",
    "pos = []\n",
    "neg = []\n",
    "\n",
    "for entry in data:\n",
    "    if entry[\"overall\"] > 3:\n",
    "        pos.append(entry[\"reviewText\"])\n",
    "    elif entry[\"overall\"] < 3:\n",
    "        neg.append(entry[\"reviewText\"])\n",
    "\n",
    "with open(\"pos.txt\", 'w') as f:\n",
    "    f.write(\"\\n\".join(pos))\n",
    "with open(\"neg.txt\", 'w') as f:\n",
    "    f.write(\"\\n\".join(neg))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
