# Mission Match Desk (portfolio → ACS offering & funding matcher)

Live tool (private artifact): https://claude.ai/artifact/9dzNeL5feAhYjnaDL7Fskv

The tool scores every account in the ACS Washington-area corporate book against ACS mission and
partnership offerings, then shows each company's dated funding paths. The logic follows Julio's
six-segment capital framework (Capital Function × Budget Pocket) and the Framework ↔ ACS crosswalk.

## What it does
- **Match**: for each account it shows the top ACS offerings (0–100 score with the reasons) and the
  framework's management rule for that capital function. It also shows funding paths and dates, research
  flags, your Stage 2 call, your v4 opportunities, and a pitch builder that turns an ask into rides and
  Hope Lodge nights. You can ask Claude to draft an opener, and save working notes (stage, next touch).
- **Deadlines**: every dated item across the book (funder deadlines, your planned asks, ACS events,
  tripwires), with the option to add the weekly PNW scan prospects that aren't in the book yet.
- **Offerings**: the 32-offering catalog with sources and the best-fit accounts for each offering.
- **Add account**: new accounts are saved in the page's store and scored right away.

## How scoring works
| Signal | Points |
|---|---|
| The offering draws from one of the account's budget pockets (Grant, Commercial, Payroll, Principal, Systems, Strategic) | +30 |
| The offering suits the account's capital function | +20 |
| Shared signals (e.g. `food`, `owner`, `rural`, `benevity`, `hospitality`) | +8 each, max +24 |
| Named in your Stage 2 primary / secondary pick, or in the v4 Opportunities tab | +30 / +15 / +12 |
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
python3 build_matcher_data.py Julio_Portfolio_Capital_Framework_vN.xlsx ACS_Account_Offering_Match_StageN.xlsx -o /tmp/matcher/data.json
```
Then ask Claude to republish the artifact with the new `data.json` (same URL). Notes, stages and added
accounts live in the page's store, so a republish keeps them.

## Add a dated funding item without rebuilding
Write a document to the artifact store's `funding_extra` collection, for example:
`{"accountId": "capitol-auto", "what": "...", "date": "2027-01-15", "kind": "funder|plan|acs|watch", "mark": "V|U|I", "src": "https://..."}`.
The weekly scan can do this for book accounts whose deadlines change.
