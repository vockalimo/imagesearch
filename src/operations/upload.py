import sys
import json


sys.path.append("..")
from config import DEFAULT_TABLE
from logs import LOGGER

def do_upload(table_name, img_path, model, milvus_client, mysql_cli,product_id,product_content):
    try:
        if not table_name:
            table_name = DEFAULT_TABLE
        feat = model.resnet50_extract_feat(img_path)
        ids = milvus_client.insert(table_name, [feat])
        milvus_client.create_index(table_name)
        mysql_cli.create_mysql_table(table_name)
        product_content = json.dumps(product_content)
        mysql_cli.load_data_to_mysql(table_name, [(str(ids[0]), img_path.encode(), product_id, product_content)])
        return ids[0]
    except Exception as e:
        LOGGER.error(f"Error with upload : {e}")
        sys.exit(1)
