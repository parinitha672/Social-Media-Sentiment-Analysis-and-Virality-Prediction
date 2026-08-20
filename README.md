# Social-Media-Sentiment-Analysis-and-Virality-Prediction

## Project Overview

**Social Media Sentiment Analysis and Virality Prediction** is a Data Science project developed to analyse social-media performance, understand audience sentiment and identify factors that influence content engagement and virality.

The project combines **Data Analysis, A/B Testing, Natural Language Processing, Machine Learning, Forecasting and Streamlit Dashboard Development** to convert raw social-media data into meaningful insights and recommendations.

## Objectives

* Analyse Instagram post-performance and engagement.
* Identify factors affecting engagement and reach.
* Analyse viral performance using the viral coefficient.
* Compare CTA and non-CTA posts using A/B testing.
* Perform sentiment analysis on YouTube comments.
* Develop a Machine Learning model for sentiment classification.
* Forecast future engagement rates.
* Identify effective posting hours, media types, content categories and traffic sources.
* Generate engagement optimization recommendations.
* Develop an interactive Streamlit dashboard.

## Datasets

### Instagram Dataset

The Instagram dataset contains **29,999 posts and 24 attributes** related to social-media performance.

Important attributes include:

* Post ID
* Account type
* Follower count
* Media type
* Content category
* Traffic source
* Post date and time
* Likes
* Comments
* Shares
* Saves
* Reach
* Impressions
* Engagement rate
* Followers gained
* Hashtags count
* Viral coefficient

### YouTube Comments Dataset

The YouTube comments dataset contains approximately **45,000 comments** with sentiment, toxicity and spam labels.

The sentiment classes used in the project are:

* Positive
* Neutral
* Negative

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Natural Language Processing
* TF-IDF
* Logistic Regression
* Linear Regression
* Streamlit
* Google Colab
* GitHub

## Project Workflow

```text
Data Collection
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Engagement Analysis
      ↓
A/B Testing
      ↓
NLP Sentiment Analysis
      ↓
Machine Learning Model
      ↓
Model Evaluation
      ↓
Trend Analysis
      ↓
Engagement Forecasting
      ↓
Optimization Recommendations
      ↓
Streamlit Dashboard
```

## Key Analysis

### Engagement Analysis

Instagram posts were analysed using engagement rate, reach, likes, comments, shares, saves and followers gained.

The analysis was performed across:

* Media types
* Content categories
* Posting hours
* Traffic sources

### A/B Testing

Posts were divided into two groups:

* **Group A:** No CTA
* **Group B:** CTA

The groups were compared using multiple engagement metrics to understand the effect of Call-to-Action elements.

### Sentiment Analysis

The YouTube comments were divided into training and testing datasets.

* Training samples: **36,000**
* Testing samples: **9,000**
* TF-IDF vocabulary: **10,000 features**

TF-IDF was used for text feature extraction and Logistic Regression was used for sentiment classification.

### Model Performance

The NLP sentiment model achieved:

**Accuracy: 69.88%**

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

The trained model and TF-IDF vectorizer were saved as `.pkl` files.

## Forecasting

Historical monthly engagement data was used to forecast future engagement rates.

Example forecast results:

| Month         | Forecast Engagement Rate |
| ------------- | -----------------------: |
| December 2025 |                 0.042067 |
| January 2026  |                 0.042064 |
| February 2026 |                 0.042062 |

## Final Optimization Recommendations

| Factor           | Recommended Choice |
| ---------------- | ------------------ |
| Media Type       | Reel               |
| Content Category | Music              |
| Posting Hour     | 3:00               |
| Traffic Source   | Profile            |

These recommendations were generated from the observed engagement performance in the dataset.

## Dashboard

An interactive **Streamlit dashboard** was developed to present:

* Instagram analytics
* Engagement metrics
* Sentiment analysis
* A/B testing results
* Monthly trends
* Engagement forecasts
* Optimization recommendations

## Project Files

```text
Social-Media-Sentiment-Analysis/
│
├── app_final.py
├── Instagram_Analytics.csv
├── YouTube Comments Dataset with Sentiment Toxicity and Spam Labels (45K Rows).csv
├── instagram_dashboard_dataset.csv
├── growth_summary.csv
├── virality_summary.csv
├── sentiment_summary.csv
├── ab_testing_results.csv
├── ab_testing_comparison.csv
├── monthly_trend_analysis.csv
├── engagement_forecast.csv
├── engagement_optimization_recommendations.csv
├── instagram_nlp_sentiment_model.pkl
├── instagram_nlp_tfidf_vectorizer.pkl
└── project_notebook.ipynb
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd Social-Media-Sentiment-Analysis
```

### 3. Install required libraries

```bash
pip install pandas numpy scikit-learn streamlit joblib
```

### 4. Run the Streamlit dashboard

```bash
streamlit run app_final.py
```

The dashboard will open in the browser.

## Results

The project successfully:

* Analysed **29,999 Instagram posts**.
* Analysed approximately **45,000 YouTube comments**.
* Performed CTA-based A/B testing.
* Developed an NLP sentiment classification model.
* Achieved **69.88% sentiment classification accuracy**.
* Performed monthly trend analysis.
* Forecast future engagement rates.
* Identified high-performing content factors.
* Generated optimization recommendations.
* Developed and tested an interactive Streamlit dashboard.

## Future Scope

The project can be further improved by:

* Using real-time social-media data.
* Increasing the size and diversity of the training dataset.
* Using advanced NLP and Deep Learning models.
* Improving negative sentiment classification.
* Adding real-time dashboard updates.
* Implementing advanced virality prediction models.
* Adding audience segmentation.
* Providing automated content recommendations.

## Conclusion

The project demonstrates how Data Science and Machine Learning can be applied to social-media data to understand engagement, audience sentiment and content performance. The combination of analytics, NLP, forecasting and optimization provides a practical approach for making data-driven social-media decisions.

## Author

**Parinitha R**

Data Science Internship Project
Rivoquix Learning Private Limited

## License

This project is developed for educational and internship purposes.
