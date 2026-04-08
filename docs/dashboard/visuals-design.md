

### Line Chart

A line chart is ideal for continuous time-series data because it emphasises the direction and rate of change between data points. Placing it top-left follows the natural F-pattern reading flow, ensuring it is the first visual seen and sets the context for everything else on the page.


### Pie Chart

A pie chart is appropriate here because the primary question is proportional composition rather than comparison of magnitudes. With only five post types, the slices remain readable. Placing it at the top-centre draws the eye naturally after scanning the trend, prompting the reader to ask which post type is responsible for that trend.


### Bar Chart

A vertical bar chart is the clearest way to compare a single numeric measure across discrete categories. Placing it immediately next to the pie chart creates a deliberate tension: Photo has the most volume and sentiment, but Text has the highest average engagement per post — this prompts deeper analysis and is made obvious by the two visuals sharing the same row.


### Key Influencers


The Key Influencers visual performs automated statistical analysis without requiring custom DAX. It surfaces non-obvious relationships that would be hidden in standard charts. Placed bottom-left, it rewards users who scroll down with actionable insight, and pairs logically with the slicer panel beside it for deeper exploration.

### Horizontal Bar Chart

A horizontal bar chart was chosen over vertical because the category labels (Information, Interaction) are longer text strings that render more clearly on the horizontal axis. Centralising this visual with its slicers makes it the interactive hub of the dashboard — all filters radiate outward to the other visuals, giving users control over the entire analytical view from one location.

### Grouped Bar Chart

A grouped bar chart is used when comparing one measure across two categorical dimensions simultaneously. It avoids the need for a matrix table while keeping values visually scannable. Placing it bottom-right positions the most complex visual as the final analytical destination, where users arrive after understanding context from the simpler top-row visuals. 

### Radar Chart

A radar chart was chosen because it allows simultaneous comparison of multiple categories (COVID phases) across multiple groups (influencer tiers) in a single view. The concentric shape makes it immediately obvious which influencer tier covers the most "area" — visually communicating dominance without needing to read every number. A bar chart would have required multiple panels to achieve the same comparison.

### Clustered Bar Chart

A clustered bar chart was chosen because it allows direct side-by-side comparison of engagement levels across verbosity categories for each influencer tier. Grouping bars by verbosity level makes the trend within each tier immediately readable. A line chart could have worked but would imply continuity between verbosity levels which are categorical, not continuous.

### Stacked Bar Chart 

A diverging stacked bar chart was chosen because sentiment data is inherently bipolar — positive on one side, negative on the other. Anchoring both bars at zero makes it visually intuitive to compare the magnitude of positive versus negative sentiment simultaneously. Splitting into two charts (Information vs Interaction) was necessary to avoid conflating what influencers express with what audiences direct back at them, addressing the core analytical distinction your group member flagged.

### Clustered Bar Chart 

A clustered bar chart was chosen because it allows comparison of follower counts across multiple states while simultaneously showing the breakdown by influencer tier within each state. This makes it immediately visible that high follower counts in certain states are driven exclusively by Celebrity influencers rather than a broad mix of tiers.

### Stacked Bar Chart 

A stacked bar chart was chosen because it shows both the total posting volume per influencer tier and the composition of post types within that total simultaneously. This dual function — volume and proportion in one view — makes it the most efficient chart for this business question. The corrected version uses count of posts rather than count of post types, ensuring the segments reflect actual posting behaviour and volume differences.

### Stacked Column Chart 

A stacked column chart was chosen to show how total engagement is distributed across post types for each influencer tier. The vertical orientation naturally suits comparison of engagement magnitude, with taller bars immediately signalling higher performing tiers. Splitting by content type (Interaction vs Information) within each stack adds a second dimension without requiring a separate chart.

### Clustered Column Chart 

A clustered column chart was chosen over a stacked version because the goal here is to compare Interaction and Information content directly at each verbosity level, not to show their combined total. Side-by-side columns make the crossover points — where one content type overtakes the other — clearly visible at a glance.

### Scatter Plot 

A scatter plot was chosen because it is the only chart type that can reveal correlation between two continuous variables — word count and engagement — across thousands of individual posts simultaneously. Each dot represents one post, allowing patterns, clusters, and outliers to emerge naturally. Trend lines per influencer tier were added to surface directional relationships that would be invisible in an aggregated bar chart.

### Map Visual 

A map visual was chosen because the business question is inherently geographic — asking which states perform highest. Plotting on an actual map allows spatial patterns and regional clusters to emerge in a way that a bar chart ranked by state name never could. It also makes the report more accessible to stakeholders who think in terms of geography rather than data tables.

### Box Plot 

A box plot was chosen because the business question is about distribution and variability, not just averages. Showing the median, interquartile range, and whiskers for each COVID phase reveals how consistently or inconsistently posts performed within each phase — something a simple bar chart of averages would completely obscure. The V-curve pattern of engagement volatility only becomes visible when the full distribution is shown.

### Heatmap Matrix 

A heatmap was chosen because it needs to display three dimensions simultaneously — day, time period, and COVID phase — in a compact, readable format. Colour intensity as the encoding mechanism allows the eye to immediately identify hotspots and cold zones without reading individual numbers. No other single chart type could display this three-way combination as clearly.

### Line Chart 

A line chart was chosen because time-series data is continuous and directional — connecting data points with lines communicates the flow and trajectory of engagement over time naturally. Multiple lines per influencer tier allow trend comparison across the full timeline. A bar chart would fragment the time dimension and make long-term trends harder to follow visually.


