# Colorize Comments

## What color is deception?

The idea of this project is quite straightforward. Suppose we've got 
a truthful and a deceptive review. Both of them are of the same 
polarity (positive or negative). However, as most of the 
researches claim, the deceptive reviews may have some underlying 
pattern which are visible to a machine, but not to a human reviewers. 
In some case, sentiment are exaggerated (e.g. I looooved the service, 
it was just BRILLIANT, etc). Consequently, what if we were able to 
colorize the comments and at one glance be able to evaluate the 
level of exaggeration? This is the goal if this project.

To analyze the sentiments we've used the [Azure Text Analytics API](https://docs.microsoft.com/en-us/python/api/overview/azure/ai-textanalytics-readme?view=azure-python&WT.mc_id=AI-MVP-5003429)
which allows us to get different aspects of a sentiment, like 
neutrality or negativity, besides analyzing mere overall sentiment, 
which not always be uniform, as some reviews are composed of 
negative and positive aspects.

To run the code, first, create environment variables

```commandline
export API_KEY="<your-api-key>"
export ENDPOINT="<your-endpoint>"
```

Then, configure your enviroment (you can use virtual environment, which is
generally the best solution, but with your global environment it 
also work fine, as there is no external dependency). To install all the 
required packages simply run:
```commandline
pip3 install -r requirements.txt
```
N.B. for Windows users (or if you are using virtual environment) simply
replace `pip3` with `pip`. 