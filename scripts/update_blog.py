# scripts/update_blog.py
import re
import os
import feedparser
import calendar
from datetime import datetime, timezone, timedelta
try:
    from zoneinfo import ZoneInfo  # Python 3.9+
except Exception:
    ZoneInfo = None

from git import Repo

# Config: can be overridden by workflow env
RSS_URL = os.getenv('RSS_URL', 'https://api.velog.io/rss/@conam')
GIT_NAME = os.getenv('GIT_COMMIT_NAME', 'Nam-I')
GIT_EMAIL = os.getenv('GIT_COMMIT_EMAIL', '71905358+Nam-I@users.noreply.github.com')

REPO_PATH = '.'
POSTS_DIR = os.path.join(REPO_PATH, 'velog-posts')
os.makedirs(POSTS_DIR, exist_ok=True)

repo = Repo(REPO_PATH)
origin = repo.remotes.origin

def sanitize_filename(title: str) -> str:
    s = re.sub(r'[\\/*?:"<>|]', '-', title)
    s = s.strip()
    if len(s) > 120:
        s = s[:120].rstrip() + '...'
    return s + '.md'

def published_to_iso_with_tz(published_parsed):
    """
    Convert feedparser.struct_time (assumed UTC) to string like:
      'YYYY-MM-DDTHH:MM:SS +0900' (Asia/Seoul)
    Returns None if published_parsed is falsy.
    """
    if not published_parsed:
        return None

    epoch = calendar.timegm(published_parsed)  # interprets struct_time as UTC
    dt_utc = datetime.fromtimestamp(epoch, tz=timezone.utc)

    # Convert to Asia/Seoul (+09:00)
    if ZoneInfo is not None:
        tz = ZoneInfo("Asia/Seoul")
        dt_local = dt_utc.astimezone(tz)
    else:
        dt_local = dt_utc.astimezone(timezone(timedelta(hours=9)))

    return dt_local.strftime('%Y-%m-%dT%H:%M:%S %z')

feed = feedparser.parse(RSS_URL)
created_files = []

for entry in feed.entries:
    title = entry.get('title', 'untitled')
    file_name = sanitize_filename(title)
    file_path = os.path.join(POSTS_DIR, file_name)

    if not os.path.exists(file_path):
        # write content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(entry.get('description', ''))
        print(f'Created: {file_path}')

        # Determine published time from RSS (published_parsed or updated_parsed)
        published_parsed = entry.get('published_parsed') or entry.get('updated_parsed')
        git_date = published_to_iso_with_tz(published_parsed)

        # Stage the file
        repo.index.add([file_path])
        commit_message = f'Add post: {title}'

        # Save old env values to restore later
        old_author_date = os.environ.get('GIT_AUTHOR_DATE')
        old_committer_date = os.environ.get('GIT_COMMITTER_DATE')

        try:
            if git_date:
                os.environ['GIT_AUTHOR_DATE'] = git_date
                os.environ['GIT_COMMITTER_DATE'] = git_date
                print(f'Using commit date: {git_date}')
            else:
                print('No published date in feed; using current time for commit date.')

            # Commit with explicit author (ensures GitHub shows Nam-I <noreply email>)
            # Use repo.git.commit so GIT_*_DATE env vars are respected by Git
            repo.git.commit('--author', f'{GIT_NAME} <{GIT_EMAIL}>', '-m', commit_message)
            created_files.append(file_name)

        finally:
            # restore environment
            if old_author_date is not None:
                os.environ['GIT_AUTHOR_DATE'] = old_author_date
            else:
                os.environ.pop('GIT_AUTHOR_DATE', None)
            if old_committer_date is not None:
                os.environ['GIT_COMMITTER_DATE'] = old_committer_date
            else:
                os.environ.pop('GIT_COMMITTER_DATE', None)

if created_files:
    try:
        origin.push()
        print(f'Pushed {len(created_files)} files: {created_files}')
    except Exception as e:
        print('Push failed:', e)
        raise
else:
    print('No new posts to add.')
