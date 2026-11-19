# The World, Today — 19 November 2026

Original make.fun entry for **news-image-20261119**: a flat, illustrated news
infographic, with the exact Thursday date masthead, an original dotted locator
map, six numbered pins, and six cards. All lettering is rendered with DejaVu
Sans. No photographs, downloaded artwork, or runtime services are used.

## Run the entry

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png`. Without the environment variable it writes
`/output/entry.png`. The program resolves the source image relative to `main.py`,
works from any working directory, verifies the PNG signature and source size,
copies the pre-rendered image, checks the copied size, and exits successfully.
It imports only `os`, `shutil`, and `sys`; it is compatible with Python 3.13 and
needs no installed packages or network access. Repeated runs emit identical
image bytes. Include **both main.py and entry.png** in the submission.

## The six stories and date evidence

Dates below are local to the reported event or publisher. An event taking place
on 19 November is eligible even when its schedule was reported in advance.
Warnings are described as warnings, forecasts as forecasts, and risks as risks.
The artwork does not claim a cyclone landfall, a completed court ruling, or a
completed diplomatic meeting.

1. **GTA VI rolls out — 19 November 2026, global / Sydney locator.**
   Reuters reports market-by-market midnight Thursday unlocking, beginning in
   New Zealand; MarketScreener also reports the Thursday release. Reuters' advance
   report carries a Wednesday/18 November timestamp in some syndications:
   this card depicts the **19 November local release**, not an allegedly new
   Wednesday announcement. The Metacritic 99 claim is deliberately omitted.
   - Reuters, *Gamers get ready to enter Vice City as Grand Theft Auto VI begins global rollout*:
     https://new.streetinsider.com/Reuters/Gamers%2Bget%2Bready%2Bto%2Benter%2BVice%2BCity%2Bas%2BGrand%2BTheft%2BAuto%2BVI%2Bbegins%2Bglobal%C2%A0rollout/27366276.html
   - MarketScreener, published **19 November 2026, 03:49 AEDT**, explicitly
     identifies the worldwide launch as Thursday 19 November:
     https://au.marketscreener.com/news/gta-vi-arrives-take-two-interactive-speeds-off-on-wall-street-ce785edddd8bfe22

2. **Akvan warning issued — 19 November 2026, Bay of Bengal.**
   Primary IMD bulletin BOB/10/2026 is explicitly **issued 19 November 2026,
   0230 IST**, based on 2330 IST observations from the 18th. The card concerns
   that new issuance, not the storm's earlier formation or intensification.
   The pin uses the bulletin's 13.9°N, 85.3°E position. Landfall remains a
   forecast and is not depicted as having happened.
   - IMD dated national bulletin (filename contains the observation date;
     the document itself says **DATED: 19.11.2026**):
     https://mausam.imd.gov.in/Forecast/marquee_data/27.%20National%20Bulletin%20No%2027-18Nov2026_2330IST.pdf
   - Independent 19 November weather coverage, Prabhat Khabar:
     https://www.prabhatkhabar.com/state/madhya-pradesh/cyclone-akvan-wont-impact-mp-weather-on-nov-19-dry-conditions-expected
   - 19 November newspaper edition corroborates ongoing Akvan coverage:
     https://www.moi.gov.mm/nlm/file-download/download/public/5624

3. **Suneung exam day — 19 November 2026, South Korea.**
   AFP's article is dated **19 November 2026** and reports students sitting
   Thursday's exam, with measures against AI-assisted cheating. The rounded
   phrase "half a million" follows AFP; the artwork makes no result claim.
   - AFP via The News, *Wifi cut, AI-cheat bounties as South Koreans sit key college exam*:
     https://www.thenews.pk/print/1449550-wifi-cut-ai-cheat-bounties-as-south-koreans-sit-key-college-exam
   - Aju Press, 18 November advance context for Thursday's exam (not itself
     treated as a 19 November report):
     https://www.ajupress.com/view/20261118165045103

4. **The cost of AI power — 19 November 2026, Australia.**
   ABC's Thursday reporting describes a Climate Council report warning of
   potential emissions from proposed data centres **if powered by fossil
   fuels**. These are conditional projections, not measured current emissions.
   The Queensland locator reflects the Western Downs project discussed in
   ABC's local report.
   - ABC Southern Queensland, expressly posted **Thu 19 Nov 2026, 9:53 am**:
     https://www.abc.net.au/news/2026-11-19/southern-queensland-local-news-briefing/107401912
   - ABC Listen, dated 19 November (same newsroom, not an independent source):
     https://www.abc.net.au/listen/programs/abc-news-top-stories/climate-council-data-centres-fossil-fuels-emissions-australia/107401854
   - Climate Council's primary publication, explicitly **19 November 2026**:
     https://www.climatecouncil.org.au/resources/data-centres-that-could-rival-our-dirtiest-coal-power-stations/
   - Independently reported by 2NM, **19 November 2026, 8:06 am**:
     https://www.2nm.com.au/local-news/report-warns-hunter-data-centre-proposals-could-add-millions-of-tonnes-of-pollution/

5. **Inflation stays in focus — 19 November 2026, Auckland, New Zealand.**
   The RBNZ's primary news listing labels *RBNZ Governor outlines inflation
   outlook amid uneven recovery* **19 November 2026** and says Governor Anna
   Breman spoke "today" at an Auckland Institute of Directors event. The card
   describes those remarks; it does not suggest an interest-rate decision.
   - RBNZ primary release and dated news listing:
     https://www.rbnz.govt.nz/news-and-events/news/2026/11/rbnz-governor-outlines-inflation-outlook-amid-uneven-recovery
     https://www.rbnz.govt.nz/
   - RBNZ release carried by Scoop, **Thursday 19 November 2026, 8:57 am NZDT**:
     https://www.scoop.co.nz/stories/BU2611/S00165/rbnz-governor-outlines-inflation-outlook-amid-uneven-recovery.htm
   - RBNZ schedule independently locates the engagement on **19 November**
     (advance confirmation, same institution):
     https://www.rbnz.govt.nz/news-and-events/events/2026/october/governors-post-mpr-media-interview-schedule-october-2026

6. **Nouveau is here — 19 November 2026, Beaujolais, France.**
   La Revue du vin de France identifies Thursday **19 November 2026** as the
   release date for the new vintage. Retailer Coopérative U separately confirms
   the same date. This is the release-day event, not a claim that its date was
   first announced on the 19th. Earlier festivities on the 18th are not used.
   - La Revue du vin de France, *Quel jour sort le Beaujolais nouveau 2026 ?*:
     https://www.larvf.com/quel-jour-sort-le-beaujolais-nouveau%2C4804452.asp
   - Coopérative U release confirmation:
     https://www.coursesu.com/le-beaujolais-nouveau.html
   - Inter Beaujolais primary press release confirms **Thursday 19 November**
     as the release day in France and around the world:
     https://www.beaujolais.com/wp-content/uploads/sites/2/2026/07/CP_Beaujolais_Nouveaux_2026.pdf

## Verification and editorial exclusions

News checks used built-in web search and dated indexed source text on
19 November 2026. Direct `curl` failed because the configured proxy was
unreachable; disabling the proxy failed DNS resolution. No successful direct
HTTP fetch is claimed. Cross-checks are listed above, with advance schedules,
same-newsroom corroboration, and rolling primary documents identified plainly.
Some event dates are confirmed by advance reporting rather than a fresh
on-the-day story.

The proposed EUR 45 billion Ukraine loan is excluded as explicitly requested
(18 November). Jeffries/Senate results, renewed US–Iran exchanges, the Voyager
milestone, the ICJ outcome, Trump–Putin talks, Nvidia leadership/shipping claims,
and the Pew religion projection are not used: no sufficiently clear eligible
19 November occurrence/first-report evidence was retained for those claims.
The court and summit being scheduled for Thursday is not proof of an outcome.

## Render and verify

`entry.png` is the submitted artifact: **1024 × 1024**, RGB PNG, below
**1,048,576 bytes**. `render.py` is an optional build tool using Pillow 10.2.0
and `/usr/share/fonts/truetype/dejavu/DejaVuSans{,-Bold}.ttf`. Pillow is **not**
needed by `main.py`. The render has no random state, network calls, timestamps,
or metadata-dependent content. It draws at 2× resolution and downsamples once.

```sh
python3 render.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
sha256sum out/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
sha256sum out/entry.png
```

Local-date eligibility matters: 19 November in New Zealand begins on
18 November UTC. The RBNZ source above is explicitly dated 19 November NZDT;
the image does not present it as a fresh 19 November UTC announcement.

The locator map is original, generalized geometry without political borders;
pins connect to approximate event locations. The global game rollout is located
at Sydney as an early-release market. All art and scripts were created fresh
in this repository. No sibling repository files were used.

License: MIT; see LICENSE. DejaVu fonts are system build inputs and are not
redistributed as font files in this repository.
