# Complex Measure Explanations

Three advanced measures are highlighted below to demonstrate DAX proficiency and business logic implementation:

## 1. Top Post Type

**Business Question:** Which content format drives the most engagement?

**What it does:**  
Identifies the single highest-performing content format (image, video, link, or text) based on total engagement.

**How it works:**  
Creates a virtual table grouping posts by type with their total engagement, selects the top performer, and returns it as readable text.

**Functions Used:** `VAR`, `TOPN`, `SUMMARIZE`, `CONCATENATEX`

**Key Techniques:**  
Unlike a simple `MAXX` which only returns a number, this measure returns the actual category name (e.g., "Video") in a stakeholder-friendly format.

**Business Value:**  
Directly answers "What type of content should we create more of?" Enables data-driven content strategy and resource allocation.



## 2. Post Type Share of Engagement

**Business Question:** What percentage of total engagement does each content format contribute?

**What it does:**  
Calculates the percentage contribution of each content type to total engagement.

**How it works:**  
First calculates total engagement across all post types (ignoring any filters), then divides the current post type's engagement by that total.

**Functions Used:** `CALCULATE`, `ALL`, `DIVIDE`

**Key Techniques:**  
Demonstrates the essential `CALCULATE` + `ALL` pattern required for percentage-of-total calculations.

**Business Value:**  
Reveals engagement concentration—for example, if videos drive 60% of engagement but only represent 20% of posts. Helps balance content strategy.



## 3. Low Positive Sentiment Engagement

**Business Question:** Does below-average positive sentiment hurt engagement performance?

**What it does:**  
Measures average engagement specifically for posts with below-average positive sentiment.

**How it works:**  
Dynamically determines the average positive sentiment score, filters the fact table to include only posts scoring at or below that threshold, then calculates average engagement.

**Functions Used:** `CALCULATE`, `FILTER`

**Key Techniques:**  
Pairs with *High Positive Sentiment Engagement* to create a true A/B test comparing performance across sentiment groups.

**Business Value:**  
Answers the critical question "Does positive content actually drive higher engagement?" Quantifies ROI of maintaining positive brand tone.