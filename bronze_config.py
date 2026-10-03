BASE_PATH = "dev_project/bronze"


INGESTION_CONFIG = [
    # CRM
    {
        "source": "crm",
        "path": f"{BASE_PATH}/source_system/cust_info.csv",
        "table": "crm_cust_info"
    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/source_system/prd_info.csv",
        "table": "crm_prd_info"
    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/source_system/sales_details.csv",
        "table": "crm_sales_details"
    },
    # ERP
    {
        "source": "erp",
        "path": f"{BASE_PATH}/source_system/CUST_AZ12.csv",
        "table": "erp_cust"
    },
    {
        "source": "erp",
        "path": f"{BASE_PATH}/source_system/LOC_A101.csv",
        "table": "erp_loc"
    },
    {
        "source": "erp",
        "path": f"{BASE_PATH}/source_system/PX_CAT_G1V2.csv",
        "table": "erp_px"
    },
]