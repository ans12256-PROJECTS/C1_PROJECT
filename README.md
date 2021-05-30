# Proposal 1: Amazon reviews tester
The idea of the project is a service delivered via a webpage (Docker?), that accepts a single URL with amazon merchandise reviews, and replies with an estimate of trustworthiness of subject reviews.
The null hypothesis $H_0$ is as follows "All(50%?) reviews are fake, and planted/paid for by merchants". Alternative hypothesis is $H_a$ "N reviews are real, and can be counted". Output is N reviews are real with average rating of X stars.
The algorithm is as follows:
1) Choose a reviewer and start rating
2) Check if reviewer is located in US (plus)
3) Check if reviewer has tag "Verified Purchase" (plus), discard otherwise
4) Check if reviewer has photos (plus)
5) **Optional** Check if photos are not available at [google images](https://images.google.com) (stock photos), if yes, discard review
6) Check if reviewer has more than one review (plus)
7) Count non-discarded reviews
8) Output results 8.1) Percentage of fake/paid? reviews, Level of trustworthiness of the rest (% of "pluses" ?)
9) **Optional** If possible recommend alternatives
10) **Optional** If possible recommend identical merchandise at lower price. Assumption all local retailers buy from the same supplier with different mark up. There is no reason to pay extra for the same product.


* Skills to feature:
  ## Web Scraping:
  Use `BeautifulSoup` to process amazon pages for analysis of the reviews

  ## Data Pipelines
  Process data procured by `BeautifulSoup` to search for applicable tags, images, and accumulate results using python, numpy, pandas, scipy libraries. PostgreSQL could be utilized for data storage, since non-SQL databases like Mongo would unlikely be required. All python routines should have a docstring preferably with OOP format

  ## Data Visualization
  Animated Bayesian curves as data is being processed is one optional feature. Supposedly one of the early developers once said that program that does not output anything in 10 seconds is no good? COnstant feedback to the user (preferably not in the form of rotating clock)

  ## Hypothesis Testing
  "50% of reviews are fake"? "Based on statistical analysis of reviews, you may want to reconsider this purchase"? "The reviews seem legit. Never mind angry reviewers - maybe competitors"?
