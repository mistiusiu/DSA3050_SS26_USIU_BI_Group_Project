
#  Line Chart
## Business Question – How has engagement grown over time by year and month?
- This line chart tracks the Engagement Growth Trend across 2020–2022. It plots the period-over-period change rate, revealing where growth accelerated or declined.
![alt text](image.png)
 
### Findings:

– 2020 Volatility: The chart shows extreme swings early in 2020, with growth spiking sharply positive before dropping to its most negative point (approximately –4), consistent with the disruption of COVID lockdowns creating an initial content surge followed by audience fatigue.

–	2021 Stabilisation: Growth rates moderate significantly through 2021, oscillating in a tighter band around zero. This reflects audiences re-establishing regular consumption patterns as restrictions eased.

–	2022 Plateau: By 2022, the growth trend flattens and hugs the zero line, indicating that engagement levels have stabilised rather than growing. The market appears to have reached a post-pandemic equilibrium.

–	Negative Dip (Mid-2020): The most dramatic negative trough — around –4 — aligns with peak lockdown fatigue. Even as audiences were home and online, overall engagement growth collapsed, mirroring findings from the box plot analysis of COVID phases.


---
---

#  Pie Chart
## Business Question – How is positive sentiment distributed across post types?
- This pie chart breaks down the total sum of Positive Sentiment by Post Type, showing which content formats collectively generate the most positive audience response.

 ![alt text](image-1.png)

### Findings:
– Photo dominates overwhelmingly: With 78.45% (23K) of all positive sentiment, Photo posts are by far the most positively received content format. This aligns with the finding that photo is also the most frequently posted type across all influencer tiers.

–	Video holds a meaningful share: Video accounts for a notable secondary slice, confirming its elevated engagement performance observed in the stacked column chart analysis. Audiences respond positively even though video is rarely used.

–	Text posts contribute modestly: Text represents 15.02% (4K) of positive sentiment, respectable given it is the second most commonly used post format, though far behind photo.

–	Link and Poll are negligible: Together, Link (4.62%, 1K) and Poll account for a very small fraction of positive sentiment, confirming that these formats rarely resonate with audiences across the dataset.

---
---


#  Bar Chart
## Business Question – Which post type generates the highest average engagement?
- This bar chart compares the Average of Engagement across five post types — Text, Video, Photo, Link, and Poll — giving a fair, volume-neutral comparison of which format resonates most per post.

 ![alt text](image-2.png)

### Findings:
–	Text leads on average: Counterintuitively, Text posts register the highest average engagement (approximately 285), edging out Video in this view. This may be driven by a small number of high-performing text posts inflating the average, or by the fact that text posts from high-tier influencers skew the mean.

–	Video is a close second: Video averages approximately 265 engagements, confirming its strong performance. Combined with the stacked column findings (where Video has the highest engagement per tier), Video remains a premium-performing format.

–	Photo performs well in volume but modestly in average: Despite dominating total sentiment and posting volume, Photo's average engagement (~190) sits below both Text and Video, suggesting diminishing returns as photo volume increases.

–	Link performs below expectations: With an average around 65, Link posts generate relatively low engagement, suggesting audiences on this platform are reluctant to leave for external content.

–	Poll barely registers: Poll has the lowest average engagement of all post types, confirming it as the least effective format in this dataset.
 

---
---

#  Key Influencers Visual
## Business Question – What factors most influence the likelihood of a post being classified as a Photo post?
This Power BI Key Influencers visual identifies the conditions under which a post is most likely to be a Photo post, quantifying each factor's multiplicative impact on that likelihood.

![alt text](image-3.png)

 
### Findings:
–	Word Count (7.91×): When the Average Word Count goes up by 8.84 words, the likelihood of the post being a Photo increases by 7.91 times. This is the single strongest driver. It may initially seem counterintuitive — one might expect photos to accompany short captions — but it suggests that photo posts in this dataset tend to carry longer descriptive captions or hashtag-heavy text.

–	Negative Sentiment (2.18×): When Average Negative Sentiment decreases by 0.02, the likelihood of a Photo post increases by 2.18 times. Lower negativity is associated with photo content, reinforcing the idea that photo posts tend to be more positive and polished in tone.

–	Engagement (1.01×): When Average Engagement decreases by 103.38, the likelihood of a Photo post increases marginally (1.01×). This is a near-neutral effect — engagement alone is not a meaningful predictor of photo format selection.

---
---

#  Clustered Horizontal Bar Chart
## Business Question – How does total engagement compare across content types for different influencer tiers?
- This chart compares Total Engagement for Information and Interaction content types across different influencer groups.

 ![alt text](image-4.png)

### Findings:
–	Interaction content leads for both groups: Both Celebrity and Macro Influencer bars are longer for Interaction content than for Information content. This universally confirms that audience engagement is higher when content is interactive rather than purely informational — consistent with the verbosity and stacked column analyses.

–	Celebrities generate more total engagement in Interaction: Celebrity Interaction bars extend noticeably further (approaching ~2M total engagements) compared to Macro Influencer Interaction, reinforcing the tier-based engagement hierarchy.

–	Information content is more evenly matched: The gap between Celebrities and Macro Influencers narrows for Information content, suggesting that the celebrity advantage is more pronounced for interactive posts.

–	Celebrity advantage is format-dependent: Celebrities do not simply outperform across the board — their lead is most pronounced in Interaction content, suggesting their audiences engage most when the content invites a response rather than delivers information.

---
---

 
#  Grouped Bar Chart
## Business Question – How does verbosity interact with post type to affect average engagement?
- This grouped bar chart cross-analyses Average Engagement by both Post Type and Verbosity level (Extreme, High, Low, Medium), revealing whether the optimal word count varies by the type of post being created.

 ![alt text](image-5.png)

### Findings:
–	Text at Extreme verbosity peaks dramatically: The most striking finding is that Text posts at Extreme verbosity (purple bar) reach nearly 1,000 average engagement — far above any other combination in the chart. This is an outlier result suggesting that long-form text content, when it does break through, generates outsized engagement.

–	Video performs consistently across verbosity levels: Video posts maintain strong average engagement across all verbosity levels, with the Medium and Low categories performing particularly well (~300–500). This reinforces video's position as the most reliable high-performing post format.

–	Photo shows moderate, stable performance: Photo posts deliver consistent but moderate engagement across all verbosity levels, with no single verbosity category dramatically outperforming others. Photo remains a volume format rather than an engagement spike driver.

–	Link and Poll remain low across all verbosity levels: Regardless of how much text accompanies them, Link and Poll posts generate very low engagement. Verbosity cannot rescue underperforming formats.

–	Extreme verbosity is high-risk, high-reward: The extreme verbosity category shows the widest spread of results — from very high (Text) to very low (Link/Poll). Short to medium captions appear safer for most formats.


