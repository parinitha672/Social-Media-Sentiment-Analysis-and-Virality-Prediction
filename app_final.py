import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Instagram Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)
dashboard_data = pd.read_csv("instagram_dashboard_dataset.csv")
growth_summary = pd.read_csv("growth_summary.csv")
virality_summary = pd.read_csv("virality_summary.csv")
sentiment_summary = pd.read_csv("sentiment_summary.csv")
st.title("📊 Instagram Analytics Dashboard")
st.caption("Data-driven analysis of Instagram content performance, growth and audience sentiment")
st.sidebar.header("Dashboard Filters")
media_options = ["All"] + sorted(
    dashboard_data["media_type"].dropna().unique().tolist()
)
category_options = ["All"] + sorted(
    dashboard_data["content_category"].dropna().unique().tolist()
)
selected_media = st.sidebar.selectbox(
    "Media Type",
    media_options
)
selected_category = st.sidebar.selectbox(
    "Content Category",
    category_options
)
filtered_data = dashboard_data.copy()
if selected_media != "All":
    filtered_data = filtered_data[
        filtered_data["media_type"] == selected_media
    ]
if selected_category != "All":
    filtered_data = filtered_data[
        filtered_data["content_category"] == selected_category
    ]
total_posts = len(filtered_data)
total_reach = filtered_data["reach"].sum()
total_likes = filtered_data["likes"].sum()
avg_engagement = filtered_data["engagement_rate"].mean()
total_shares = filtered_data["shares"].sum()
total_saves = filtered_data["saves"].sum()
total_followers = filtered_data["followers_gained"].sum()
st.subheader("📌 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Posts", f"{total_posts:,}")
col2.metric("Total Reach", f"{total_reach:,}")
col3.metric("Total Likes", f"{total_likes:,}")
col4.metric("Avg Engagement Rate", f"{avg_engagement:.2%}")
col5, col6, col7 = st.columns(3)
col5.metric("Total Shares", f"{total_shares:,}")
col6.metric("Total Saves", f"{total_saves:,}")
col7.metric("Followers Gained", f"{total_followers:,}")
st.divider()
st.subheader("📈 Monthly Growth Analysis")
growth_display = growth_summary.copy()
st.line_chart(
    growth_display.set_index("post_datetime")[
        ["followers_gained", "total_reach"]
    ]
)
st.dataframe(
    growth_summary,
    use_container_width=True,
    hide_index=True
)
st.subheader("🔥 Content Virality Analysis")
virality_display = virality_summary.copy()
st.bar_chart(
    virality_display.set_index("content_category")[
        ["avg_viral_coefficient"]
    ]
)
st.dataframe(
    virality_summary,
    use_container_width=True,
    hide_index=True
)
st.subheader("💬 Audience Sentiment")
sentiment_chart = sentiment_summary.set_index(
    "label_sentiment"
)[["comment_count"]]
st.bar_chart(sentiment_chart)
st.dataframe(
    sentiment_summary,
    use_container_width=True,
    hide_index=True
)
st.subheader("🎬 Content Performance by Media Type")
media_analysis = filtered_data.groupby(
    "media_type"
).agg(
    posts=("post_id", "count"),
    avg_engagement_rate=("engagement_rate", "mean"),
    avg_likes=("likes", "mean"),
    avg_comments=("comments", "mean"),
    avg_shares=("shares", "mean"),
    avg_saves=("saves", "mean"),
    avg_followers_gained=("followers_gained", "mean")
).reset_index()
st.dataframe(
    media_analysis,
    use_container_width=True,
    hide_index=True
)
st.subheader("💡 Data-Driven Recommendations")
best_media = (
    media_analysis.sort_values(
        "avg_engagement_rate",
        ascending=False
    )
    .iloc[0]["media_type"]
)
best_category = (
    virality_summary.sort_values(
        "avg_viral_coefficient",
        ascending=False
    )
    .iloc[0]["content_category"]
)
best_growth_month = (
    growth_summary.sort_values(
        "followers_gained",
        ascending=False
    )
    .iloc[0]["post_datetime"]
)
rec1, rec2, rec3 = st.columns(3)
with rec1:
    st.info(
        f"🎬 **Best Media Type**\n\n"
        f"{best_media} currently has the highest average "
        f"engagement rate in the selected data."
    )
with rec2:
    st.success(
        f"🔥 **Top Viral Category**\n\n"
        f"{best_category} has the highest average "
        f"viral coefficient."
    )
with rec3:
    st.warning(
        f"📈 **Strongest Growth Month**\n\n"
        f"{best_growth_month} recorded the highest "
        f"followers gained."
    )
st.divider()
st.caption(
    "Instagram Analytics Dashboard | Data Science Major Project"
)
