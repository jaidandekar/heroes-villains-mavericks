# Character pack data for DC reading guides. No imports — valid Python 3.

DC_TYPES = {
    "main": "Main Continuity",
    "multiverse": "Multiverse",
    "elseworlds": "Elseworlds",
    "future": "Future",
    "alternate": "Alternate Reality",
}


def run_obj(slug, version_slug, title, creators, years, collects, era, prerequisites, summary, reading, asin, format_="Trade Paperback"):
    return {
        "slug": slug,
        "versionSlug": version_slug,
        "title": title,
        "creators": creators,
        "years": years,
        "collects": collects,
        "era": era,
        "prerequisites": prerequisites,
        "summary": summary,
        "readingOrder": [reading],
        "amazon": [{"asin": asin, "title": title, "format": format_, "recommended": True}],
    }


def version_obj(slug, name, universe, typ, first, tagline, description, wiki, runs):
    return {
        "slug": slug,
        "name": name,
        "universe": universe,
        "type": typ,
        "firstAppearance": first,
        "tagline": tagline,
        "description": description,
        "wikipedia": wiki,
        "runs": runs,
    }


def screen_item(id_, title, note, wiki, imdb, year=None, years=None):
    item = {"id": id_, "title": title, "note": note, "wikipedia": wiki, "imdb": imdb}
    if year is not None:
        item["year"] = year
    if years is not None:
        item["years"] = years
    return item


def pack_green_lantern():
    versions = [
        version_obj(
            "hal-jordan", "Hal Jordan", "Earth-0 / Prime Earth", "main",
            "Showcase #22 (1959)", "The greatest Green Lantern",
            "Test pilot Hal Jordan was chosen by a dying Abin Sur to wield a power ring of the Green Lantern Corps — willpower made into light.",
            "https://en.wikipedia.org/wiki/Hal_Jordan",
            ["gl-secret-origin", "gl-rebirth", "sinestro-corps-war", "blackest-night"],
        ),
        version_obj(
            "john-stewart", "John Stewart", "Earth-0 / Prime Earth", "main",
            "Green Lantern Vol. 2 #87 (1971)", "Architect of the Corps",
            "A former Marine and architect who became one of the most respected Green Lanterns — often Earth's primary ring-bearer in modern stories.",
            "https://en.wikipedia.org/wiki/John_Stewart_(character)",
            ["gl-mosaic", "gl-corps-recon"],
        ),
        version_obj(
            "guy-gardner", "Guy Gardner", "Earth-0 / Prime Earth", "main",
            "Green Lantern Vol. 2 #59 (1968)", "The Corps' blunt instrument",
            "Brash, abrasive, and fiercely loyal — Guy Gardner is the Lantern who says what everyone else is thinking.",
            "https://en.wikipedia.org/wiki/Guy_Gardner_(character)",
            ["guy-gardner-warrior"],
        ),
        version_obj(
            "kyle-rayner", "Kyle Rayner", "Earth-0 / Prime Earth", "main",
            "Green Lantern Vol. 3 #48 (1994)", "The Torchbearer",
            "When the Corps fell, freelance artist Kyle Rayner became the last Green Lantern — and later helped rebuild everything.",
            "https://en.wikipedia.org/wiki/Kyle_Rayner",
            ["emerald-knights", "gl-ion"],
        ),
        version_obj(
            "jessica-cruz", "Jessica Cruz", "Earth-0 / Prime Earth", "main",
            "Green Lantern Vol. 5 #20 (2013)", "The ring that chose fear — then courage",
            "Jessica Cruz overcame crippling anxiety to master a power ring, becoming a defining Lantern of the modern era.",
            "https://en.wikipedia.org/wiki/Jessica_Cruz",
            ["gl-rebirth-jessica"],
        ),
        version_obj(
            "alan-scott", "Alan Scott", "Earth-2", "multiverse",
            "All-American Comics #16 (1940)", "The Golden Age Green Lantern",
            "The original Green Lantern of Earth-2, empowered by the magic of the Starheart rather than a Corps battery.",
            "https://en.wikipedia.org/wiki/Alan_Scott",
            ["alan-scott-golden-age"],
        ),
        version_obj(
            "gl-earth-one", "Green Lantern: Earth One", "Earth One", "elseworlds",
            "Green Lantern: Earth One Vol. 1 (2018)", "A sci-fi reinvention",
            "Gabriel Hardman and Corinna Bechko's graphic novel reimagining of Hal's origin as cosmic first contact.",
            "https://en.wikipedia.org/wiki/Green_Lantern:_Earth_One",
            ["gl-earth-one-vol1"],
        ),
        version_obj(
            "parallax-hal", "Parallax (Hal Jordan)", "Earth-0", "alternate",
            "Green Lantern Vol. 3 #50 (1994)", "Willpower corrupted",
            "Possessed by fear entity Parallax, Hal Jordan destroyed the Corps in Emerald Twilight — a fall that reshaped the mythos.",
            "https://en.wikipedia.org/wiki/Parallax_(character)",
            ["emerald-twilight"],
        ),
    ]
    runs = {
        "gl-secret-origin": {
            **run_obj(
                "gl-secret-origin", "hal-jordan", "Green Lantern: Secret Origin",
                "Geoff Johns & Ivan Reis", "2008", "Green Lantern #29\u201335",
                "Modern Age", "None \u2014 ideal entry",
                "Geoff Johns retells Hal Jordan's origin and sets the stage for the modern Corps mythology.",
                "Green Lantern: Secret Origin", "1401221900",
            ),
            "isbn": "9781401221904",
        },
        "gl-rebirth": {
            **run_obj(
                "gl-rebirth", "hal-jordan", "Green Lantern: Rebirth",
                "Geoff Johns & Ethan Van Sciver", "2004\u201305", "Green Lantern: Rebirth #1\u20136",
                "Modern Age", "None",
                "Hal Jordan returns from the dead and reclaims the mantle that defined him.",
                "Green Lantern: Rebirth", "1401204615",
            ),
            "isbn": "9781401204617",
        },
        "sinestro-corps-war": {
            **run_obj(
                "sinestro-corps-war", "hal-jordan", "Green Lantern: The Sinestro Corps War",
                "Geoff Johns & others", "2007", "GL / GLC crossover",
                "Modern Age", "Green Lantern: Rebirth",
                "Sinestro builds an army fueled by fear to destroy the Green Lantern Corps.",
                "The Sinestro Corps War", "1401216503",
            ),
            "isbn": "9781401216504",
        },
        "blackest-night": {
            **run_obj(
                "blackest-night", "hal-jordan", "Blackest Night",
                "Geoff Johns & Ivan Reis", "2009\u201310", "Blackest Night #0\u20138",
                "Modern Age", "Sinestro Corps War",
                "The dead rise wearing black rings in the emotional-spectrum event that crowns Johns's Lantern era.",
                "Blackest Night", "1401228067",
            ),
            "isbn": "9781401228064",
        },
        "gl-mosaic": {
            **run_obj(
                "gl-mosaic", "john-stewart", "Green Lantern: Mosaic",
                "Gerard Jones & others", "1992\u201393", "Green Lantern: Mosaic #1\u201318 (select)",
                "Modern Age", "None",
                "John Stewart's surreal tenure as caretaker of a patchwork world \u2014 cult favorite character work.",
                "Green Lantern: Mosaic", "1401254567",
            ),
            "isbn": "9781401254568",
        },
        "gl-corps-recon": {
            **run_obj(
                "gl-corps-recon", "john-stewart", "Green Lantern Corps: Recharge",
                "Dave Gibbons & Patrick Gleason", "2005\u201306", "Green Lantern Corps: Recharge #1\u20135",
                "Modern Age", "Green Lantern: Rebirth",
                "The Corps rebuilds with John Stewart among its leaders.",
                "Green Lantern Corps: Recharge", "1401210120",
            ),
            "isbn": "9781401210120",
        },
        "guy-gardner-warrior": {
            **run_obj(
                "guy-gardner-warrior", "guy-gardner", "Guy Gardner: Warrior",
                "Beau Smith & others", "1994\u201396", "Guy Gardner: Warrior (select)",
                "Modern Age", "None",
                "Guy without a ring \u2014 still picking fights and somehow saving the day.",
                "Guy Gardner: Collateral Damage", "1401208907",
            ),
            "isbn": "9781401208905",
        },
        "emerald-knights": {
            **run_obj(
                "emerald-knights", "kyle-rayner", "Green Lantern: The Road Back",
                "Ron Marz & Darryl Banks", "1994", "Green Lantern #48\u201350",
                "Modern Age", "None",
                "Kyle Rayner inherits the last ring after Emerald Twilight.",
                "Green Lantern: The Road Back", "1563899999",
            ),
            "isbn": "9781563899997",
        },
        "gl-ion": {
            **run_obj(
                "gl-ion", "kyle-rayner", "Green Lantern: Ion",
                "Ron Marz & others", "2006", "Ion / GL specials",
                "Modern Age", "None",
                "Kyle ascends to Ion, the living embodiment of willpower.",
                "Green Lantern: Ion", "1401215043",
            ),
            "isbn": "9781401215040",
        },
        "gl-rebirth-jessica": {
            **run_obj(
                "gl-rebirth-jessica", "jessica-cruz", "Green Lanterns: Rage Planet",
                "Sam Humphries & Robson Rocha", "2016", "Green Lanterns #1\u20136",
                "Rebirth", "None",
                "Jessica Cruz and Simon Baz share Earth duty in the Rebirth era.",
                "Green Lanterns Vol. 1: Rage Planet", "1401267722",
            ),
            "isbn": "9781401267728",
        },
        "alan-scott-golden-age": {
            **run_obj(
                "alan-scott-golden-age", "alan-scott", "All-Star Comics: Golden Age Green Lantern",
                "Bill Finger & Martin Nodell", "1940s", "Golden Age reprints",
                "Golden Age", "None",
                "The magic-ring adventures that started the Green Lantern legacy.",
                "Golden Age Green Lantern Archives", "1563895079",
            ),
            "isbn": "9781563895074",
        },
        "gl-earth-one-vol1": {
            **run_obj(
                "gl-earth-one-vol1", "gl-earth-one", "Green Lantern: Earth One Vol. 1",
                "Gabriel Hardman & Corinna Bechko", "2018", "Graphic novel",
                "Earth One", "None",
                "A grounded, cinematic reinvention of Hal's first contact with the Corps.",
                "Green Lantern: Earth One Vol. 1", "1401241858",
            ),
            "isbn": "9781401241852",
        },
        "emerald-twilight": {
            **run_obj(
                "emerald-twilight", "parallax-hal", "Green Lantern: Emerald Twilight",
                "Ron Marz & Bill Willingham", "1994", "Green Lantern #48\u201350",
                "Modern Age", "None",
                "Hal Jordan's catastrophic fall that ends the classic Corps era.",
                "Emerald Twilight / New Dawn", "1401207860",
            ),
            "isbn": "9781401207861",
        },
    }
    return {
        "id": "green-lantern",
        "brand": "Green Lantern",
        "title": "Green Lantern \u2014 Willpower Across the Multiverse",
        "nav_who": "Who is Green Lantern",
        "nav_verses": "Corps & Verses",
        "who_id": "who-is-green-lantern",
        "header_img": "green-lantern-homepage-header-image.jpg",
        "hero_gradient": "radial-gradient(circle at 30% 25%, #2db84b, #0d5c28 45%, #041208)",
        "verses_h2": "Green Lantern Across the Multiverse",
        "verses_p": "versions across DC's emotional spectrum \u2014 Earth-0, Earth-2, Elseworlds, and every ring-bearer worth knowing.",
        "comics_p": "Essential Green Lantern stories \u2014 from Secret Origin and Rebirth to Sinestro Corps War and Blackest Night.",
        "screen_p": "Live-action and animated appearances \u2014 from the 2011 film and Justice League to the Emerald Knights animated features.",
        "types": DC_TYPES,
        "versions": versions,
        "runs": runs,
        "home_runs": [
            "gl-secret-origin", "gl-rebirth", "sinestro-corps-war", "blackest-night",
            "emerald-twilight", "gl-earth-one-vol1", "gl-rebirth-jessica", "gl-corps-recon",
            "emerald-knights", "gl-ion",
        ],
        "profile": {
            "wikipedia": "https://en.wikipedia.org/wiki/Green_Lantern",
            "lead": "In brightest day, in blackest night \u2014 willpower forged into a weapon of light.",
            "summary": "Green Lantern is the shared mantle of intergalactic peacekeepers wielding power rings fueled by will. Earth's most famous Lantern, Hal Jordan, debuted in Showcase #22 (1959), created by John Broome and Gil Kane. The mythos expanded into a cosmic Corps, an emotional spectrum of rival lanterns, and a roster of human ring-bearers from John Stewart to Jessica Cruz.",
            "facts": [
                {"label": "Notable bearers", "value": "Hal Jordan, John Stewart, Kyle Rayner"},
                {"label": "First appearance", "value": "All-American Comics #16 (1940) / Showcase #22 (1959)"},
                {"label": "Created by", "value": "Bill Finger & Martin Nodell; Broome & Kane"},
                {"label": "Publisher", "value": "DC Comics"},
                {"label": "Base of operations", "value": "Oa / Sector 2814 (Earth)"},
                {"label": "Allies", "value": "Green Lantern Corps, Justice League"},
                {"label": "Notable foes", "value": "Sinestro, Parallax, Atrocitus"},
                {"label": "Powers", "value": "Hard-light constructs powered by will"},
            ],
        },
        "screen": [
            {
                "group": "Live-action films",
                "items": [
                    screen_item("gl-2011", "Green Lantern", "Ryan Reynolds as Hal Jordan", "https://en.wikipedia.org/wiki/Green_Lantern_(film)", "https://www.imdb.com/title/tt1133985/", year="2011"),
                    screen_item("jl-2017-gl", "Justice League", "Cameo constructs; Snyder Cut expanded", "https://en.wikipedia.org/wiki/Justice_League_(film)", "https://www.imdb.com/title/tt0974015/", year="2017"),
                ],
            },
            {
                "group": "Animated films",
                "items": [
                    screen_item("gl-first-flight", "Green Lantern: First Flight", "Origin animated feature", "https://en.wikipedia.org/wiki/Green_Lantern:_First_Flight", "https://www.imdb.com/title/tt1389096/", year="2009"),
                    screen_item("gl-emerald-knights", "Green Lantern: Emerald Knights", "Corps anthology", "https://en.wikipedia.org/wiki/Green_Lantern:_Emerald_Knights", "https://www.imdb.com/title/tt1682778/", year="2011"),
                ],
            },
            {
                "group": "Animated television",
                "items": [
                    screen_item("gltas", "Green Lantern: The Animated Series", "CGI \u00b7 Cartoon Network", "https://en.wikipedia.org/wiki/Green_Lantern:_The_Animated_Series", "https://www.imdb.com/title/tt1649913/", years="2011\u20132013"),
                    screen_item("jl-unlimited-gl", "Justice League Unlimited", "John Stewart era", "https://en.wikipedia.org/wiki/Justice_League_Unlimited", "https://www.imdb.com/title/tt0402022/", years="2004\u20132006"),
                ],
            },
        ],
        "themes": {
            "hal-jordan": (8, 48, 24),
            "john-stewart": (12, 40, 28),
            "guy-gardner": (20, 52, 18),
            "kyle-rayner": (10, 36, 40),
            "jessica-cruz": (16, 44, 32),
            "alan-scott": (40, 36, 12),
            "gl-earth-one": (6, 28, 22),
            "parallax-hal": (36, 28, 8),
        },
        "issues": {
            "gl-rebirth": [
                {"id": "GL: Rebirth #1", "title": "Blackest Night"},
                {"id": "#2", "title": "Part Two"},
                {"id": "#3", "title": "Part Three"},
                {"id": "#4", "title": "Part Four"},
                {"id": "#5", "title": "Part Five"},
                {"id": "#6", "title": "Part Six"},
            ],
        },
    }


def pack_flash():
    versions = [
        version_obj(
            "barry-allen", "Barry Allen", "Earth-0 / Prime Earth", "main",
            "Showcase #4 (1956)", "The Fastest Man Alive",
            "Forensic scientist Barry Allen was struck by lightning and bathed in chemicals, becoming the Scarlet Speedster who anchors the modern Flash mythos.",
            "https://en.wikipedia.org/wiki/Barry_Allen",
            ["flash-rebirth", "flash-new52", "flash-robertson"],
        ),
        version_obj(
            "wally-west", "Wally West", "Earth-0 / Prime Earth", "main",
            "The Flash Vol. 1 #110 (1959)", "Kid Flash who grew up",
            "Barry's nephew and sidekick became the fan-favorite Flash of the 1990s \u2014 the hero who made the Speed Force personal.",
            "https://en.wikipedia.org/wiki/Wally_West",
            ["flash-v2-mark-waid", "flash-return-barry"],
        ),
        version_obj(
            "jay-garrick", "Jay Garrick", "Earth-0 / Earth-2", "multiverse",
            "Flash Comics #1 (1940)", "The Golden Age Flash",
            "The original Flash of the Golden Age \u2014 a college student who gained super-speed from hard-water fumes and a winged helmet.",
            "https://en.wikipedia.org/wiki/Jay_Garrick",
            ["flash-golden-age", "flash-earth2"],
        ),
        version_obj(
            "bart-allen", "Bart Allen / Impulse", "Earth-0 / Prime Earth", "main",
            "The Flash Vol. 2 #92 (1994)", "Chaos in sneakers",
            "Barry Allen's time-lost grandson who raced through adolescence as Impulse before inheriting the Flash mantle.",
            "https://en.wikipedia.org/wiki/Bart_Allen",
            ["impulse-young-justice", "flash-bart-tenure"],
        ),
        version_obj(
            "flashpoint-barry", "Flashpoint Barry Allen", "Flashpoint Timeline", "elseworlds",
            "Flashpoint #1 (2011)", "One changed moment",
            "Barry's attempt to save his mother rewrote history \u2014 spawning a darker DC universe and the New 52 reboot.",
            "https://en.wikipedia.org/wiki/Flashpoint_(comics)",
            ["flashpoint-event"],
        ),
        version_obj(
            "future-flash", "Future Flash (Barry Allen)", "Near-future Earth-0", "future",
            "The Flash Vol. 4 #19 (2013)", "Tomorrow's tragedy",
            "A broken Barry Allen from a future where the Speed Force consumed everything \u2014 a warning made flesh.",
            "https://en.wikipedia.org/wiki/Flash_(Barry_Allen)",
            ["flash-future-arc"],
        ),
        version_obj(
            "john-fox", "John Fox", "21st Century / 27th Century", "future",
            "The Flash Vol. 2 #105 (1995)", "The Flash of two centuries",
            "A historian from the 27th century who briefly wore the ring when Wally vanished \u2014 a cult favorite one-shot hero.",
            "https://en.wikipedia.org/wiki/John_Fox_(character)",
            ["flash-john-fox"],
        ),
        version_obj(
            "max-mercury", "Max Mercury", "Earth-0", "main",
            "National Comics #5 (1940)", "Zen master of speed",
            "The elder statesman of speedsters who mentored Wally and Bart through the mysteries of the Speed Force.",
            "https://en.wikipedia.org/wiki/Max_Mercury",
            ["flash-speed-force"],
        ),
    ]
    runs = {
        "flash-rebirth": {
            **run_obj(
                "flash-rebirth", "barry-allen", "The Flash: Rebirth",
                "Geoff Johns & Ethan Van Sciver", "2009\u201310", "The Flash: Rebirth #1\u20136",
                "Modern Age", "None",
                "Barry Allen returns to the DC Universe and confronts the Speed Force mystery that defines his second life.",
                "The Flash: Rebirth", "1401226796",
            ),
            "isbn": "9781401226794",
        },
        "flash-new52": {
            **run_obj(
                "flash-new52", "barry-allen", "The Flash Vol. 1: Move Forward",
                "Francis Manapul & Brian Buccellato", "2011\u201312", "The Flash (2011) #0\u20138",
                "New 52", "Flashpoint (optional)",
                "Barry's New 52 relaunch blends crime-lab drama with cosmic Speed Force horror.",
                "The Flash Vol. 1: Move Forward", "1401235540",
            ),
            "isbn": "9781401235543",
        },
        "flash-robertson": {
            **run_obj(
                "flash-robertson", "barry-allen", "The Flash by Mark Waid Book One",
                "Mark Waid & Mike Wieringo", "2000", "The Flash (1987) #0, #62\u201368",
                "Modern Age", "None",
                "Waid's beloved run on Barry-era legacy through Wally \u2014 included here as essential Speed Force lore.",
                "The Flash by Mark Waid Book One", "1401273841",
            ),
            "isbn": "9781401273842",
        },
        "flash-v2-mark-waid": {
            **run_obj(
                "flash-v2-mark-waid", "wally-west", "The Flash: Born to Run",
                "Mark Waid & others", "1991\u201392", "The Flash Vol. 2 #62\u201365, Annual #8",
                "Modern Age", "None",
                "Wally West's definitive origin and the story that made him the Flash for a generation.",
                "The Flash: Born to Run", "1563891394",
            ),
            "isbn": "9781563891397",
        },
        "flash-return-barry": {
            **run_obj(
                "flash-return-barry", "wally-west", "The Flash: The Return of Barry Allen",
                "Mark Waid & Paul Ryan", "1994", "The Flash Vol. 2 #74\u201379",
                "Modern Age", "Born to Run",
                "Barry Allen seemingly returns from the dead \u2014 and Wally must prove he earned the mantle.",
                "The Flash: The Return of Barry Allen", "1563892684",
            ),
            "isbn": "9781563892684",
        },
        "flash-golden-age": {
            **run_obj(
                "flash-golden-age", "jay-garrick", "The Golden Age Flash Archives Vol. 1",
                "Gardner Fox & Harry Lampert", "1940s", "Flash Comics #1\u201317",
                "Golden Age", "None",
                "Jay Garrick's earliest adventures \u2014 the birth of super-speed in comics.",
                "The Golden Age Flash Archives Vol. 1", "1563896353",
            ),
            "isbn": "9781563896354",
        },
        "flash-earth2": {
            **run_obj(
                "flash-earth2", "jay-garrick", "Earth 2: World's End",
                "Tom Taylor & Nicola Scott", "2014\u201315", "Earth 2: World's End #0\u201316",
                "New 52", "Earth 2 (2012)",
                "Jay Garrick on the rebuilt Earth-2 \u2014 a veteran speedster in a dying world.",
                "Earth 2: World's End Vol. 1", "1401254192",
            ),
            "isbn": "9781401254195",
        },
        "impulse-young-justice": {
            **run_obj(
                "impulse-young-justice", "bart-allen", "Young Justice Book One",
                "Peter David & Todd Nauck", "1998\u201399", "Young Justice #1\u20137",
                "Modern Age", "None",
                "Impulse teams with Robin and Superboy before graduating to the Flash family.",
                "Young Justice Book One", "1401274750",
            ),
            "isbn": "9781401274759",
        },
        "flash-bart-tenure": {
            **run_obj(
                "flash-bart-tenure", "bart-allen", "The Flash: The Fastest Man Alive",
                "Danny Bilson & Paul DeMeo", "2006\u201307", "The Flash: The Fastest Man Alive #1\u201313",
                "Modern Age", "None",
                "Bart Allen's brief but memorable run as the Flash before Flashpoint.",
                "The Flash: The Fastest Man Alive Vol. 1", "1401214896",
            ),
            "isbn": "9781401214896",
        },
        "flashpoint-event": {
            **run_obj(
                "flashpoint-event", "flashpoint-barry", "Flashpoint",
                "Geoff Johns & Andy Kubert", "2011", "Flashpoint #1\u20135",
                "Modern Age", "The Flash: Rebirth",
                "Barry wakes in a world without heroes \u2014 Thomas Wayne is Batman and Wonder Woman and Aquaman wage war.",
                "Flashpoint", "1401232368",
            ),
            "isbn": "9781401232368",
        },
        "flash-future-arc": {
            **run_obj(
                "flash-future-arc", "future-flash", "The Flash Vol. 4: Reverse",
                "Brian Buccellato & Francis Manapul", "2013\u201314", "The Flash (2011) #19\u201325, Annual #1",
                "New 52", "Move Forward",
                "Barry meets his future self and uncovers the tragedy that breaks the Flash.",
                "The Flash Vol. 4: Reverse", "1401242762",
            ),
            "isbn": "9781401242763",
        },
        "flash-john-fox": {
            **run_obj(
                "flash-john-fox", "john-fox", "The Flash: Future Flash",
                "Mark Waid & Paul Ryan", "1995", "The Flash Vol. 2 #105\u2013106",
                "Modern Age", "None",
                "John Fox arrives from the 27th century to fill the void when Wally disappears.",
                "The Flash: Future Flash", "1563893120",
            ),
            "isbn": "9781563893124",
        },
        "flash-speed-force": {
            **run_obj(
                "flash-speed-force", "max-mercury", "The Flash: Dead Heat",
                "Mark Waid & Paul Ryan", "2000", "The Flash Vol. 2 #108\u2013111",
                "Modern Age", "Born to Run",
                "Max Mercury and the Flash family confront Savitar and the secrets of the Speed Force.",
                "The Flash: Dead Heat", "1563896235",
            ),
            "isbn": "9781563896231",
        },
    }
    return {
        "id": "flash",
        "brand": "The Flash",
        "title": "The Flash \u2014 Speed Force Across the Multiverse",
        "nav_who": "Who is The Flash",
        "nav_verses": "Speed Force",
        "who_id": "who-is-the-flash",
        "header_img": "flash-homepage-header-image.jpg",
        "hero_gradient": "radial-gradient(circle at 30% 25%, #ff3b2f, #8a1008 45%, #1a0505)",
        "verses_h2": "The Flash Across the Multiverse",
        "verses_p": "versions across DC's speedster family \u2014 Barry, Wally, Jay, Bart, and every timeline the Speed Force touches.",
        "comics_p": "Essential Flash stories \u2014 from Born to Run and Rebirth to Flashpoint and the modern Speed Force sagas.",
        "screen_p": "Live-action and animated appearances \u2014 from the CW's Arrowverse to Justice League and classic animated series.",
        "types": DC_TYPES,
        "versions": versions,
        "runs": runs,
        "home_runs": [
            "flash-rebirth", "flash-v2-mark-waid", "flashpoint-event", "flash-return-barry",
            "flash-new52", "flash-golden-age", "impulse-young-justice", "flash-speed-force",
            "flash-future-arc", "flash-bart-tenure",
        ],
        "profile": {
            "wikipedia": "https://en.wikipedia.org/wiki/Flash_(DC_Comics_character)",
            "lead": "Faster than light, bound to the Speed Force \u2014 the hero who outruns death itself.",
            "summary": "The Flash is DC's premier speedster mantle, most famously held by Barry Allen since Showcase #4 (1956). Created by Robert Kanigher, John Broome, and Carmine Infantino, the Flash mythos grew through Wally West, Jay Garrick, and Bart Allen into a family tied to the cosmic Speed Force. Barry's Flashpoint rewrote the DC Universe; Wally's 1990s run defined a generation.",
            "facts": [
                {"label": "Notable bearers", "value": "Barry Allen, Wally West, Jay Garrick"},
                {"label": "First appearance", "value": "Flash Comics #1 (1940) / Showcase #4 (1956)"},
                {"label": "Created by", "value": "Gardner Fox & Harry Lampert; Broome & Infantino"},
                {"label": "Publisher", "value": "DC Comics"},
                {"label": "Base of operations", "value": "Central City / Keystone City"},
                {"label": "Allies", "value": "Justice League, Titans, Flash family"},
                {"label": "Notable foes", "value": "Reverse-Flash, Zoom, Gorilla Grodd"},
                {"label": "Powers", "value": "Super-speed, Speed Force energy, time travel"},
            ],
        },
        "screen": [
            {
                "group": "Live-action films",
                "items": [
                    screen_item("flash-2023", "The Flash", "Ezra Miller as Barry Allen", "https://en.wikipedia.org/wiki/The_Flash_(film)", "https://www.imdb.com/title/tt0439572/", year="2023"),
                    screen_item("jl-flash", "Justice League", "Barry Allen joins the League", "https://en.wikipedia.org/wiki/Justice_League_(film)", "https://www.imdb.com/title/tt0974015/", year="2017"),
                ],
            },
            {
                "group": "Live-action television",
                "items": [
                    screen_item("flash-cw", "The Flash", "Grant Gustin \u00b7 Arrowverse", "https://en.wikipedia.org/wiki/The_Flash_(2014_TV_series)", "https://www.imdb.com/title/tt3107288/", years="2014\u20132023"),
                    screen_item("flash-1990", "The Flash", "John Wesley Shipp \u00b7 CBS", "https://en.wikipedia.org/wiki/The_Flash_(1990_TV_series)", "https://www.imdb.com/title/tt0098791/", years="1990\u20131991"),
                ],
            },
            {
                "group": "Animated",
                "items": [
                    screen_item("jla-flash", "Justice League / Unlimited", "Michael Rosenbaum as Wally West", "https://en.wikipedia.org/wiki/Justice_League_(TV_series)", "https://www.imdb.com/title/tt0275137/", years="2001\u20132006"),
                    screen_item("flash-paradox", "Justice League: The Flashpoint Paradox", "Animated Flashpoint adaptation", "https://en.wikipedia.org/wiki/Justice_League:_The_Flashpoint_Paradox", "https://www.imdb.com/title/tt2820460/", year="2013"),
                ],
            },
        ],
        "themes": {
            "barry-allen": (255, 59, 47),
            "wally-west": (220, 40, 30),
            "jay-garrick": (180, 50, 35),
            "bart-allen": (255, 120, 40),
            "flashpoint-barry": (140, 20, 15),
            "future-flash": (100, 30, 25),
            "john-fox": (60, 80, 140),
            "max-mercury": (90, 70, 50),
        },
        "issues": {
            "flashpoint-event": [
                {"id": "Flashpoint #1", "title": "Flashpoint"},
                {"id": "#2", "title": "Flashpoint"},
                {"id": "#3", "title": "Flashpoint"},
                {"id": "#4", "title": "Flashpoint"},
                {"id": "#5", "title": "Flashpoint"},
            ],
        },
    }


def pack_superman():
    versions = [
        version_obj(
            "superman-prime", "Superman (Clark Kent)", "Earth-0 / Prime Earth", "main",
            "Action Comics #1 (1938)", "The Man of Steel",
            "Kal-El of Krypton, raised in Smallville as Clark Kent \u2014 the original superhero and blueprint for the DC Universe.",
            "https://en.wikipedia.org/wiki/Superman",
            ["superman-birthright", "superman-all-star", "superman-red-blue"],
        ),
        version_obj(
            "kingdom-come-superman", "Kingdom Come Superman", "Earth-22", "elseworlds",
            "Kingdom Come #1 (1996)", "The weary god among men",
            "An older Superman who retired after Magog's world of violent heroes \u2014 until he must lead again.",
            "https://en.wikipedia.org/wiki/Kingdom_Come_(comics)",
            ["kingdom-come"],
        ),
        version_obj(
            "red-son-superman", "Red Son Superman", "Earth-30", "elseworlds",
            "Superman: Red Son #1 (2003)", "What if he landed in the USSR?",
            "Kal-El's rocket lands in Soviet Ukraine instead of Kansas \u2014 a global superpower built on communist ideals.",
            "https://en.wikipedia.org/wiki/Superman:_Red_Son",
            ["superman-red-son"],
        ),
        version_obj(
            "all-star-superman", "All-Star Superman", "All-Star Universe", "elseworlds",
            "All-Star Superman #1 (2006)", "Twelve labors of legend",
            "Grant Morrison and Frank Quitely's definitive love letter \u2014 Superman facing mortality with mythic grace.",
            "https://en.wikipedia.org/wiki/All-Star_Superman",
            ["all-star-superman-run"],
        ),
        version_obj(
            "superman-earth2", "Superman (Earth-2)", "Earth-2", "multiverse",
            "Action Comics #1 (1938)", "The Golden Age Man of Tomorrow",
            "The original Superman of Earth-2 who aged, married Lois Lane, and died saving the multiverse in Crisis on Infinite Earths.",
            "https://en.wikipedia.org/wiki/Superman_(Earth-Two)",
            ["superman-earth2-golden"],
        ),
        version_obj(
            "absolute-superman", "Absolute Superman", "Absolute Universe", "alternate",
            "Absolute Superman #1 (2024)", "A harsher origin reimagined",
            "DC's Absolute line reimagines Kal-El as a working-class hero forged by a harder, more grounded Kryptonian exile.",
            "https://en.wikipedia.org/wiki/Absolute_Superman",
            ["absolute-superman-vol1"],
        ),
        version_obj(
            "superman-new52", "Superman (New 52)", "Earth-0 (New 52)", "main",
            "Action Comics Vol. 2 #1 (2011)", "Jeans and cape",
            "The post-Flashpoint Superman \u2014 younger, brasher, and still learning what the S-shield means.",
            "https://en.wikipedia.org/wiki/The_New_52",
            ["superman-new52-action"],
        ),
        version_obj(
            "superboy-prime", "Superboy-Prime", "Earth-Prime", "alternate",
            "DC Comics Presents #87 (1985)", "The fan who broke the world",
            "A Superman from a world where heroes were fiction \u2014 driven mad by loss and cosmic power during Infinite Crisis.",
            "https://en.wikipedia.org/wiki/Superboy-Prime",
            ["infinite-crisis"],
        ),
    ]
    runs = {
        "superman-birthright": {
            **run_obj(
                "superman-birthright", "superman-prime", "Superman: Birthright",
                "Mark Waid & Leinil Francis Yu", "2003\u201304", "Superman: Birthright #1\u201312",
                "Modern Age", "None",
                "A grounded, widescreen retelling of Clark Kent's path from Smallville to Metropolis.",
                "Superman: Birthright", "1401202545",
            ),
            "isbn": "9781401202545",
        },
        "superman-all-star": {
            **run_obj(
                "superman-all-star", "superman-prime", "Superman: Up, Up and Away!",
                "Geoff Johns & Kurt Busiek", "2006", "Superman #650\u2013653, Action #840\u2013841",
                "Modern Age", "None",
                "Clark lives without powers and rediscovers why he became Superman.",
                "Superman: Up, Up and Away!", "1401213396",
            ),
            "isbn": "9781401213398",
        },
        "superman-red-blue": {
            **run_obj(
                "superman-red-blue", "superman-prime", "Superman: Red & Blue",
                "Various", "2021", "Superman: Red & Blue #1\u20136",
                "Infinite Frontier", "None",
                "Anthology celebrating Superman's legacy through all-star creative teams.",
                "Superman: Red & Blue", "1779500510",
            ),
            "isbn": "9781779500514",
        },
        "kingdom-come": {
            **run_obj(
                "kingdom-come", "kingdom-come-superman", "Kingdom Come",
                "Mark Waid & Alex Ross", "1996\u201397", "Kingdom Come #1\u20134",
                "Modern Age", "None",
                "Painted masterpiece of a world where heroes and villains blur and Superman must restore hope.",
                "Kingdom Come", "1563893304",
            ),
            "isbn": "9781563893309",
        },
        "superman-red-son": {
            **run_obj(
                "superman-red-son", "red-son-superman", "Superman: Red Son",
                "Mark Millar & Dave Johnson", "2003", "Superman: Red Son #1\u20133",
                "Modern Age", "None",
                "The Soviet Superman epic that asks whether truth and justice survive any political system.",
                "Superman: Red Son", "1401201913",
            ),
            "isbn": "9781401201913",
        },
        "all-star-superman-run": {
            **run_obj(
                "all-star-superman-run", "all-star-superman", "All-Star Superman",
                "Grant Morrison & Frank Quitely", "2006\u201308", "All-Star Superman #1\u201312",
                "Modern Age", "None",
                "Superman's final adventures \u2014 poetic, playful, and universally acclaimed.",
                "All-Star Superman", "1401213329",
            ),
            "isbn": "9781401213320",
        },
        "superman-earth2-golden": {
            **run_obj(
                "superman-earth2-golden", "superman-earth2", "Superman: The Golden Age Vol. 1",
                "Jerry Siegel & Joe Shuster", "1930s\u201340s", "Action Comics #1\u2013 (select)",
                "Golden Age", "None",
                "The earliest adventures of the Man of Steel \u2014 including the debut that invented superheroes.",
                "Superman: The Golden Age Vol. 1", "1401241890",
            ),
            "isbn": "9781401241897",
        },
        "absolute-superman-vol1": {
            **run_obj(
                "absolute-superman-vol1", "absolute-superman", "Absolute Superman Vol. 1",
                "Jason Aaron & Rafa Sandoval", "2024\u201325", "Absolute Superman #1\u20136",
                "Absolute", "None",
                "A bold reimagining of Superman's origin in DC's Absolute Universe.",
                "Absolute Superman Vol. 1", "1779523456",
            ),
            "isbn": "9781779523452",
        },
        "superman-new52-action": {
            **run_obj(
                "superman-new52-action", "superman-new52", "Superman: Action Comics Vol. 1",
                "Grant Morrison & Rags Morales", "2011\u201312", "Action Comics Vol. 2 #1\u20138",
                "New 52", "Flashpoint (optional)",
                "Grant Morrison reboots Superman's early days with punk-rock Kryptonian action.",
                "Superman: Action Comics Vol. 1", "1401235460",
            ),
            "isbn": "9781401235468",
        },
        "infinite-crisis": {
            **run_obj(
                "infinite-crisis", "superboy-prime", "Infinite Crisis",
                "Geoff Johns & Phil Jimenez", "2005\u201306", "Infinite Crisis #1\u20137",
                "Modern Age", "Crisis on Infinite Earths (optional)",
                "Multiversal war where Superboy-Prime shatters worlds to restore his lost Earth.",
                "Infinite Crisis", "1401209305",
            ),
            "isbn": "9781401209308",
        },
        "superman-daily-planet": {
            **run_obj(
                "superman-daily-planet", "superman-prime", "Superman: Lois and Clark",
                "Dan Jurgens & others", "1993", "Superman: The Man of Steel #19\u201320",
                "Modern Age", "Death of Superman",
                "Clark and Lois's relationship deepens after the return from the grave.",
                "Superman: The Death and Return of Superman", "1563890951",
            ),
            "isbn": "9781563890958",
        },
        "superman-smoke-mirror": {
            **run_obj(
                "superman-smoke-mirror", "superman-prime", "Superman: For All Seasons",
                "Jeph Loeb & Tim Sale", "1998\u201399", "Superman: For All Seasons #1\u20134",
                "Modern Age", "None",
                "Four seasons of Superman's life told through the eyes of those who love him.",
                "Superman: For All Seasons", "1563894191",
            ),
            "isbn": "9781563894192",
        },
    }
    return {
        "id": "superman",
        "brand": "Superman",
        "title": "Superman \u2014 Truth and Justice Across the Multiverse",
        "nav_who": "Who is Superman",
        "nav_verses": "Multiverse",
        "who_id": "who-is-superman",
        "header_img": "superman-homepage-header-image.jpg",
        "hero_gradient": "radial-gradient(circle at 30% 25%, #0066ff, #003399 45%, #001133)",
        "verses_h2": "Superman Across the Multiverse",
        "verses_p": "versions across every Earth and Elseworld \u2014 from Action Comics #1 to Red Son, Kingdom Come, and Absolute.",
        "comics_p": "Essential Superman stories \u2014 from Birthright and All-Star Superman to Red Son and Kingdom Come.",
        "screen_p": "Live-action and animated appearances \u2014 from Christopher Reeve to Henry Cavill, Smallville, and My Adventures with Superman.",
        "types": DC_TYPES,
        "versions": versions,
        "runs": runs,
        "home_runs": [
            "superman-birthright", "all-star-superman-run", "kingdom-come", "superman-red-son",
            "superman-new52-action", "infinite-crisis", "superman-smoke-mirror", "superman-earth2-golden",
            "absolute-superman-vol1", "superman-daily-planet",
        ],
        "profile": {
            "wikipedia": "https://en.wikipedia.org/wiki/Superman",
            "lead": "Look up in the sky \u2014 hope made flesh, the hero who started it all.",
            "summary": "Superman is Kal-El of Krypton, sent to Earth as an infant and raised as Clark Kent of Smallville. Created by Jerry Siegel and Joe Shuster in Action Comics #1 (1938), he is the archetype of the superhero. His stories span cosmic epics, intimate human drama, and Elseworlds that reimagine his symbol across the multiverse.",
            "facts": [
                {"label": "Alter ego", "value": "Clark Kent / Kal-El"},
                {"label": "First appearance", "value": "Action Comics #1 (1938)"},
                {"label": "Created by", "value": "Jerry Siegel & Joe Shuster"},
                {"label": "Publisher", "value": "DC Comics"},
                {"label": "Base of operations", "value": "Metropolis / Fortress of Solitude"},
                {"label": "Allies", "value": "Justice League, Super-family, Lois Lane"},
                {"label": "Notable foes", "value": "Lex Luthor, Brainiac, Doomsday, Zod"},
                {"label": "Powers", "value": "Flight, strength, heat vision, freeze breath"},
            ],
        },
        "screen": [
            {
                "group": "Live-action films",
                "items": [
                    screen_item("superman-1978", "Superman", "Christopher Reeve \u00b7 Richard Donner", "https://en.wikipedia.org/wiki/Superman_(1978_film)", "https://www.imdb.com/title/tt0078346/", year="1978"),
                    screen_item("superman-man-steel", "Man of Steel", "Henry Cavill \u00b7 Zack Snyder", "https://en.wikipedia.org/wiki/Man_of_Steel_(film)", "https://www.imdb.com/title/tt0770828/", year="2013"),
                    screen_item("superman-2025", "Superman", "James Gunn DCU reboot", "https://en.wikipedia.org/wiki/Superman_(2025_film)", "https://www.imdb.com/title/tt5950044/", year="2025"),
                ],
            },
            {
                "group": "Live-action television",
                "items": [
                    screen_item("smallville", "Smallville", "Tom Welling as young Clark Kent", "https://en.wikipedia.org/wiki/Smallville", "https://www.imdb.com/title/tt0279600/", years="2001\u20132011"),
                    screen_item("lois-clark", "Lois & Clark: The New Adventures of Superman", "Dean Cain & Teri Hatcher", "https://en.wikipedia.org/wiki/Lois_%26_Clark:_The_New_Adventures_of_Superman", "https://www.imdb.com/title/tt0106057/", years="1993\u20131997"),
                ],
            },
            {
                "group": "Animated",
                "items": [
                    screen_item("superman-tas", "Superman: The Animated Series", "Bruce Timm \u00b7 DCAU", "https://en.wikipedia.org/wiki/Superman:_The_Animated_Series", "https://www.imdb.com/title/tt0114814/", years="1996\u20132000"),
                    screen_item("my-adventures-superman", "My Adventures with Superman", "Young Clark at the Daily Planet", "https://en.wikipedia.org/wiki/My_Adventures_with_Superman", "https://www.imdb.com/title/tt21059136/", years="2023\u20132024"),
                ],
            },
        ],
        "themes": {
            "superman-prime": (0, 102, 255),
            "kingdom-come-superman": (180, 160, 120),
            "red-son-superman": (180, 30, 30),
            "all-star-superman": (255, 220, 60),
            "superman-earth2": (60, 80, 140),
            "absolute-superman": (40, 60, 100),
            "superman-new52": (0, 80, 200),
            "superboy-prime": (200, 200, 220),
        },
        "issues": {
            "all-star-superman-run": [
                {"id": "All-Star Superman #1", "title": "Superman and the Sun"},
                {"id": "#2", "title": "Superman's Secret Room"},
                {"id": "#3", "title": "Sweet Dreams, Superwoman"},
                {"id": "#4", "title": "The Superman Squad"},
                {"id": "#5", "title": "The Gospel According to Lex Luthor"},
            ],
        },
    }


def pack_wonder_woman():
    versions = [
        version_obj(
            "diana-prime", "Wonder Woman (Diana Prince)", "Earth-0 / Prime Earth", "main",
            "All Star Comics #8 (1941)", "Ambassador of peace",
            "Diana of Themyscira, princess of the Amazons \u2014 sent to Man's World as an emissary of truth, compassion, and unstoppable force.",
            "https://en.wikipedia.org/wiki/Wonder_Woman",
            ["ww-george-perez", "ww-rebirth", "ww-greg-ruka"],
        ),
        version_obj(
            "ww-earth2", "Wonder Woman (Earth-2)", "Earth-2", "multiverse",
            "All Star Comics #8 (1941)", "Golden Age Amazon",
            "The original Wonder Woman of Earth-2 who fought through World War II and married Steve Trevor in the Golden Age tradition.",
            "https://en.wikipedia.org/wiki/Wonder_Woman_(Earth-Two)",
            ["ww-golden-age"],
        ),
        version_obj(
            "ww-new52", "Wonder Woman (New 52)", "Earth-0 (New 52)", "main",
            "Wonder Woman Vol. 4 #1 (2011)", "Daughter of Zeus",
            "Brian Azzarello's Wonder Woman reimagined as Greek-myth epic \u2014 demigod, warrior, and reluctant god.",
            "https://en.wikipedia.org/wiki/Wonder_Woman_(comic_book)",
            ["ww-azzarello-vol1"],
        ),
        version_obj(
            "kingdom-come-ww", "Kingdom Come Wonder Woman", "Earth-22", "elseworlds",
            "Kingdom Come #1 (1996)", "The warrior queen",
            "An armored, battle-hardened Diana who leads the Amazons after Man's World failed.",
            "https://en.wikipedia.org/wiki/Kingdom_Come_(comics)",
            ["kingdom-come"],
        ),
        version_obj(
            "flashpoint-ww", "Flashpoint Wonder Woman", "Flashpoint Timeline", "elseworlds",
            "Flashpoint #1 (2011)", "Empress of war",
            "In Flashpoint, Diana and Aquaman's alliance shattered the world \u2014 a darker Amazon at the center of global catastrophe.",
            "https://en.wikipedia.org/wiki/Flashpoint_(comics)",
            ["flashpoint-event"],
        ),
        version_obj(
            "absolute-wonder-woman", "Absolute Wonder Woman", "Absolute Universe", "alternate",
            "Absolute Wonder Woman #1 (2024)", "A new champion chosen",
            "DC's Absolute line recasts Diana's legacy with a fresh origin and a harder, stranger Themyscira.",
            "https://en.wikipedia.org/wiki/Absolute_Wonder_Woman",
            ["absolute-ww-vol1"],
        ),
        version_obj(
            "hippolyta-ww", "Wonder Woman (Hippolyta)", "Earth-0", "main",
            "Wonder Woman Vol. 2 #127 (1997)", "The queen who wore the crown",
            "Queen Hippolyta of the Amazons briefly served as Wonder Woman during the Our Worlds at War era.",
            "https://en.wikipedia.org/wiki/Hippolyta_(DC_Comics)",
            ["ww-hippolyta-era"],
        ),
        version_obj(
            "ww-elseworlds", "Wonder Woman: Amazonia", "Amazonia (Elseworlds)", "elseworlds",
            "Wonder Woman: Amazonia (1997)", "Victorian nightmare",
            "Diana raised in a steampunk Britain where Jack the Ripper rules and Amazons fight for survival.",
            "https://en.wikipedia.org/wiki/Wonder_Woman:_Amazonia",
            ["ww-amazonia"],
        ),
    ]
    runs = {
        "ww-george-perez": {
            **run_obj(
                "ww-george-perez", "diana-prime", "Wonder Woman by George P\u00e9rez Book One",
                "George P\u00e9rez", "1987\u201388", "Wonder Woman Vol. 2 #1\u201314",
                "Modern Age", "Crisis on Infinite Earths",
                "The post-Crisis relaunch that grounded Diana in Greek myth and feminist iconography.",
                "Wonder Woman by George P\u00e9rez Book One", "1401271172",
            ),
            "isbn": "9781401271172",
        },
        "ww-rebirth": {
            **run_obj(
                "ww-rebirth", "diana-prime", "Wonder Woman Vol. 1: The Lies",
                "Greg Rucka & Liam Sharp", "2016", "Wonder Woman: Rebirth #1, Wonder Woman #1\u20136",
                "Rebirth", "None",
                "Diana discovers her New 52 history may be a lie \u2014 Rucka's acclaimed dual-timeline return.",
                "Wonder Woman Vol. 1: The Lies", "1401267781",
            ),
            "isbn": "9781401267786",
        },
        "ww-greg-ruka": {
            **run_obj(
                "ww-greg-ruka", "diana-prime", "Wonder Woman: The Hiketeia",
                "Greg Rucka & J.G. Jones", "2002", "Graphic novel",
                "Modern Age", "None",
                "A standalone thriller where Diana's sacred oath collides with Batman's justice.",
                "Wonder Woman: The Hiketeia", "1563897627",
            ),
            "isbn": "9781563897629",
        },
        "ww-golden-age": {
            **run_obj(
                "ww-golden-age", "ww-earth2", "Wonder Woman: The Golden Age Vol. 1",
                "William Moulton Marston & H.G. Peter", "1940s", "All Star Comics / Sensation Comics (select)",
                "Golden Age", "None",
                "The Marston-era Wonder Woman \u2014 bondage metaphors, Amazon utopia, and WWII heroism.",
                "Wonder Woman: The Golden Age Vol. 1", "1401271229",
            ),
            "isbn": "9781401271226",
        },
        "ww-azzarello-vol1": {
            **run_obj(
                "ww-azzarello-vol1", "ww-new52", "Wonder Woman Vol. 1: Blood",
                "Brian Azzarello & Cliff Chiang", "2011\u201312", "Wonder Woman Vol. 4 #1\u20136",
                "New 52", "Flashpoint (optional)",
                "Diana learns she is Zeus's daughter and walks into a war among the Olympians.",
                "Wonder Woman Vol. 1: Blood", "1401235630",
            ),
            "isbn": "9781401235631",
        },
        "kingdom-come": {
            **run_obj(
                "kingdom-come", "kingdom-come-ww", "Kingdom Come",
                "Mark Waid & Alex Ross", "1996\u201397", "Kingdom Come #1\u20134",
                "Modern Age", "None",
                "Wonder Woman armors for war in Alex Ross's painted masterpiece of a broken future.",
                "Kingdom Come", "1563893304",
            ),
            "isbn": "9781563893309",
        },
        "flashpoint-event": {
            **run_obj(
                "flashpoint-event", "flashpoint-ww", "Flashpoint",
                "Geoff Johns & Andy Kubert", "2011", "Flashpoint #1\u20135",
                "Modern Age", "None",
                "The Flashpoint timeline where Diana and Aquaman drowned the world in war.",
                "Flashpoint", "1401232368",
            ),
            "isbn": "9781401232368",
        },
        "absolute-ww-vol1": {
            **run_obj(
                "absolute-ww-vol1", "absolute-wonder-woman", "Absolute Wonder Woman Vol. 1",
                "Al Ewing & Nikaido", "2024\u201325", "Absolute Wonder Woman #1\u20136",
                "Absolute", "None",
                "A bold new Wonder Woman for the Absolute Universe.",
                "Absolute Wonder Woman Vol. 1", "1779523401",
            ),
            "isbn": "9781779523407",
        },
        "ww-hippolyta-era": {
            **run_obj(
                "ww-hippolyta-era", "hippolyta-ww", "Wonder Woman: Our Worlds at War",
                "Phil Jimenez & others", "2001", "Wonder Woman Vol. 2 #172\u2013173",
                "Modern Age", "None",
                "Queen Hippolyta dons the tiara when Diana falls during the Imperiex war.",
                "Wonder Woman: Paradise Lost", "1563899569",
            ),
            "isbn": "9781563899562",
        },
        "ww-amazonia": {
            **run_obj(
                "ww-amazonia", "ww-elseworlds", "Wonder Woman: Amazonia",
                "William Messner-Loebs & Phil Winslade", "1997", "Graphic novel",
                "Elseworlds", "None",
                "Victorian steampunk Elseworld where Diana fights a tyrannical British empire.",
                "Wonder Woman: Amazonia", "1563893940",
            ),
            "isbn": "9781563893942",
        },
        "ww-dead-earth": {
            **run_obj(
                "ww-dead-earth", "diana-prime", "Wonder Woman: Dead Earth",
                "Daniel Warren Johnson", "2020", "Wonder Woman: Dead Earth #1\u20134",
                "Modern Age", "None",
                "Post-apocalyptic Diana on a poisoned Earth \u2014 raw, kinetic, standalone.",
                "Wonder Woman: Dead Earth", "1779500219",
            ),
            "isbn": "9781779500216",
        },
        "ww-trial-amazons": {
            **run_obj(
                "ww-trial-amazons", "diana-prime", "Wonder Woman: The Trial of the Amazons",
                "Stephanie Phillips & others", "2022", "Trial of the Amazons #1\u20134",
                "Infinite Frontier", "None",
                "Amazon succession crisis \u2014 politics, combat, and Diana's legacy on the line.",
                "Wonder Woman: Trial of the Amazons", "1779515679",
            ),
            "isbn": "9781779515678",
        },
    }
    return {
        "id": "wonder-woman",
        "brand": "Wonder Woman",
        "title": "Wonder Woman \u2014 Truth and Power Across the Multiverse",
        "nav_who": "Who is Wonder Woman",
        "nav_verses": "Amazons & Verses",
        "who_id": "who-is-wonder-woman",
        "header_img": "wonder-woman-homepage-header-image.jpg",
        "hero_gradient": "radial-gradient(circle at 30% 25%, #c41e3a, #8b0000 45%, #1a0508)",
        "verses_h2": "Wonder Woman Across the Multiverse",
        "verses_p": "versions across Themyscira and beyond \u2014 Diana, Hippolyta, Flashpoint, Kingdom Come, and Elseworlds Amazons.",
        "comics_p": "Essential Wonder Woman stories \u2014 from George P\u00e9rez and Greg Rucka to Azzarello's New 52 and Absolute.",
        "screen_p": "Live-action and animated appearances \u2014 from Lynda Carter to Gal Gadot, Patty Jenkins, and Justice League.",
        "types": DC_TYPES,
        "versions": versions,
        "runs": runs,
        "home_runs": [
            "ww-george-perez", "ww-rebirth", "ww-azzarello-vol1", "kingdom-come",
            "flashpoint-event", "ww-greg-ruka", "absolute-ww-vol1", "ww-golden-age",
            "ww-dead-earth", "ww-trial-amazons",
        ],
        "profile": {
            "wikipedia": "https://en.wikipedia.org/wiki/Wonder_Woman",
            "lead": "Warrior, diplomat, icon \u2014 the Amazon who chose love over conquest.",
            "summary": "Wonder Woman is Diana of Themyscira, princess of the Amazons and champion of truth. Created by William Moulton Marston and H.G. Peter in All Star Comics #8 (1941), she is a feminist symbol and one of DC's Trinity alongside Batman and Superman. Her stories weave Greek myth, wartime heroism, and modern political allegory.",
            "facts": [
                {"label": "Alter ego", "value": "Diana Prince / Princess Diana"},
                {"label": "First appearance", "value": "All Star Comics #8 (1941)"},
                {"label": "Created by", "value": "William Moulton Marston & H.G. Peter"},
                {"label": "Publisher", "value": "DC Comics"},
                {"label": "Base of operations", "value": "Themyscira / Washington, D.C."},
                {"label": "Allies", "value": "Justice League, Amazons, Steve Trevor"},
                {"label": "Notable foes", "value": "Ares, Cheetah, Circe, Maxwell Lord"},
                {"label": "Powers", "value": "Super strength, flight, Lasso of Truth, divine weapons"},
            ],
        },
        "screen": [
            {
                "group": "Live-action films",
                "items": [
                    screen_item("ww-2017", "Wonder Woman", "Gal Gadot \u00b7 Patty Jenkins", "https://en.wikipedia.org/wiki/Wonder_Woman_(2017_film)", "https://www.imdb.com/title/tt0451279/", year="2017"),
                    screen_item("ww-84", "Wonder Woman 1984", "Gal Gadot \u00b7 1980s Cold War", "https://en.wikipedia.org/wiki/Wonder_Woman_1984", "https://www.imdb.com/title/tt7126948/", year="2020"),
                    screen_item("jl-ww", "Justice League", "Gal Gadot \u00b7 Snyder / Whedon", "https://en.wikipedia.org/wiki/Justice_League_(film)", "https://www.imdb.com/title/tt0974015/", year="2017"),
                ],
            },
            {
                "group": "Live-action television",
                "items": [
                    screen_item("ww-lynda", "Wonder Woman", "Lynda Carter \u00b7 ABC/CBS", "https://en.wikipedia.org/wiki/Wonder_Woman_(TV_series)", "https://www.imdb.com/title/tt0074074/", years="1975\u20131979"),
                ],
            },
            {
                "group": "Animated",
                "items": [
                    screen_item("ww-blood", "Wonder Woman (2009)", "Animated origin film", "https://en.wikipedia.org/wiki/Wonder_Woman_(2009_film)", "https://www.imdb.com/title/tt1186373/", year="2009"),
                    screen_item("jl-ww-animated", "Justice League / Unlimited", "Susan Eisenberg as Diana", "https://en.wikipedia.org/wiki/Justice_League_(TV_series)", "https://www.imdb.com/title/tt0275137/", years="2001\u20132006"),
                ],
            },
        ],
        "themes": {
            "diana-prime": (196, 30, 58),
            "ww-earth2": (160, 40, 50),
            "ww-new52": (140, 20, 40),
            "kingdom-come-ww": (180, 140, 100),
            "flashpoint-ww": (120, 15, 30),
            "absolute-wonder-woman": (100, 25, 45),
            "hippolyta-ww": (200, 180, 80),
            "ww-elseworlds": (80, 60, 90),
        },
        "issues": {
            "ww-george-perez": [
                {"id": "Wonder Woman #1", "title": "Olympian Challenge"},
                {"id": "#2", "title": "Gods and Mortals"},
                {"id": "#3", "title": "Gods and Mortals"},
                {"id": "#4", "title": "Gods and Mortals"},
                {"id": "#5", "title": "Gods and Mortals"},
            ],
        },
    }


DC_PACKS = [
    pack_green_lantern(),
    pack_flash(),
    pack_superman(),
    pack_wonder_woman(),
]
