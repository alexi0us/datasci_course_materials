
rt sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def create_sent_dictionary(file):
    afinnfile = open(file)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    
    return scores.items() # Print every (term, score) pair in the dictionary

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
#     hw()
#     lines(sent_file)
#     lines(tweet_file)
    sentiment = create_sent_dictionary(sys.argv[1])
    tweets = []

    for line in open(sys.argv[2]):
      try: 
        tweets.append(json.loads(line))
      except:
        pass
    
    texts = []
    for tweet in tweets:
        try:
            texts.append(tweet['text'].encode('utf-8'))
        except:
            pass
#     print len(texts)

    scores =[]
    for text in texts:
        score = 0
        for key,value in sentiment:
            if key in text:
                score = score + int(value)
                print score
        scores.append(score)
    
#     print len(scores)

if __name__ == '__main__':
    main()

