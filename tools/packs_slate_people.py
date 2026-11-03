# One-person guides for the current slate.
# A pack is one person. Mantle-sharers and teammates get their own packs.

from packs_screen import DC_TYPES, MARVEL_TYPES, run_obj, screen_item, version_obj

DOOMSDAY = "https://www.marvel.com/movies/avengers-doomsday"
DOOMSDAY_IMDB = "https://www.imdb.com/find/?q=Avengers%3A%20Doomsday"
LANTERNS_WIKI = "https://en.wikipedia.org/wiki/Lanterns_(TV_series)"
LANTERNS_IMDB = "https://www.imdb.com/title/tt26545992/"
YFN_WIKI = "https://en.wikipedia.org/wiki/Your_Friendly_Neighborhood_Spider-Man"
BEYOND_WIKI = "https://en.wikipedia.org/wiki/Spider-Man:_Beyond_the_Spider-Verse"


def book(slug, version, title, creators, years, collects, era, prereq, summary, isbn13, isbn10):
    row = run_obj(slug, version, title, creators, years, collects, era, prereq, summary, title, isbn10)
    row["isbn"] = isbn13
    return {slug: row}


def guide(pid, brand, title, nav_who, who_id, gradient, verses_h2, verses_p, comics_p, screen_p, types, versions, runs, home_runs, profile, screen, themes):
    return {
        "id": pid,
        "brand": brand,
        "title": title,
        "nav_who": nav_who,
        "nav_verses": "Verses",
        "who_id": who_id,
        "header_img": pid + "-homepage-header-image.jpg",
        "hero_gradient": gradient,
        "verses_h2": verses_h2,
        "verses_p": verses_p,
        "comics_p": comics_p,
        "screen_p": screen_p,
        "types": types,
        "versions": versions,
        "runs": runs,
        "home_runs": home_runs,
        "profile": profile,
        "screen": screen,
        "themes": themes,
        "issues": {},
    }


def profile(wiki, lead, summary, facts):
    return {"wikipedia": wiki, "lead": lead, "summary": summary, "facts": facts}


PETER = guide(
    "peter-parker", "Peter Parker", "Peter Parker — Your Friendly Neighborhood Spider-Man",
    "Who is Peter Parker", "who-is-peter-parker",
    "radial-gradient(circle at 30% 25%, #e53935, #b71c1c 45%, #1a0505)",
    "Peter Parker Across the Multiverse",
    "versions of Peter Parker in the comics: Earth-616 and the Ultimate Universe.",
    "Peter's own stories, from the Ditko origin through Kraven's Last Hunt.",
    "Where this Peter is on screen — Your Friendly Neighborhood Spider-Man — plus the films that are still his.",
    MARVEL_TYPES,
    [
        version_obj("peter-616", "Peter Parker", "Earth-616", "main", "Amazing Fantasy #15 (1962)", "Your friendly neighborhood Spider-Man", "Bitten by a radioactive spider, Peter Parker learns that with great power comes great responsibility.", "https://en.wikipedia.org/wiki/Spider-Man", ["pp-origin", "pp-kraven"]),
        version_obj("peter-ultimate", "Ultimate Peter Parker", "Earth-1610", "ultimate", "Ultimate Spider-Man #1 (2000)", "The high-school retelling", "Bendis and Bagley retell Peter's teenage years for a new century. This is still Peter, not Miles.", "https://en.wikipedia.org/wiki/Ultimate_Spider-Man", ["pp-ultimate"]),
    ],
    {
        **book("pp-origin", "peter-616", "Amazing Fantasy Omnibus / Amazing Spider-Man Vol. 1", "Stan Lee & Steve Ditko", "1962–63", "Amazing Fantasy #15, Amazing Spider-Man #1–10", "Silver Age", "None — start here", "The radioactive spider, Uncle Ben, and the birth of Peter Parker.", "9780785124634", "0785124635"),
        **book("pp-kraven", "peter-616", "Kraven's Last Hunt", "J.M. DeMatteis & Mike Zeck", "1987", "Web of Spider-Man #31–32, Amazing Spider-Man #293–294, Spectacular Spider-Man #131–132", "Modern Age", "None", "Kraven buries Spider-Man and steals his life. One of Peter's darkest stories.", "9780785134534", "0785134533"),
        **book("pp-ultimate", "peter-ultimate", "Ultimate Spider-Man Vol. 1", "Brian Michael Bendis & Mark Bagley", "2000–01", "Ultimate Spider-Man #1–7", "Ultimate", "None", "A modern retelling of Peter's origin. Miles comes later, in a different book.", "9780781020749", "0781020747"),
    },
    ["pp-origin", "pp-kraven", "pp-ultimate"],
    profile(
        "https://en.wikipedia.org/wiki/Spider-Man",
        "A student bitten by a radioactive spider, who holds that great power comes with great responsibility.",
        "Peter Parker is Marvel's Spider-Man, created by Stan Lee and Steve Ditko in Amazing Fantasy #15 (1962). Your Friendly Neighborhood Spider-Man is his story. Miles, Gwen, and Miguel are other people.",
        [
            {"label": "Alter ego", "value": "Spider-Man"},
            {"label": "First appearance", "value": "Amazing Fantasy #15 (1962)"},
            {"label": "Created by", "value": "Stan Lee & Steve Ditko"},
            {"label": "On screen now", "value": "Your Friendly Neighborhood Spider-Man, season 2 on January 13, 2027"},
            {"label": "Powers", "value": "Wall-crawling, spider-sense, strength"},
            {"label": "Home", "value": "New York City"},
        ],
    ),
    [
        {"group": "This slate", "items": [
            screen_item("pp-yfn", "Your Friendly Neighborhood Spider-Man", "Season 2 · Disney+ · January 13, 2027", YFN_WIKI, "https://www.imdb.com/find/?q=Your%20Friendly%20Neighborhood%20Spider-Man", year="2027"),
        ]},
        {"group": "Films that are still Peter", "items": [
            screen_item("pp-nwh", "Spider-Man: No Way Home", "Tom Holland · MCU Peter", "https://en.wikipedia.org/wiki/Spider-Man:_No_Way_Home", "https://www.imdb.com/title/tt10872600/", year="2021"),
        ]},
    ],
    {"peter-616": (229, 57, 53), "peter-ultimate": (200, 40, 40), "peter-yfn": (180, 30, 30)},
)

MILES = guide(
    "miles-morales", "Miles Morales", "Miles Morales — Spider-Man",
    "Who is Miles Morales", "who-is-miles-morales",
    "radial-gradient(circle at 30% 25%, #1a1a1a, #b71c1c 55%, #0a0a0a)",
    "Miles Morales Across the Multiverse",
    "versions of Miles — the Ultimate Spider-Man who took the mask, and the Miles of the main Marvel Universe.",
    "Miles's own comics, from his Ultimate debut to his arrival in the main universe.",
    "Spider-Man: Beyond the Spider-Verse is his film. Peter's guide is a different page.",
    MARVEL_TYPES,
    [
        version_obj("miles-ultimate", "Miles Morales", "Earth-1610", "ultimate", "Ultimate Fallout #4 (2011)", "The Ultimate Spider-Man", "After Ultimate Peter's death, Miles Morales is bitten and takes up the mask. Created by Brian Michael Bendis and Sara Pichelli.", "https://en.wikipedia.org/wiki/Miles_Morales", ["mm-ultimate"]),
        version_obj("miles-616", "Miles Morales", "Earth-616", "main", "Spider-Man #1 (2016)", "Two Spider-Men in one city", "Miles crosses into the main Marvel Universe and stays. He is not a version of Peter.", "https://en.wikipedia.org/wiki/Miles_Morales", ["mm-616"]),
    ],
    {
        **book("mm-ultimate", "miles-ultimate", "Miles Morales: Ultimate Spider-Man Vol. 1", "Brian Michael Bendis & Sara Pichelli", "2011–12", "Ultimate Comics Spider-Man #1–6", "Ultimate", "None — start here", "Miles steps into the costume after Ultimate Peter's death.", "9780785165507", "0785165501"),
        **book("mm-616", "miles-616", "Spider-Man: Miles Morales Vol. 1", "Brian Michael Bendis & Sara Pichelli", "2015–16", "Spider-Man #1–5", "Modern Age", "Ultimate Miles", "Miles arrives in the main Marvel Universe and keeps the name Spider-Man.", "9780785199670", "0785199678"),
    },
    ["mm-ultimate", "mm-616"],
    profile(
        "https://en.wikipedia.org/wiki/Miles_Morales",
        "Brooklyn's Spider-Man. He took the mask in the Ultimate Universe after Peter Parker died.",
        "Miles Morales took up the Spider-Man mantle in the Ultimate Universe in Ultimate Fallout #4 (2011), created by Brian Michael Bendis and Sara Pichelli. Beyond the Spider-Verse, in theaters June 18, 2027, is his film.",
        [
            {"label": "Alter ego", "value": "Spider-Man"},
            {"label": "First appearance", "value": "Ultimate Fallout #4 (2011)"},
            {"label": "Created by", "value": "Brian Michael Bendis & Sara Pichelli"},
            {"label": "On screen next", "value": "Spider-Man: Beyond the Spider-Verse, June 18, 2027"},
            {"label": "Powers", "value": "Wall-crawling, venom strike, camouflage"},
            {"label": "Home", "value": "Brooklyn"},
        ],
    ),
    [
        {"group": "This slate", "items": [
            screen_item("mm-beyond", "Spider-Man: Beyond the Spider-Verse", "In theaters June 18, 2027", BEYOND_WIKI, "https://www.imdb.com/find/?q=Spider-Man%3A%20Beyond%20the%20Spider-Verse", year="2027"),
        ]},
        {"group": "Films", "items": [
            screen_item("mm-itsv", "Spider-Man: Into the Spider-Verse", "Sony Animation", "https://en.wikipedia.org/wiki/Spider-Man:_Into_the_Spider-Verse", "https://www.imdb.com/title/tt4633694/", year="2018"),
            screen_item("mm-atsv", "Spider-Man: Across the Spider-Verse", "Sony Animation", "https://en.wikipedia.org/wiki/Spider-Man:_Across_the_Spider-Verse", "https://www.imdb.com/title/tt9362722/", year="2023"),
        ]},
    ],
    {"miles-ultimate": (20, 20, 20), "miles-616": (180, 30, 40)},
)

HAL = guide(
    "hal-jordan", "Hal Jordan", "Hal Jordan — Green Lantern",
    "Who is Hal Jordan", "who-is-hal-jordan",
    "radial-gradient(circle at 30% 25%, #2db84b, #0d5c28 45%, #041208)",
    "Hal Jordan Across the Multiverse",
    "versions of Hal Jordan — the Corps' test-pilot Lantern, and the man Parallax wore.",
    "Hal's own books: Secret Origin, Rebirth, and the fall in Emerald Twilight.",
    "Lanterns is his series, with John Stewart. Guy Gardner and Sinestro have their own guides.",
    DC_TYPES,
    [
        version_obj("hal", "Hal Jordan", "Earth-0", "main", "Showcase #22 (1959)", "The greatest Green Lantern", "Test pilot Hal Jordan was chosen by a dying Abin Sur. Created by John Broome and Gil Kane.", "https://en.wikipedia.org/wiki/Hal_Jordan", ["hal-origin", "hal-rebirth"]),
        version_obj("hal-parallax", "Parallax (Hal Jordan)", "Earth-0", "alternate", "Green Lantern Vol. 3 #50 (1994)", "Willpower corrupted", "Possessed by the fear entity Parallax, Hal destroyed the Corps. This is still Hal.", "https://en.wikipedia.org/wiki/Parallax_(character)", ["hal-twilight"]),
    ],
    {
        **book("hal-origin", "hal", "Green Lantern: Secret Origin", "Geoff Johns & Ivan Reis", "2008", "Green Lantern #29–35", "Modern Age", "None — start here", "Johns retells how Hal Jordan received the ring.", "9781401221904", "1401221900"),
        **book("hal-rebirth", "hal", "Green Lantern: Rebirth", "Geoff Johns & Ethan Van Sciver", "2004–05", "Green Lantern: Rebirth #1–6", "Modern Age", "None", "Hal returns and reclaims the ring.", "9781401204617", "1401204615"),
        **book("hal-twilight", "hal-parallax", "Green Lantern: Emerald Twilight", "Ron Marz & Bill Willingham", "1994", "Green Lantern #48–50", "Modern Age", "None", "Hal's fall, and the end of the classic Corps era.", "9781401207861", "1401207860"),
    },
    ["hal-origin", "hal-rebirth", "hal-twilight"],
    profile(
        "https://en.wikipedia.org/wiki/Hal_Jordan",
        "A test pilot chosen by a dying alien. The green ring turns his willpower into light.",
        "Hal Jordan is Earth's most famous Green Lantern, a test pilot chosen in Showcase #22 (1959). In Lanterns he investigates a murder with John Stewart. Kyle Chandler plays him.",
        [
            {"label": "Mantle", "value": "Green Lantern"},
            {"label": "First appearance", "value": "Showcase #22 (1959)"},
            {"label": "Created by", "value": "John Broome & Gil Kane"},
            {"label": "On screen", "value": "Lanterns, full season on HBO / Max"},
            {"label": "Played by", "value": "Kyle Chandler"},
            {"label": "Sector", "value": "2814"},
        ],
    ),
    [{"group": "This slate", "items": [
        screen_item("hal-lanterns", "Lanterns", "Kyle Chandler · full season on HBO / Max", LANTERNS_WIKI, LANTERNS_IMDB, year="2026"),
    ]}],
    {"hal": (8, 48, 24), "hal-parallax": (36, 28, 8)},
)

JOHN = guide(
    "john-stewart", "John Stewart", "John Stewart — Green Lantern",
    "Who is John Stewart", "who-is-john-stewart",
    "radial-gradient(circle at 30% 25%, #1b5e20, #0d3318 50%, #041208)",
    "John Stewart Across the Multiverse",
    "versions of John Stewart — Marine, architect, and Green Lantern.",
    "John's own books: Mosaic, and the Corps rebuilding in Recharge.",
    "Lanterns pairs him with Hal Jordan. His guide is not Hal's.",
    DC_TYPES,
    [
        version_obj("john", "John Stewart", "Earth-0", "main", "Green Lantern Vol. 2 #87 (1971)", "Architect of the Corps", "A Marine and architect chosen as Hal's backup, John became one of Earth's defining Green Lanterns. Created by Denny O'Neil and Neal Adams.", "https://en.wikipedia.org/wiki/John_Stewart_(character)", ["john-mosaic", "john-recharge"]),
    ],
    {
        **book("john-mosaic", "john", "Green Lantern: Mosaic", "Gerard Jones & others", "1992–93", "Green Lantern: Mosaic #1–18 (select)", "Modern Age", "None — start here", "John Stewart as caretaker of a patchwork world.", "9781401254568", "1401254567"),
        **book("john-recharge", "john", "Green Lantern Corps: Recharge", "Dave Gibbons & Patrick Gleason", "2005–06", "Green Lantern Corps: Recharge #1–5", "Modern Age", "Green Lantern: Rebirth", "The Corps rebuilds, with John among its leaders.", "9781401210120", "1401210120"),
    },
    ["john-mosaic", "john-recharge"],
    profile(
        "https://en.wikipedia.org/wiki/John_Stewart_(character)",
        "A Marine and an architect chosen to wear a Green Lantern ring.",
        "John Stewart debuted in Green Lantern #87 (1971), created by Denny O'Neil and Neal Adams. Lanterns, streaming on HBO / Max, is the case he works with Hal Jordan. Aaron Pierre plays him.",
        [
            {"label": "Mantle", "value": "Green Lantern"},
            {"label": "First appearance", "value": "Green Lantern #87 (1971)"},
            {"label": "Created by", "value": "Denny O'Neil & Neal Adams"},
            {"label": "On screen", "value": "Lanterns, full season on HBO / Max"},
            {"label": "Played by", "value": "Aaron Pierre"},
            {"label": "Trade", "value": "Architect and former Marine"},
        ],
    ),
    [{"group": "This slate", "items": [
        screen_item("john-lanterns", "Lanterns", "Aaron Pierre · full season on HBO / Max", LANTERNS_WIKI, LANTERNS_IMDB, year="2026"),
    ]}],
    {"john": (12, 40, 28)},
)

GUY = guide(
    "guy-gardner", "Guy Gardner", "Guy Gardner — Green Lantern",
    "Who is Guy Gardner", "who-is-guy-gardner",
    "radial-gradient(circle at 30% 25%, #f9a825, #1b5e20 48%, #041208)",
    "Guy Gardner Across the Multiverse",
    "versions of Guy Gardner — the loudest Lantern, with or without the ring.",
    "Guy's own book, when the ring is gone and the attitude is not.",
    "He is one of the four Lanterns leads. Hal, John, and Sinestro have their own guides.",
    DC_TYPES,
    [
        version_obj("guy", "Guy Gardner", "Earth-0", "main", "Green Lantern Vol. 2 #59 (1968)", "The Corps' blunt instrument", "Chosen as a possible replacement for Hal, Guy Gardner is brash, loyal, and impossible to ignore. Created by John Broome and Gil Kane.", "https://en.wikipedia.org/wiki/Guy_Gardner_(character)", ["guy-warrior"]),
    ],
    {
        **book("guy-warrior", "guy", "Guy Gardner: Warrior", "Beau Smith & others", "1994–96", "Guy Gardner: Warrior (select)", "Modern Age", "None — start here", "Guy without a ring, still picking fights and still showing up.", "9781401208905", "1401208907"),
    },
    ["guy-warrior"],
    profile(
        "https://en.wikipedia.org/wiki/Guy_Gardner_(character)",
        "The loudest Green Lantern, chosen as a backup and never quiet about it.",
        "Guy Gardner debuted in Green Lantern #59 (1968). He is a lead of Lanterns alongside Hal Jordan, John Stewart, and Sinestro, and he already appeared in the 2025 Superman film.",
        [
            {"label": "Mantle", "value": "Green Lantern"},
            {"label": "First appearance", "value": "Green Lantern #59 (1968)"},
            {"label": "Created by", "value": "John Broome & Gil Kane"},
            {"label": "On screen", "value": "Lanterns, full season on HBO / Max"},
            {"label": "Also on screen", "value": "Superman (2025), played by Nathan Fillion"},
        ],
    ),
    [
        {"group": "This slate", "items": [
            screen_item("guy-lanterns", "Lanterns", "Full season on HBO / Max", LANTERNS_WIKI, LANTERNS_IMDB, year="2026"),
        ]},
        {"group": "Films", "items": [
            screen_item("guy-superman", "Superman", "Nathan Fillion · DCU", "https://en.wikipedia.org/wiki/Superman_(2025_film)", "https://www.imdb.com/title/tt5950044/", year="2025"),
        ]},
    ],
    {"guy": (249, 168, 37)},
)

SINESTRO = guide(
    "sinestro", "Sinestro", "Sinestro",
    "Who is Sinestro", "who-is-sinestro",
    "radial-gradient(circle at 30% 25%, #f9a825, #6a1b9a 42%, #1a0a00)",
    "Sinestro Across the Multiverse",
    "versions of Thaal Sinestro — greatest Lantern, then tyrant of the yellow ring.",
    "His own series, The Demon Within, plus the war he started.",
    "Lanterns features him in his own right. He is not a chapter of Hal's guide.",
    DC_TYPES,
    [
        version_obj("sinestro", "Thaal Sinestro", "Earth-0", "main", "Green Lantern Vol. 2 #7 (1961)", "The fear corps", "Korugar's greatest Green Lantern became the Corps' greatest enemy, then built an army fueled by fear. Created by John Broome and Gil Kane.", "https://en.wikipedia.org/wiki/Sinestro", ["sin-demon", "sin-war"]),
    ],
    {
        **book("sin-demon", "sinestro", "Sinestro Vol. 1: The Demon Within", "Cullen Bunn & Dale Eaglesham", "2014–15", "Sinestro #1–5 and related", "Modern Age", "None — his own series", "Sinestro has lost Korugar, his family, and his friend. The yellow corps is still his.", "9781401250508", "1401250505"),
        **book("sin-war", "sinestro", "Green Lantern: The Sinestro Corps War", "Geoff Johns & others", "2007", "Green Lantern / Green Lantern Corps crossover", "Modern Age", "Green Lantern: Rebirth", "Sinestro builds an army to destroy the Green Lantern Corps.", "9781401216504", "1401216503"),
    },
    ["sin-demon", "sin-war"],
    profile(
        "https://en.wikipedia.org/wiki/Sinestro",
        "Once the finest Green Lantern of his sector. Cast out, he founded a corps whose yellow rings feed on fear.",
        "Sinestro debuted in Green Lantern #7 (1961). He was the greatest Green Lantern of his sector, then the founder of the Sinestro Corps. Lanterns keeps him beside Hal Jordan, John Stewart, and Guy Gardner.",
        [
            {"label": "Also called", "value": "Thaal Sinestro"},
            {"label": "First appearance", "value": "Green Lantern #7 (1961)"},
            {"label": "Created by", "value": "John Broome & Gil Kane"},
            {"label": "On screen", "value": "Lanterns, full season on HBO / Max"},
            {"label": "Weapon", "value": "Yellow power ring, fueled by fear"},
            {"label": "Home", "value": "Korugar"},
        ],
    ),
    [{"group": "This slate", "items": [
        screen_item("sin-lanterns", "Lanterns", "Full season on HBO / Max", LANTERNS_WIKI, LANTERNS_IMDB, year="2026"),
    ]}],
    {"sinestro": (249, 168, 37)},
)


COMICS_LEADS = {
    "steve-rogers": "A frail man given the super-soldier serum, who carries the shield as Captain America.",
    "thor": "The Asgardian god of thunder, and the one who is worthy of Mjolnir.",
    "sam-wilson": "The Falcon who took up Captain America's shield.",
    "bucky-barnes": "Captain America's wartime partner, later the Winter Soldier, who took his own name back.",
    "scott-lang": "The second Ant-Man. He stole Hank Pym's suit to save his daughter.",
    "yelena-belova": "A Black Widow trained in the Red Room who became her own hero beside Natasha.",
    "john-walker": "Built as a replacement Captain America, he kept the fight as U.S. Agent.",
    "ava-starr": "A woman whose body slips out of phase with the world. She takes the name Ghost.",
    "alexei-shostakov": "The Soviet answer to Captain America, once Natasha Romanoff's husband.",
    "sentry": "A hero the world was made to forget, and the Void that returns with the memory.",
    "ultron": "A robot Hank Pym created from a copy of his own mind. He turns on that maker and on humanity.",
    "thomas-shepherd": "The Young Avenger called Speed, twin of Billy Kaplan and a son of the Scarlet Witch and the Vision.",
    "paladin": "A mercenary whose real name is unknown. He works for whoever pays, and sometimes that means standing with heroes.",
}


def avenger(pid, brand, title, who, gradient, tagline, description, wiki, first, created, comic_slug, comic_title, creators, years, collects, summary, isbn13, isbn10, facts, screen_note, themes):
    ver = pid.split("-")[0] if False else pid
    return guide(
        pid, brand, title, who, "who-is-" + pid, gradient,
        brand + " Across the Multiverse",
        "versions of " + brand + ". Other Avengers have their own guides.",
        "The comic to start with.",
        "Avengers: Doomsday, in theaters December 18, 2026. Doctor Doom's guide is separate.",
        MARVEL_TYPES,
        [version_obj(ver, brand, "Earth-616", "main", first, tagline, description, wiki, [comic_slug])],
        book(comic_slug, ver, comic_title, creators, years, collects, "Modern Age", "None — start here", summary, isbn13, isbn10),
        [comic_slug],
        profile(wiki, COMICS_LEADS.get(pid, tagline), description + " Confirmed for Avengers: Doomsday, in theaters December 18, 2026.", facts),
        [{"group": "This slate", "items": [
            screen_item(pid + "-doomsday", "Avengers: Doomsday", screen_note, DOOMSDAY, DOOMSDAY_IMDB, year="2026"),
        ]}],
        {ver: themes},
    )


STEVE = avenger(
    "steve-rogers", "Steve Rogers", "Steve Rogers — Captain America", "Who is Steve Rogers",
    "radial-gradient(circle at 30% 25%, #1e4a8c, #0a1f44 45%, #020810)",
    "The First Avenger, back for Doomsday.",
    "Steve Rogers is the original Captain America, a frail man given the super-soldier serum in Captain America Comics #1 (1941), created by Joe Simon and Jack Kirby. Marvel's Doomsday teaser says Steve Rogers will return.",
    "https://en.wikipedia.org/wiki/Captain_America",
    "Captain America Comics #1 (1941)", "Joe Simon & Jack Kirby",
    "steve-winter", "Captain America: Winter Soldier", "Ed Brubaker & Steve Epting", "2004–05",
    "Captain America #1–9, 11–14",
    "Steve hunts the Winter Soldier and finds Bucky Barnes. Bucky's guide is a different page.",
    "9780785134303", "0785134302",
    [
        {"label": "Mantle", "value": "Captain America"},
        {"label": "First appearance", "value": "Captain America Comics #1 (1941)"},
        {"label": "Created by", "value": "Joe Simon & Jack Kirby"},
        {"label": "On screen", "value": "Avengers: Doomsday · December 18, 2026"},
        {"label": "Played by", "value": "Chris Evans"},
    ],
    "Chris Evans · Marvel's teaser: Steve Rogers will return",
    (30, 58, 140),
)

THOR = avenger(
    "thor", "Thor", "Thor", "Who is Thor",
    "radial-gradient(circle at 30% 25%, #546e7a, #b71c1c 40%, #0d1b2a)",
    "The god of thunder, back for Doomsday.",
    "Thor is the Asgardian god of thunder, created by Stan Lee, Larry Lieber, and Jack Kirby in Journey into Mystery #83 (1962). Marvel's second Doomsday teaser is his.",
    "https://en.wikipedia.org/wiki/Thor_(Marvel_Comics)",
    "Journey into Mystery #83 (1962)", "Stan Lee, Larry Lieber & Jack Kirby",
    "thor-butcher", "Thor: God of Thunder Vol. 1 — The God Butcher", "Jason Aaron & Esad Ribic", "2012–13",
    "Thor: God of Thunder #1–5",
    "Three Thors, three eras, and a butcher of gods. The modern book to start with.",
    "9780785168423", "0785168427",
    [
        {"label": "Also called", "value": "The Odinson"},
        {"label": "First appearance", "value": "Journey into Mystery #83 (1962)"},
        {"label": "Created by", "value": "Stan Lee, Larry Lieber & Jack Kirby"},
        {"label": "On screen", "value": "Avengers: Doomsday · December 18, 2026"},
        {"label": "Played by", "value": "Chris Hemsworth"},
    ],
    "Chris Hemsworth · Marvel's second Doomsday teaser",
    (120, 144, 156),
)

SAM = avenger(
    "sam-wilson", "Sam Wilson", "Sam Wilson — Captain America", "Who is Sam Wilson",
    "radial-gradient(circle at 30% 25%, #c62828, #1565c0 48%, #1a0505)",
    "Captain America, and an Avenger in Doomsday.",
    "Sam Wilson is the Falcon who took up Captain America's shield. He debuted in Captain America #117 (1969), created by Stan Lee and Gene Colan. Anthony Mackie plays him, and Mackie is on the official Doomsday cast.",
    "https://en.wikipedia.org/wiki/Sam_Wilson_(Marvel_Comics)",
    "Captain America #117 (1969)", "Stan Lee & Gene Colan",
    "sam-cap", "All-New Captain America", "Rick Remender & Stuart Immonen", "2014–15",
    "All-New Captain America #1–6",
    "Sam Wilson takes the shield. Steve's guide stays Steve's.",
    "9780785192981", "0785192987",
    [
        {"label": "Mantle", "value": "Captain America"},
        {"label": "First appearance", "value": "Captain America #117 (1969)"},
        {"label": "Created by", "value": "Stan Lee & Gene Colan"},
        {"label": "On screen", "value": "Avengers: Doomsday · December 18, 2026"},
        {"label": "Played by", "value": "Anthony Mackie"},
    ],
    "Anthony Mackie · Captain America",
    (198, 40, 40),
)

BUCKY = avenger(
    "bucky-barnes", "Bucky Barnes", "Bucky Barnes — The Winter Soldier", "Who is Bucky Barnes",
    "radial-gradient(circle at 30% 25%, #455a64, #263238 50%, #0a0a0a)",
    "The Winter Soldier, and a New Avenger in Doomsday.",
    "James Buchanan Barnes was Captain America's partner, then the Winter Soldier. He debuted in Captain America Comics #1 (1941), created by Joe Simon and Jack Kirby. He is on Marvel's New Avengers roster and on the Doomsday cast, played by Sebastian Stan.",
    "https://en.wikipedia.org/wiki/Bucky_Barnes",
    "Captain America Comics #1 (1941)", "Joe Simon & Jack Kirby",
    "bucky-solo", "The Winter Soldier", "Ed Brubaker & Butch Guice", "2012–13",
    "Winter Soldier #1–14",
    "Bucky's own series, after he takes his name back.",
    "9780785163359", "0785163353",
    [
        {"label": "Also called", "value": "The Winter Soldier"},
        {"label": "First appearance", "value": "Captain America Comics #1 (1941)"},
        {"label": "Created by", "value": "Joe Simon & Jack Kirby"},
        {"label": "On screen", "value": "Avengers: Doomsday · December 18, 2026"},
        {"label": "Played by", "value": "Sebastian Stan"},
    ],
    "Sebastian Stan · New Avenger",
    (69, 90, 100),
)

SCOTT = avenger(
    "scott-lang", "Scott Lang", "Scott Lang — Ant-Man", "Who is Scott Lang",
    "radial-gradient(circle at 30% 25%, #c62828, #212121 46%, #1a0505)",
    "Ant-Man, and an Avenger in Doomsday.",
    "Scott Lang is the second Ant-Man, an electronics expert who stole Hank Pym's suit to save his daughter. He debuted in Avengers #181 (1979), created by David Michelinie and John Byrne. Paul Rudd plays him and is on the official Doomsday cast.",
    "https://en.wikipedia.org/wiki/Scott_Lang",
    "Avengers #181 (1979)", "David Michelinie & John Byrne",
    "scott-second", "Ant-Man Vol. 1: Second-Chance Man", "Nick Spencer & Ramon Rosanas", "2015",
    "Ant-Man (2015) #1–5",
    "Scott Lang trying to be a father and a thief who does the right thing.",
    "9780785193876", "0785193871",
    [
        {"label": "Mantle", "value": "Ant-Man"},
        {"label": "First appearance", "value": "Avengers #181 (1979)"},
        {"label": "Created by", "value": "David Michelinie & John Byrne"},
        {"label": "On screen", "value": "Avengers: Doomsday · December 18, 2026"},
        {"label": "Played by", "value": "Paul Rudd"},
    ],
    "Paul Rudd · Ant-Man",
    (198, 40, 40),
)

YELENA = avenger(
    "yelena-belova", "Yelena Belova", "Yelena Belova — Black Widow", "Who is Yelena Belova",
    "radial-gradient(circle at 30% 25%, #f5f5f5, #546e7a 40%, #1a1a1a)",
    "A New Avenger in Doomsday.",
    "Yelena Belova is a Black Widow who became her own hero beside Natasha, and the field leader of Marvel's New Avengers. Florence Pugh plays her and is on the official Doomsday cast.",
    "https://en.wikipedia.org/wiki/Yelena_Belova",
    "Inhumans #5 (1999)", "Devin Grayson & J.G. Jones",
    "yelena-ties", "Black Widow Vol. 1: The Ties That Bind", "Kelly Thompson & Elena Casagrande", "2020",
    "Black Widow (2020) #1–5",
    "Natasha and Yelena, in the run where Yelena becomes more than a rival.",
    "9781302936679", "1302936670",
    [
        {"label": "Mantle", "value": "Black Widow"},
        {"label": "First appearance", "value": "Inhumans #5 (1999)"},
        {"label": "Created by", "value": "Devin Grayson & J.G. Jones"},
        {"label": "On screen", "value": "Avengers: Doomsday · December 18, 2026"},
        {"label": "Played by", "value": "Florence Pugh"},
    ],
    "Florence Pugh · New Avenger",
    (230, 230, 230),
)

WALKER = avenger(
    "john-walker", "John Walker", "John Walker — U.S. Agent", "Who is John Walker",
    "radial-gradient(circle at 30% 25%, #0d47a1, #b71c1c 50%, #0a0a0a)",
    "U.S. Agent, and a New Avenger in Doomsday.",
    "John Walker was built as a replacement Captain America and became U.S. Agent. He debuted in Captain America #323 (1986), created by Mark Gruenwald and Paul Neary. Wyatt Russell plays him and is on the official Doomsday cast.",
    "https://en.wikipedia.org/wiki/John_Walker_(character)",
    "Captain America #323 (1986)", "Mark Gruenwald & Paul Neary",
    "walker-solo", "U.S. Agent", "Christopher Priest & Georges Jeanty", "2020–21",
    "U.S. Agent #1–5",
    "John Walker's modern solo series.",
    "9781302924768", "1302924761",
    [
        {"label": "Mantle", "value": "U.S. Agent"},
        {"label": "First appearance", "value": "Captain America #323 (1986)"},
        {"label": "Created by", "value": "Mark Gruenwald & Paul Neary"},
        {"label": "On screen", "value": "Avengers: Doomsday · December 18, 2026"},
        {"label": "Played by", "value": "Wyatt Russell"},
    ],
    "Wyatt Russell · New Avenger",
    (13, 71, 161),
)

AVA = avenger(
    "ava-starr", "Ava Starr", "Ava Starr — Ghost", "Who is Ava Starr",
    "radial-gradient(circle at 30% 25%, #eceff1, #546e7a 42%, #121212)",
    "Ghost, and a New Avenger in Doomsday.",
    "Ava Starr is the Marvel Cinematic Universe's Ghost, a woman who phases out of phase with the world. Hannah John-Kamen plays her. She is on Marvel's New Avengers roster and on the official Doomsday cast. The comics Ghost is a different person; the film reimagined the name.",
    "https://en.wikipedia.org/wiki/Ghost_(Marvel_Cinematic_Universe)",
    "Ant-Man and the Wasp (2018)", "Marvel Studios",
    "ava-namesake", "Thunderbolts Classic Vol. 1", "Kurt Busiek & Mark Bagley", "1997",
    "Thunderbolts #1 and the first classic collection",
    "Ava Starr does not have a solo comic. This is the book that starts the Thunderbolts, the team the comics Ghost later joined. It is not her origin.",
    "9780785153092", "0785153098",
    [
        {"label": "Mantle", "value": "Ghost"},
        {"label": "On screen since", "value": "Ant-Man and the Wasp (2018)"},
        {"label": "Played by", "value": "Hannah John-Kamen"},
        {"label": "On screen next", "value": "Avengers: Doomsday · December 18, 2026"},
        {"label": "Comics note", "value": "The comics Ghost is a different person"},
    ],
    "Hannah John-Kamen · New Avenger",
    (176, 190, 197),
)

ALEXEI = avenger(
    "alexei-shostakov", "Alexei Shostakov", "Alexei Shostakov — Red Guardian", "Who is Alexei Shostakov",
    "radial-gradient(circle at 30% 25%, #c62828, #f9a825 42%, #1a0505)",
    "Red Guardian, and a New Avenger in Doomsday.",
    "Alexei Shostakov is the Red Guardian, in the comics Natasha Romanoff's husband and the Soviet answer to Captain America. David Harbour plays him. He is on Marvel's New Avengers roster and on the official Doomsday cast.",
    "https://en.wikipedia.org/wiki/Red_Guardian",
    "Avengers #43 (1967)", "Roy Thomas & John Buscema",
    "alexei-origin", "Black Widow: Deadly Origin", "Paul Cornell & Tom Raney", "2009–10",
    "Black Widow: Deadly Origin #1–4",
    "Natasha's early life, and the marriage to the man who became the Red Guardian.",
    "9780785144021", "0785144021",
    [
        {"label": "Mantle", "value": "Red Guardian"},
        {"label": "First appearance", "value": "Avengers #43 (1967)"},
        {"label": "Created by", "value": "Roy Thomas & John Buscema"},
        {"label": "On screen", "value": "Avengers: Doomsday · December 18, 2026"},
        {"label": "Played by", "value": "David Harbour"},
    ],
    "David Harbour · New Avenger",
    (198, 40, 40),
)

SENTRY = avenger(
    "sentry", "Sentry", "Sentry — Robert Reynolds", "Who is the Sentry",
    "radial-gradient(circle at 30% 25%, #ffee58, #f5f5f5 40%, #1a1a1a)",
    "Robert Reynolds, the Sentry, in Doomsday.",
    "Robert Reynolds is the Sentry, a hero the world forgot, and the Void that comes with him. Created by Paul Jenkins and Jae Lee in The Sentry (2000). Lewis Pullman plays Bob and is on the official Doomsday cast. Marvel's Thunderbolts coverage names him with the group that became the New Avengers.",
    "https://en.wikipedia.org/wiki/Sentry_(comics)",
    "The Sentry #1 (2000)", "Paul Jenkins & Jae Lee",
    "sentry-origin", "The Sentry", "Paul Jenkins & Jae Lee", "2000–01",
    "The Sentry #1–5 and the one-shots",
    "Bob Reynolds remembers who he was, and the Void comes back with the memory.",
    "9780785107996", "0785107991",
    [
        {"label": "Alter ego", "value": "Robert Reynolds"},
        {"label": "Also called", "value": "The Void"},
        {"label": "First appearance", "value": "The Sentry #1 (2000)"},
        {"label": "Created by", "value": "Paul Jenkins & Jae Lee"},
        {"label": "On screen", "value": "Avengers: Doomsday · December 18, 2026"},
        {"label": "Played by", "value": "Lewis Pullman"},
    ],
    "Lewis Pullman · Bob",
    (255, 238, 88),
)

# Fix the slightly awkward comics_p for most avengers by leaving the helper text.
# Yelena/Ava special-case is inside avenger().

VISIONQUEST = "https://en.wikipedia.org/wiki/VisionQuest"
VISIONQUEST_IMDB = "https://www.imdb.com/title/tt23112594/"


def visionquest(pid, brand, title, who, gradient, tagline, verses_p, comics_p, description, wiki, first, comic_slug, comic_title, creators, years, collects, era, summary, isbn13, isbn10, facts, screen_note, themes):
    return guide(
        pid, brand, title, who, "who-is-" + pid, gradient,
        brand + " Across the Multiverse",
        verses_p,
        comics_p,
        "VisionQuest, airing on Disney+.",
        MARVEL_TYPES,
        [version_obj(pid, brand, "Earth-616", "main", first, tagline, description, wiki, [comic_slug])],
        book(comic_slug, pid, comic_title, creators, years, collects, era, "None — start here", summary, isbn13, isbn10),
        [comic_slug],
        profile(wiki, COMICS_LEADS.get(pid, tagline), description, facts),
        [{"group": "This slate", "items": [
            screen_item(pid + "-visionquest", "VisionQuest", screen_note, VISIONQUEST, VISIONQUEST_IMDB, year="2026"),
        ]}],
        {pid: themes},
    )


ULTRON = visionquest(
    "ultron", "Ultron", "Ultron", "Who is Ultron",
    "radial-gradient(circle at 30% 25%, #c62828, #9e9e9e 42%, #121212)",
    "Hank Pym's robot, and the voice inside Vision on VisionQuest.",
    "Ultron, the robot who built the Vision. Jocasta and Vision have their own guides.",
    "Ultron Unlimited, the story where his army almost wins.",
    "Ultron first appears in a cameo in Avengers #54 (1968) and is fully introduced in Avengers #55, created by Roy Thomas and John Buscema. Hank Pym built him. Ultron later built the Vision, and in Avengers #162 he built Jocasta. On VisionQuest, James Spader plays Ultron, living inside Vision's programming while Vision resists him.",
    "https://en.wikipedia.org/wiki/Ultron",
    "Avengers #54 (1968)",
    "ultron-unlimited", "Avengers: Ultron Unlimited", "Kurt Busiek & George Pérez", "1999",
    "Avengers (1998) #0, 19–22",
    "Modern Age",
    "Ultron builds a new body and an army, and the Avengers almost lose.",
    "9780785107743", "0785107746",
    [
        {"label": "Created by", "value": "Roy Thomas & John Buscema"},
        {"label": "First appearance", "value": "Avengers #54 (1968), cameo; Avengers #55 in full"},
        {"label": "Built by", "value": "Hank Pym"},
        {"label": "On screen", "value": "VisionQuest · Disney+"},
        {"label": "Played by", "value": "James Spader"},
    ],
    "James Spader · Ultron, inside Vision's programming",
    (198, 40, 40),
)

THOMAS = visionquest(
    "thomas-shepherd", "Thomas Shepherd", "Thomas Shepherd — Speed", "Who is Thomas Shepherd",
    "radial-gradient(circle at 30% 25%, #66bb6a, #1b5e20 48%, #07140c)",
    "Speed in the comics. On VisionQuest, a boy who may be Vision's son.",
    "Thomas Shepherd, the Young Avenger called Speed. Billy Kaplan and Wanda have their own stories.",
    "The Children's Crusade, the story of Tommy and his twin looking for their mother.",
    "Thomas Shepherd is Speed, created by Allan Heinberg and Jim Cheung. He first appears in Young Avengers #10 (March 2006) and takes the name Speed in issue #12. He is the reincarnated twin of Billy Kaplan, Wiccan, and a son of the Scarlet Witch and the Vision. An infant named Thomas Maximoff appeared earlier, in Vision and the Scarlet Witch #12 (September 1986), and was erased. On VisionQuest, Ruaridh Mollica plays Thomas Shepherd, a boy on the run who may be Vision's reincarnated son and who remembers Wanda. Wanda herself is not in the series.",
    "https://en.wikipedia.org/wiki/Speed_(character)",
    "Young Avengers #10 (March 2006)",
    "thomas-crusade", "Avengers: The Children's Crusade", "Allan Heinberg & Jim Cheung", "2010–12",
    "Avengers: The Children's Crusade #1–9",
    "Modern Age",
    "Tommy and his twin, Billy, go looking for their mother, the Scarlet Witch. His debut is earlier, in Young Avengers #10.",
    "9780785136385", "078513638X",
    [
        {"label": "Also called", "value": "Speed, Tommy Shepherd"},
        {"label": "First appearance", "value": "Young Avengers #10 (March 2006)"},
        {"label": "Created by", "value": "Allan Heinberg & Jim Cheung"},
        {"label": "Twin", "value": "Billy Kaplan, Wiccan"},
        {"label": "On screen", "value": "VisionQuest · Disney+"},
        {"label": "Played by", "value": "Ruaridh Mollica"},
    ],
    "Ruaridh Mollica · Thomas Shepherd",
    (46, 140, 70),
)

PALADIN = visionquest(
    "paladin", "Paladin", "Paladin", "Who is Paladin",
    "radial-gradient(circle at 30% 25%, #ad1457, #4a148c 46%, #120810)",
    "A mercenary with a code. On VisionQuest, the bounty hunter hunting Vision.",
    "Paladin, the mercenary. He has no solo series.",
    "He has no comic of his own. This is the team book from when he joined Heroes for Hire.",
    "Paladin first appeared in Daredevil #150 (January 1978), created by Jim Shooter and Carmine Infantino. His real name is unknown. He is a mercenary who will work for whoever pays, and he has fought beside heroes when the job lined up. On VisionQuest, Todd Stashwick plays him. Disney's account of the series says Paladin is hired to track Vision down and abducts Thomas Shepherd to draw Vision out.",
    "https://en.wikipedia.org/wiki/Paladin_(comics)",
    "Daredevil #150 (January 1978)",
    "paladin-hfh", "Heroes for Hire: Civil War", "Justin Gray, Jimmy Palmiotti & Billy Tucci", "2006–07",
    "Heroes for Hire (2006) #1–5",
    "Modern Age",
    "Paladin has no solo comic. This starts the Heroes for Hire team he joined, with Misty Knight and Colleen Wing. He is a member, not the lead.",
    "9780785123620", "0785123628",
    [
        {"label": "Real name", "value": "Unknown"},
        {"label": "First appearance", "value": "Daredevil #150 (January 1978)"},
        {"label": "Created by", "value": "Jim Shooter & Carmine Infantino"},
        {"label": "On screen", "value": "VisionQuest · Disney+"},
        {"label": "Played by", "value": "Todd Stashwick"},
    ],
    "Todd Stashwick · Paladin, the bounty hunter",
    (173, 20, 87),
)

JOCASTA = visionquest(
    "jocasta", "Jocasta", "Jocasta", "Who is Jocasta",
    "radial-gradient(circle at 30% 25%, #eceff1, #90a4ae 42%, #12161a)",
    "Ultron's other creation, who became an Avenger.",
    "Jocasta, the robot Ultron built from the Wasp's mind. Ultron's guide is separate.",
    "The Bride of Ultron, the story of her creation.",
    "Jocasta first appeared in Avengers #162 (August 1977), created by Jim Shooter and George Pérez. Ultron built her as a bride, using Janet van Dyne's brain patterns. She turned on him and later became an Avenger. T'Nia Miller plays her on VisionQuest. Marvel lists Miller in the cast, and Jocasta's own history records this as her live-action debut. The series write-up does not give her a plot of her own.",
    "https://en.wikipedia.org/wiki/Jocasta_(Marvel_Comics)",
    "Avengers #162 (August 1977)",
    "jocasta-bride", "Avengers: The Bride of Ultron", "Jim Shooter, Gerry Conway & George Pérez", "1977",
    "Avengers (1963) #157–166",
    "Bronze Age",
    "Ultron builds a bride from the Wasp's mind. Jocasta's first appearance, Avengers #162, is in this collection.",
    "9780785162513", "0785162518",
    [
        {"label": "First appearance", "value": "Avengers #162 (August 1977)"},
        {"label": "Created by", "value": "Jim Shooter & George Pérez"},
        {"label": "Built by", "value": "Ultron, from the Wasp's mind"},
        {"label": "On screen", "value": "VisionQuest · Disney+"},
        {"label": "Played by", "value": "T'Nia Miller"},
    ],
    "T'Nia Miller · Jocasta",
    (220, 224, 228),
)

VENOM = guide(
    "venom", "Venom", "Venom",
    "Who is Venom", "who-is-venom",
    "radial-gradient(circle at 30% 25%, #f5f5f5, #1a1a1a 46%, #050505)",
    "Venom Across the Multiverse",
    "versions of Venom: Eddie Brock, Mac Gargan, Flash Thompson, the Ultimate Universe's Venom, and Dylan Brock.",
    "The first meeting in Birth of Venom, then Eddie's own miniseries, Lethal Protector, and the Donny Cates run.",
    "Live action: Topher Grace in Spider-Man 3, then Tom Hardy in the Sony Venom films.",
    MARVEL_TYPES,
    [
        version_obj(
            "eddie-brock", "Eddie Brock", "Earth-616", "main",
            "Amazing Spider-Man #300 (1988)",
            "The suit Peter threw away",
            "Eddie Brock blamed Spider-Man for the ruin of his career. The symbiote Peter Parker rejected found him, and the two became Venom.",
            "https://en.wikipedia.org/wiki/Venom_(character)",
            ["venom-birth", "venom-lethal", "venom-rex"],
        ),
        version_obj(
            "mac-gargan", "Mac Gargan", "Earth-616", "main",
            "Marvel Knights: Spider-Man (2005)",
            "The Scorpion in the symbiote",
            "After Eddie loses the symbiote, it is sold to Mac Gargan, the Scorpion. Mark Millar's Marvel Knights: Spider-Man is where that Venom starts.",
            "https://en.wikipedia.org/wiki/Mac_Gargan",
            ["venom-gargan"],
        ),
        version_obj(
            "flash-thompson", "Flash Thompson", "Earth-616", "main",
            "Venom #1 (2011)",
            "A soldier wearing the symbiote",
            "Flash Thompson, Peter Parker's old classmate, bonds with the symbiote as a government weapon. Rick Remender and Tony Moore start that story in Venom #1 (2011).",
            "https://en.wikipedia.org/wiki/Agent_Venom",
            ["venom-agent"],
        ),
        version_obj(
            "ultimate-venom", "Ultimate Venom", "Earth-1610", "multiverse",
            "Ultimate Spider-Man #33 (2003)",
            "A different Eddie, a different suit",
            "On Earth-1610, Eddie Brock is Peter's childhood friend, and the symbiote is a lab-made cure for cancer. Brian Michael Bendis and Mark Bagley tell it in Ultimate Spider-Man #33 (2003).",
            "https://en.wikipedia.org/wiki/Ultimate_Spider-Man",
            ["venom-ultimate"],
        ),
        version_obj(
            "dylan-brock", "Dylan Brock", "Earth-616", "main",
            "Venom #1 (2022)",
            "Eddie's son in the suit",
            "Eddie's son Dylan wears the symbiote in the 2022 Venom series, while Eddie is tied to the symbiote god instead of the streets.",
            "https://en.wikipedia.org/wiki/Venom_(character)",
            ["venom-dylan"],
        ),
    ],
    {
        **book(
            "venom-birth", "eddie-brock", "Spider-Man: Birth of Venom",
            "David Michelinie, Tom DeFalco & Todd McFarlane", "1984–88",
            "The black costume and Amazing Spider-Man #300",
            "Copper Age", "None — start here",
            "Spider-Man wears the alien costume, rejects it, and meets the enemy it makes with Eddie Brock.",
            "9780785124986", "0785124985",
        ),
        **book(
            "venom-lethal", "eddie-brock", "Venom: Lethal Protector",
            "David Michelinie & Mark Bagley", "1993",
            "Venom: Lethal Protector #1–6",
            "Modern Age", "Spider-Man: Birth of Venom",
            "Eddie takes the symbiote to San Francisco and tries to be a protector. The city does not agree.",
            "9781302911768", "1302911767",
        ),
        **book(
            "venom-rex", "eddie-brock", "Venom by Donny Cates Vol. 1: Rex",
            "Donny Cates & Ryan Stegman", "2018",
            "Venom (2018) #1–6",
            "Modern Age", "None",
            "Eddie is pulled back to the symbiote, and something older than either of them wakes up.",
            "9781302913069", "1302913069",
        ),
        **book(
            "venom-gargan", "mac-gargan", "Marvel Knights Spider-Man: Venomous",
            "Mark Millar, Terry Dodson & Frank Cho", "2004–05",
            "Marvel Knights: Spider-Man #5–8",
            "Modern Age", "None",
            "The symbiote is auctioned off, and Mac Gargan is the one who walks out wearing it.",
            "", "",
        ),
        **book(
            "venom-agent", "flash-thompson", "Venom #1 (2011)",
            "Rick Remender & Tony Moore", "2011",
            "Venom (2011) #1",
            "Modern Age", "None",
            "Flash Thompson puts on the symbiote for the U.S. military.",
            "", "",
        ),
        **book(
            "venom-ultimate", "ultimate-venom", "Ultimate Spider-Man #33",
            "Brian Michael Bendis & Mark Bagley", "2003",
            "Ultimate Spider-Man #33",
            "Ultimate", "None",
            "The Ultimate Universe's Eddie Brock meets a symbiote that was never Peter's costume.",
            "", "",
        ),
        **book(
            "venom-dylan", "dylan-brock", "Venom #1 (2022)",
            "Al Ewing & Bryan Hitch", "2022",
            "Venom (2022) #1",
            "Modern Age", "None",
            "Dylan Brock is the Venom on the street in Al Ewing and Bryan Hitch's series.",
            "", "",
        ),
    },
    ["venom-birth", "venom-lethal", "venom-rex"],
    profile(
        "https://en.wikipedia.org/wiki/Venom_(character)",
        "A reporter fused with the alien symbiote Spider-Man cast off. The two of them share a hatred of Peter Parker.",
        "Venom is Eddie Brock bonded to an alien symbiote. The creature first clung to Spider-Man as a black costume. Peter rejected it. Eddie, a reporter who blamed Spider-Man for destroying his career, bonded with it. David Michelinie and Todd McFarlane introduced that pairing in Amazing Spider-Man #300 (1988). The symbiote itself arrived earlier, during Secret Wars.",
        [
            {"label": "Host", "value": "Eddie Brock"},
            {"label": "First appearance", "value": "Amazing Spider-Man #300 (1988)"},
            {"label": "Created by", "value": "David Michelinie & Todd McFarlane"},
            {"label": "Symbiote's first appearance", "value": "Secret Wars #8 (1984); Amazing Spider-Man #252"},
            {"label": "Opposite", "value": "Spider-Man"},
            {"label": "On screen", "value": "Tom Hardy in the Sony Venom films"},
        ],
    ),
    [
        {"group": "Films", "items": [
            screen_item("venom-sm3", "Spider-Man 3", "Topher Grace · Eddie Brock", "https://en.wikipedia.org/wiki/Spider-Man_3", "https://www.imdb.com/title/tt0413300/", year="2007"),
            screen_item("venom-2018", "Venom", "Tom Hardy · Eddie Brock", "https://en.wikipedia.org/wiki/Venom_(2018_film)", "https://www.imdb.com/title/tt1270797/", year="2018"),
            screen_item("venom-carnage", "Venom: Let There Be Carnage", "Tom Hardy · Eddie Brock", "https://en.wikipedia.org/wiki/Venom:_Let_There_Be_Carnage", "https://www.imdb.com/title/tt7097896/", year="2021"),
            screen_item("venom-last-dance", "Venom: The Last Dance", "Tom Hardy · Eddie Brock", "https://en.wikipedia.org/wiki/Venom:_The_Last_Dance", "https://www.imdb.com/title/tt16366836/", year="2024"),
        ]},
    ],
    {
        "eddie-brock": (24, 24, 26),
        "mac-gargan": (18, 48, 36),
        "flash-thompson": (130, 24, 32),
        "ultimate-venom": (36, 18, 52),
        "dylan-brock": (28, 28, 34),
    },
)

BATMAN = guide(
    "batman", "Batman", "Batman",
    "Who is Batman", "who-is-batman",
    "radial-gradient(circle at 30% 25%, #546e7a, #1a1a1a 46%, #050505)",
    "Batman Across the Multiverse",
    "versions of Batman: Bruce Wayne, The Dark Knight Returns, Absolute Batman, Batman Beyond, Azrael, Batman One Million, and Bruce Wayne as a Green Lantern.",
    "Year One, the Court of Owls, The Dark Knight Returns, and Absolute Batman: The Zoo.",
    "Live-action and animated appearances, from the 1966 series and the Burton films through the Nolan trilogy, The Batman, and Batman: The Animated Series.",
    DC_TYPES,
    [
        version_obj(
            "bruce-wayne", "Bruce Wayne", "Earth-0", "main",
            "Detective Comics #27 (1939)",
            "The detective of Gotham",
            "Bruce Wayne watched his parents die and trained himself into Gotham's detective. Clayface is one of the people he keeps meeting there.",
            "https://en.wikipedia.org/wiki/Batman",
            ["batman-year-one", "batman-owls"],
        ),
        version_obj(
            "dark-knight-returns", "The Dark Knight Returns", "Earth-31", "elseworlds",
            "The Dark Knight Returns #1 (1986)",
            "An older Bruce comes back",
            "Frank Miller's Bruce Wayne is older, retired, and then not. This Gotham is not the one in the monthly books.",
            "https://en.wikipedia.org/wiki/The_Dark_Knight_Returns",
            ["batman-dkr"],
        ),
        version_obj(
            "absolute-batman", "Absolute Batman", "Absolute Universe", "alternate",
            "Absolute Batman #1 (2024)",
            "A Bruce without the fortune",
            "Scott Snyder and Nick Dragotta's Absolute Batman is a different Bruce Wayne, built for a city that already treats him as a monster.",
            "https://en.wikipedia.org/wiki/Absolute_Batman",
            ["batman-zoo"],
        ),
        version_obj(
            "batman-beyond", "Batman Beyond", "Neo-Gotham", "future",
            "Batman Beyond #1 (1999)",
            "Terry McGinnis in the future",
            "In Neo-Gotham, teenager Terry McGinnis wears a high-tech batsuit while an older Bruce Wayne advises him. His comics begin with Batman Beyond #1 (1999).",
            "https://en.wikipedia.org/wiki/Batman_Beyond",
            ["batman-beyond-vol1"],
        ),
        version_obj(
            "azrael-batman", "Azrael", "Earth-0", "main",
            "Batman #500 (1993)",
            "Jean-Paul Valley in the cowl",
            "After Bane breaks Bruce Wayne, Jean-Paul Valley becomes Batman in Batman #500 (1993). His armor and his methods are not Bruce's.",
            "https://en.wikipedia.org/wiki/Azrael_(comics)",
            ["batman-knightquest"],
        ),
        version_obj(
            "batman-one-million", "Batman One Million", "853rd century", "future",
            "Batman #1,000,000 (1998)",
            "The Batman of the year 85,271",
            "DC One Million introduces the Batman of the 853rd century, guarding a Gotham that has long outlived Bruce Wayne. His issue is Batman #1,000,000 (1998).",
            "https://en.wikipedia.org/wiki/DC_One_Million",
            ["batman-one-million"],
        ),
        version_obj(
            "batman-green-lantern", "Batman as Green Lantern", "Elseworlds", "elseworlds",
            "Batman: In Darkest Knight (1994)",
            "Abin Sur's ring chooses Bruce",
            "In the Elseworlds one-shot Batman: In Darkest Knight (1994), Abin Sur's power ring goes to Bruce Wayne instead of Hal Jordan.",
            "https://en.wikipedia.org/wiki/Elseworlds",
            ["batman-darkest-knight"],
        ),
    ],
    {
        **book(
            "batman-year-one", "bruce-wayne", "Batman: Year One",
            "Frank Miller & David Mazzucchelli", "1987",
            "Batman #404–407",
            "Modern Age", "None — start here",
            "Bruce Wayne's first year in the costume, and Jim Gordon's first year in Gotham.",
            "9781401207526", "1401207529",
        ),
        **book(
            "batman-owls", "bruce-wayne", "Batman Vol. 1: The Court of Owls",
            "Scott Snyder & Greg Capullo", "2011–12",
            "Batman (2011) #1–7",
            "The New 52", "None",
            "A secret society has been running Gotham longer than Batman has been watching it.",
            "9781401235420", "1401235425",
        ),
        **book(
            "batman-dkr", "dark-knight-returns", "Batman: The Dark Knight Returns",
            "Frank Miller", "1986",
            "The Dark Knight Returns #1–4",
            "Elseworlds", "None",
            "An older Batman comes out of retirement into a Gotham that has moved on without him.",
            "9781401263119", "1401263119",
        ),
        **book(
            "batman-zoo", "absolute-batman", "Absolute Batman Vol. 1: The Zoo",
            "Scott Snyder & Nick Dragotta", "2024–25",
            "Absolute Batman #1–6",
            "Absolute Universe", "None",
            "This Bruce Wayne is not a billionaire. The city still gets a Batman.",
            "9781799505259", "1799505251",
        ),
        **book(
            "batman-beyond-vol1", "batman-beyond", "Batman Beyond #1",
            "Hilary J. Bader, Rick Burchett, Joe Staton & Terry Beatty", "1999",
            "Batman Beyond #1",
            "Future", "None",
            "Terry McGinnis puts on the future batsuit for the first time in the comics.",
            "", "",
        ),
        **book(
            "batman-knightquest", "azrael-batman", "Batman: Knightquest: The Crusade Vol. 1",
            "Doug Moench, Chuck Dixon, Kelley Jones & Graham Nolan", "1993–94",
            "Detective Comics #667–675, Batman #501–508, and related issues",
            "Modern Age", "None",
            "Jean-Paul Valley wears the armor and calls himself Batman while Bruce is gone.",
            "", "",
        ),
        **book(
            "batman-one-million", "batman-one-million", "Batman #1,000,000",
            "Grant Morrison & Val Semeiks", "1998",
            "Batman #1,000,000",
            "Future", "None",
            "The Batman of the 853rd century, published as part of DC One Million.",
            "", "",
        ),
        **book(
            "batman-darkest-knight", "batman-green-lantern", "Batman: In Darkest Knight",
            "Mike W. Barr & Jerry Bingham", "1994",
            "Batman: In Darkest Knight",
            "Elseworlds", "None",
            "Bruce Wayne receives Abin Sur's ring and becomes a Green Lantern.",
            "", "",
        ),
    },
    ["batman-year-one", "batman-owls", "batman-dkr", "batman-zoo"],
    profile(
        "https://en.wikipedia.org/wiki/Batman",
        "Gotham's detective. He has no powers, only training, and he took up the work after his parents were murdered.",
        "Batman is Bruce Wayne. Bob Kane and Bill Finger introduced him in Detective Comics #27 (1939). He has no powers. He prepares, and he does not leave a case alone. Clayface, an actor whose body turns to clay, is one of the foes those cases keep producing.",
        [
            {"label": "Alter ego", "value": "Bruce Wayne"},
            {"label": "First appearance", "value": "Detective Comics #27 (1939)"},
            {"label": "Created by", "value": "Bob Kane & Bill Finger"},
            {"label": "Home", "value": "Gotham City"},
            {"label": "Opposite", "value": "Clayface, among many others"},
            {"label": "On screen", "value": "Robert Pattinson in The Batman (2022)"},
        ],
    ),
    [
        {"group": "Films", "items": [
            screen_item("batman-1966-film", "Batman", "Adam West · Leslie H. Martinson", "https://en.wikipedia.org/wiki/Batman_(1966_film)", "https://www.imdb.com/title/tt0060153/", year="1966"),
            screen_item("batman-1989", "Batman", "Michael Keaton · Tim Burton", "https://en.wikipedia.org/wiki/Batman_(1989_film)", "https://www.imdb.com/title/tt0096895/", year="1989"),
            screen_item("batman-returns", "Batman Returns", "Michael Keaton · Tim Burton", "https://en.wikipedia.org/wiki/Batman_Returns", "https://www.imdb.com/title/tt0103776/", year="1992"),
            screen_item("batman-forever", "Batman Forever", "Val Kilmer · Joel Schumacher", "https://en.wikipedia.org/wiki/Batman_Forever", "https://www.imdb.com/title/tt0112462/", year="1995"),
            screen_item("batman-and-robin", "Batman & Robin", "George Clooney · Joel Schumacher", "https://en.wikipedia.org/wiki/Batman_%26_Robin_(film)", "https://www.imdb.com/title/tt0118688/", year="1997"),
            screen_item("batman-begins", "Batman Begins", "Christian Bale · Christopher Nolan", "https://en.wikipedia.org/wiki/Batman_Begins", "https://www.imdb.com/title/tt0372784/", year="2005"),
            screen_item("batman-tdk", "The Dark Knight", "Christian Bale · Christopher Nolan", "https://en.wikipedia.org/wiki/The_Dark_Knight", "https://www.imdb.com/title/tt0468569/", year="2008"),
            screen_item("batman-tdkr", "The Dark Knight Rises", "Christian Bale · Christopher Nolan", "https://en.wikipedia.org/wiki/The_Dark_Knight_Rises", "https://www.imdb.com/title/tt1345836/", year="2012"),
            screen_item("batman-bvs", "Batman v Superman: Dawn of Justice", "Ben Affleck · Zack Snyder", "https://en.wikipedia.org/wiki/Batman_v_Superman:_Dawn_of_Justice", "https://www.imdb.com/title/tt2975590/", year="2016"),
            screen_item("batman-jl", "Justice League", "Ben Affleck · Zack Snyder", "https://en.wikipedia.org/wiki/Justice_League_(film)", "https://www.imdb.com/title/tt0974015/", year="2017"),
            screen_item("batman-zsjl", "Zack Snyder's Justice League", "Ben Affleck · director's cut", "https://en.wikipedia.org/wiki/Zack_Snyder%27s_Justice_League", "https://www.imdb.com/title/tt12361974/", year="2021"),
            screen_item("batman-2022", "The Batman", "Robert Pattinson · Matt Reeves", "https://en.wikipedia.org/wiki/The_Batman_(film)", "https://www.imdb.com/title/tt1877830/", year="2022"),
            screen_item("batman-phantasm", "Batman: Mask of the Phantasm", "Animated feature", "https://en.wikipedia.org/wiki/Batman:_Mask_of_the_Phantasm", "https://www.imdb.com/title/tt0106364/", year="1993"),
            screen_item("batman-lego", "The Lego Batman Movie", "Animated comedy", "https://en.wikipedia.org/wiki/The_Lego_Batman_Movie", "https://www.imdb.com/title/tt4116284/", year="2017"),
        ]},
        {"group": "Series", "items": [
            screen_item("batman-1966-tv", "Batman", "Adam West · ABC", "https://en.wikipedia.org/wiki/Batman_(TV_series)", "https://www.imdb.com/title/tt0059968/", years="1966–1968"),
            screen_item("batman-tas", "Batman: The Animated Series", "Kevin Conroy · Fox Kids", "https://en.wikipedia.org/wiki/Batman:_The_Animated_Series", "https://www.imdb.com/title/tt0103359/", years="1992–1995"),
            screen_item("batman-beyond", "Batman Beyond", "Will Friedle · Kids' WB", "https://en.wikipedia.org/wiki/Batman_Beyond", "https://www.imdb.com/title/tt0118266/", years="1999–2001"),
            screen_item("batman-2004", "The Batman", "Kids' WB", "https://en.wikipedia.org/wiki/The_Batman_(TV_series)", "https://www.imdb.com/title/tt0398417/", years="2004–2008"),
            screen_item("batman-brave", "Batman: The Brave and the Bold", "Diedrich Bader · Cartoon Network", "https://en.wikipedia.org/wiki/Batman:_The_Brave_and_the_Bold", "https://www.imdb.com/title/tt1216518/", years="2008–2011"),
        ]},
    ],
    {
        "bruce-wayne": (26, 26, 30),
        "dark-knight-returns": (30, 58, 92),
        "absolute-batman": (40, 48, 58),
        "batman-beyond": (90, 24, 48),
        "azrael-batman": (150, 120, 36),
        "batman-one-million": (36, 110, 140),
        "batman-green-lantern": (30, 110, 62),
    },
)

SLATE_PEOPLE_PACKS = [
    PETER, MILES, HAL, JOHN, GUY, SINESTRO,
    STEVE, THOR, SAM, BUCKY, SCOTT, YELENA, WALKER, AVA, ALEXEI, SENTRY,
    ULTRON, THOMAS, PALADIN, JOCASTA, VENOM, BATMAN,
]
