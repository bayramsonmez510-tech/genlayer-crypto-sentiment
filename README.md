
# CryptoSentimentAnalyzer — GenLayer Intelligent Contract

An on-chain crypto news sentiment analyzer powered by LLM inference via the GenLayer py-genlayer SDK.

## What it does

- Accepts any crypto-related news text as input
- Uses LLM (gl.exec_prompt) to score sentiment from -1.0 (very bearish) to +1.0 (very bullish)
- Stores results on-chain with a hash key for full auditability
- Exposes read methods for individual lookups and aggregate statistics

## Why this matters

Traditional sentiment analysis runs off-chain and cannot be verified. This contract brings LLM reasoning onto the GenLayer blockchain, making every analysis transparent and tamper-proof.

## Contract Methods

- analyze_news(news_text) — write: Analyze and store sentiment
- get_sentiment(news_hash) — read: Retrieve a specific result
- get_all_sentiments() — read: List all analyses
- get_stats() — read: Aggregate score and overall market mood

## Tech Stack

- GenLayer py-genlayer SDK
- @gl.contract, @gl.public.write, @gl.public.read, gl.exec_prompt
- Tested on GenLayer Studio (Bradbury testnet)

## Author

bayram25 — GenLayer Bradbury Testnet Contributor
