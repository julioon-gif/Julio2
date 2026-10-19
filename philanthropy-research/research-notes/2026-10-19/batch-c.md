# Batch C: re-verification of 4 tracked prospects + 4 new PNW prospects (research date 2026-10-19)

Companies: Part 1 (re-verify) Bank of America, Wells Fargo, Boeing, Avista. Part 2 (new) Lamb Weston, Banner Bank, Washington Trust Bank, Philips (Bothell).

**Labels used below.**
- **VERIFIED** means read today on the company's or foundation's own page or official PDF, in an SEC filing (EDGAR submissions API), or in the foundation's own IRS 990-PF (self-hosted PDF or ProPublica full-text rendering).
- **UNVERIFIED** means it came from a search snippet, a third-party directory, news, or a page that no longer exists.
- 990-PF figures are what the foundation reported paying in that tax year. They are not a promise of future giving.

**Method notes.**
- Pages were read with `tools/readpage.py`. `pdftotext` is not installed on this machine, so PDFs were extracted with `pypdf`. ProPublica 990-PF text was read from `projects.propublica.org/nonprofits/full_text/<object_id>/IRS990PF` (the XML download returns a "Security Check" page).
- HQ cities were checked against SEC EDGAR business addresses (data.sec.gov submissions API) where the company is SEC-registered.
- **ACS partner pages are gone.** `cancer.org/about-us/our-partners/wells-fargo.html` (302) and `.../bank-of-america.html` (301) now redirect to the generic `our-partners.html`, which does not mention either company. Every fact previously sourced from those pages is now **UNVERIFIED**. The Wayback Machine was unreachable from here.
- **Name trap:** `washtrust.com` belongs to The Washington Trust Company (Rhode Island). Its "90 days prior" sponsorship rule does **not** apply to Washington Trust Bank (Spokane), whose site is `watrust.com`. Search engines and grant aggregators mix the two up.
- About 21 of the ~55 WebSearch calls were used.

## Verified deadlines in next 90 days (2026-10-19 to 2027-01-17)

- **Avista Foundation, Health and Human Service proposals: window opens January 1 and closes February 1.** VERIFIED on Avista's application page (CyberGrants, linked from avistafoundation.com). The table gives month/day only, with no year. It is a standing annual schedule, so the next window should be **Jan 1 – Feb 1, 2027**, but the year is an inference. The opening falls inside this 90-day window; the **Feb 1 close is just outside it**. Awards are announced April 1. https://www.cybergrants.com/pls/cybergrants/quiz.display_question?x_gm_id=5440&x_quiz_id=7208&x_order_by=1
  - Also open now: Avista Environmental and Arts & Culture proposals (Oct 1 – Nov 1, VERIFIED). These are not ACS fits; listed only so the calendar is complete.
- **No other verified, dated ACS-relevant deadline falls in this window.**
  - Boeing ECF Puget Sound: both 2026 cycles are closed (the second closed 8/30/2026; awards are announced 12/1/2026). The 2027 timeline is not posted. In the 2026 cycle the first window opened 12/1/2025, so a ~Dec 1, 2026 opening is plausible but **UNVERIFIED (inference only)**. VERIFIED (2026 PDF).
  - Boeing ECF Portland: "Not accepting grant applications at this time"; dates "To be determined". VERIFIED (2026 PDF).
  - Bank of America Charitable Foundation: both 2026 RFP windows are closed. 2027 dates are not posted. VERIFIED (FAQ still shows 2026 dates only).
  - Banner Gives: "The cutoff date to request funding each year is September 30" (VERIFIED), so the 2026 cutoff has passed.
  - Wells Fargo, Lamb Weston and the Philips foundations accept no unsolicited requests (VERIFIED). Washington Trust Bank has no posted cycle (contact a banker).

## Other dated items in the next 12 months (for planning)

- **Avista HHS window Jan 1 – Feb 1 (2027 by inference)**; awards Apr 1. VERIFIED month/day.
- **Banner Gives annual cutoff Sept 30 (2027 by inference)**; allow 45–60 days for review. VERIFIED month/day.
- **BofA RFPs:** the 2026 pattern was Basic Needs & Income Creation 2/2–3/2 and Stable Housing & Empowering Communities 5/18–6/29. 2027 dates are not posted, so don't publish a date.
- **Boeing ECF Puget Sound 2027:** not posted. 2026 had two cycles (12/1/2025–2/28/2026 and 6/1/2026–8/30/2026). Watch boeing.com/community in early December.

---

## Bank of America (Bank of America Charitable Foundation)

- **HQ:** Charlotte, NC (VERIFIED, SEC EDGAR). PNW: the eligible local markets include **Seattle, WA; Spokane, WA; Portland/Vancouver, OR; and Boise, ID**. VERIFIED: https://about.bankofamerica.com/en/making-an-impact/eligible-states-local-markets
- **Foundation / program:**
  - Bank of America Charitable Foundation local grants through two RFP cycles. VERIFIED.
  - Neighborhood Builders, described as "a two-year leadership development and grant program" giving "core operating support, leadership development and access to a national network of peers". VERIFIED: https://about.bankofamerica.com/en/making-an-impact/neighborhood-builders
  - Employee matching gifts (details below).
- **Focus areas:** "basic needs, income creation, stable housing, and/or empowering communities" (economic mobility). VERIFIED (grant page). Health is not a named priority, so ACS must frame its request as basic needs or access.
- **Typical grant size:** "Grant amounts vary by market and organization size" (VERIFIED, FAQ). No range is published. The Neighborhood Builders award amount ($200K, or $100K–$400K per aggregators) is UNVERIFIED; the official page no longer states a figure.
- **Geographic limits:** a 501(c)(3) public charity (not a private foundation, no fiscal sponsor) that is "based and serve[s] communities in these markets". Seattle, Spokane, Portland/Vancouver and Boise are all on the list. VERIFIED. ACS is one national 501(c)(3), so how a national org qualifies as "based in" a market should be confirmed with the market team. Applications that pass the RFP go "through a local market committee for final decisioning" (VERIFIED, FAQ).
- **How to apply:**
  - Take the CyberGrants eligibility quiz, then the RFP application during posted windows only. "Unsolicited applications are not accepted outside of posted dates."
  - Organizations must register in NPO Hub (formerly FrontDoor) and accept ACH.
  - An organization is funded "no more than once in a calendar year".
  - VERIFIED: https://about.bankofamerica.com/en/making-an-impact/grant-funding-for-nonprofits-sponsorship-programs
- **Deadlines (next 12 months):** none posted. The 2026 windows were Basic Needs and Income Creation 2/2/2026–3/2/2026 and Stable Housing and Empowering Communities 5/18/2026–6/29/2026, both closed (VERIFIED). 2027 dates are not yet published.
- **Past cancer / ACS ties:**
  - The prior claim of a $50K 2015 grant for ACS rides in Dallas came from cancer.org/about-us/our-partners/bank-of-america.html. That page now 301-redirects to the generic partners page, so the claim is **UNVERIFIED** (source retired). Two searches found no independent confirmation.
  - An ACS DonorDrive "2026 Fit2Be Bank of America Dallas TX Challenge" page (supporting Hope Lodge Dallas) appeared in search but did not render. UNVERIFIED: https://raiseyourway.donordrive.com/events/1853
  - ACS Financial Services Cares Gala (NYC) sponsorship: from last run, not rechecked. UNVERIFIED.
- **Employee giving:** a matching gifts program exists. The "up to $5,000 per employee per year" figure is **UNVERIFIED**: the official matching-gifts URL now redirects to a general impact page that gives no amount.
- **Contact page:** foundation@bofa.com, 800.218.9946 (VERIFIED, FAQ: "Once I submit a grant application, who can I contact for assistance?")
- **Suggested Tier:** **2** (unchanged). Basic needs and access framing is craftable; the ACS precedent is now unverified.
- **ACS angle:** Pitch Road to Recovery rides and lodging access as a basic-needs program in the 2027 Basic Needs and Income Creation RFP, routed to the Seattle, Spokane, Portland/Vancouver and Boise market committees. Register in NPO Hub now so ACS is ready when the 2027 window posts.
- **Changes vs. prior claims:**
  1. 2026 windows **confirmed** (Feb 2–Mar 2 = *Basic Needs and Income Creation*; May 18–Jun 29 = *Stable Housing and Empowering Communities*). The prior entry called the cycle a "Basic Needs RFP" only. Road to Recovery fits the Feb cycle, not the May one.
  2. **2027 dates are not posted** (the "likely Feb" claim is still an assumption).
  3. Markets: **all four confirmed** (Seattle, Spokane, Portland/Vancouver, Boise) on the official eligible-markets list.
  4. The **$50K Dallas ACS grant is downgraded to UNVERIFIED**: the ACS partner page that sourced it was retired.
  5. The match of up to $5K is **UNVERIFIED** (the official page no longer states it).
  6. Neighborhood Builders is confirmed as a two-year leadership plus operating-support program; the award amount is unverified.
- **Sources:**
  - VERIFIED: https://about.bankofamerica.com/en/making-an-impact/grant-funding-for-nonprofits-sponsorship-programs
  - VERIFIED: https://about.bankofamerica.com/en/making-an-impact/eligible-states-local-markets
  - VERIFIED: https://about.bankofamerica.com/en/making-an-impact/neighborhood-builders
  - VERIFIED (HQ): SEC EDGAR CIK 0000070858
  - UNVERIFIED: https://www.cancer.org/about-us/our-partners/bank-of-america.html (now redirects) ; https://raiseyourway.donordrive.com/events/1853 ; https://about.bankofamerica.com/en/making-an-impact/matching-gifts-features-and-eligibility (redirects; $5K figure only in a search snippet) ; https://grantedai.com/grants/neighborhood-builders-program-bank-of-america-charitable-foundation-c47be1d8

---

## Wells Fargo (Wells Fargo Foundation / Community Giving)

- **HQ:** San Francisco, CA (VERIFIED, SEC EDGAR business address). PNW: branch network in WA, OR and ID (not counted today).
- **Foundation / program:** Wells Fargo and the Wells Fargo Foundation make national and local grants (VERIFIED). There is also a separate sponsorship portal (VERIFIED).
- **Focus areas:** "financial opportunity, housing access and affordability, and small business growth". VERIFIED: https://www.wellsfargo.com/about/responsibility-and-impact/community-giving/
- **Typical grant size:** not published. UNVERIFIED.
- **Geographic limits:** must be a 501(c)(3) (or a government, tribal or school entity). Exclusions include individuals, political groups, fraternal groups, sports and travel. VERIFIED (grant-process page). No PNW-specific limits are published.
- **How to apply:** "Wells Fargo and the Wells Fargo Foundation have implemented an invitation process." Invited nonprofits "will use the invitation code provided". VERIFIED: https://www.wellsfargo.com/about/responsibility-and-impact/community-giving/grant-process/
  - Sponsorships: submit "at least 90 days prior to the sponsorship start date", and most reviews take 60 days. However, the portal says 501(c)(3) organizations and/or operating or program grant seekers should go to Community Investment. So an ACS event sponsorship request may be redirected. VERIFIED: https://sponsorships.wf.com/
- **Deadlines (next 12 months):** none (invitation only). VERIFIED.
- **Past cancer / ACS ties:** The prior claims (five-time "Excellence in Philanthropy" honoree; more than $4.3M from Relay teams; 102 teams in 2015) came from https://www.cancer.org/about-us/our-partners/wells-fargo.html. **That page now 302-redirects to the generic ACS partners page, which does not mention Wells Fargo.** All of these claims are now **UNVERIFIED**. A 2014 3BL Media release reportedly lists Wells Fargo among 20 Excellence in Philanthropy honorees (search snippet only, UNVERIFIED): https://www.3blmedia.com/News/American-Cancer-Society-Honors-20-Companies-Excellence-Philanthropy-Recognition
- **Employee giving:** "eligible employees receive 16 hours of paid volunteer time". Employee Impact Teams "organize and lead group volunteer events ... and nurture lasting relationships with local charities". VERIFIED (community-giving page). No matching-gift details were found on that page.
- **Contact page:** https://www.wellsfargo.com/about/responsibility-and-impact/community-giving/grant-process/ (no public grants inbox found); sponsorships at https://sponsorships.wf.com/
- **Suggested Tier:** **2 → 3 (recommend downgrade)**. Grants are invitation-only, the funding priorities do not include health, and the ACS history is now unverifiable from ACS's own site. Keep Tier 2 only if ACS's internal records confirm recent Wells Fargo giving.
- **ACS angle:** Ask ACS's corporate relations team to check its internal records for Wells Fargo payroll giving and Relay team history. If that history is still active, use PNW Employee Impact Teams for Relay and Making Strides volunteering, and invite a regional leader to an ACS event.
- **Changes vs. prior claims:**
  1. Invitation-only is **confirmed** (VERIFIED).
  2. The cancer.org page **no longer exists** (it redirects). The "5× Excellence in Philanthropy" and "$4.3M+ Relay" claims are **downgraded to UNVERIFIED**.
  3. New: the sponsorship portal redirects 501(c)(3)s to Community Investment; 90-day lead time (VERIFIED).
  4. HQ San Francisco, CA, is now VERIFIED (SEC); last run's note called it unverified.
- **Sources:**
  - VERIFIED: https://www.wellsfargo.com/about/responsibility-and-impact/community-giving/
  - VERIFIED: https://www.wellsfargo.com/about/responsibility-and-impact/community-giving/grant-process/
  - VERIFIED: https://sponsorships.wf.com/
  - VERIFIED (HQ): SEC EDGAR CIK 0000072971
  - UNVERIFIED: https://www.cancer.org/about-us/our-partners/wells-fargo.html (now redirects) ; https://www.3blmedia.com/News/American-Cancer-Society-Honors-20-Companies-Excellence-Philanthropy-Recognition

---

## Boeing (Boeing Global Engagement / Employees Community Fund)

- **HQ:** Arlington, VA (VERIFIED, SEC EDGAR). PNW: Puget Sound and Portland ECF chapters (VERIFIED, chapter PDFs). The manufacturing footprint was not re-verified today.
- **Foundation / program:**
  1. Boeing corporate community investments, "managed locally". The community page tells interested organizations to email a named Boeing staff contact (linked on the page) with the city and state of the request. VERIFIED: https://www.boeing.com/community
  2. **Employees Community Fund (ECF)**: "Employee-led grantmaking committees at 23 Boeing sites". ECF chapters invested $3.2M in 2025. VERIFIED (same page). The ECF is a separate entity from The Boeing Company (VERIFIED, Portland PDF).
- **Focus areas:**
  - **ECF Puget Sound:** "501(c)(3) Health & Human Service nonprofits such as food banks, job-training programs, shelters, transitional housing, mental health services, and low-income medical clinics", with "direct client benefit". VERIFIED.
  - **ECF Portland:** the same areas plus youth programs. VERIFIED.
- **Typical grant size:**
  - Puget Sound Supporting Grants up to **$50,000** (no more than 10% of the agency's gross revenue). Capital Campaign grants **$125,000–$250,000**, limited to King, Pierce and Snohomish counties. VERIFIED.
  - Portland: "up to $40,000". VERIFIED.
- **What ECF funds:** capital items only, such as equipment, vehicles that support clients, phone systems, remodels, computers or software for direct client use, and buildings. VERIFIED.
- **Exclusions that hurt ACS (VERIFIED, Puget Sound PDF):**
  - "Medical research"
  - "National fund drives"
  - "Fundraising foundations (ECF only supports nonprofits that are direct to client providers)"
  - fundraising efforts
  - "Hospitals or other medical organizations with revenues greater than $50,000,000"
  - operating costs and salaries
  - Portland excludes "Medical research", fundraising foundations and capital campaigns (VERIFIED).
  - **ACS (a national organization with revenue well over $50M) may be screened out as a "national fund drive" or under the large-medical-organization rule.** Confirm eligibility with the chapter inbox before investing time.
- **Geographic limits:** Supporting grants "only for agencies benefiting residents in the Puget Sound Region"; Portland grants for "the greater Portland metropolitan area". VERIFIED.
- **How to apply:** apply through STAR (https://boeing.smartsimple.com). First-time applicants email the chapter inbox to request access. Capital-campaign applicants email a project summary first. Required documents: bids, operating budget, 990 or audit, project budget, and IRS determination letter. VERIFIED.
- **Deadlines (next 12 months):**
  - **Puget Sound 2026 timeline (VERIFIED):** Cycle 1 open 12/1/2025, deadline 2/28/2026, awards 5/31/2026. Cycle 2 open 6/1/2026, deadline 8/30/2026, awards 12/1/2026. Both are closed. The 2027 timeline is not posted.
  - **Portland:** "Not accepting grant applications at this time. To be determined." VERIFIED.
- **Past cancer / ACS ties:** none found today.
- **Employee giving:** ECF is itself the employee payroll-giving vehicle (VERIFIED). Boeing's corporate gift-match details are not on the pages read (UNVERIFIED).
- **Contact page:** https://www.boeing.com/community ; ECF Puget Sound: PSEmployeesCommunityFund@exchange.boeing.com (VERIFIED) ; ECF Portland: ECFPortland@boeing.com (VERIFIED)
- **Suggested Tier:** **3 (recommend downgrade from 2).** ECF's exclusions (national fund drives, medical research, large medical organizations, operating costs) are a poor fit for ACS. The corporate route is relationship-only.
- **ACS angle:** The only realistic ECF ask is a capital item with direct client benefit, such as a wheelchair-accessible vehicle for patient transport in King, Pierce or Snohomish counties. Even that requires the chapter to confirm that ACS is not excluded as a national organization. Otherwise, contact the Boeing community team about workforce cancer-screening education.
- **Changes vs. prior claims:**
  1. ECF Puget Sound guidelines and 2026 dates are **now VERIFIED** (previously "PDF blocked").
  2. **New exclusions found** (national fund drives, medical research, medical organizations with revenue over $50M, operating costs) that likely rule out most ACS asks. The prior "pitch Road to Recovery and Hope Lodge" angle is weakened.
  3. Portland ECF is **not accepting applications**.
  4. "Global Engagement by invitation only": the current community page does not use the word "invitation". It directs requests to a named local contact (relationship-based). The 2024 Washington State guidelines PDF cited last time is from an older URL path and was not re-read.
  5. The old PDF URL under `/boeingdotcom/principles/.../ecf/` now returns 404; the current URL is under `/v2/company/community-engagement/pdf/`.
- **Sources:**
  - VERIFIED: https://www.boeing.com/community
  - VERIFIED: https://www.boeing.com/content/dam/boeing/v2/company/community-engagement/pdf/Washington-Puget-Sound-ECF.pdf
  - VERIFIED: https://www.boeing.com/content/dam/boeing/v2/company/community-engagement/pdf/Oregon-ECF.pdf
  - VERIFIED (HQ): SEC EDGAR CIK 0000012927
  - UNVERIFIED: https://grantable.co/grants/ecf-of-boeing-washington-puget-sound-grant-4b88e1342ac8 (says "rolling" and a $40K cap; conflicts with the official PDF, ignore)

---

## Avista (Avista Foundation)

- **HQ:** Spokane, WA (VERIFIED, SEC EDGAR). PNW: Avista Utilities service area.
- **Foundation / program:** the Avista Foundation, "a community investment program of Avista Corp." It funds nonprofits serving communities "served by Avista Utilities in eastern Washington, northern Idaho, portions of southern Oregon, and Sanders County, Montana", plus Juneau, AK (AEL&P). VERIFIED: https://www.avistafoundation.com
- **Focus areas:** "education, vulnerable and limited income populations, and economic and cultural vitality". VERIFIED (application page; also the myavista giving page).
- **Typical grant size:**
  - The 2025 990-PF reports **$2,243,054** in contributions and grants paid, and net assets of $10.56M at year-end. VERIFIED (self-hosted 990-PF).
  - The grant list is dominated by small awards (hundreds to a few thousand dollars, including matching gifts). The largest single line is $350,000.
  - Health-related examples: Providence INW Foundation $25,000 (medical supplies and Heart Institute campaign); MultiCare Inland NW Foundation $2,500 (general operating support). VERIFIED.
- **Geographic limits:** "You must be serving the needs of people within our service area." VERIFIED.
- **How to apply:**
  - Take the online eligibility quiz on CyberGrants, then submit the application. "All applications created in the online system are immediately submitted."
  - Sponsorships (events, not programs) are accepted year-round; allow 90 days.
  - Requests for religious or political activities, individuals and private foundations are "likely to be declined". VERIFIED.
- **Deadlines (next 12 months), VERIFIED (month/day only):**

  | Track | Opens | Closes | Awards |
  |---|---|---|---|
  | Health and Human Service | Jan 1 | Feb 1 | Apr 1 |
  | Education and Youth Development | Mar 1 | Apr 1 | Jul 1 |
  | Economic and Community Vitality | Jul 1 | Aug 1 | Oct 1 |
  | Environmental | Oct 1 | Nov 1 | Dec 1 |
  | Arts and Culture | Oct 1 | Nov 1 | Dec 1 |

  The relevant ACS window is **Jan 1 – Feb 1 (2027, by inference from the standing annual table)**.
- **Past cancer / ACS ties:** no American Cancer Society grant appears in the 2025 990-PF (text search). The only cancer line is Childhood Cancer Coalition, $200, as a "Matching Gifts" entry. VERIFIED.
- **Employee giving:** the 990-PF lists many "Matching Gifts" grants, so an employee match exists. The match terms are not published on the pages read (UNVERIFIED).
- **Contact page:** contributions@avistacorp.com ; 509.495.8156 ; Avista Foundation, MSC-68, PO Box 3727, Spokane, WA 99220-3727 (VERIFIED, avistafoundation.com footer)
- **Suggested Tier:** **2** (unchanged).
- **ACS angle:** Apply in the Jan 1 – Feb 1 Health and Human Service window for Road to Recovery rides and navigation for limited-income patients in Spokane, North Idaho and the rural service area. That matches the "vulnerable and limited income populations" priority. Size the request modestly (low thousands to about $25K) based on 2025 grant patterns.
- **Changes vs. prior claims:**
  1. **"Quarterly applications" is wrong.** Each focus area has **one annual one-month window**. The HHS window is **Jan 1 – Feb 1**, with awards Apr 1 (VERIFIED). Fix prospects.md.
  2. The HHS track is confirmed. The limited-income priority is confirmed ("vulnerable and limited income populations").
  3. New: 2025 990-PF totals and health-grant examples (VERIFIED). No ACS grant found.
  4. The prior "site is blocked" note is resolved: avistafoundation.com and the CyberGrants page both load.
- **Sources:**
  - VERIFIED: https://www.cybergrants.com/pls/cybergrants/quiz.display_question?x_gm_id=5440&x_quiz_id=7208&x_order_by=1
  - VERIFIED: https://www.avistafoundation.com
  - VERIFIED: https://www.myavista.com/about-us/our-community/giving-back
  - VERIFIED (990-PF 2025): https://www.avistafoundation.com/annualreturns/Documents/Form%20990-PF%20For%202025%20AS%20FILED.pdf
  - VERIFIED (HQ): SEC EDGAR CIK 0000104918
  - Not readable: https://investor.avistacorp.com/news-releases/news-release-details/avista-provide-475500-community-non-profit-agencies-grants-will (403)

---

## Lamb Weston (Lamb Weston Charitable Foundation) (NEW)

- **HQ:** Eagle, ID (VERIFIED, SEC EDGAR and 2025 Sustainability Report). PNW footprint (VERIFIED, report facility map): corporate offices in Kennewick, WA; plants in Pasco, Paterson, Quincy, Richland (×2), Warden and Connell, WA; Boardman (×3) and Hermiston, OR; American Falls and Twin Falls, ID.
- **Foundation / program:**
  - **Lamb Weston Charitable Foundation** ("Lamb Weston Foundation"), Eagle, ID, EIN 83-0562671, a private foundation filing a 990-PF. VERIFIED (ProPublica).
  - Corporate local donations and sponsorships. VERIFIED (report).
- **Focus areas:** the Foundation "focuses its giving on food insecurity and hunger, as well as granting scholarships" (VERIFIED, 2025 Sustainability Report p.25). Corporate local giving covers "a wide range of community needs" (VERIFIED).
- **Typical grant size:**
  - 2024 990-PF: grants paid **$1,343,045**. Most of it went through employee-directed giving platforms (American Online Giving Foundation $795,172; Canadian and Australian counterparts).
  - Direct grants were food banks at $25,000–$110,000 (Idaho Foodbank $110,000; Oregon Food Bank $100,000; Second Harvest Inland Northwest $100,000). VERIFIED.
  - Net assets $12.9M (2024). VERIFIED.
- **Geographic limits:** global. The foundation's direct grants follow plant communities. No published geographic rule.
- **How to apply:** **no unsolicited requests.** The 2024 990-PF has the "only makes contributions to preselected charitable organizations" box checked, with no application address or deadlines. VERIFIED (ProPublica full text). Corporate local sponsorships happen (see ties) but no public request form was found.
- **Deadlines (next 12 months):** none (preselected only). VERIFIED.
- **Past cancer / ACS ties:** 2025 local donations and sponsorships included the **"Tri-Cities Cancer Foundation"**, alongside other Tri-Cities and Idaho causes. VERIFIED (2025 Sustainability Report p.24). No ACS ties found.
- **Employee giving (VERIFIED, report p.25):**
  - Matching gifts of "up to $1,000 per person annually" to any eligible 501(c)(3). Board members are matched up to $5,000. More than $80,000 was matched in 2025.
  - **Pay It Forward:** a $50 giving account per eligible team member. 75% participated, directing $300,000 to more than 1,400 charities.
  - **Give Get Give:** $5 per volunteer hour, up to $500 a year.
  - **Board service grants:** $2,500 after one year on a nonprofit board.
  - 8 hours of paid volunteer time off for salaried team members.
  - **September Month of Service:** 80 hours were "focused on health-related and rehabilitative support".
- **Contact page:** https://www.lambweston.com (Contact Us). No public foundation inbox was found.
- **Suggested Tier:** **3.** The foundation is preselected and hunger-focused. The open doors are employee giving and Tri-Cities corporate sponsorship.
- **ACS angle:** Make sure ACS is selectable in Lamb Weston's employee giving portal (the matching, Pay It Forward and Give Get Give platform) so that the large Tri-Cities, Columbia Basin and Magic Valley workforce can direct gifts. Then pitch a local Relay For Life or Road to Recovery sponsorship to the Kennewick and Richland team, which already supports the Tri-Cities Cancer Foundation.
- **Sources:**
  - VERIFIED: https://projects.propublica.org/nonprofits/organizations/830562671
  - VERIFIED (2024 990-PF): https://projects.propublica.org/nonprofits/full_text/202502689349100500/IRS990PF
  - VERIFIED: https://esg.lambweston.com ; https://www.lambweston.com/content/dam/lamb-weston/website/general-content/pdf/sustainability/2025-Sustainability-Report.pdf
  - VERIFIED (HQ): SEC EDGAR CIK 0001679273
  - UNVERIFIED: https://www.zeffy.com/foundations/830562671 ; https://platform.grantexec.com/foundations/830562671-lamb-weston-charitable-foundation

---

## Banner Bank (Banner Gives) (NEW)

- **HQ:** Walla Walla, WA (VERIFIED, SEC EDGAR: Banner Corp, 10 S First Avenue). PNW footprint: the bank operates in "Washington, Oregon, California and Idaho" (VERIFIED, community-support page). It recently completed the acquisition of Pacific Financial Corp. (Bank of the Pacific), which per the site banner adds western WA and OR presence (VERIFIED banner text; the footprint detail is UNVERIFIED).
- **Foundation / program:** **Banner Gives** grants, run by the bank. No separate foundation was found. VERIFIED: https://bannerbank.com/about-us/community-support
- **Focus areas (VERIFIED):** priority for "programs serving low- and moderate-income populations" in:
  - housing and homelessness
  - youth academic achievement, civic involvement, financial literacy, and "physical and emotional development"
  - financial education
  - economic development
  - **Health is not a listed area.**
- **Request priorities (VERIFIED, request-community-support page):**
  - shelter or housing
  - small business development
  - "current client organizations"
  - "organizations in which current employees are active volunteers"
- **Typical grant size:**
  - Not published. Aggregators cite $1,500–$25,000 (UNVERIFIED).
  - 2025: "$852,500 in charitable donations", 18,398 volunteer hours with nearly 800 organizations. VERIFIED: https://bannerbank.com/impact
  - The request page says more than $3.5M was contributed "last year" to more than 1,000 causes. The two figures likely measure different things; both are as stated by Banner.
- **Geographic limits:** WA, OR, CA and ID communities served. VERIFIED.
- **Exclusions:** endowments, "fundraising campaigns", sports and athletic events, memorial campaigns, travel, and individuals. VERIFIED. The fundraising-campaign exclusion may rule out Relay For Life and Making Strides event asks.
- **How to apply:** take the eligibility quiz at https://www.cybergrants.com/bannerbank/BannerGivesEligibilityQuiz, which leads to the application. "Please allow 45-60 days." VERIFIED (the quiz page is a jump page and did not render text).
- **Deadlines (next 12 months):** "The cutoff date to request funding each year is September 30." VERIFIED. The 2026 cutoff has passed, so the next is **Sept 30, 2027** (year by inference). Requests are otherwise accepted on a rolling basis.
- **Past cancer / ACS ties:** none found (one search, no results). UNVERIFIED either way.
- **Employee giving:** strong volunteer culture (VERIFIED volunteer-hour figures). No matching-gift program was found on the pages read.
- **Contact page:** https://bannerbank.com/about-us/request-community-support ; https://bannerbank.com/about-us/community-support
- **Suggested Tier:** **3.** Health is not a priority and fundraising campaigns are excluded. The best lever is the employee-volunteer priority.
- **ACS angle:** Recruit Banner employees as Road to Recovery drivers or Relay volunteers in Walla Walla, the Tri-Cities and Spokane first. Then submit a small Banner Gives request before the Sept 30, 2027 cutoff for rides for low-income rural patients, citing the "employees are active volunteers" priority.
- **Sources:**
  - VERIFIED: https://bannerbank.com/about-us/community-support
  - VERIFIED: https://bannerbank.com/about-us/request-community-support
  - VERIFIED: https://bannerbank.com/impact
  - VERIFIED (HQ): SEC EDGAR CIK 0000946673
  - UNVERIFIED: https://grantable.co/grants/banner-bank-community-support-program-grant-9c984131f278 ; https://grantedai.com/grants/banner-gives-community-support-program-banner-bank-1f3c1e8f (aggregators; one still shows an outdated Oct 15, 2024 cutoff)

---

## Washington Trust Bank (NEW)

- **HQ:** Spokane, WA (UNVERIFIED: Wikipedia and search snippet, 717 W Sprague Ave; the bank is private, so there is no SEC check). The bank's own page says it is "a wholly owned subsidiary of W.T.B. Financial Corporation" with "more than 40 branches and offices in Washington, Idaho, and Oregon" and $11B in assets. VERIFIED: https://www.watrust.com/about/investor-relations
- **Foundation / program:** corporate sponsorships, partnerships and CRA donations. No foundation or grant portal was found. VERIFIED: https://www.watrust.com/community
- **Focus areas:** "sponsorship and volunteer opportunities with a focus on supporting community development and economic sustainability within underserved areas". 2025 giving supported "affordable housing, community services, economic development, and community revitalization". VERIFIED (community page and the "Beyond Big Checks" article, 2026-06-24).
- **Typical grant size:**
  - Not published.
  - Totals: "more than $3.8 million" donated in 2025. In 2024, 394 organizations through 463 sponsorships and events, and 105 CRA-qualified donations.
  - The bank ranked #10 on the Puget Sound Business Journal's list of the largest corporate philanthropists in Washington.
  - VERIFIED: https://www.watrust.com/articles/beyond-big-checks-our-approach-to-corporate-giving
- **Geographic limits:** WA, ID and OR communities served. VERIFIED.
- **How to apply:** "If your organization is a tax-exempt nonprofit (501c3), we want to hear from you. Please contact a banker to discuss your organization" (relationship-based, no form). VERIFIED.
  - **Do not use washtrust.com.** That is a different bank (The Washington Trust Company, Rhode Island). Its "90 days prior" sponsorship rule does not apply here.
- **Deadlines (next 12 months):** none posted. VERIFIED (no cycle on the pages).
- **Past cancer / ACS ties:** none found.
  - The bank cites "a decades long commitment to providing a home-away-from-home for families traveling for medical care". The link goes to a LinkedIn post, so the organization was not confirmed; it may be Ronald McDonald House (UNVERIFIED). This medical-lodging commitment is the closest analog to Hope Lodge.
  - One search for ACS or Relay ties found nothing.
- **Employee giving:** "Crew in Blue" employee-led volunteer initiative. 2,452 volunteer hours to 155 organizations (2024); CRA service of 3,992 hours. The bank says it "continuously explore[s] ... matching gifts", so no current match program is confirmed. VERIFIED (article).
- **Contact page:** https://www.watrust.com/community ("Find a Location / contact a banker"); general contact via watrust.com "Contact Us".
- **Suggested Tier:** **2.** The bank is large for the region, Spokane-rooted and sponsorship-driven, and it has a stated record of supporting medical-travel lodging, a craftable tie to ACS patient lodging and Road to Recovery. The "underserved areas" framing fits health-equity programs.
- **ACS angle:** Through a Spokane banker relationship, pitch an underserved-patient access sponsorship: Road to Recovery rides plus lodging assistance for rural Inland Northwest patients traveling to Spokane for treatment. Frame it as an extension of the bank's medical-travel lodging commitment, with Crew in Blue volunteer driving.
- **Sources:**
  - VERIFIED: https://www.watrust.com/community
  - VERIFIED: https://www.watrust.com/articles/beyond-big-checks-our-approach-to-corporate-giving
  - VERIFIED: https://www.watrust.com/about/investor-relations
  - UNVERIFIED: https://en.wikipedia.org/wiki/Washington_Trust_Bank (HQ address)
  - NOT THIS COMPANY: https://www.washtrust.com/about/community-support/sponsorships (Rhode Island bank)

---

## Philips (Bothell, WA ultrasound site) (NEW)

- **HQ:** Amsterdam, Netherlands, for Koninklijke Philips N.V. (common knowledge, not re-verified). The US foundation files from Cambridge, MA (VERIFIED, ProPublica). PNW: **Philips Ultrasound LLC, 22100 Bothell Everett Hwy, Bothell, WA 98021** (VERIFIED, Philips-issued document). Workforce of about 2,000 and roughly 80% of Philips ultrasound units made in Bothell (UNVERIFIED, HeraldNet snippet). Reports of a planned campus sale (UNVERIFIED, GeekWire tag-page snippet, undated).
- **Foundation / program:**
  1. **Philips Foundation** (Stichting, Netherlands). Mission: "enable access to quality healthcare for underserved communities" through grants and impact investments. Its "strategic focus is on cardiovascular disease and maternal and child health", plus disaster readiness. VERIFIED: https://www.philips-foundation.com ; Annual Report 2025.
     - US activity in 2025: Philips Foundation and Philips North America partnered with MedShare on disaster-readiness equipment (VERIFIED, AR 2025 p.16). North America accounted for 0.4M people reached (VERIFIED, AR 2025 p.8).
     - A breast-cancer screening project (Mamotest) appears in the portfolio, outside the US (VERIFIED, AR 2025 p.3).
  2. **Philips Electronics North America Foundation** (EIN 13-2961300). The 2025 990-PF shows $191,250 paid, **all employee-dependent academic scholarships** (76 lines, none to a public charity), with the "preselected only" box checked. VERIFIED.
- **Focus areas:** cardiovascular, maternal and child health, community and primary care, disaster readiness (Foundation). Cancer is not a strategic focus. VERIFIED.
- **Typical grant size:** Philips Foundation grant-based projects totaled EUR 4.1M in 2025 (figure as shown on the AR 2025 key-figures page; layout extraction was imperfect, so treat it as approximate). The US foundation gives scholarships of $2,500–$3,750. VERIFIED.
- **Geographic limits:** global, aimed at underserved communities, mostly in low- and middle-income countries. No PNW program was found.
- **How to apply:** no open application. The US foundation is preselected-only (VERIFIED, 990-PF). The Philips Foundation site has no application route; the public inbox is philipsfoundation@philips.com (VERIFIED, decoded from the site's mailto link).
- **Deadlines (next 12 months):** none.
- **Past cancer / ACS ties:** none found. One search for an ACS or National Lung Cancer Roundtable link to Philips found nothing.
- **Employee giving:** a matching-gift program is reported as **inactive** (UNVERIFIED, Double the Donation): https://doublethedonation.com/matching-gifts/philips
- **Contact page:** philipsfoundation@philips.com ; https://www.usa.philips.com/healthcare (no community-giving page for Bothell found)
- **Suggested Tier:** **3.** There is no grant route. Possible upside lies in in-kind or corporate partnership (imaging and screening), not philanthropy.
- **ACS angle:** Approach Philips North America as a corporate partner, not a grantor. Possible asks: sponsorship of a lung or breast screening awareness event, or Bothell employee volunteering (Road to Recovery drivers). Low expected yield, and the reported site-sale and layoff news needs checking first.
- **Sources:**
  - VERIFIED: https://www.philips-foundation.com
  - VERIFIED: https://www.philips.com/c-dam/philips-foundation/Files/annualreports/Philips_Foundation_Annual_Report_2025.pdf
  - VERIFIED: https://projects.propublica.org/nonprofits/organizations/132961300 ; https://projects.propublica.org/nonprofits/full_text/202631109349100153/IRS990PF
  - VERIFIED (Bothell address): https://www.documents.philips.com/assets/IHE%20Integration%20Statements/20250604/03ddee51e5ea41588c92b2f200653197.pdf
  - UNVERIFIED: https://heraldnet.com/business/medical-devices-made-in-county-one-of-states-top-exports ; https://www.geekwire.com/tag/philips/ ; https://doublethedonation.com/matching-gifts/philips ; https://www.zeffy.com/foundations/132961300

---

## Suggested prospects.md updates

| Company | Change |
|---|---|
| Avista | Deadline column: "HHS window Jan 1 – Feb 1 annually (V); awards Apr 1". Remove "Quarterly". |
| Bank of America | Keep Tier 2. Mark the Dallas $50K precedent "unverified (ACS page retired)". Markets confirmed (V). |
| Wells Fargo | Mark the ACS history "unverified (ACS page retired)". Consider Tier 3. |
| Boeing | Add ECF Puget Sound 2026 dates (V) and exclusions (national fund drives, medical research, medical orgs >$50M revenue). Portland ECF closed. Consider Tier 3. |
| Lamb Weston (new) | Tier 3; preselected foundation; employee giving and Tri-Cities sponsorship route. |
| Banner Bank (new) | Tier 3; Banner Gives annual cutoff Sept 30 (V). |
| Washington Trust Bank (new) | Tier 2; relationship/banker route; medical-travel lodging tie. |
| Philips (new) | Tier 3; no grant route. |
