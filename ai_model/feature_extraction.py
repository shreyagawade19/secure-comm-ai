import pandas as pd
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Official UNSW-NB15 column names
COLUMNS = [
    'srcip','sport','dstip','dsport','proto','state','dur','sbytes',
    'dbytes','sttl','dttl','sloss','dloss','service','sload','dload',
    'spkts','dpkts','swin','dwin','stcpb','dtcpb','smeansz','dmeansz',
    'trans_depth','res_bdy_len','sjit','djit','stime','ltime',
    'sintpkt','dintpkt','tcprtt','synack','ackdat',
    'is_sm_ips_ports','ct_state_ttl','ct_flw_http_mthd',
    'is_ftp_login','ct_ftp_cmd','ct_srv_src','ct_srv_dst',
    'ct_dst_ltm','ct_src_ltm','ct_src_dport_ltm',
    'ct_dst_sport_ltm','ct_dst_src_ltm','attack_cat','label'
]

def prepare_network_data():
    # Load CSVs with correct encoding
    df1 = pd.read_csv(
        DATA_DIR / "UNSW-NB15_1.csv",
        header=None,
        encoding="latin1",
        low_memory=False
    )

    df2 = pd.read_csv(
        DATA_DIR / "UNSW-NB15_2.csv",
        header=None,
        encoding="latin1",
        low_memory=False
    )

    # Assign column names
    df1.columns = COLUMNS
    df2.columns = COLUMNS

    # Combine
    df = pd.concat([df1, df2], ignore_index=True)

    # Select metadata-only features (SAFE for encrypted traffic)
    selected_cols = ['dur', 'sbytes', 'dbytes', 'sttl']
    features = df[selected_cols].fillna(0)

    # Normalize
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    # Save cleaned dataset
    output = DATA_DIR / "network_logs.csv"
    pd.DataFrame(scaled, columns=selected_cols).to_csv(output, index=False)

    print("✅ network_logs.csv created successfully")
    print("✅ Features used:", selected_cols)

if __name__ == "__main__":
    prepare_network_data()
