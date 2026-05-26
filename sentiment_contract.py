from genlayer import *


@gl.contract
class CryptoSentimentAnalyzer:

    sentiments: dict
    total_analyzed: int

    def init(self):
        self.sentiments = {}
        self.total_analyzed = 0

    @gl.public.write
    def analyze_news(self, news_text: str) -> None:
        result = gl.exec_prompt(
            f"""You are a crypto market sentiment analyst.
Analyze the following news text and respond with ONLY a JSON object:
{{
  "score": <float between -1.0 and 1.0>,
  "label": "<very_bearish, bearish, neutral, bullish, or very_bullish>",
  "reasoning": "<one sentence>"
}}
News text: "{news_text}"
Respond with ONLY the JSON object."""
        )
        import json
        import hashlib
        data = json.loads(result)
        news_hash = hashlib.sha256(news_text.encode()).hexdigest()[:16]
        self.sentiments[news_hash] = {
            "score": float(data["score"]),
            "label": data["label"],
            "reasoning": data["reasoning"],
            "news_preview": news_text[:100],
        }
        self.total_analyzed += 1

    @gl.public.read
    def get_sentiment(self, news_hash: str) -> dict:
        if news_hash not in self.sentiments:
            return {"error": "Not found"}
        return self.sentiments[news_hash]

    @gl.public.read
    def get_all_sentiments(self) -> dict:
        return self.sentiments

    @gl.public.read
    def get_stats(self) -> dict:
        if self.total_analyzed == 0:
            return {"total_analyzed": 0, "average_score": 0, "overall_sentiment": "neutral"}
        scores = [v["score"] for v in self.sentiments.values()]
        avg = sum(scores) / len(scores)
        if avg >= 0.5:
            overall = "very_bullish"
        elif avg >= 0.1:
            overall = "bullish"
        elif avg <= -0.5:
            overall = "very_bearish"
        elif avg <= -0.1:
            overall = "bearish"
        else:
            overall = "neutral"
        return {"total_analyzed": self.total_analyzed, "average_score": round(avg, 4), "overall_sentiment": overall}
