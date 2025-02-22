import json
import xml.etree.ElementTree as ET

def get_last_feed(feeds_dir, podcast_id):
    try:
        path = f"{feeds_dir}/{podcast_id}.xml"
        tree = ET.parse(path)
        root = tree.getroot()
        return root
    except:
        print(f"No existing feed found for podcast {podcast_id}")
        return None

def get_podcasts_config(podcasts_cfg_file):
    with open(podcasts_cfg_file, 'r') as file:
        data = file.read()
        return json.loads(data)

def write_feeds_file(feeds_file, podcasts):
    f = open(feeds_file, "w")
    str = json.dumps(podcasts)
    f.write(f"const feeds = {str}")
    f.close()
    
    print(f"Podcasts config written to file: {feeds_file}")

def get_version():
    with open("version.txt") as file:
        return file.read()
