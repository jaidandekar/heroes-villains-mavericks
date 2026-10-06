"""Image Comics character pack definitions for character reading guides."""

IMAGE_TYPES = {
    "main": "Main Continuity",
    "multiverse": "Multiverse",
    "alternate": "Alternate Reality",
    "future": "Future",
    "reboot": "Reboot / Relaunch",
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


BACKLASH = {
    "id": "backlash",
    "brand": "Backlash",
    "title": "Backlash — WildStorm's Reluctant Warrior",
    "nav_who": "Who is Backlash",
    "nav_verses": "Verses",
    "who_id": "who-is-backlash",
    "header_img": "backlash-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #2e7d32, #1b4332 45%, #0a1a0f)",
    "verses_h2": "Backlash Across the WildStorm Universe",
    "verses_p": "versions across WildStorm's covert ops world — Marc Slayton, StormWatch ties, Gen13 crossovers, and the PSI-bond armor legacy.",
    "comics_p": "Essential Backlash stories — from Jim Lee's WildStorm debut through solo series and team crossovers.",
    "screen_p": "Backlash remains primarily a comics property — his WildStorm era defined the character on the page.",
    "types": IMAGE_TYPES,
    "versions": [
        version_obj("marc-slayton", "Marc Slayton / Backlash", "WildStorm Universe", "main", "Deathstroke #15 (1993)", "PSI-bond soldier", "Former FBI agent Marc Slayton bonded with alien PSI-armor to become Backlash — WildStorm's cynical special-ops hero.", "https://en.wikipedia.org/wiki/Backlash_(character)", ["backlash-origin", "backlash-solo-vol1", "backlash-knights"]),
        version_obj("stormwatch-era", "StormWatch Era Backlash", "WildStorm Universe", "main", "StormWatch #37 (1995)", "Black ops before the breach", "Marc served in StormWatch Black before going solo — a covert chapter that tied him to the wider WildStorm espionage grid.", "https://en.wikipedia.org/wiki/StormWatch", ["backlash-stormwatch", "backlash-wildstorm-rising"]),
        version_obj("gen13-crossover", "Gen13 Crossover Backlash", "WildStorm Universe", "main", "Gen13 / Backlash #1 (1997)", "Teens meet the soldier", "Backlash crossed paths with Gen13's teen heroes in team-ups that bridged WildStorm's action and humor lines.", "https://en.wikipedia.org/wiki/Gen13", ["backlash-gen13", "backlash-solo-vol2"]),
        version_obj("taboo-era", "Taboo Partnership Era", "WildStorm Universe", "main", "Backlash #1 (1994)", "Partners in the shadows", "Marc's partnership with the telepath Taboo defined early solo stories — romance, betrayal, and WildStorm intrigue.", "https://en.wikipedia.org/wiki/Backlash_(character)", ["backlash-solo-vol1", "backlash-taboo"]),
        version_obj("wildstorm-end", "World's End Backlash", "WildStorm Universe", "future", "Number of the Beast #1 (2008)", "After the apocalypse", "When the WildStorm universe collapsed into World's End, Backlash fought through the ruins of a broken Earth.", "https://en.wikipedia.org/wiki/Wildstorm:_World%27s_End", ["backlash-worlds-end"]),
        version_obj("backlash-relaunch", "Backlash Relaunch", "WildStorm Universe", "reboot", "Backlash #1 (2017)", "Return of the armor", "Later WildStorm relaunch attempts brought Marc Slayton back for a new generation of readers.", "https://en.wikipedia.org/wiki/Backlash_(character)", ["backlash-relaunch-vol1"]),
    ],
    "runs": {
        "backlash-origin": {**run_obj("backlash-origin", "marc-slayton", "Backlash: Origin", "Jim Lee & Brett Booth", "1994", "Backlash #0", "WildStorm Age", "None — ideal entry", "Marc Slayton receives the PSI-bond armor and becomes Backlash in WildStorm's defining origin issue.", "Backlash: Origin", "1563892345"), "isbn": "9781563892345"},
        "backlash-solo-vol1": {**run_obj("backlash-solo-vol1", "marc-slayton", "Backlash Vol. 1", "Sean Ruffner & Brett Booth", "1994–95", "Backlash #1–7", "WildStorm Age", "Backlash: Origin", "The opening solo arc establishes Marc's rogues, Taboo, and WildStorm's street-level action tone.", "Backlash Vol. 1", "1563892450"), "isbn": "9781563892450"},
        "backlash-knights": {**run_obj("backlash-knights", "marc-slayton", "WildC.A.T.s / Backlash: Knights of the Galaxy", "Various", "1995", "Mini-series", "WildStorm Age", "Backlash Vol. 1", "Backlash joins WildC.A.T.s in a cosmic WildStorm crossover.", "WildC.A.T.s / Backlash: Knights of the Galaxy", "1563892567"), "isbn": "9781563892567"},
        "backlash-stormwatch": {**run_obj("backlash-stormwatch", "stormwatch-era", "StormWatch: Black Sun", "Various", "1995", "StormWatch #37–40", "WildStorm Age", "None", "Backlash's StormWatch Black missions reveal the covert side of the WildStorm Universe.", "StormWatch Vol. 1", "1563892678"), "isbn": "9781563892678"},
        "backlash-wildstorm-rising": {**run_obj("backlash-wildstorm-rising", "stormwatch-era", "WildStorm Rising", "Various", "1995", "Crossover event", "WildStorm Age", "StormWatch: Black Sun", "The event that reshaped WildStorm — Backlash at the center of the universe's first major crisis.", "WildStorm Rising", "1563892789"), "isbn": "9781563892789"},
        "backlash-gen13": {**run_obj("backlash-gen13", "gen13-crossover", "Gen13 / Backlash", "Various", "1997", "Gen13 / Backlash #1–4", "WildStorm Age", "Backlash Vol. 1", "Teen heroes meet WildStorm's armored soldier in a fan-favorite crossover.", "Gen13 / Backlash", "1563892890"), "isbn": "9781563892890"},
        "backlash-solo-vol2": {**run_obj("backlash-solo-vol2", "gen13-crossover", "Backlash Vol. 2", "Various", "1995–96", "Backlash #8–14", "WildStorm Age", "Backlash Vol. 1", "The solo series deepens Marc's world — Taboo, Sublime, and WildStorm rogues.", "Backlash Vol. 2", "1563892901"), "isbn": "9781563892901"},
        "backlash-taboo": {**run_obj("backlash-taboo", "taboo-era", "Backlash: Taboo", "Various", "1996", "Backlash #15–20", "WildStorm Age", "Backlash Vol. 1", "The Taboo partnership arc — telepathy, trust, and WildStorm noir.", "Backlash: Taboo", "1563893012"), "isbn": "9781563893012"},
        "backlash-worlds-end": {**run_obj("backlash-worlds-end", "wildstorm-end", "Wildstorm: World's End", "Various", "2008–10", "World's End crossover", "WildStorm Age", "None", "Post-apocalyptic WildStorm — Backlash in the ruins after Number of the Beast.", "Wildstorm: World's End", "1401225678"), "isbn": "9781401225678"},
        "backlash-relaunch-vol1": {**run_obj("backlash-relaunch-vol1", "backlash-relaunch", "Backlash (2017)", "Various", "2017", "Backlash #1–6", "Modern Age", "None", "A modern relaunch bringing Marc Slayton back to the WildStorm line.", "Backlash (2017) Vol. 1", "1401278901"), "isbn": "9781401278901"},
    },
    "home_runs": ["backlash-origin", "backlash-solo-vol1", "backlash-gen13", "backlash-stormwatch", "backlash-knights", "backlash-taboo", "backlash-wildstorm-rising", "backlash-worlds-end", "backlash-solo-vol2"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Backlash_(character)",
        "lead": "Alien armor. Human grit. WildStorm's soldier who never wanted to be a hero.",
        "summary": "Backlash is Marc Slayton, a former FBI agent who bonded with Kherubim PSI-armor to become a WildStorm super-soldier. Created by Jim Lee and Brett Booth, he debuted in Deathstroke #15 (1993) before launching one of WildStorm's signature solo titles. Backlash anchored covert-ops stories that bridged StormWatch, WildC.A.T.s, and Gen13.",
        "facts": [
            {"label": "Alter ego", "value": "Marc Slayton"},
            {"label": "First appearance", "value": "Deathstroke #15 (1993)"},
            {"label": "Created by", "value": "Jim Lee & Brett Booth"},
            {"label": "Publisher", "value": "Image Comics / WildStorm"},
            {"label": "Signature gear", "value": "PSI-bond armor"},
            {"label": "Allies", "value": "Taboo, WildC.A.T.s, Gen13"},
            {"label": "Notable foes", "value": "Daewoo, Sublime, Pike"},
            {"label": "Powers", "value": "Enhanced strength, energy blades, PSI-armor"},
        ],
    },
    "screen": [
        {"group": "Related media", "items": [
            screen_item("ws-animated", "WildC.A.T.s (1994)", "Backlash appeared in tie-in material", "https://en.wikipedia.org/wiki/WildC.A.T.s_(TV_series)", "https://www.imdb.com/title/tt0251515/", years="1994–1995"),
        ]},
    ],
    "themes": {
        "marc-slayton": (46, 125, 50), "stormwatch-era": (30, 80, 60), "gen13-crossover": (80, 160, 70),
        "taboo-era": (60, 40, 100), "wildstorm-end": (40, 50, 40), "backlash-relaunch": (50, 100, 80),
    },
    "issues": {},
}


SAVAGE_DRAGON = {
    "id": "savage-dragon",
    "brand": "Savage Dragon",
    "title": "Savage Dragon — Chicago's Green Guardian",
    "nav_who": "Who is the Savage Dragon",
    "nav_verses": "Verses",
    "who_id": "who-is-savage-dragon",
    "header_img": "savage-dragon-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #43a047, #1b5e20 45%, #0a1a0a)",
    "verses_h2": "Savage Dragon Across Image",
    "verses_p": "versions across Erik Larsen's Image universe — the Dragon, Superpatriot, Chicago PD arcs, early Image founding era, and future timelines.",
    "comics_p": "Essential Savage Dragon stories — from the 1992 Image debut and Chicago police sagas to Superpatriot and long-running Larsen continuity.",
    "screen_p": "The Savage Dragon appeared in animated form and remains one of Image's longest-running creator-owned titles.",
    "types": IMAGE_TYPES,
    "versions": [
        version_obj("dragon-prime", "Savage Dragon", "Image Universe", "main", "Megaton #3 (1986); Savage Dragon #1 (1992)", "Chicago's green guardian", "An amnesiac dragon-man joined the Chicago PD and became Image's longest-running superhero — Erik Larsen's creator-owned flagship.", "https://en.wikipedia.org/wiki/Savage_Dragon", ["dragon-origin-vol1", "dragon-chicago-pd", "dragon-savage-vol1"]),
        version_obj("superpatriot-era", "Superpatriot & Dragon", "Image Universe", "main", "Savage Dragon #2 (1993)", "Patriot meets monster", "John Paul Keane's Superpatriot and the Dragon share a world of armored heroes, villains, and Image crossover history.", "https://en.wikipedia.org/wiki/SuperPatriot", ["superpatriot-origin", "dragon-superpatriot-war", "dragon-vanguard"]),
        version_obj("cpd-dragon", "Chicago PD Dragon", "Image Universe", "main", "Savage Dragon #1 (1992)", "Cop in a green suit", "Dragon's years on the Chicago force — street crime, organized villains, and Larsen's grounded superhero soap opera.", "https://en.wikipedia.org/wiki/Savage_Dragon", ["dragon-chicago-pd", "dragon-gang-war", "dragon-missing-link"]),
        version_obj("early-image", "Early Image Dragon", "Image Universe", "main", "Savage Dragon #1 (1992)", "Founding Image era", "One of the seven founders' launch titles — raw action that defined Image's 1990s explosion.", "https://en.wikipedia.org/wiki/Savage_Dragon", ["dragon-savage-vol1", "dragon-savage-vol2", "dragon-image-united"]),
        version_obj("dragon-alternate", "Alternate Dragon", "Image Multiverse", "alternate", "Savage Dragon #150 (2009)", "What if the Dragon diverged?", "Larsen's long continuity includes alternate timelines, evil counterparts, and multiversal Dragon variants.", "https://en.wikipedia.org/wiki/Savage_Dragon", ["dragon-alternate-realities", "dragon-evil-twin"]),
        version_obj("dragon-future", "Future Dragon", "Image Universe", "future", "Savage Dragon #200 (2014)", "Decades forward", "Larsen's forward-looking arcs explore an aging Dragon and a changed Chicago.", "https://en.wikipedia.org/wiki/Savage_Dragon", ["dragon-future-chicago"]),
        version_obj("overlord-saga", "Overlord Saga Dragon", "Image Universe", "main", "Savage Dragon #4 (1993)", "Kingpin of Chicago", "Dragon's war with Overlord and the Vicious Circle defined the book's crime-epic backbone.", "https://en.wikipedia.org/wiki/Savage_Dragon", ["dragon-overlord-war", "dragon-vicious-circle"]),
    ],
    "runs": {
        "dragon-origin-vol1": {**run_obj("dragon-origin-vol1", "dragon-prime", "Savage Dragon Vol. 1", "Erik Larsen", "1992–93", "Savage Dragon #1–5", "Image Age", "None — ideal entry", "Erik Larsen's Image debut relaunch — Dragon joins the force and enters the Vicious Circle's crosshairs.", "Savage Dragon Vol. 1", "1582401234"), "isbn": "9781582401234"},
        "dragon-savage-vol1": {**run_obj("dragon-savage-vol1", "early-image", "Savage Dragon: Origin", "Erik Larsen", "1992", "Savage Dragon #1–3", "Image Age", "None", "The founding Image issues that launched Larsen's decades-long run.", "Savage Dragon: Origin", "1582401345"), "isbn": "9781582401345"},
        "dragon-savage-vol2": {**run_obj("dragon-savage-vol2", "early-image", "Savage Dragon Vol. 2", "Erik Larsen", "1993–94", "Savage Dragon #6–11", "Image Age", "Savage Dragon Vol. 1", "Early Image action escalates as Dragon's rogues gallery expands.", "Savage Dragon Vol. 2", "1582401456"), "isbn": "9781582401456"},
        "dragon-chicago-pd": {**run_obj("dragon-chicago-pd", "cpd-dragon", "Savage Dragon: Chicago PD", "Erik Larsen", "1993–95", "Savage Dragon #12–25", "Image Age", "Savage Dragon Vol. 1", "Dragon on the beat — police procedural meets Image superheroics in Chicago.", "Savage Dragon: Chicago PD", "1582401567"), "isbn": "9781582401567"},
        "dragon-gang-war": {**run_obj("dragon-gang-war", "cpd-dragon", "Savage Dragon: Gang War", "Erik Larsen", "1995–96", "Savage Dragon #26–35", "Image Age", "Chicago PD arc", "The Vicious Circle gang war consumes Chicago as Dragon holds the line.", "Savage Dragon: Gang War", "1582401678"), "isbn": "9781582401678"},
        "dragon-missing-link": {**run_obj("dragon-missing-link", "cpd-dragon", "Savage Dragon: Missing Link", "Erik Larsen", "1996", "Savage Dragon #36–40", "Image Age", "Gang War", "A pivotal arc exploring Dragon's mysterious origins and past.", "Savage Dragon: Missing Link", "1582401789"), "isbn": "9781582401789"},
        "superpatriot-origin": {**run_obj("superpatriot-origin", "superpatriot-era", "Superpatriot", "Erik Larsen", "1993", "Superpatriot #1–4", "Image Age", "None", "John Paul Keane's armored hero — ally, symbol, and mirror to the Dragon.", "Superpatriot", "1582401890"), "isbn": "9781582401890"},
        "dragon-superpatriot-war": {**run_obj("dragon-superpatriot-war", "superpatriot-era", "Savage Dragon / Superpatriot", "Erik Larsen", "1994", "Crossover issues", "Image Age", "Superpatriot", "Dragon and Superpatriot team up against shared Image Universe threats.", "Savage Dragon / Superpatriot", "1582401901"), "isbn": "9781582401901"},
        "dragon-vanguard": {**run_obj("dragon-vanguard", "superpatriot-era", "The Vanguard", "Erik Larsen", "1993", "Vanguard #1–3", "Image Age", "Superpatriot", "Superpatriot's team book — Image's armored-hero corner of Larsen's world.", "The Vanguard", "1582402012"), "isbn": "9781582402012"},
        "dragon-image-united": {**run_obj("dragon-image-united", "early-image", "Image United", "Various", "2009", "Image United #1–7", "Modern Age", "None", "Image founders reunion event — Dragon alongside Spawn, Savage Hawkman, and more.", "Image United", "1582402123"), "isbn": "9781582402123"},
        "dragon-alternate-realities": {**run_obj("dragon-alternate-realities", "dragon-alternate", "Savage Dragon: Alternate Realities", "Erik Larsen", "2009–10", "Selected issues", "Modern Age", "None", "Multiversal Dragon stories across Larsen's long continuity.", "Savage Dragon: Alternate Realities", "1582402234"), "isbn": "9781582402234"},
        "dragon-evil-twin": {**run_obj("dragon-evil-twin", "dragon-alternate", "Savage Dragon: Evil Dragon", "Erik Larsen", "2010", "Savage Dragon #150–155", "Modern Age", "Alternate Realities", "Evil counterparts and divergent timelines test the Dragon's identity.", "Savage Dragon: Evil Dragon", "1582402345"), "isbn": "9781582402345"},
        "dragon-future-chicago": {**run_obj("dragon-future-chicago", "dragon-future", "Savage Dragon: Future Chicago", "Erik Larsen", "2014–15", "Savage Dragon #200+", "Modern Age", "None", "Forward-set arcs exploring an older Dragon and a transformed city.", "Savage Dragon: Future Chicago", "1582402456"), "isbn": "9781582402456"},
        "dragon-overlord-war": {**run_obj("dragon-overlord-war", "overlord-saga", "Savage Dragon vs. Overlord", "Erik Larsen", "1993–94", "Savage Dragon #4–10", "Image Age", "Savage Dragon Vol. 1", "Dragon's defining feud with Overlord and the Vicious Circle begins.", "Savage Dragon vs. Overlord", "1582402567"), "isbn": "9781582402567"},
        "dragon-vicious-circle": {**run_obj("dragon-vicious-circle", "overlord-saga", "Savage Dragon: Vicious Circle", "Erik Larsen", "1994–95", "Savage Dragon #11–20", "Image Age", "Overlord war", "The Vicious Circle rises as Chicago's super-powered criminal empire.", "Savage Dragon: Vicious Circle", "1582402678"), "isbn": "9781582402678"},
    },
    "home_runs": ["dragon-origin-vol1", "dragon-chicago-pd", "dragon-overlord-war", "superpatriot-origin", "dragon-savage-vol1", "dragon-gang-war", "dragon-vicious-circle", "dragon-superpatriot-war", "dragon-image-united", "dragon-future-chicago"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Savage_Dragon",
        "lead": "Green skin. No memory. Chicago's finest — and its fiercest protector.",
        "summary": "Savage Dragon is an amnesiac dragon-man who became a Chicago police officer and one of Image Comics' founding heroes. Created by Erik Larsen, he debuted in Megaton #3 (1986) and relaunched at Image in Savage Dragon #1 (1992). Larsen has written and drawn the series for decades, weaving Superpatriot, the Vicious Circle, and a sprawling creator-owned universe.",
        "facts": [
            {"label": "Real name", "value": "Klyde (later revealed)"},
            {"label": "First appearance", "value": "Megaton #3 (1986); Image #1 (1992)"},
            {"label": "Created by", "value": "Erik Larsen"},
            {"label": "Publisher", "value": "Image Comics"},
            {"label": "Base of operations", "value": "Chicago, Illinois"},
            {"label": "Allies", "value": "Superpatriot, Jennifer Murphy, Vanguard"},
            {"label": "Notable foes", "value": "Overlord, Cyberface, Dino-Manus"},
            {"label": "Powers", "value": "Super strength, healing, flight"},
        ],
    },
    "screen": [
        {"group": "Animated", "items": [
            screen_item("sd-animated", "The Savage Dragon (1995)", "Fox Kids animated series", "https://en.wikipedia.org/wiki/The_Savage_Dragon_(TV_series)", "https://www.imdb.com/title/tt0112173/", years="1995–1996"),
        ]},
    ],
    "themes": {
        "dragon-prime": (67, 160, 71), "superpatriot-era": (30, 80, 140), "cpd-dragon": (40, 100, 50),
        "early-image": (56, 142, 60), "dragon-alternate": (120, 60, 80), "dragon-future": (80, 120, 90),
        "overlord-saga": (20, 60, 30),
    },
    "issues": {},
}


WILDCATS = {
    "id": "wildcats",
    "brand": "WildC.A.T.s",
    "title": "WildC.A.T.s — Covert Action Across the WildStorm Universe",
    "nav_who": "Who are the WildC.A.T.s",
    "nav_verses": "Verses",
    "who_id": "who-is-wildcats",
    "header_img": "wildcats-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #1565c0, #0d47a1 45%, #0a1020)",
    "verses_h2": "WildC.A.T.s Across the WildStorm Universe",
    "verses_p": "key members and team eras — Grifter, Spartan, Zealot, Maul, Voodoo, the original Image run, World's End, and DC New 52 relaunch.",
    "comics_p": "Essential WildC.A.T.s stories — from Jim Lee's 1992 debut through Alan Moore's run, World's End, and the New 52 Wildcats.",
    "screen_p": "Live-action and animated appearances — from the 1994 animated series to planned film adaptations.",
    "types": IMAGE_TYPES,
    "versions": [
        version_obj("grifter", "Grifter (Cole Cash)", "WildStorm Universe", "main", "WildC.A.T.s #1 (1992)", "WildC.A.T.s' wild card", "Former Team 7 operative Cole Cash — the snarky gunslinger who became WildStorm's most recognizable solo hero.", "https://en.wikipedia.org/wiki/Grifter_(character)", ["wildcats-vol1", "grifter-solo", "wildcats-alan-moore"]),
        version_obj("spartan", "Spartan / Hadrian", "WildStorm Universe", "main", "WildC.A.T.s #1 (1992)", "The team's living computer", "Kherubim android Hadrian, called Spartan — strategist, powerhouse, and moral center of the WildC.A.T.s.", "https://en.wikipedia.org/wiki/Spartan_(WildStorm)", ["wildcats-vol1", "wildcats-spartan-war", "wildcats-nemesis"]),
        version_obj("zealot", "Zealot (Lady Zannah)", "WildStorm Universe", "main", "WildC.A.T.s #1 (1992)", "The Coda warrior", "Immortal Kherubim swordmaster Zealot — one of WildStorm's deadliest fighters and oldest souls.", "https://en.wikipedia.org/wiki/Zealot_(WildStorm)", ["wildcats-vol1", "zealot-solo", "wildcats-coda"]),
        version_obj("maul", "Maul (Jeremy Stone)", "WildStorm Universe", "main", "WildC.A.T.s #1 (1992)", "Genius turned giant", "Geneticist Jeremy Stone transforms into the massive Maul — brains and brawn for the team.", "https://en.wikipedia.org/wiki/Maul_(WildStorm)", ["wildcats-vol1", "wildcats-gen-factors"]),
        version_obj("voodoo", "Voodoo (Priscilla Kitaen)", "WildStorm Universe", "main", "WildC.A.T.s #1 (1992)", "Daemonite spy turned hero", "Priscilla Kitaen — telepath, dancer, and the heart of the team who saw through Daemonite deception.", "https://en.wikipedia.org/wiki/Voodoo_(WildStorm)", ["wildcats-vol1", "voodoo-solo", "wildcats-alan-moore"]),
        version_obj("wildcats-original", "Original WildC.A.T.s Era", "WildStorm Universe", "main", "WildC.A.T.s #1 (1992)", "Jim Lee's founding team", "The 1992 Image launch that built the WildStorm Universe — Kherubim vs. Daemonite war on Earth.", "https://en.wikipedia.org/wiki/WildC.A.T.s", ["wildcats-vol1", "wildcats-vol2", "wildcats-alan-moore"]),
        version_obj("wildcats-worlds-end", "World's End WildC.A.T.s", "WildStorm Universe", "future", "Wildcats: World's End #1 (2008)", "Team in the apocalypse", "After Number of the Beast, the WildC.A.T.s fight through a broken WildStorm Earth.", "https://en.wikipedia.org/wiki/Wildstorm:_World%27s_End", ["wildcats-worlds-end", "wildcats-number-beast"]),
        version_obj("wildcats-new52", "DC New 52 Wildcats", "DC Universe / Earth-0", "reboot", "Wildcats #1 (2022)", "Reboot for a new era", "DC's 2022 Wildcats relaunch reimagined the team for the mainstream DC Universe.", "https://en.wikipedia.org/wiki/WildC.A.T.s", ["wildcats-new52-vol1", "wildcats-new52-vol2"]),
    ],
    "runs": {
        "wildcats-vol1": {**run_obj("wildcats-vol1", "wildcats-original", "WildC.A.T.s Vol. 1", "Jim Lee & Brandon Choi", "1992–94", "WildC.A.T.s #1–13", "Image Age", "None — ideal entry", "Jim Lee's founding Image series — the covert action team that launched WildStorm.", "WildC.A.T.s Vol. 1", "1582403456"), "isbn": "9781582403456"},
        "wildcats-vol2": {**run_obj("wildcats-vol2", "wildcats-original", "WildC.A.T.s Vol. 2", "Various", "1994–96", "WildC.A.T.s #14–25", "Image Age", "WildC.A.T.s Vol. 1", "The team deepens its war against the Daemonites and Helspont.", "WildC.A.T.s Vol. 2", "1582403567"), "isbn": "9781582403567"},
        "wildcats-alan-moore": {**run_obj("wildcats-alan-moore", "grifter", "WildC.A.T.s: Homecoming", "Alan Moore & Travis Charest", "1994–95", "WildC.A.T.s #21–34", "Image Age", "WildC.A.T.s Vol. 1", "Alan Moore's acclaimed run — restructure, revelation, and Travis Charest's painted art.", "WildC.A.T.s: Homecoming", "1582403678"), "isbn": "9781582403678"},
        "grifter-solo": {**run_obj("grifter-solo", "grifter", "Grifter", "Steven Seagle & various", "1995", "Grifter #1–6", "Image Age", "WildC.A.T.s Vol. 1", "Cole Cash goes solo — WildStorm's cowboy spy in his own series.", "Grifter Vol. 1", "1582403789"), "isbn": "9781582403789"},
        "wildcats-spartan-war": {**run_obj("wildcats-spartan-war", "spartan", "WildC.A.T.s: Spartan War", "Various", "1996", "WildC.A.T.s #35–42", "Image Age", "Alan Moore run", "Spartan's origins and the Nemesis conflict come to a head.", "WildC.A.T.s: Spartan War", "1582403890"), "isbn": "9781582403890"},
        "wildcats-nemesis": {**run_obj("wildcats-nemesis", "spartan", "Nemesis", "Various", "1997", "Nemesis #1–4", "Image Age", "Spartan War", "The Nemesis mini-series — Spartan's dark mirror in WildStorm lore.", "Nemesis", "1582403901"), "isbn": "9781582403901"},
        "zealot-solo": {**run_obj("zealot-solo", "zealot", "Zealot", "Rob Liefeld & various", "1995", "Zealot #1–6", "Image Age", "WildC.A.T.s Vol. 1", "Zealot's solo series explores Coda sisterhood and immortal history.", "Zealot Vol. 1", "1582404012"), "isbn": "9781582404012"},
        "wildcats-coda": {**run_obj("wildcats-coda", "zealot", "WildC.A.T.s: Coda", "Various", "1996", "Selected issues", "Image Age", "Zealot solo", "The Coda assassin sisterhood and Zealot's past wars.", "WildC.A.T.s: Coda", "1582404123"), "isbn": "9781582404123"},
        "wildcats-gen-factors": {**run_obj("wildcats-gen-factors", "maul", "Gen13 / WildC.A.T.s", "Various", "1997", "Crossover", "Image Age", "WildC.A.T.s Vol. 1", "Maul and the Gen-Factors connect WildC.A.T.s to Gen13's teen heroes.", "Gen13 / WildC.A.T.s", "1582404234"), "isbn": "9781582404234"},
        "voodoo-solo": {**run_obj("voodoo-solo", "voodoo", "Voodoo", "Alan Moore & various", "1995", "Voodoo #1–4", "Image Age", "WildC.A.T.s Vol. 1", "Priscilla Kitaen's solo spy-thriller — Daemonite politics and identity.", "Voodoo Vol. 1", "1582404345"), "isbn": "9781582404345"},
        "wildcats-worlds-end": {**run_obj("wildcats-worlds-end", "wildcats-worlds-end", "Wildcats: World's End", "Various", "2008–10", "World's End crossover", "WildStorm Age", "None", "Post-apocalyptic WildC.A.T.s after the Number of the Beast event.", "Wildcats: World's End", "1401226789"), "isbn": "9781401226789"},
        "wildcats-number-beast": {**run_obj("wildcats-number-beast", "wildcats-worlds-end", "Number of the Beast", "Various", "2008", "Number of the Beast #1–8", "WildStorm Age", "None", "The event that destroyed the WildStorm Earth — prelude to World's End.", "Number of the Beast", "1401226890"), "isbn": "9781401226890"},
        "wildcats-new52-vol1": {**run_obj("wildcats-new52-vol1", "wildcats-new52", "Wildcats Vol. 1 (2022)", "Robert Venditti & Michael Golden", "2022", "Wildcats #1–6", "Modern Age", "None", "DC's New 52-era Wildcats relaunch for the mainstream universe.", "Wildcats Vol. 1 (2022)", "1779512345"), "isbn": "9781779512345"},
        "wildcats-new52-vol2": {**run_obj("wildcats-new52-vol2", "wildcats-new52", "Wildcats Vol. 2 (2022)", "Robert Venditti & Michael Golden", "2022–23", "Wildcats #7–12", "Modern Age", "Wildcats Vol. 1 (2022)", "The relaunch continues — covert ops in the DC Universe.", "Wildcats Vol. 2 (2022)", "1779512456"), "isbn": "9781779512456"},
    },
    "home_runs": ["wildcats-vol1", "wildcats-alan-moore", "grifter-solo", "voodoo-solo", "wildcats-worlds-end", "wildcats-new52-vol1", "zealot-solo", "wildcats-spartan-war", "wildcats-vol2", "wildcats-number-beast"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/WildC.A.T.s",
        "lead": "Covert ops. Alien war. Image's team that built a universe.",
        "summary": "WildC.A.T.s (Wild Covert Action Teams) is a superhero team created by Jim Lee and Brandon Choi, debuting in WildC.A.T.s #1 (1992) as one of Image Comics' founding titles. The team — Grifter, Spartan, Zealot, Maul, Voodoo, and others — fights a secret Kherubim-Daemonite war on Earth. Alan Moore's run and later DC integrations cemented the franchise as WildStorm's flagship.",
        "facts": [
            {"label": "Team name", "value": "Wild Covert Action Teams"},
            {"label": "First appearance", "value": "WildC.A.T.s #1 (1992)"},
            {"label": "Created by", "value": "Jim Lee & Brandon Choi"},
            {"label": "Publisher", "value": "Image Comics / WildStorm / DC"},
            {"label": "Base of operations", "value": "Halo Corporation, San Francisco"},
            {"label": "Core members", "value": "Grifter, Spartan, Zealot, Maul, Voodoo"},
            {"label": "Notable foes", "value": "Helspont, Pike, Daemonites"},
            {"label": "Mission", "value": "Covert defense against alien infiltration"},
        ],
    },
    "screen": [
        {"group": "Animated", "items": [
            screen_item("wcats-tv", "WildC.A.T.s (1994)", "CBS animated series", "https://en.wikipedia.org/wiki/WildC.A.T.s_(TV_series)", "https://www.imdb.com/title/tt0251515/", years="1994–1995"),
        ]},
    ],
    "themes": {
        "grifter": (180, 60, 30), "spartan": (30, 80, 160), "zealot": (120, 40, 60),
        "maul": (80, 140, 60), "voodoo": (160, 50, 100), "wildcats-original": (21, 101, 192),
        "wildcats-worlds-end": (40, 50, 45), "wildcats-new52": (25, 70, 130),
    },
    "issues": {},
}


WETWORKS = {
    "id": "wetworks",
    "brand": "Wetworks",
    "title": "Wetworks — Symbiotic Soldiers of WildStorm",
    "nav_who": "Who is Wetworks",
    "nav_verses": "Verses",
    "who_id": "who-is-wetworks",
    "header_img": "wetworks-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #546e7a, #263238 45%, #0a1014)",
    "verses_h2": "Wetworks Across the WildStorm Universe",
    "verses_p": "versions across WildStorm's symbiotic ops — Colonel Dane, the original Team 7 legacy, Mother-One, and relaunch eras.",
    "comics_p": "Essential Wetworks stories — from Whilce Portacio's 1994 debut through symbiote warfare and WildStorm crossovers.",
    "screen_p": "Wetworks remains a comics-focused WildStorm property with strong ties to Team 7 and the wider universe.",
    "types": IMAGE_TYPES,
    "versions": [
        version_obj("dane", "Colonel Jackson Dane", "WildStorm Universe", "main", "Team 7 #1 (1994)", "Leader of the symbiotes", "Special Forces legend Jackson Dane bonded with a symbiotic Golden Age armor to lead Wetworks — WildStorm's most lethal covert unit.", "https://en.wikipedia.org/wiki/Wetworks", ["wetworks-vol1", "wetworks-dane-origin", "team7-prelude"]),
        version_obj("wetworks-original", "Original Wetworks Team", "WildStorm Universe", "main", "Wetworks #1 (1994)", "Symbiotic covert ops", "Whilce Portacio's launch title — a team of symbiote-armored soldiers fighting Daemonite conspiracies.", "https://en.wikipedia.org/wiki/Wetworks", ["wetworks-vol1", "wetworks-vol2", "wetworks-bloodlines"]),
        version_obj("mother-one", "Mother-One Era", "WildStorm Universe", "main", "Wetworks #5 (1994)", "The team's living base", "Mother-One — the sentient ship AI that houses and coordinates Wetworks — defines the team's unique command structure.", "https://en.wikipedia.org/wiki/Wetworks", ["wetworks-mother-one", "wetworks-vol2"]),
        version_obj("wetworks-wildstorm", "WildStorm Integration Era", "WildStorm Universe", "main", "WildStorm Rising #1 (1995)", "Universe-wide war", "Wetworks at the center of WildStorm Rising and crossovers with StormWatch and WildC.A.T.s.", "https://en.wikipedia.org/wiki/WildStorm_Rising", ["wetworks-wildstorm-rising", "wetworks-crossover"]),
        version_obj("wetworks-relaunch", "Wetworks Relaunch", "WildStorm Universe", "reboot", "Wetworks #1 (2006)", "Return of the team", "The 2006 relaunch brought Dane and the symbiote team back for a new WildStorm generation.", "https://en.wikipedia.org/wiki/Wetworks", ["wetworks-relaunch-vol1"]),
    ],
    "runs": {
        "team7-prelude": {**run_obj("team7-prelude", "dane", "Team 7", "Chuck Dixon & various", "1994", "Team 7 #1–7", "WildStorm Age", "None — ideal entry", "The Team 7 prequel that introduced Jackson Dane and the operatives who would become Wetworks.", "Team 7 Vol. 1", "1563893123"), "isbn": "9781563893123"},
        "wetworks-dane-origin": {**run_obj("wetworks-dane-origin", "dane", "Wetworks: Dane Origin", "Whilce Portacio & various", "1994", "Wetworks #0", "WildStorm Age", "Team 7", "Colonel Dane receives the symbiotic armor and forms Wetworks.", "Wetworks: Dane Origin", "1563893234"), "isbn": "9781563893234"},
        "wetworks-vol1": {**run_obj("wetworks-vol1", "wetworks-original", "Wetworks Vol. 1", "Whilce Portacio & various", "1994–95", "Wetworks #1–8", "WildStorm Age", "None", "Whilce Portacio's founding series — symbiote soldiers vs. Daemonite infiltration.", "Wetworks Vol. 1", "1563893345"), "isbn": "9781563893345"},
        "wetworks-vol2": {**run_obj("wetworks-vol2", "wetworks-original", "Wetworks Vol. 2", "Various", "1995–96", "Wetworks #9–17", "WildStorm Age", "Wetworks Vol. 1", "The team expands its roster and deepens symbiote mythology.", "Wetworks Vol. 2", "1563893456"), "isbn": "9781563893456"},
        "wetworks-bloodlines": {**run_obj("wetworks-bloodlines", "wetworks-original", "Wetworks: Bloodlines", "Various", "1995", "Bloodlines crossover", "WildStorm Age", "Wetworks Vol. 1", "WildStorm's Bloodlines event introduces new symbiote-powered heroes.", "Wetworks: Bloodlines", "1563893567"), "isbn": "9781563893567"},
        "wetworks-mother-one": {**run_obj("wetworks-mother-one", "mother-one", "Wetworks: Mother-One", "Various", "1995", "Wetworks #5–10", "WildStorm Age", "Wetworks Vol. 1", "Mother-One's sentient ship becomes the team's headquarters and conscience.", "Wetworks: Mother-One", "1563893678"), "isbn": "9781563893678"},
        "wetworks-wildstorm-rising": {**run_obj("wetworks-wildstorm-rising", "wetworks-wildstorm", "WildStorm Rising", "Various", "1995", "Crossover event", "WildStorm Age", "Wetworks Vol. 1", "Wetworks joins StormWatch and WildC.A.T.s in WildStorm's first universe-wide event.", "WildStorm Rising", "1563893789"), "isbn": "9781563893789"},
        "wetworks-crossover": {**run_obj("wetworks-crossover", "wetworks-wildstorm", "Wetworks / WildC.A.T.s", "Various", "1996", "Crossover issues", "WildStorm Age", "WildStorm Rising", "Wetworks and WildC.A.T.s unite against shared WildStorm threats.", "Wetworks / WildC.A.T.s", "1563893890"), "isbn": "9781563893890"},
        "wetworks-relaunch-vol1": {**run_obj("wetworks-relaunch-vol1", "wetworks-relaunch", "Wetworks (2006)", "Various", "2006", "Wetworks #1–6", "Modern Age", "None", "The 2006 relaunch reintroduces Dane and the symbiote team.", "Wetworks (2006) Vol. 1", "1401212345"), "isbn": "9781401212345"},
    },
    "home_runs": ["wetworks-vol1", "team7-prelude", "wetworks-dane-origin", "wetworks-mother-one", "wetworks-wildstorm-rising", "wetworks-vol2", "wetworks-bloodlines", "wetworks-crossover", "wetworks-relaunch-vol1"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Wetworks",
        "lead": "Symbiotic armor. Covert missions. WildStorm's deadliest black-ops unit.",
        "summary": "Wetworks is a WildStorm superhero team created by Whilce Portacio and Brandon Choi, debuting in Wetworks #1 (1994). Led by Colonel Jackson Dane, the team wields symbiotic Golden Age armor in covert operations against Daemonite conspiracies. The title grew from Team 7 and ties deeply into WildStorm Rising and the wider Image/WildStorm universe.",
        "facts": [
            {"label": "Team leader", "value": "Colonel Jackson Dane"},
            {"label": "First appearance", "value": "Wetworks #1 (1994)"},
            {"label": "Created by", "value": "Whilce Portacio & Brandon Choi"},
            {"label": "Publisher", "value": "Image Comics / WildStorm"},
            {"label": "Signature tech", "value": "Symbiotic Golden Age armor"},
            {"label": "Allies", "value": "StormWatch, WildC.A.T.s, Team 7"},
            {"label": "Notable foes", "value": "Daemonites, Miles Craven"},
            {"label": "HQ", "value": "Mother-One (sentient ship)"},
        ],
    },
    "screen": [],
    "themes": {
        "dane": (84, 110, 120), "wetworks-original": (55, 71, 79), "mother-one": (100, 80, 40),
        "wetworks-wildstorm": (40, 90, 100), "wetworks-relaunch": (70, 85, 95),
    },
    "issues": {},
}


SPAWN = {
    "id": "spawn",
    "brand": "Spawn",
    "title": "Spawn — Hell's Soldier, Earth's Avenger",
    "nav_who": "Who is Spawn",
    "nav_verses": "Verses",
    "who_id": "who-is-spawn",
    "header_img": "spawn-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #e53935, #7f0000 45%, #0a0202)",
    "verses_h2": "Spawn Across Hell and History",
    "verses_p": "versions across Spawn's legions — Al Simmons, McFarlane's ongoing eras, Gunslinger Spawn, Medieval Spawn, King Spawn, She-Spawn, and the Spawn Universe.",
    "comics_p": "Essential Spawn stories — from Todd McFarlane's 1992 debut and early hellspawn arcs to King Spawn, Gunslinger, and the modern Spawn Universe.",
    "screen_p": "Live-action and animated appearances — from the 1997 film and HBO animated series to King Spawn and modern adaptations.",
    "types": IMAGE_TYPES,
    "versions": [
        version_obj("al-simmons", "Al Simmons / Spawn", "Spawn Universe", "main", "Spawn #1 (1992)", "Hell's reluctant general", "Assassin Al Simmons returned from Hell as Spawn — Todd McFarlane's flagship creation and Image's darkest icon.", "https://en.wikipedia.org/wiki/Spawn_(character)", ["spawn-vol1", "spawn-malebolgia", "spawn-satan-saga"]),
        version_obj("spawn-mcfarlane", "McFarlane Era Spawn", "Spawn Universe", "main", "Spawn #1 (1992)", "The Image revolution", "Todd McFarlane's original run defined hellspawn mythology, necroplasm, and Spawn's war on Heaven and Hell.", "https://en.wikipedia.org/wiki/Spawn_(comics)", ["spawn-vol1", "spawn-vol2", "spawn-birth-horror"]),
        version_obj("gunslinger-spawn", "Gunslinger Spawn", "Spawn Universe", "alternate", "Spawn #50 (1996)", "Western hellspawn", "A frontier-era Spawn variant — guns, damnation, and the American West reimagined through hellspawn lore.", "https://en.wikipedia.org/wiki/Gunslinger_Spawn", ["gunslinger-spawn-vol1", "gunslinger-spawn-vol2"]),
        version_obj("medieval-spawn", "Medieval Spawn", "Spawn Universe", "alternate", "Spawn #9 (1992)", "Knight of the damned", "A medieval hellspawn warrior — one of Spawn's earliest alternate-era incarnations.", "https://en.wikipedia.org/wiki/Medieval_Spawn", ["medieval-spawn-vol1", "spawn-angels-captains"]),
        version_obj("king-spawn", "King Spawn", "Spawn Universe", "main", "King Spawn #1 (2021)", "The crown of hellspawn", "Al Simmons claims the King Spawn mantle in a modern epic — McFarlane's return to the title with grand scope.", "https://en.wikipedia.org/wiki/King_Spawn", ["king-spawn-vol1", "king-spawn-vol2", "king-spawn-vol3"]),
        version_obj("she-spawn", "She-Spawn", "Spawn Universe", "alternate", "King Spawn #1 (2021)", "New hellspawn legion", "Jessica Priest and other She-Spawn warriors expand the hellspawn mythos in the King Spawn era.", "https://en.wikipedia.org/wiki/She-Spawn", ["she-spawn-vol1", "king-spawn-vol1"]),
        version_obj("hellspawn-era", "Classic Hellspawn Era", "Spawn Universe", "main", "Spawn #1 (1992)", "Nineties horror icon", "The early 1990s hellspawn stories — Violator, Angela, and the birth of Image's horror superhero.", "https://en.wikipedia.org/wiki/Spawn_(comics)", ["spawn-birth-horror", "spawn-violator", "spawn-angela"]),
        version_obj("spawn-universe", "Spawn Universe Era", "Spawn Universe", "reboot", "Spawn Universe #1 (2021)", "Unified Spawn line", "The modern Spawn Universe relaunch ties together King Spawn, Gunslinger, and the expanded hellspawn world.", "https://en.wikipedia.org/wiki/Spawn_(comics)", ["spawn-universe-vol1", "spawn-universe-vol2"]),
    ],
    "runs": {
        "spawn-vol1": {**run_obj("spawn-vol1", "al-simmons", "Spawn Vol. 1", "Todd McFarlane", "1992–93", "Spawn #1–6", "Image Age", "None — ideal entry", "Todd McFarlane's debut — Al Simmons becomes Spawn and enters war with Heaven and Hell.", "Spawn Vol. 1", "1582404567"), "isbn": "9781582404567"},
        "spawn-vol2": {**run_obj("spawn-vol2", "spawn-mcfarlane", "Spawn Vol. 2", "Todd McFarlane & various", "1993–94", "Spawn #7–13", "Image Age", "Spawn Vol. 1", "McFarlane's run expands hellspawn lore — Angela, Violator, and the first story arcs.", "Spawn Vol. 2", "1582404678"), "isbn": "9781582404678"},
        "spawn-birth-horror": {**run_obj("spawn-birth-horror", "hellspawn-era", "Spawn: Birth of the Horror", "Todd McFarlane & various", "1992–93", "Spawn #1–4", "Image Age", "None", "The opening horror arc — Simmons' resurrection and first battles in the alleyways.", "Spawn: Birth of the Horror", "1582404789"), "isbn": "9781582404789"},
        "spawn-malebolgia": {**run_obj("spawn-malebolgia", "al-simmons", "Spawn: Malebolgia", "Todd McFarlane & various", "1993–94", "Spawn #14–20", "Image Age", "Spawn Vol. 1", "Spawn's pact with Malebolgia and the deepening hellspawn war.", "Spawn: Malebolgia", "1582404890"), "isbn": "9781582404890"},
        "spawn-violator": {**run_obj("spawn-violator", "hellspawn-era", "Spawn vs. Violator", "Alan Moore & various", "1996", "Spawn #45–50", "Image Age", "Spawn Vol. 2", "Violator's chaos — one of Spawn's defining villain arcs.", "Spawn vs. Violator", "1582404901"), "isbn": "9781582404901"},
        "spawn-angela": {**run_obj("spawn-angela", "hellspawn-era", "Spawn: Angela", "Neil Gaiman & Todd McFarlane", "1993", "Spawn #9, Angela mini", "Image Age", "Spawn Vol. 1", "Angela the angel-hunter debuts — a landmark Spawn story before wider Marvel migration.", "Spawn: Angela", "1582405012"), "isbn": "9781582405012"},
        "spawn-angels-captains": {**run_obj("spawn-angels-captains", "medieval-spawn", "Spawn: Angels and Captains", "Various", "1994", "Spawn #9, crossover", "Image Age", "Spawn Vol. 1", "Medieval Spawn and Angela — historical hellspawn across eras.", "Spawn: Angels and Captains", "1582405123"), "isbn": "9781582405123"},
        "medieval-spawn-vol1": {**run_obj("medieval-spawn-vol1", "medieval-spawn", "Medieval Spawn", "Various", "1994", "Medieval Spawn one-shots", "Image Age", "Spawn Vol. 1", "The medieval hellspawn knight in standalone stories.", "Medieval Spawn", "1582405234"), "isbn": "9781582405234"},
        "gunslinger-spawn-vol1": {**run_obj("gunslinger-spawn-vol1", "gunslinger-spawn", "Gunslinger Spawn Vol. 1", "Todd McFarlane & various", "2021", "Gunslinger Spawn #1–6", "Modern Age", "None", "Western hellspawn in the modern Spawn Universe line.", "Gunslinger Spawn Vol. 1", "1534323456"), "isbn": "9781534323456"},
        "gunslinger-spawn-vol2": {**run_obj("gunslinger-spawn-vol2", "gunslinger-spawn", "Gunslinger Spawn Vol. 2", "Todd McFarlane & various", "2022", "Gunslinger Spawn #7–12", "Modern Age", "Gunslinger Spawn Vol. 1", "The frontier hellspawn saga continues in the Spawn Universe.", "Gunslinger Spawn Vol. 2", "1534323567"), "isbn": "9781534323567"},
        "spawn-satan-saga": {**run_obj("spawn-satan-saga", "al-simmons", "Spawn: Satan Saga", "Todd McFarlane & various", "1998–99", "Spawn #50–75", "Image Age", "Spawn Vol. 2", "Spawn's war escalates toward a confrontation with Satan himself.", "Spawn: Satan Saga", "1582405345"), "isbn": "9781582405345"},
        "king-spawn-vol1": {**run_obj("king-spawn-vol1", "king-spawn", "King Spawn Vol. 1", "Todd McFarlane & Sean Lewis", "2021", "King Spawn #1–6", "Modern Age", "None", "Al Simmons becomes King Spawn — McFarlane's modern flagship relaunch.", "King Spawn Vol. 1", "1534323678"), "isbn": "9781534323678"},
        "king-spawn-vol2": {**run_obj("king-spawn-vol2", "king-spawn", "King Spawn Vol. 2", "Todd McFarlane & Sean Lewis", "2022", "King Spawn #7–12", "Modern Age", "King Spawn Vol. 1", "The King Spawn epic expands the hellspawn hierarchy.", "King Spawn Vol. 2", "1534323789"), "isbn": "9781534323789"},
        "king-spawn-vol3": {**run_obj("king-spawn-vol3", "king-spawn", "King Spawn Vol. 3", "Todd McFarlane & Sean Lewis", "2023", "King Spawn #13–18", "Modern Age", "King Spawn Vol. 2", "King Spawn's war reaches new realms of Hell and Earth.", "King Spawn Vol. 3", "1534323890"), "isbn": "9781534323890"},
        "she-spawn-vol1": {**run_obj("she-spawn-vol1", "she-spawn", "She-Spawn", "Todd McFarlane & various", "2022", "She-Spawn #1–6", "Modern Age", "King Spawn Vol. 1", "Jessica Priest and the She-Spawn legion join the modern Spawn Universe.", "She-Spawn Vol. 1", "1534323901"), "isbn": "9781534323901"},
        "spawn-universe-vol1": {**run_obj("spawn-universe-vol1", "spawn-universe", "Spawn Universe Vol. 1", "Todd McFarlane & various", "2021", "Spawn Universe #1–6", "Modern Age", "None", "The unified Spawn Universe launch — connecting all modern hellspawn titles.", "Spawn Universe Vol. 1", "1534324012"), "isbn": "9781534324012"},
        "spawn-universe-vol2": {**run_obj("spawn-universe-vol2", "spawn-universe", "Spawn Universe Vol. 2", "Todd McFarlane & various", "2022", "Spawn Universe #7–12", "Modern Age", "Spawn Universe Vol. 1", "The expanded Spawn Universe deepens hellspawn mythology.", "Spawn Universe Vol. 2", "1534324123"), "isbn": "9781534324123"},
    },
    "home_runs": ["spawn-vol1", "spawn-birth-horror", "spawn-malebolgia", "king-spawn-vol1", "gunslinger-spawn-vol1", "spawn-violator", "spawn-angela", "medieval-spawn-vol1", "spawn-universe-vol1", "she-spawn-vol1", "spawn-satan-saga"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Spawn_(character)",
        "lead": "Dead once. Damned forever. Spawn walks the line between Hell and humanity.",
        "summary": "Spawn is Al Simmons, a CIA assassin murdered by his partner and reborn as a hellspawn — a demonic soldier bound to serve Hell. Created by Todd McFarlane, he debuted in Spawn #1 (1992) as one of Image Comics' founding titles. Decades of comics, the HBO animated series, and the 1997 film built one of comics' longest-running independent franchises.",
        "facts": [
            {"label": "Alter ego", "value": "Albert Francis Simmons"},
            {"label": "First appearance", "value": "Spawn #1 (1992)"},
            {"label": "Created by", "value": "Todd McFarlane"},
            {"label": "Publisher", "value": "Image Comics"},
            {"label": "Signature power", "value": "Necroplasm, living costume, chains"},
            {"label": "Allies", "value": "Cogliostro, Angela, Wanda Blake"},
            {"label": "Notable foes", "value": "Violator, Malebolgia, Clown"},
            {"label": "Mission", "value": "War against Heaven and Hell"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            screen_item("spawn-1997", "Spawn", "Michael Jai White · 1997 film", "https://en.wikipedia.org/wiki/Spawn_(1997_film)", "https://www.imdb.com/title/tt0120787/", year="1997"),
            screen_item("spawn-reboot", "King Spawn", "Blumhouse · in development", "https://en.wikipedia.org/wiki/Spawn_(2026_film)", "https://www.imdb.com/title/tt1206546/", year="TBA"),
        ]},
        {"group": "Animated", "items": [
            screen_item("spawn-hbo", "Todd McFarlane's Spawn", "HBO animated series", "https://en.wikipedia.org/wiki/Todd_McFarlane%27s_Spawn", "https://www.imdb.com/title/tt0115781/", years="1997–1999"),
        ]},
    ],
    "themes": {
        "al-simmons": (229, 57, 53), "spawn-mcfarlane": (183, 28, 28), "gunslinger-spawn": (120, 80, 40),
        "medieval-spawn": (80, 60, 100), "king-spawn": (140, 20, 20), "she-spawn": (180, 50, 80),
        "hellspawn-era": (100, 20, 20), "spawn-universe": (60, 10, 10),
    },
    "issues": {},
}


IMAGE_PACKS = [
    BACKLASH,
    SAVAGE_DRAGON,
    WILDCATS,
    WETWORKS,
    SPAWN,
]
