# Colorize Comments

## What color is deception?

With increasing popularity of web reviews, there’s been an explosion of web authorship from individuals. These reviews may be classified as false reviews or Opinion Spam. Opinion Spam is inappropriate or fraudulent reviews. It can range from self-promotion of an unrelated website or blog to deliberate review fraud with a potential for monetary gain.

One risk of Opinion Spam is the reviews that falsely praise inferior products or criticize superior products, as they may affect a potential consumer’s actions. Therefore, companies are highly motivated to automatically detect and remove Opinion Spam. Other Natural Language Processing (NLP) tasks, like sentiment analysis or intent recognition, have received considerable computational attention. But, relatively little study has been conducted in detecting Opinion Spam using text classification techniques.

Some types of Opinion Spam are easily identified by a human reader. For example, advertisements, questions, or other non-opinion texts. These instances belong to Disruptive Opinion Spam—irrelevant statements that are evident to a reader and pose a minimal risk, since the user can always choose to ignore them. However, for more insidious types of fictitious texts, like Deceptive Opinion Spam, the task is non-trivial. These statements have been intentionally produced to sound authentic and mislead the reviewer. Deceptive Opinion Spam commonly takes the form of fake reviews (negative or positive). A malicious web user posts the reviews to hurt or inflate a company’s image. As these reviews have been deliberately written to deceive the reader, human reviewers are faring little better than a chance in detecting these deceptive statements. Thus, there’s a dire need to address this issue. Extracting text patterns from the fraudulent texts with meaningful substructures remains a challenge.

To understand how lies are expressed in texts, we investigated the usefulness of the other approaches. The Azure Text Analytics client library for Python is used for the investigation. The library allows you to:

* Get various aspects of a sentiment. For example, neutrality or negativity.
* Analyze overall sentiment, which may not always be uniform. Some reviews are composed of both negative and positive aspects.


# Prerequisites
* Python 2.7, or 3.5 or later
* Azure subscription and a Cognitive Services or Text Analytics resource. For more information, see the official documentation.
* Azure Text Analytics library for Python. Install the library using pip:
```commandline
pip install azure-ai-textanalytics
```
* OpenCV for data visualization. Similarly, install the package via pip:
```commandline
pip install opencv-python
```
* Dataset. For this experiment, we’re using the Ott Deceptive Opinion spam corpus—one of the first large-scale, publicly available datasets in this domain. It’s composed of 400 truthful and 400 gold-standard deceptive reviews, collected using Amazon Mechanical Turk. 


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
