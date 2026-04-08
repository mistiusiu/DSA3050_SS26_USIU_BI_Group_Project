# Data Architecture

## Overview

The data model is designed using a **star schema**. This means there is one main table (fact table) in the center, and several smaller tables (dimension tables) around it.

* The **fact table** stores the main values (like engagement and likes)
* The **dimension tables** describe the data (like date, content type, state, etc.)

All the dimension tables connect to the fact table, which makes it easy to analyze the data from different angles.

![alt text](../assets/data_model_diagram.png)

## Fact Table

### Fact Table Social Media Engagement

This is the **main table** in the model.

Each row represents **one tweet**.

![Fact Table Social Media Engagement Snippet 1](../assets/fact_social_media_1.png)

![Fact Table Social Media Engagement Snippet 2](../assets/fact_social_media_2.png)

![Fact Table Social Media Engagement Snippet 3](../assets/fact_social_media_3.png)

This table is used to:

* Calculate totals (e.g. total engagement)
* Compare values (e.g. engagement by content type)



## Dimension Tables

These tables give **extra information** about the data in the fact table.

### Dimension Table Date

![Dimension Table Date](../assets/dim_date.png)

Used to:

* Analyze trends over time
* Compare engagement by month or year



### Dimension Table Day Power Query

![Dimension Table Day Power Query](../assets/dim_day.png)

Used to:

* Analyze engagement per day


### Dimension Table Day Type

![Dimension Table Day Type](../assets/dim_day_type.png)

Used to:

* Compare weekend vs weekday performance



### Dimension Table Open Hours

![Dimension Table Open Hours](../assets/dim_open_hours.png)

Used to:

* Find the best time to post



### Dimension Table Content Type

![Dimension Table Content Type](../assets/dim_content_type.png)

Used to:

* See which content performs best



### Dimension Table Post Type

![Dimension Table Post Type](../assets/dim_post_type.png)

Used to:

* Analyze different types of posts



### Dimension Table State

![Dimension Table State](../assets/dim_state.png)

Used to:

* Compare engagement across locations



### Dimension Table Influencer Status

![Dimension Table Influencer Status](../assets/dim_influencer_status.png)

Used to:

* Compare high vs low influence accounts


### Dimension Table Phase

![Dimension Table Phase](../assets/dim_phase.png)

Used to:

* Analyze how engagement changed over time


### Dimension Table Verbosity

![Dimension Table Verbosity](../assets/dim_verbosity.png)

Used to:

* Write something here 


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

