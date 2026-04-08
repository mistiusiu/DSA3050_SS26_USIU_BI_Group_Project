# Advanced Logic

To demonstrate the analytical power of DAX in a real-world business context, I’ve developed a suite of measures that transform raw social media data into actionable strategy. These calculations go beyond simple arithmetic to solve complex questions regarding content performance and audience psychology.

### Identifying the Winning Format

The first priority for any content team is knowing where to double down. My Top Post Type measure identifies the single highest-performing content format by creating a virtual table that aggregates engagement across images, videos, links, and text. By utilizing VAR, TOPN, and CONCATENATEX, the measure doesn’t just crunch numbers; it returns a human-readable result like "Video" or "Infographic." This allows stakeholders to instantly see which format is winning without digging through raw data tables.

### Measuring Impact through Contribution

Understanding raw totals is helpful, but context is better. To provide that, I built the Post Type Share of Engagement measure. This calculation uses the classic CALCULATE and ALL pattern to determine what percentage of total engagement a specific format contributes. It is a vital tool for identifying "efficiency gaps"—for instance, if video content only accounts for 10% of your posts but generates 50% of your engagement, the data is sending a clear signal to shift resource allocation.

### Quantifying the Sentiment Gap

Finally, to bridge the gap between brand tone and performance, I developed the Low Positive Sentiment Engagement measure. This is a dynamic calculation that first benchmarks the average positive sentiment across the entire dataset, then filters for posts that fall below that threshold to measure their specific engagement rate. When compared against its high-sentiment counterpart, this measure acts as a built-in A/B test, quantifying the exact ROI of maintaining a positive brand voice and proving whether "happy" content actually drives higher interaction.
