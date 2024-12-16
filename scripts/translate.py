import re
from typing import List, Optional
import requests
import json,os
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
import logging
from process_changes import Bookmark,get_title_from_content,log_execution_time,BOOKMARK_COLLECTION_REPO_NAME,get_text_content,CURRENT_MONTH,slugify

TRANSLATE_TAG: str="#translate"
DATA_PATH_NAME: str="data"

@log_execution_time
def translate_text(website_url: str,task_type="翻译") -> str:
    api_key: str = os.environ['DIFY_API_TRANSLATE']
    url = 'https://api.dify.ai/v1/workflows/run'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "inputs": {
            "input_url": website_url,
            "task_type":task_type,
        },
        "response_mode": "blocking",
        "user": "github"
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    return response_data["data"]['outputs']['text']

@log_execution_time
def process_bookmark_file():
    with open(f'{BOOKMARK_COLLECTION_REPO_NAME}/README.md', 'r', encoding='utf-8') as f:
        bookmark_lines: List[str] = f.readlines()

    with open(f'{BOOKMARK_COLLECTION_REPO_NAME}/translate.json', 'r', encoding='utf-8') as f:
        translate_bookmark_dicts = json.load(f)
        translate_bookmarks = [Bookmark(**bookmark) for bookmark in translate_bookmark_dicts]

    translate_urls = set([bookmark.url for bookmark in translate_bookmarks])

    # find the first unprocessed && summary-not-present bookmark
    title: Optional[str] = None
    url: Optional[str] = None
    for line in bookmark_lines:
        match: re.Match = re.search(r'- \[(.*?)\]\((.*?)\)', line)
        if match and match.group(2) not in translate_urls:
            if TRANSLATE_TAG not in line:
                logging.debug(f"Skipping bookmark with {TRANSLATE_TAG} tag: {match.group(1)}")
                continue
            title, url = match.groups()
            break

    if title and url:
        # Create folder for month if it doesn't exist
        Path(f'{DATA_PATH_NAME}').mkdir(parents=True, exist_ok=True)

        # process the bookmark
        text_content: str = get_text_content(url)
        title_from_content: str = get_title_from_content(text_content)
        if title_from_content=="":
            title_from_content = title
        translate_text_content: str = translate_text(url)
        translate_text_content+=f"## 原文\n- [{title_from_content}]({url})"
        timestamp = int(datetime.now().timestamp())

        translate_bookmarks.append(Bookmark(
            month=CURRENT_MONTH,
            title=title,
            url=url,
            timestamp=timestamp
        ))
        with open(get_file_path(title), 'w', encoding='utf-8') as f:
            f.write(translate_text_content)
        
        # Update .json
        with open(f'{BOOKMARK_COLLECTION_REPO_NAME}/translate.json', 'w', encoding='utf-8') as f:
            json.dump([asdict(bookmark) for bookmark in translate_bookmarks], f, indent=2, ensure_ascii=False)
def get_file_path(title:str)->str:
    return f'{DATA_PATH_NAME}/{slugify(title)}.md'
    
def main():
    process_bookmark_file()

if __name__ == "__main__":
    main()