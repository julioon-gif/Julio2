# Mission Match Desk (portfolio → ACS offering & funding matcher)

Live tool (private artifact): https://claude.ai/artifact/9dzNeL5feAhYjnaDL7Fskv

The tool scores every account in the ACS Washington-area corporate book against ACS mission and
partnership offerings, then shows each company's dated funding paths. The logic follows Julio's
six-segment capital framework (Capital Function × Budget Pocket) and the Framework ↔ ACS crosswalk.

## What it does
- **Match**: for each account it shows the top ACS offerings (0–100 score with the reasons) and the
  framework's management rule for that capital function. It also shows funding paths and dates, research
  flags, your Stage 2 call and your v4 opportunities.
- **Sales motion** (per account): Discovery → Ideation → Ask → Execute → Close.
  - Discovery: questions tailored to the account's budget pockets and capital function; answers are saved.
  - Ideation: 2–3 ideas tied to those answers, seeded from the one-pager if one was shared.
  - Ask: gate checklist, then one invitation at a level that can be adjusted.
  - Execute and Close: checklists.
  The email drafter (template or Claude) matches the stage: no dollars before the Ask, and the Ask offers
  to adjust the level or timing.
- **Shared with them**: the opportunities in one-pagers already sent after discovery meetings.
- **Deadlines**: every dated item across the book (funder deadlines, your planned asks, ACS events,
  tripwires), with the option to add the weekly PNW scan prospects that aren't in the book yet.
- **Offerings**: the 39-offering catalog with sources and the best-fit accounts for each offering.
- **Add account**: new accounts are saved in the page's store and scored right away.

## How scoring works
| Signal | Points |
|---|---|
| The offering draws from one of the account's budget pockets (Grant, Commercial, Payroll, Principal, Systems, Strategic) | +30 |
| The offering suits the account's capital function | +20 |
| Shared signals (e.g. `food`, `owner`, `rural`, `benevity`, `hospitality`) | +8 each, max +24 |
| Named in your Stage 2 primary / secondary pick, or in the v4 Opportunities tab | +30 / +15 / +12 |
| Already shared in a one-pager sent to them | +20 |
| Tier 4 (pre-revenue screen) outside Research/Advocacy | −35 |
| Sunset record | −60 |
| Komen holds the breast lane (PCC) | −25 |
| Dormant account matched with an executive-network offering | −10 |

Offerings scoring below 20 are hidden.

## Files
| File | In repo? | What |
|---|---|---|
| `offerings.json` | yes | ACS offering catalog. `verify`: V = read on an ACS page/PDF, U = unverified, I = internal term from Julio's workbooks |
| `account-research.json` | yes | Public-source research per account: region, signals, dated funding paths, flags |
| `build_matcher_data.py` | yes | Merges the workbooks + these files + `../prospects.md` into `data.json` |
| `data.json` | **no** | Contains internal plans, contacts and forecasts from the workbooks; published only inside the private artifact |

## Refresh the tool (any time the Capital Map or Stage 2 sheet changes)
```
python3 build_matcher_data.py Julio_Portfolio_Capital_Framework_vN.xlsx ACS_Account_Offering_Match_StageN.xlsx -o /tmp/matcher/data.json --private /tmp/matcher/private.json
```
`private.json` (kept out of the repo) holds accounts added after discovery that are not yet in the Capital
Map (currently Bank of America and the Tulalip Tribes), the one-pagers shared with each account, and ACS
event dates. Add new one-pagers there.
Then ask Claude to republish the artifact with the new `data.json` (same URL). Notes, stages and added
accounts live in the page's store, so a republish keeps them.

## Add a dated funding item without rebuilding
Write a document to the artifact store's `funding_extra` collection, for example:
`{"accountId": "capitol-auto", "what": "...", "date": "2027-01-15", "kind": "funder|plan|acs|watch", "mark": "V|U|I", "src": "https://..."}`.
The weekly scan can do this for book accounts whose deadlines change.
