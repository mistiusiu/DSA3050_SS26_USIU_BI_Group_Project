# Social Media Sentiment Business Intelligence Analytics

## Problem Statement

Social media platforms like Twitter are widely used by organizations to engage with audiences. However, it is often unclear which factors—such as content type, posting time, sentiment, or audience size—drive higher engagement (likes, replies, and retweets). This project analyzes a dataset of tweets from Destination Marketing Organizations to identify patterns and factors that influence social media engagement.


## Business Questions
The analysis aims to answer the following questions:
1.	How does influencer status affect tweet engagement?
2.	Which generates the highest engagement?
3.	How did engagement patterns change across different phases (pre-COVID, lockdown,        post-COVID)?
4.	Which day of the week has more engagement?
5.	Which state has the influencers with highest number of followers based on average?
6.	Which influencer type have most negative /positive sentiments?
7.	Does posting during working hours or non-working hours affect engagement?
8.	Do tweets posted on weekends perform differently than weekdays?
9.	What content type does different influencers post?
10.	In what state when posts are made that have the highest engagement?
11.	Does word count (WC) influence engagement levels?


## Data Sources

Dataset: DMO Social Media Engagement Dataset

Source: Kaggle

Accessed via Kaggle:
https://www.kaggle.com/datasets/jocelyndumlao/dmo-social-media-engagement-dataset

Primary Source:
https://data.mendeley.com/datasets/bfk3hvdcnt/1

This dataset contains 21,677 tweets collected from 23 Destination Marketing Organizations (DMOs) between March 25, 2019 and January 31, 2022. It was created to study how social media content strategies and linguistic features affect user engagement on Twitter. 

## Data Model Description

The project uses a star schema data model designed to analyze social media engagement. In this model, a central fact table stores engagement metrics for tweets, while several dimension tables provide contextual information such as time, content type, influencer status, and posting characteristics.

## Fact Table

### Fact_SocialMediaEngagement

This table contains the quantitative metrics related to tweet performance and engagement.

Examples of measures include:

-	Retweet_Count

-	Reply_Count

-	Like_Count

-	Quote_Count

-	Buzz (overall engagement indicator)

-	Sentiment scores (Positive, Negative, Total Sentiment)

Each record represents one tweet and links to several dimension tables.

## Dimension Tables

### Dim_Date

Provides temporal information about when a tweet was posted.

Attributes:

- Date

- Day Name

- Month

- Month Name

- Year

This dimension allows analysis of engagement trends over time.

### Dim_Day

Contains the numeric representation of the day of the week.

Attribute:

-	Day

Used to analyze engagement patterns across different days.


### Dim_DayType

Categorizes days into broader groups.

Attribute:

- Day_Type (Weekday or Weekend)

This allows comparison of engagement during weekdays versus weekends.

### Dim_OpenHours

Represents the time of day when tweets were posted.

Attribute:

- Open_Hours

This dimension enables analysis of engagement patterns by posting time.

### Dim_ContentType

Describes the type of content shared in the tweet.

Attribute:

- Content_Type

Examples may include:

- Image

- Video

- Text

This helps determine which type of content generates the most engagement.

### Dim_PostType

Represents the structure or format of the tweet.

Attribute:

- Post_Type

This dimension helps analyze how different post formats influence engagement.

### Dim_State

Represents the geographic location of the account posting the tweet.

Attribute:

- State

This allows comparison of engagement across different regions or organizations.

### Dim_InfluencerStatus

Categorizes accounts based on their influence or follower size.

Attribute:

- Influencer_Status

This dimension allows analysis of how account influence impacts engagement.

### Dim_Phase

Represents the period during which the tweet was posted.

Attribute:

4_Phase

The dataset categorizes tweets into phases such as:

- Pre-COVID

- Lockdown

- Post-Lockdown

This allows analysis of how engagement patterns changed across different time periods.
## Data Model Diagram
![Alt text]("C:\Users\Admin\Pictures\Screenshots\Screenshot 2026-03-10 225107.png")
