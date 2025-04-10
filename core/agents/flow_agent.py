def generate_data_flow_recommendations():
    return {
        "ingress": "Data ingestion via Kafka (daily batches)",
        "egress": "APIs + analytics layer via Snowflake or DataMart",
        "storage": "AWS S3 (Parquet) or PostgreSQL warehouse",
        "searchable": True,
        "data_governance": "Taggable, discoverable via data catalog"
    }
