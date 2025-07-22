# Claude Code Best Practices - Data Pipeline Example

This is an EXAMPLE of a customized best practices document for a data pipeline project. 
It shows how the general template should be adapted for a specific project.

## 🎯 Project Overview
**Project**: Customer Analytics Pipeline  
**Description**: ETL pipeline for processing customer behavior data from multiple sources  
**Technology Stack**: Python, Apache Airflow, BigQuery, Pandas  
**Deployment Platform**: Google Cloud Platform  
**Database/Storage**: BigQuery (project: analytics-prod)  

## 📁 Project Structure (MANDATORY)
```
customer-analytics-pipeline/
├── src/                              ← Production code ONLY
│   ├── controllers/                  ← Main orchestration logic
│   │   └── customer_data_controller.py
│   ├── pipelines/                    ← Data processing pipelines
│   │   ├── extract_pipeline.py
│   │   ├── transform_pipeline.py
│   │   └── load_pipeline.py
│   ├── calculators/                  ← Business logic calculations
│   │   ├── calculate_ltv.py
│   │   └── calculate_churn_score.py
│   ├── utils/                        ← Reusable utilities
│   │   ├── bigquery_helpers.py
│   │   ├── data_validators.py
│   │   └── log_writer.py
│   └── schemas/                      ← Data schemas
│       └── customer_schema.py
├── tests/                            ← All test files
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── experiments/                      ← Research & temporary code
│   ├── sandbox/
│   └── 2025-01-15-new-metric-exploration/
├── config/                           ← Configuration files
│   ├── airflow_dags/
│   ├── settings.yaml
│   └── credentials/
├── docs/                             ← Documentation
│   ├── claude/
│   └── customer-analytics-pipeline-bestpractices.md
├── scripts/                          ← Utility scripts & runners
│   ├── run_daily_pipeline.py
│   ├── backfill_historical_data.py
│   └── verify_data_quality.py
└── data/                             ← Sample data for testing
    └── samples/
```

## 🚨 CRITICAL RULES for Claude Code

[Same as template - these don't change]

## 📝 File Naming Conventions

### Production Code (src/):
- `customer_data_controller.py` ✅
- `calculate_ltv.py` ✅
- `extract_pipeline.py` ✅

### Scripts (scripts/):
- `run_daily_pipeline.py` ✅
- `backfill_historical_data.py` ✅
- `check_pipeline_status.py` ✅

## 🔄 Workflow Guidelines

### Starting New Data Source Integration:
**USER**: "Add integration for Shopify data"  
**CLAUDE**: Creates files in experiments/2025-01-21-shopify-integration/  
           Tests connection and data structure first

### Updating Pipeline Logic:
**USER**: "Update the LTV calculation to include new factors"  
**CLAUDE**: Modifies src/calculators/calculate_ltv.py  
           Updates corresponding tests in tests/unit/

## 📦 Import Structure

```python
# Standard library imports
import json
import os
from datetime import datetime
from pathlib import Path

# Third-party imports
import pandas as pd
from google.cloud import bigquery
from apache_airflow import DAG

# Internal imports
from src.utils.bigquery_helpers import create_table, load_data
from src.calculators.calculate_ltv import calculate_customer_ltv
from src.pipelines.extract_pipeline import extract_shopify_data
```

## 🗃️ Database & Table Standards

### BigQuery Tables:
- `raw_customer_events` - Raw event data
- `processed_customer_metrics` - Calculated metrics
- `customer_ltv_scores` - LTV calculations
- `customer_segments` - Segmentation results

### Table Naming Convention:
- `raw_[source]_[entity]` for raw data
- `processed_[entity]_[metric]` for processed data
- `tmp_[purpose]_[date]` for temporary tables

### Customer ID Format:
- Always use format: `CUST-XXXXXXXX`
- Source system IDs mapped in `customer_id_mapping` table

## 🧪 Testing Guidelines

### Data Quality Tests:
```bash
# Run data quality checks
python scripts/verify_data_quality.py --date 2025-01-21

# Test pipeline components
pytest tests/unit/test_calculate_ltv.py
```

### Integration Tests:
- Test with sample data first
- Verify BigQuery permissions
- Check Airflow DAG syntax

## 🚀 Key Processes

### 1. Daily Pipeline Run:
```bash
# Run full pipeline
python scripts/run_daily_pipeline.py --date 2025-01-21
```

### 2. Historical Backfill:
```bash
# Backfill specific date range
python scripts/backfill_historical_data.py --start 2025-01-01 --end 2025-01-20
```

### 3. Data Quality Monitoring:
```bash
# Check today's data quality
python scripts/verify_data_quality.py
```

[Rest of template sections customized for data pipeline context...]

---

**Last Updated**: 2025-01-21  
**Project**: Customer Analytics Pipeline  
**Repository**: customer-analytics-pipeline  
**Maintained By**: Data Engineering Team
