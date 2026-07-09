#!/usr/bin/env python3
"""
Direct Perplexity Search API client for the BiH Daily Topic Monitor.

Reads the API key from:
    PERPLEXITY_API_KEY

Examples:
    python perplexity_search.py \
        --query "BiH sigurnosni incident danas" \
        --recency day

    python perplexity_search.py \
        --query "paravojne grupe Bosna i Hercegovina" \
        --query "radikalne organizacije BiH obuka" \
        --language bs \
        --language sr \
        --language hr \
        --max-results 8

    python perplexity_search.py \
        --query "Kosovo Republika Srpska mobilizacija" \
        --language sr \
        --language en \
        --domain n1info.ba \
        --domain klix.ba \
        --recency day
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime
from typing import Any

API_URL = "https://api.perplexity.ai/search"


def bounded_int(min_value: int, max_value: int):
    """Return an argparse type validator for bounded integers."""

    def validator(value: str) -> int:
        try:
            number = int(value)
        except ValueError as exc:
            raise argparse.ArgumentTypeError(
                f"Expected integer, received: {value}"
            ) from exc

        if not min_value <= number <= max_value:
            raise argparse.ArgumentTypeError(
                f"Value must be between {min_value} and {max_value}"
            )

        return number

    return validator


def valid_date(value: str) -> str:
    """Validate Perplexity date-filter format MM/DD/YYYY."""
    try:
        datetime.strptime(value, "%m/%d/%Y")
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "Date must use MM/DD/YYYY format"
        ) from exc

    return value


def valid_country(value: str) -> str:
    """Validate a two-letter country code."""
    normalized = value.strip().upper()

    if len(normalized) != 2 or not normalized.isalpha():
        raise argparse.ArgumentTypeError(
            "Country must be a two-letter code, for example BA or RS"
        )

    return normalized


def valid_language(value: str) -> str:
    """Validate a two-letter ISO-style language code."""
    normalized = value.strip().lower()

    if len(normalized) != 2 or not normalized.isalpha():
        raise argparse.ArgumentTypeError(
            "Language must be a two-letter code, for example bs, sr, hr, en or sq"
        )

    return normalized


def normalize_domain(value: str) -> str:
    """Normalize domain filters by removing protocol and trailing slash."""
    domain = value.strip()

    for prefix in ("https://", "http://"):
        if domain.startswith(prefix):
            domain = domain[len(prefix):]

    domain = domain.rstrip("/")

    if not domain:
        raise argparse.ArgumentTypeError("Domain cannot be empty")

    return domain


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Search the web through the Perplexity Search API "
            "and print structured JSON results."
        )
    )

    parser.add_argument(
        "--query",
        action="append",
        required=True,
        help=(
            "Search query. Repeat --query to send multiple related queries "
            "in one API request."
        ),
    )

    parser.add_argument(
        "--max-results",
        type=bounded_int(1, 20),
        default=8,
        help="Maximum number of ranked results to return. Default: 8.",
    )

    parser.add_argument(
        "--context-size",
        choices=("low", "medium", "high"),
        default="low",
        help="Amount of extracted page context. Default: low.",
    )

    parser.add_argument(
        "--recency",
        choices=("hour", "day", "week", "month", "year"),
        help="Relative publication-recency filter.",
    )

    parser.add_argument(
        "--after-date",
        type=valid_date,
        help="Only results published after this date: MM/DD/YYYY.",
    )

    parser.add_argument(
        "--before-date",
        type=valid_date,
        help="Only results published before this date: MM/DD/YYYY.",
    )

    parser.add_argument(
        "--country",
        type=valid_country,
        help="Two-letter country code, for example BA.",
    )

    parser.add_argument(
        "--language",
        action="append",
        type=valid_language,
        help=(
            "Two-letter language code. Repeat for multiple languages, "
            "for example --language bs --language sr --language hr."
        ),
    )

    parser.add_argument(
        "--domain",
        action="append",
        type=normalize_domain,
        help=(
            "Limit results to a domain. Repeat for multiple domains, "
            "for example --domain klix.ba --domain n1info.ba."
        ),
    )

    parser.add_argument(
        "--timeout",
        type=bounded_int(5, 180),
        default=60,
        help="HTTP timeout in seconds. Default: 60.",
    )

    return parser


def build_payload(args: argparse.Namespace) -> dict[str, Any]:
    if args.recency and (args.after_date or args.before_date):
        raise ValueError(
            "Use either --recency or exact date filters, not both."
        )

    query_value: str | list[str]

    if len(args.query) == 1:
        query_value = args.query[0]
    else:
        query_value = args.query

    payload: dict[str, Any] = {
        "query": query_value,
        "max_results": args.max_results,
        "search_context_size": args.context_size,
    }

    if args.recency:
        payload["search_recency_filter"] = args.recency

    if args.after_date:
        payload["search_after_date_filter"] = args.after_date

    if args.before_date:
        payload["search_before_date_filter"] = args.before_date

    if args.country:
        payload["country"] = args.country

    if args.language:
        payload["search_language_filter"] = list(dict.fromkeys(args.language))

    if args.domain:
        payload["search_domain_filter"] = list(dict.fromkeys(args.domain))

    return payload


def perform_search(
    payload: dict[str, Any],
    api_key: str,
    timeout: int,
) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        API_URL,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "BiH-Daily-Topic-Monitor/1.0",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw_body = response.read().decode("utf-8")

    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")

        raise RuntimeError(
            f"Perplexity API returned HTTP {exc.code}: {error_body}"
        ) from exc

    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"Network error while contacting Perplexity API: {exc.reason}"
        ) from exc

    try:
        parsed = json.loads(raw_body)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Perplexity API returned invalid JSON."
        ) from exc

    if not isinstance(parsed, dict):
        raise RuntimeError(
            "Unexpected Perplexity API response structure."
        )

    return parsed


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    api_key = os.environ.get("PERPLEXITY_API_KEY", "").strip()

    if not api_key:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": (
                        "PERPLEXITY_API_KEY environment variable "
                        "is missing or empty."
                    ),
                },
                ensure_ascii=False,
                indent=2,
            ),
            file=sys.stderr,
        )
        return 2

    try:
        payload = build_payload(args)

        response = perform_search(
            payload=payload,
            api_key=api_key,
            timeout=args.timeout,
        )

    except (ValueError, RuntimeError) as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": str(exc),
                },
                ensure_ascii=False,
                indent=2,
            ),
            file=sys.stderr,
        )
        return 1

    output = {
        "ok": True,
        "request": {
            "query": payload.get("query"),
            "max_results": payload.get("max_results"),
            "search_recency_filter": payload.get("search_recency_filter"),
            "search_after_date_filter": payload.get(
                "search_after_date_filter"
            ),
            "search_before_date_filter": payload.get(
                "search_before_date_filter"
            ),
            "country": payload.get("country"),
            "search_language_filter": payload.get(
                "search_language_filter"
            ),
            "search_domain_filter": payload.get(
                "search_domain_filter"
            ),
        },
        "response_id": response.get("id"),
        "server_time": response.get("server_time"),
        "result_count": len(response.get("results", [])),
        "results": response.get("results", []),
    }

    print(
        json.dumps(
            output,
            ensure_ascii=False,
            indent=2,
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
