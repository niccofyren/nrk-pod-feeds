# Open NRK Podcast Feeds

Publishes RSS feeds with the last 10 episodes of every configured podcast, without delay. For personal use.

## Feeds

**Go to [this page](https://sindrel.github.io/nrk-pod-feeds) for a list of available feeds.**

## Contribute

Feel free to open a pull request or create an issue.

## Development

<details>
  <summary>Instructions</summary>

## Getting started

### Install dependencies

`python3 -m pip install -r requirements.txt`

### Run tests

`pytest -v --disable-warnings --log-cli-level=DEBUG`

### Build or update podcast feeds

`python3 generate_feeds.py`

</details>

<details>
    <summary>Want to add a new show</summary>

## Find show ID

`https://psapi.nrk.no/radio/search/title?q=<show name or show keywords>`

## Verify show ID

`https://psapi.nrk.no/radio/catalog/podcast/<show id>`

## Create entry in `podcast.json`

```json
  {
    "id": "<show id>",
    "title": "De 10 siste fra <show name/title>",
    "season": null,
    "enabled": true
  },
```

</details>
