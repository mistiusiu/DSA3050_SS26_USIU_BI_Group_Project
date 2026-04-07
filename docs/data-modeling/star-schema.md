
# Data Model Description

## Overview

The data model is designed using a **star schema**. This means there is one main table (fact table) in the center, and several smaller tables (dimension tables) around it.

* The **fact table** stores the main values (like engagement and likes)
* The **dimension tables** describe the data (like date, content type, state, etc.)

All the dimension tables connect to the fact table, which makes it easy to analyze the data from different angles.

![alt text](../assets/data_model_diagram.png)

## Fact Table

### Fact_SocialMediaEngagement

This is the **main table** in the model.

Each row represents **one tweet**.

It contains:

* Engagement
* Like_Count
* Negative_Sentiment
* Content_Type
* Date
* Day
* Day_Type
* Influencer_Status
* Phase

This table is used to:

* Calculate totals (e.g. total engagement)
* Compare values (e.g. engagement by content type)



## Dimension Tables

These tables give **extra information** about the data in the fact table.



### Dim_Date

Contains:

* Date
* Day Name
* Month
* Month Name
* Year

Used to:

* Analyze trends over time
* Compare engagement by month or year



### Dim_Day

Contains:

* Day

 Used to:

* Analyze engagement per day


### Dim_DayType

Contains:

* Day_Type (Weekday / Weekend)

 Used to:

* Compare weekend vs weekday performance



### Dim_OpenHours

Contains:

* Open_Hours (time of posting)

 Used to:

* Find the best time to post



### Dim_ContentType

Contains:

* Content_Type (image, video, text)

 Used to:

* See which content performs best



### Dim_PostType

Contains:

* Post_Type

Used to:

* Analyze different types of posts



### Dim_State

Contains:

* State

Used to:

* Compare engagement across locations



### Dim_InfluencerStatus

Contains:

* Influencer_Status

Used to:

* Compare high vs low influence accounts


### Dim_Phase

Contains:

* 4_Phase (pre-COVID, lockdown, post-COVID)

Used to:

* Analyze how engagement changed over time



## Relationships

All tables are connected in this way:

 **Dimension → Fact (One-to-Many relationship)**

This means:

* One value in a dimension (e.g. one date)
* Can relate to many tweets in the fact table



### Example:

* One date → many tweets
* One content type → many tweets
* One state → many tweets



## Important Points

* All dimension tables connect **only to the fact table**
* Dimension tables do **not connect to each other**
* Filtering always goes from dimension → fact



### Example of how it works

If you select:

* Content Type = Video
* Day Type = Weekend

The model will filter the fact table and show:

* Only weekend video tweets
* Then calculate engagement


## Summary

* The fact table stores **numbers (engagement, likes, sentiment)**
* Dimension tables store **descriptions (date, content type, state, etc.)**
* The model allows you to analyze data from many perspectives easily

