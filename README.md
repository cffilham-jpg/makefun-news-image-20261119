# A Daily Atlas — 19 November 2026

An original square infographic for make.fun competition `news-image-20261119`.
A dotted, schematic world map connects six numbered locations to six illustrated
news cards. The date is the organizing idea: these are events occurring, or
reports issued, on Thursday 19 November 2026. Map positions are approximate;
Vice City is represented by the Miami area, its fictional inspiration.

## Editorial record

1. **GTA VI arrives — 19 November 2026.** The global console release begins.
   T3's launch guide says it launches globally on 19 November; GameMapa's
   release calendar independently lists the same date. These advance sources
   establish the event date, rather than a new announcement on that date.
   - https://www.t3.com/tech/gaming/how-to-play-grand-theft-auto-vi-early
   - https://gamemapa.com/en/gta-6/guides/gta-6-timeline-dates/
2. **Akvan warning — bulletin issued 19 November 2026, 02:30 IST.** India's
   Meteorological Department issued bulletin BOB/10/2026 concerning the severe
   cyclonic storm in the Bay of Bengal. The card reports the dated warning,
   not landfall. Its underlying observation is from late 18 November.
   Rediff's 19 November archive also reports preparations in Odisha.
   - https://mausam.imd.gov.in/backend/assets/cyclone_pdf/custom_bulletins/refineries.pdf
   - https://news.rediff.com/archives/archhome.htm
3. **Exam day, AI checks — 19 November 2026, South Korea.** SBS's 06:07 KST
   roundup and 06:10 exam report confirm the Suneung takes place that day amid
   AI cheating concerns. The security measures were announced earlier; this
   card covers their use on exam day. AFP's Boursorama report, published
   19 November at 00:54, directly confirms the exam and extra precautions.
   - https://news.sbs.co.kr/amp/news.amp?news_id=N1008852883
   - https://news.sbs.co.kr/english/newsFlash.do?pageDate=20261119
   - https://www.boursorama.com/actualite-economique/actualites/coree-du-sud-l-examen-d-entree-a-l-universite-s-ouvre-en-plein-scandale-de-triche-a-l-ia-076ed49df0855294f8069a76d819c2ed
4. **Data-centre warning — report published 19 November 2026, Australia.**
   Climate Council's publication warns that proposed fossil-powered centres
   could increase emissions without new renewable supply and storage. ABC's
   Southern Queensland briefing is independently dated 19 November. The
   artwork presents a conditional warning, not measured current emissions.
   - https://www.climatecouncil.org.au/resources/data-centres-that-could-rival-our-dirtiest-coal-power-stations/
   - https://www.abc.net.au/news/2026-11-19/southern-queensland-local-news-briefing/107401912
5. **Inflation in focus — 19 November 2026, New Zealand.** RBNZ's release,
   syndicated by Scoop at 08:57 NZDT, is titled “RBNZ Governor Outlines
   Inflation Outlook Amid Uneven Recovery.” Newswire.nz carries a related
   08:33 report; the Institute of Directors lists the governor's Auckland
   conversation for 07:00–09:00 on 19 November. This local date is used even
   though it is still 18 November in UTC.
   - https://info.scoop.co.nz/The_Reserve_Bank_of_New_Zealand_
   - https://newswire.nz/
   - https://www.iod.org.nz/all-events/auckland-branch-event/conversation-with-the-governor-of-the-reserve-bank-of-new-zealand-te-putea-matua
6. **Nouveau is here — 19 November 2026, France and worldwide.** The new
   Beaujolais Nouveau vintage is released on November's third Thursday.
   Discover Beaujolais explicitly dates the 2026 release to 19 November;
   CCI France Vietnam confirms the same date and worldwide tradition.
   Destination Beaujolais lists local celebrations that day as well.
   - https://www.discoverbeaujolais.com/beaujolais-nouveau
   - https://www.ccifv.org/en/events/upcoming/event-details/event/hn-beaujolais-nouveau-2026.html
   - https://www.beaujolais-tourisme.com/en/beaujolais-nouveaux/soiree-beaujolais-nouveau-8044954.html

Research used web search during production. No source is fetched at runtime.
Rolling archives and live bulletin URLs may subsequently change. No claim of
completed landfall, an ICJ judgment, or a Voyager milestone is included.

## Run the submission

Requires Python 3.13 and its standard library only:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Without the environment variable, the destination is `/output/entry.png`.
The program copies the bundled PNG, checks the destination byte count against
the source, and prints the output path. It makes no network requests, reads no
clock, uses no randomness, and writes identical image bytes on every run.

## Rebuild the artwork

`render.py` is a separate production tool requiring Pillow (tested with 10.2.0)
and the system DejaVu Sans regular and bold fonts in
`/usr/share/fonts/truetype/dejavu/`. Run `python3 render.py` from any directory.
It draws all dots, pins, cards, icons and typography directly, then downsamples
from a double-resolution canvas for clean edges. `main.py` never imports Pillow
or runs the renderer. The included `entry.png` is the submission asset.

The image is 1024 × 1024 pixels, RGB PNG, below the 1 MiB limit. The code,
original text and illustration are supplied under the MIT license in LICENSE.
