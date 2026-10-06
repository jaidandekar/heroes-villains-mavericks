"""Marvel character pack definitions for character reading guides."""

MARVEL_TYPES = {
    "main": "Main Continuity",
    "ultimate": "Ultimate Universe",
    "multiverse": "Multiverse",
    "future": "Future",
    "alternate": "Alternate Reality",
}


def _run(slug, version_slug, title, creators, years, collects, era, prerequisites, summary, reading, asin, format_="Trade Paperback"):
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


def _ver(slug, name, universe, typ, first, tagline, description, wiki, runs):
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


def _screen(id_, title, note, wiki, imdb, year=None, years=None):
    item = {"id": id_, "title": title, "note": note, "wikipedia": wiki, "imdb": imdb}
    if year:
        item["year"] = year
    if years:
        item["years"] = years
    return item


CAPTAIN_AMERICA = {
    "id": "captain-america",
    "brand": "Captain America",
    "title": "Captain America — Sentinel Across the Multiverse",
    "nav_who": "Who is Captain America",
    "nav_verses": "Verses",
    "who_id": "who-is-captain-america",
    "header_img": "captain-america-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #1e4a8c, #0a1f44 45%, #020810)",
    "verses_h2": "Captain America Across the Multiverse",
    "verses_p": "versions across Marvel's timelines — Steve Rogers, Sam Wilson, Bucky Barnes, Isaiah Bradley, Ultimate Cap, and alternate realities.",
    "comics_p": "Essential Captain America stories — from Simon & Kirby's wartime origin to Brubaker's Winter Soldier and Sam Wilson's shield.",
    "screen_p": "Live-action and animated appearances — from the MCU films and The First Avenger to What If...? and Captain America: Brave New World.",
    "types": MARVEL_TYPES,
    "versions": [
        _ver("steve-rogers", "Steve Rogers", "Earth-616 / Prime Marvel", "main", "Captain America Comics #1 (1941)", "The First Avenger", "Frail Steve Rogers became the super-soldier symbol of liberty — a man out of time who never stopped fighting for the dream.", "https://en.wikipedia.org/wiki/Captain_America", ["cap-man-out-of-time", "cap-winter-soldier", "cap-civil-war"]),
        _ver("sam-wilson", "Sam Wilson", "Earth-616 / Prime Marvel", "main", "Captain America #117 (1969)", "The shield passes forward", "The Falcon became Captain America when Steve Rogers stepped aside — carrying the mantle with wings and conviction.", "https://en.wikipedia.org/wiki/Sam_Wilson_(Marvel_Comics)", ["sam-all-new-cap", "sam-captain-america"]),
        _ver("bucky-barnes", "Bucky Barnes / Winter Soldier", "Earth-616 / Prime Marvel", "main", "Captain America Comics #1 (1941)", "The ghost in the machine", "Steve's partner returned as the brainwashed Winter Soldier — and later wielded the shield when the world needed him.", "https://en.wikipedia.org/wiki/Bucky_Barnes", ["cap-winter-soldier", "bucky-winter-soldier-solo"]),
        _ver("isaiah-bradley", "Isaiah Bradley", "Earth-616 / Prime Marvel", "main", "Truth: Red, White & Black #1 (2003)", "The forgotten super-soldier", "Before Steve Rogers, Black soldiers were subjected to the super-soldier program — Isaiah Bradley survived and became a legend.", "https://en.wikipedia.org/wiki/Isaiah_Bradley", ["truth-red-white-black"]),
        _ver("ultimate-cap", "Ultimate Captain America", "Earth-1610", "ultimate", "Ultimate Marvel Team-Up #4 (2001)", "A harder edge", "Mark Millar and Bryan Hitch's Ultimate Universe reimagined Cap as a man of uncompromising wartime values dropped into the modern world.", "https://en.wikipedia.org/wiki/Ultimate_Captain_America", ["ultimate-cap-vol1", "ultimate-civil-war"]),
        _ver("cap-2099", "Captain America 2099", "Earth-928 / 2099", "future", "2099: World of Tomorrow #1 (1999)", "Tomorrow's shield", "In the corporate dystopia of 2099, a new Captain America rises to defend a future that forgot its heroes.", "https://en.wikipedia.org/wiki/Captain_America_2099", ["2099-world-tomorrow"]),
        _ver("hydra-cap", "Hydra Captain America", "Earth-616", "alternate", "Captain America: Steve Rogers #1 (2016)", "Hail Hydra", "Steve Rogers rewritten by the Cosmic Cube to serve Hydra — the most controversial Cap story of the modern era.", "https://en.wikipedia.org/wiki/Hydra_Captain_America", ["secret-empire"]),
        _ver("peggy-carter-cap", "Peggy Carter Captain America", "Earth-82601", "alternate", "Exiles #9 (2002)", "What if Peggy took the serum?", "In alternate timelines and What If...? stories, Peggy Carter becomes the super-soldier — a symbol forged in a different war.", "https://en.wikipedia.org/wiki/Peggy_Carter", ["what-if-captain-carter"]),
    ],
    "runs": {
        "cap-man-out-of-time": {**_run("cap-man-out-of-time", "steve-rogers", "Captain America: Man Out of Time", "Mark Waid & Jorge Molina", "2010–11", "Limited series", "Modern Age", "None — ideal entry", "Steve Rogers wakes in the 21st century and learns what America became while he was frozen.", "Captain America: Man Out of Time", "0785145401"), "isbn": "9780785145408"},
        "cap-winter-soldier": {**_run("cap-winter-soldier", "steve-rogers", "Captain America: Winter Soldier", "Ed Brubaker & Steve Epting", "2004–05", "Captain America #1–9, 11–14", "Modern Age", "None", "The Cold War assassin the Winter Soldier is revealed — Brubaker's definitive Captain America run begins.", "Captain America: Winter Soldier Ultimate Collection", "0785134302"), "isbn": "9780785134303"},
        "cap-civil-war": {**_run("cap-civil-war", "steve-rogers", "Civil War", "Mark Millar & Steve McNiven", "2006–07", "Civil War #1–7", "Modern Age", "None", "Steve Rogers leads the anti-registration side against Iron Man in Marvel's defining superhero conflict.", "Civil War", "0785121789"), "isbn": "9780785121787"},
        "sam-all-new-cap": {**_run("sam-all-new-cap", "sam-wilson", "All-New Captain America", "Rick Remender & Stuart Immonen", "2014–15", "All-New Captain America #1–6", "Modern Age", "None", "Sam Wilson takes up the shield for the first time as the new Captain America.", "All-New Captain America Vol. 1", "0785192987"), "isbn": "9780785192981"},
        "sam-captain-america": {**_run("sam-captain-america", "sam-wilson", "Captain America: Sam Wilson", "Nick Spencer & Daniel Acuña", "2015–17", "Captain America: Sam Wilson #1–10", "Modern Age", "All-New Captain America", "Sam's tenure as Cap confronts politics, immigration, and what the shield means today.", "Captain America: Sam Wilson Vol. 1", "0785197067"), "isbn": "9780785197061"},
        "bucky-winter-soldier-solo": {**_run("bucky-winter-soldier-solo", "bucky-barnes", "The Winter Soldier", "Ed Brubaker & Butch Guice", "2012–13", "Winter Soldier #1–14", "Modern Age", "Captain America: Winter Soldier", "Bucky Barnes reclaims his identity and hunts the sins of his past as the Winter Soldier.", "Winter Soldier Vol. 1", "0785163353"), "isbn": "9780785163359"},
        "truth-red-white-black": {**_run("truth-red-white-black", "isaiah-bradley", "Truth: Red, White & Black", "Robert Morales & Kyle Baker", "2003", "Truth: Red, White & Black #1–7", "Modern Age", "None", "The hidden history of the super-soldier program and Isaiah Bradley's sacrifice.", "Truth: Red, White & Black", "0785110953"), "isbn": "9780785110950"},
        "ultimate-cap-vol1": {**_run("ultimate-cap-vol1", "ultimate-cap", "Ultimate Captain America Vol. 1", "Mark Millar & Bryan Hitch", "2002", "Ultimates #1–6", "Ultimate", "None", "The Ultimate Universe's Captain America joins a government-sponsored super-team in a post-9/11 world.", "The Ultimates Vol. 1", "0785107880"), "isbn": "9780785107880"},
        "ultimate-civil-war": {**_run("ultimate-civil-war", "ultimate-cap", "Ultimate Comics: Avengers", "Mark Millar & Leinil Yu", "2009–10", "Ultimate Comics: Avengers #1–6", "Ultimate", "Ultimate Cap Vol. 1", "Ultimate Cap faces Nick Fury's black-ops Avengers and the cost of patriotism.", "Ultimate Comics: Avengers Vol. 1", "0785139789"), "isbn": "9780785139789"},
        "2099-world-tomorrow": {**_run("2099-world-tomorrow", "cap-2099", "2099: World of Tomorrow", "Various", "1999", "2099: World of Tomorrow #1–3", "2099", "None", "The 2099 line introduces a dystopian future where new heroes inherit old names.", "2099: World of Tomorrow", "0785107120"), "isbn": "9780785107120"},
        "secret-empire": {**_run("secret-empire", "hydra-cap", "Secret Empire", "Nick Spencer & Steve McNiven", "2017", "Secret Empire #0–10", "Modern Age", "Captain America: Steve Rogers", "Hydra Captain America conquers America — the event that divided fandom.", "Secret Empire", "1302905494"), "isbn": "9781302905494"},
        "what-if-captain-carter": {**_run("what-if-captain-carter", "peggy-carter-cap", "What If... Captain Carter", "Various", "2021", "What If...? one-shots / Exiles", "Multiverse", "None", "Stories exploring Peggy Carter as the super-soldier across alternate realities.", "What If... Captain Carter", "1302928397"), "isbn": "9781302928394"},
    },
    "home_runs": ["cap-winter-soldier", "cap-man-out-of-time", "truth-red-white-black", "sam-all-new-cap", "cap-civil-war", "ultimate-cap-vol1", "bucky-winter-soldier-solo", "secret-empire", "sam-captain-america", "what-if-captain-carter"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Captain_America",
        "lead": "One shield. Many who carry it. The symbol of liberty outlasts any single bearer.",
        "summary": "Captain America is the superhero identity of Steve Rogers, a frail young man transformed by the Super-Soldier Serum into the pinnacle of human perfection. Created by Joe Simon and Jack Kirby, he debuted in Captain America Comics #1 (1941). Over decades the mantle passed to Sam Wilson, Bucky Barnes, and others — while alternate timelines reimagined the symbol for new wars and new worlds.",
        "facts": [
            {"label": "Notable bearers", "value": "Steve Rogers, Sam Wilson, Bucky Barnes"},
            {"label": "First appearance", "value": "Captain America Comics #1 (1941)"},
            {"label": "Created by", "value": "Joe Simon & Jack Kirby"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Signature weapon", "value": "Vibranium shield"},
            {"label": "Allies", "value": "Avengers, Falcon, Sharon Carter"},
            {"label": "Notable foes", "value": "Red Skull, Hydra, Baron Zemo"},
            {"label": "Powers", "value": "Peak human strength, agility, and endurance"},
        ],
    },
    "screen": [
        {"group": "MCU films", "items": [
            _screen("ca-tfa", "Captain America: The First Avenger", "Chris Evans · Origin", "https://en.wikipedia.org/wiki/Captain_America:_The_First_Avenger", "https://www.imdb.com/title/tt0458339/", year="2011"),
            _screen("ca-ws", "Captain America: The Winter Soldier", "Chris Evans · Political thriller", "https://en.wikipedia.org/wiki/Captain_America:_The_Winter_Soldier", "https://www.imdb.com/title/tt1843866/", year="2014"),
            _screen("ca-cw", "Captain America: Civil War", "Chris Evans · Avengers split", "https://en.wikipedia.org/wiki/Captain_America:_Civil_War", "https://www.imdb.com/title/tt3498820/", year="2016"),
            _screen("ca-bnw", "Captain America: Brave New World", "Anthony Mackie · Sam Wilson", "https://en.wikipedia.org/wiki/Captain_America:_Brave_New_World", "https://www.imdb.com/title/tt1457767/", year="2025"),
        ]},
        {"group": "Animated", "items": [
            _screen("ca-tas", "The Marvel Super Heroes", "1966 animated shorts", "https://en.wikipedia.org/wiki/The_Marvel_Super_Heroes", "https://www.imdb.com/title/tt0060004/", years="1966"),
            _screen("what-if-carter", "What If...?", "Captain Carter episodes", "https://en.wikipedia.org/wiki/What_If...%3F_(TV_series)", "https://www.imdb.com/title/tt10168312/", years="2021–2024"),
        ]},
    ],
    "themes": {
        "steve-rogers": (30, 58, 140), "sam-wilson": (180, 50, 40), "bucky-barnes": (60, 70, 90),
        "isaiah-bradley": (120, 40, 30), "ultimate-cap": (20, 40, 100), "cap-2099": (10, 80, 120),
        "hydra-cap": (140, 20, 30), "peggy-carter-cap": (160, 50, 70),
    },
    "issues": {},
}


IRON_MAN = {
    "id": "iron-man",
    "brand": "Iron Man",
    "title": "Iron Man — Genius Across the Multiverse",
    "nav_who": "Who is Iron Man",
    "nav_verses": "Verses",
    "who_id": "who-is-iron-man",
    "header_img": "iron-man-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #c41e1e, #6b0f0f 45%, #1a0505)",
    "verses_h2": "Iron Man Across the Multiverse",
    "verses_p": "versions across Marvel's armored legacies — Tony Stark, Extremis, Superior Iron Man, 2020, Ultimate Tony, War Machine, and Ironheart.",
    "comics_p": "Essential Iron Man stories — from Demon in a Bottle and Extremis to Superior Iron Man and the Armor Wars.",
    "screen_p": "Live-action and animated appearances — from the MCU Iron Man trilogy and Avengers films to Iron Man: Armored Adventures.",
    "types": MARVEL_TYPES,
    "versions": [
        _ver("tony-stark", "Tony Stark", "Earth-616 / Prime Marvel", "main", "Tales of Suspense #39 (1963)", "Genius, billionaire, playboy, philanthropist", "Tony Stark built his first suit in a cave and never stopped inventing — the armored Avenger who defined the modern Marvel era.", "https://en.wikipedia.org/wiki/Iron_Man", ["iron-man-extremis", "iron-man-demon", "iron-man-armor-wars"]),
        _ver("extremis-tony", "Extremis Iron Man", "Earth-616 / Prime Marvel", "main", "Iron Man Vol. 4 #1 (2005)", "The armor is inside him", "Warren Ellis's Extremis rewrote Tony's biology — nanotech armor stored in his bones, a sleek new paradigm.", "https://en.wikipedia.org/wiki/Extremis_(comics)", ["iron-man-extremis", "iron-man-execute"]),
        _ver("superior-iron-man", "Superior Iron Man", "Earth-616", "alternate", "Superior Iron Man #1 (2014)", "Evil Tony in San Francisco", "When the Axis inversion flips heroes and villains, Tony becomes a predatory tech mogul in a symbiote-style armor.", "https://en.wikipedia.org/wiki/Superior_Iron_Man", ["superior-iron-man-run"]),
        _ver("iron-man-2020", "Iron Man 2020", "Earth-616 / 2020 line", "future", "Machine Man Vol. 1 #1 (1978)", "Arno Stark's future", "Tony's brother Arno and the 2020 timeline explore a dystopian future where corporate Iron Man rules.", "https://en.wikipedia.org/wiki/Iron_Man_2020", ["iron-man-2020-event"]),
        _ver("ultimate-tony", "Ultimate Iron Man", "Earth-1610", "ultimate", "Ultimate Marvel Team-Up #4 (2001)", "Bio-armor inventor", "The Ultimate Universe's Tony Stark — a bio-mechanical genius with a very different origin and temperament.", "https://en.wikipedia.org/wiki/Ultimate_Iron_Man", ["ultimate-iron-man-vol1", "ultimate-ultimates"]),
        _ver("war-machine", "War Machine", "Earth-616 / Prime Marvel", "main", "Iron Man #118 (1979)", "Rhodey's heavy artillery", "James Rhodes donned the armor when Tony fell — and built his own identity as the militarized War Machine.", "https://en.wikipedia.org/wiki/War_Machine", ["war-machine-iron-man-2", "war-machine-solo"]),
        _ver("ironheart", "Ironheart", "Earth-616 / Prime Marvel", "main", "Invincible Iron Man Vol. 4 #7 (2016)", "The next generation", "Teen genius Riri Williams reverse-engineered Iron Man tech and earned Tony's blessing to carry the legacy forward.", "https://en.wikipedia.org/wiki/Ironheart_(character)", ["ironheart-vol1"]),
    ],
    "runs": {
        "iron-man-demon": {**_run("iron-man-demon", "tony-stark", "Iron Man: Demon in a Bottle", "David Michelinie & Bob Layton", "1979", "Iron Man #120–128", "Bronze Age", "None — classic entry", "Tony Stark confronts alcoholism in the story that humanized the armored Avenger.", "Iron Man: Demon in a Bottle", "0785120430"), "isbn": "9780785120438"},
        "iron-man-extremis": {**_run("iron-man-extremis", "extremis-tony", "Iron Man: Extremis", "Warren Ellis & Adi Granov", "2005–06", "Iron Man Vol. 4 #1–6", "Modern Age", "None", "Tony's origin and biology are reinvented for the MCU era — sleek, cinematic, definitive.", "Iron Man: Extremis", "0785122581"), "isbn": "9780785122586"},
        "iron-man-armor-wars": {**_run("iron-man-armor-wars", "tony-stark", "Iron Man: Armor Wars", "David Michelinie & Bob Layton", "1987–88", "Iron Man #225–232", "Modern Age", "None", "Tony hunts down stolen Stark tech in his most paranoid, driven storyline.", "Iron Man: Armor Wars", "0785131645"), "isbn": "9780785131649"},
        "iron-man-execute": {**_run("iron-man-execute", "extremis-tony", "Iron Man: Execute Program", "Daniel Knauf & others", "2005–07", "Iron Man Vol. 4 #7–12", "Modern Age", "Extremis", "A murder mystery forces Tony to question who controls his technology.", "Iron Man: Execute Program", "0785125092"), "isbn": "9780785125098"},
        "superior-iron-man-run": {**_run("superior-iron-man-run", "superior-iron-man", "Superior Iron Man", "Tom Taylor & Yildiray Cinjar", "2014–15", "Superior Iron Man #1–9", "Modern Age", "Axis event", "Evil Tony sells Extremis 3.0 to San Francisco in a chilling inversion arc.", "Superior Iron Man Vol. 1", "0785193002"), "isbn": "9780785193001"},
        "iron-man-2020-event": {**_run("iron-man-2020-event", "iron-man-2020", "Iron Man 2020", "Dan Slott & Christos Gage", "2020", "Iron Man 2020 #1–6", "Modern Age", "None", "Arno Stark seizes control in a near-future event exploring Tony's legacy.", "Iron Man 2020", "1302921376"), "isbn": "9781302921371"},
        "ultimate-iron-man-vol1": {**_run("ultimate-iron-man-vol1", "ultimate-tony", "Ultimate Iron Man", "Orson Scott Card & others", "2005", "Ultimate Iron Man #1–5", "Ultimate", "None", "The Ultimate Universe's bio-armor origin for Tony Stark.", "Ultimate Iron Man", "0785117800"), "isbn": "9780785117800"},
        "ultimate-ultimates": {**_run("ultimate-ultimates", "ultimate-tony", "The Ultimates", "Mark Millar & Bryan Hitch", "2002", "Ultimates #1–13", "Ultimate", "None", "Ultimate Tony joins the government super-team that redefined Marvel in the 2000s.", "The Ultimates Vol. 1", "0785107880"), "isbn": "9780785107880"},
        "war-machine-iron-man-2": {**_run("war-machine-iron-man-2", "war-machine", "Iron Man: War Machine", "Len Kaminski & others", "1994", "Iron Man #291–292, War Machine #1–7", "Modern Age", "None", "Rhodey steps into the armor permanently and launches his solo series.", "War Machine Vol. 1", "0785100150"), "isbn": "9780785100157"},
        "war-machine-solo": {**_run("war-machine-solo", "war-machine", "War Machine: Weapons of Destruction", "Greg Pak & Leonardo Manco", "2009–10", "War Machine Vol. 2 #1–12", "Modern Age", "None", "Rhodey goes full military in a solo run about accountability and firepower.", "War Machine: Weapons of Destruction", "0785146742"), "isbn": "9780785146743"},
        "ironheart-vol1": {**_run("ironheart-vol1", "ironheart", "Invincible Iron Man: Ironheart", "Brian Michael Bendis & Stefano Caselli", "2017", "Invincible Iron Man #1–6", "Modern Age", "None", "Riri Williams builds her first suit and steps into Tony Stark's shadow.", "Invincible Iron Man: Ironheart Vol. 1", "1302906938"), "isbn": "9781302906934"},
    },
    "home_runs": ["iron-man-extremis", "iron-man-demon", "iron-man-armor-wars", "ultimate-ultimates", "war-machine-iron-man-2", "superior-iron-man-run", "ironheart-vol1", "iron-man-2020-event", "ultimate-iron-man-vol1", "iron-man-execute"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Iron_Man",
        "lead": "When the world needed a hero, Tony Stark built one — in a cave, with a box of scraps.",
        "summary": "Iron Man is Tony Stark, a billionaire industrialist and genius inventor who built a powered suit of armor to escape captivity and became a founding Avenger. Created by Stan Lee, Larry Lieber, Don Heck, and Jack Kirby, he debuted in Tales of Suspense #39 (1963). The character's tech-noir evolution — from Demon in a Bottle to Extremis — mirrors Marvel's shift into the modern age.",
        "facts": [
            {"label": "Alter ego", "value": "Anthony Edward Stark"},
            {"label": "First appearance", "value": "Tales of Suspense #39 (1963)"},
            {"label": "Created by", "value": "Stan Lee, Larry Lieber, Don Heck, Jack Kirby"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Company", "value": "Stark Industries"},
            {"label": "Allies", "value": "Avengers, War Machine, Pepper Potts"},
            {"label": "Notable foes", "value": "Mandarin, Obadiah Stane, Justin Hammer"},
            {"label": "Powers", "value": "Powered armor, genius intellect"},
        ],
    },
    "screen": [
        {"group": "MCU films", "items": [
            _screen("im-2008", "Iron Man", "Robert Downey Jr. · Origin", "https://en.wikipedia.org/wiki/Iron_Man_(2008_film)", "https://www.imdb.com/title/tt0371746/", year="2008"),
            _screen("im-2", "Iron Man 2", "Robert Downey Jr.", "https://en.wikipedia.org/wiki/Iron_Man_2", "https://www.imdb.com/title/tt1228705/", year="2010"),
            _screen("im-3", "Iron Man 3", "Robert Downey Jr.", "https://en.wikipedia.org/wiki/Iron_Man_3", "https://www.imdb.com/title/tt1300854/", year="2013"),
            _screen("avengers-im", "The Avengers", "Robert Downey Jr.", "https://en.wikipedia.org/wiki/The_Avengers_(2012_film)", "https://www.imdb.com/title/tt0848228/", year="2012"),
        ]},
        {"group": "Animated", "items": [
            _screen("ima", "Iron Man: Armored Adventures", "Teen Tony animated series", "https://en.wikipedia.org/wiki/Iron_Man:_Armored_Adventures", "https://www.imdb.com/title/tt1327706/", years="2009–2012"),
            _screen("im-heroes", "Iron Man (1994)", "Marvel Action Hour", "https://en.wikipedia.org/wiki/Iron_Man_(TV_series)", "https://www.imdb.com/title/tt0108843/", years="1994–1996"),
        ]},
    ],
    "themes": {
        "tony-stark": (196, 30, 30), "extremis-tony": (180, 50, 20), "superior-iron-man": (220, 180, 40),
        "iron-man-2020": (100, 100, 120), "ultimate-tony": (160, 40, 40), "war-machine": (60, 70, 80),
        "ironheart": (200, 60, 100),
    },
    "issues": {},
}


INCREDIBLE_HULK = {
    "id": "incredible-hulk",
    "brand": "Incredible Hulk",
    "title": "Incredible Hulk — Rage Across the Multiverse",
    "nav_who": "Who is the Hulk",
    "nav_verses": "Verses",
    "who_id": "who-is-incredible-hulk",
    "header_img": "incredible-hulk-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #4caf50, #1b5e20 45%, #0a1a0a)",
    "verses_h2": "Incredible Hulk Across the Multiverse",
    "verses_p": "versions across Marvel's gamma spectrum — Bruce Banner, World War Hulk, Immortal Hulk, Maestro, Joe Fixit, Ultimate Hulk, and Red Hulk.",
    "comics_p": "Essential Hulk stories — from Peter David's run and Planet Hulk to Immortal Hulk and Future Imperfect.",
    "screen_p": "Live-action and animated appearances — from The Incredible Hulk films and MCU cameos to the 1980s animated series.",
    "types": MARVEL_TYPES,
    "versions": [
        _ver("banner-hulk", "Bruce Banner / Hulk", "Earth-616 / Prime Marvel", "main", "The Incredible Hulk #1 (1962)", "The strongest one there is", "Bruce Banner's gamma accident created the Hulk — a man and a monster sharing one body, forever hunted and forever angry.", "https://en.wikipedia.org/wiki/Hulk", ["hulk-peter-david", "hulk-origin"]),
        _ver("world-war-hulk", "World War Hulk", "Earth-616", "main", "Incredible Hulk Vol. 2 #106 (2007)", "Hulk wants justice", "After the Illuminati exiled him, Hulk returns from Sakaar to make Earth's heroes pay.", "https://en.wikipedia.org/wiki/World_War_Hulk", ["planet-hulk", "world-war-hulk-event"]),
        _ver("immortal-hulk", "Immortal Hulk", "Earth-616", "main", "The Immortal Hulk #1 (2018)", "Horror reborn", "Al Ewing's reinvention — the Hulk as a night creature of gamma horror, tied to the One Below All.", "https://en.wikipedia.org/wiki/Immortal_Hulk", ["immortal-hulk-vol1", "immortal-hulk-vol2"]),
        _ver("maestro", "Maestro", "Earth-9200", "future", "The Incredible Hulk: Future Imperfect #1 (1992)", "Hulk king of ruins", "An aged, evil Bruce Banner rules a post-apocalyptic world as the tyrant Maestro.", "https://en.wikipedia.org/wiki/Maestro_(character)", ["future-imperfect"]),
        _ver("joe-fixit", "Joe Fixit / Grey Hulk", "Earth-616", "main", "The Incredible Hulk Vol. 2 #331 (1987)", "Las Vegas enforcer", "The cunning grey Hulk worked as a mob enforcer in Vegas — a smarter, crueler side of Banner.", "https://en.wikipedia.org/wiki/Joe_Fixit", ["hulk-peter-david", "hulk-grey-goliath"]),
        _ver("ultimate-hulk", "Ultimate Hulk", "Earth-1610", "ultimate", "Ultimate Marvel Team-Up #2 (2001)", "Cannibal monster", "The Ultimate Universe's Hulk is a grotesque, cannibalistic weapon of mass destruction.", "https://en.wikipedia.org/wiki/Ultimate_Hulk", ["ultimate-hulk-vol1"]),
        _ver("red-hulk", "Red Hulk", "Earth-616", "main", "Hulk Vol. 2 #1 (2008)", "General Ross transformed", "Thunderbolt Ross became the Red Hulk — hotter, smarter, and as destructive as the green original.", "https://en.wikipedia.org/wiki/Red_Hulk", ["hulk-red-hulk-origin"]),
    ],
    "runs": {
        "hulk-origin": {**_run("hulk-origin", "banner-hulk", "Hulk: Gray", "Jeph Loeb & Tim Sale", "2003–04", "Hulk: Gray #1–6", "Modern Age", "None", "A moody retelling of Bruce Banner's first days as the Hulk.", "Hulk: Gray", "0785110988"), "isbn": "9780785110987"},
        "hulk-peter-david": {**_run("hulk-peter-david", "banner-hulk", "The Incredible Hulk by Peter David Vol. 1", "Peter David & Todd McFarlane", "1987–88", "Incredible Hulk #330–337, 340–345", "Modern Age", "None", "Peter David's legendary run begins — multiple Hulk personalities emerge.", "Incredible Hulk Epic Collection: Ghosts of the Past", "1302908094"), "isbn": "9781302908094"},
        "planet-hulk": {**_run("planet-hulk", "world-war-hulk", "Planet Hulk", "Greg Pak & Carlo Pagulayan", "2006–07", "Incredible Hulk #92–105", "Modern Age", "None", "The Hulk is exiled to Sakaar and becomes a gladiator king.", "Planet Hulk", "0785122581"), "isbn": "9780785122586"},
        "world-war-hulk-event": {**_run("world-war-hulk-event", "world-war-hulk", "World War Hulk", "Greg Pak & John Romita Jr.", "2007", "World War Hulk #1–5", "Modern Age", "Planet Hulk", "Hulk returns to Earth and fights every hero who wronged him.", "World War Hulk", "0785128504"), "isbn": "9780785128502"},
        "immortal-hulk-vol1": {**_run("immortal-hulk-vol1", "immortal-hulk", "The Immortal Hulk Vol. 1", "Al Ewing & Joe Bennett", "2018", "The Immortal Hulk #1–5", "Modern Age", "None", "Horror-tinged Hulk storytelling that reinvents the gamma mythos.", "The Immortal Hulk Vol. 1", "1302912554"), "isbn": "9781302912554"},
        "immortal-hulk-vol2": {**_run("immortal-hulk-vol2", "immortal-hulk", "The Immortal Hulk Vol. 2", "Al Ewing & Joe Bennett", "2018–19", "The Immortal Hulk #6–10", "Modern Age", "Immortal Hulk Vol. 1", "The One Below All and the Devil Hulk escalate Ewing's cosmic horror.", "The Immortal Hulk Vol. 2", "1302915103"), "isbn": "9781302915103"},
        "future-imperfect": {**_run("future-imperfect", "maestro", "Future Imperfect", "Peter David & George Pérez", "1992–93", "Incredible Hulk: Future Imperfect #1–2", "Modern Age", "None", "The Hulk meets his future self — the tyrant Maestro.", "Hulk: Future Imperfect", "0785100789"), "isbn": "9780785100789"},
        "hulk-grey-goliath": {**_run("hulk-grey-goliath", "joe-fixit", "Hulk: Pardoned", "Peter David & Jeff Purves", "1990", "Incredible Hulk #377", "Modern Age", "Peter David run", "The landmark issue where Banner and his personalities merge.", "Incredible Hulk Epic Collection: Pardoned", "1302908108"), "isbn": "9781302908108"},
        "ultimate-hulk-vol1": {**_run("ultimate-hulk-vol1", "ultimate-hulk", "The Ultimates: Hulk", "Mark Millar & Bryan Hitch", "2002", "Ultimates #1–6 (Hulk focus)", "Ultimate", "None", "Ultimate Hulk as a cannibalistic weapon in the Ultimates.", "The Ultimates Vol. 1", "0785107880"), "isbn": "9780785107880"},
        "hulk-red-hulk-origin": {**_run("hulk-red-hulk-origin", "red-hulk", "Hulk Vol. 2: Red Hulk", "Jeff Parker & Ed McGuinness", "2008–09", "Hulk Vol. 2 #1–6", "Modern Age", "None", "The Red Hulk debuts — hotter, red, and punching the Abomination to death.", "Hulk Vol. 2: Red Hulk", "0785139835"), "isbn": "9780785139835"},
    },
    "home_runs": ["hulk-peter-david", "planet-hulk", "world-war-hulk-event", "immortal-hulk-vol1", "future-imperfect", "hulk-origin", "immortal-hulk-vol2", "ultimate-hulk-vol1", "hulk-red-hulk-origin", "hulk-grey-goliath"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Hulk",
        "lead": "The madder Hulk gets, the stronger Hulk gets — a walking gamma bomb with a human heart.",
        "summary": "The Hulk is Bruce Banner, a physicist transformed by gamma radiation into a green-skinned powerhouse of rage. Created by Stan Lee and Jack Kirby, he debuted in The Incredible Hulk #1 (1962). Peter David's personality-driven run, Planet Hulk, and Al Ewing's Immortal Hulk represent the character's greatest reinventions across horror, epic, and tragedy.",
        "facts": [
            {"label": "Alter ego", "value": "Robert Bruce Banner"},
            {"label": "First appearance", "value": "The Incredible Hulk #1 (1962)"},
            {"label": "Created by", "value": "Stan Lee & Jack Kirby"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Catchphrase", "value": "Hulk smash!"},
            {"label": "Allies", "value": "Rick Jones, She-Hulk, Skaar"},
            {"label": "Notable foes", "value": "Abomination, Leader, General Ross"},
            {"label": "Powers", "value": "Superhuman strength scaling with rage"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            _screen("hulk-2003", "Hulk", "Ang Lee · Eric Bana", "https://en.wikipedia.org/wiki/Hulk_(film)", "https://www.imdb.com/title/tt0286716/", year="2003"),
            _screen("hulk-2008", "The Incredible Hulk", "Edward Norton", "https://en.wikipedia.org/wiki/The_Incredible_Hulk_(film)", "https://www.imdb.com/title/tt0800080/", year="2008"),
            _screen("hulk-ragnarok", "Thor: Ragnarok", "Mark Ruffalo · Planet Hulk homage", "https://en.wikipedia.org/wiki/Thor:_Ragnarok", "https://www.imdb.com/title/tt3501632/", year="2017"),
        ]},
        {"group": "Animated", "items": [
            _screen("hulk-tas", "The Incredible Hulk (1982)", "Classic animated series", "https://en.wikipedia.org/wiki/The_Incredible_Hulk_(1982_TV_series)", "https://www.imdb.com/title/tt0084051/", years="1982–1983"),
            _screen("hulk-1996", "The Incredible Hulk (1996)", "Fox Kids animated", "https://en.wikipedia.org/wiki/The_Incredible_Hulk_(1996_TV_series)", "https://www.imdb.com/title/tt0115216/", years="1996–1997"),
        ]},
    ],
    "themes": {
        "banner-hulk": (76, 175, 80), "world-war-hulk": (40, 120, 50), "immortal-hulk": (20, 80, 40),
        "maestro": (100, 60, 120), "joe-fixit": (120, 120, 120), "ultimate-hulk": (60, 140, 60),
        "red-hulk": (180, 40, 30),
    },
    "issues": {},
}


HAWKEYE = {
    "id": "hawkeye",
    "brand": "Hawkeye",
    "title": "Hawkeye — Aim Across the Multiverse",
    "nav_who": "Who is Hawkeye",
    "nav_verses": "Verses",
    "who_id": "who-is-hawkeye",
    "header_img": "hawkeye-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #7b1fa2, #4a148c 45%, #1a0a2e)",
    "verses_h2": "Hawkeye Across the Multiverse",
    "verses_p": "versions across Marvel's sharpshooters — Clint Barton, Kate Bishop, Ronin, Ultimate Hawkeye, and the Fraction street-level era.",
    "comics_p": "Essential Hawkeye stories — from West Coast Avengers and Ronin to Matt Fraction's acclaimed solo run and Kate Bishop's rise.",
    "screen_p": "Live-action and animated appearances — from the MCU Hawkeye series and Avengers films to animated Young Avengers.",
    "types": MARVEL_TYPES,
    "versions": [
        _ver("clint-barton", "Clint Barton", "Earth-616 / Prime Marvel", "main", "Tales of Suspense #57 (1964)", "The world's greatest marksman", "A circus orphan turned Avenger — Clint Barton has no powers, just perfect aim and stubborn heart.", "https://en.wikipedia.org/wiki/Hawkeye_(Clint_Barton)", ["hawkeye-solo-classic", "hawkeye-west-coast"]),
        _ver("kate-bishop", "Kate Bishop", "Earth-616 / Prime Marvel", "main", "Young Avengers #1 (2005)", "Hawkeye, obviously", "A wealthy Young Avenger who earned the Hawkeye name through skill, sass, and sheer determination.", "https://en.wikipedia.org/wiki/Kate_Bishop", ["kate-young-avengers", "kate-hawkeye-fraction"]),
        _ver("ronin-clint", "Ronin (Clint Barton)", "Earth-616", "main", "New Avengers #11 (2005)", "The blade in the dark", "After Civil War, Clint Barton donned the Ronin identity — a ninja warrior with a katana instead of a bow.", "https://en.wikipedia.org/wiki/Ronin_(Marvel_Comics)", ["ronin-new-avengers", "hawkeye-ronin"]),
        _ver("ultimate-hawkeye", "Ultimate Hawkeye", "Earth-1610", "ultimate", "Ultimates #5 (2002)", "Weapon X marksman", "The Ultimate Universe's Clint Barton — a cynical soldier with enhanced vision and brutal efficiency.", "https://en.wikipedia.org/wiki/Ultimate_Hawkeye", ["ultimate-hawkeye-vol1"]),
        _ver("fraction-hawkeye", "Hawkeye (Fraction Era)", "Earth-616", "main", "Hawkeye Vol. 4 #1 (2012)", "Bro, you look like Hawkeye", "Matt Fraction and David Aja's street-level masterpiece — Pizza Dog, the Tracksuit Mafia, and everyday heroism.", "https://en.wikipedia.org/wiki/Hawkeye_(2012_comic_book)", ["hawkeye-fraction-vol1", "hawkeye-fraction-vol2"]),
    ],
    "runs": {
        "hawkeye-solo-classic": {**_run("hawkeye-solo-classic", "clint-barton", "Hawkeye: Solo", "Tom DeFalco & various", "1983", "Hawkeye #1–4 (1983 miniseries)", "Modern Age", "None", "Clint Barton's first solo miniseries establishes his rogues and roguish charm.", "Hawkeye: Solo", "0785184545"), "isbn": "9780785184545"},
        "hawkeye-west-coast": {**_run("hawkeye-west-coast", "clint-barton", "West Coast Avengers", "Steve Englehart & Al Milgrom", "1984–86", "West Coast Avengers #1–12", "Modern Age", "None", "Clint leads the West Coast team and marries Mockingbird.", "West Coast Avengers Vol. 1", "0785195199"), "isbn": "9780785195199"},
        "kate-young-avengers": {**_run("kate-young-avengers", "kate-bishop", "Young Avengers", "Allan Heinberg & Jim Cheung", "2005–06", "Young Avengers #1–12", "Modern Age", "None", "Kate Bishop debuts as the Young Avenger who takes the Hawkeye name.", "Young Avengers", "0785123049"), "isbn": "9780785123049"},
        "kate-hawkeye-fraction": {**_run("kate-hawkeye-fraction", "kate-bishop", "Hawkeye: Kate Bishop", "Kelly Thompson & Leonardo Romero", "2021–23", "Hawkeye Vol. 5 #1–6", "Modern Age", "Fraction Hawkeye", "Kate Bishop's solo era after Clint — private investigator in Los Angeles.", "Hawkeye: Kate Bishop Vol. 1", "1302933846"), "isbn": "9781302933846"},
        "ronin-new-avengers": {**_run("ronin-new-avengers", "ronin-clint", "New Avengers: Ronin", "Brian Michael Bendis & David Finch", "2005", "New Avengers #11–13", "Modern Age", "None", "The mysterious Ronin joins the New Avengers — later revealed as Clint Barton.", "New Avengers Vol. 2", "0785117720"), "isbn": "9780785117720"},
        "hawkeye-ronin": {**_run("hawkeye-ronin", "ronin-clint", "Hawkeye: Ronin", "Mike Benson & various", "2007–08", "Hawkeye Vol. 3 #1–5", "Modern Age", "New Avengers Ronin", "Clint reconciles his Ronin past with the Hawkeye identity.", "Hawkeye: Ronin", "0785129923"), "isbn": "9780785129923"},
        "ultimate-hawkeye-vol1": {**_run("ultimate-hawkeye-vol1", "ultimate-hawkeye", "Ultimate Comics: Hawkeye", "Jonathan Hickman & Rafa Sandoval", "2011", "Ultimate Comics: Hawkeye #1–4", "Ultimate", "None", "Ultimate Hawkeye in a post-Ultimatum world — brutal and stripped down.", "Ultimate Comics: Hawkeye", "0785157370"), "isbn": "9780785157370"},
        "hawkeye-fraction-vol1": {**_run("hawkeye-fraction-vol1", "fraction-hawkeye", "Hawkeye Vol. 1: My Life as a Weapon", "Matt Fraction & David Aja", "2012", "Hawkeye Vol. 4 #1–5", "Modern Age", "None", "The acclaimed street-level run — Pizza Dog, tracksuits, and Brooklyn.", "Hawkeye Vol. 1: My Life as a Weapon", "0785165628"), "isbn": "9780785165628"},
        "hawkeye-fraction-vol2": {**_run("hawkeye-fraction-vol2", "fraction-hawkeye", "Hawkeye Vol. 2: Little Hits", "Matt Fraction & David Aja", "2013", "Hawkeye Vol. 4 #6–11", "Modern Age", "Fraction Vol. 1", "The Tracksuit Mafia war escalates in Fraction and Aja's visual masterpiece.", "Hawkeye Vol. 2: Little Hits", "0785165636"), "isbn": "9780785165636"},
    },
    "home_runs": ["hawkeye-fraction-vol1", "hawkeye-fraction-vol2", "kate-young-avengers", "ronin-new-avengers", "hawkeye-west-coast", "ultimate-hawkeye-vol1", "kate-hawkeye-fraction", "hawkeye-solo-classic", "hawkeye-ronin"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Hawkeye_(Clint_Barton)",
        "lead": "No superpowers. No invincibility. Just a bow, a quiver, and aim that never misses.",
        "summary": "Hawkeye is Clint Barton, a master archer and founding West Coast Avenger who proves you don't need powers to stand beside gods. Created by Stan Lee and Don Heck, he debuted in Tales of Suspense #57 (1964). Kate Bishop later claimed the mantle, and Matt Fraction's 2012 run became the definitive modern take on the character.",
        "facts": [
            {"label": "Notable bearers", "value": "Clint Barton, Kate Bishop"},
            {"label": "First appearance", "value": "Tales of Suspense #57 (1964)"},
            {"label": "Created by", "value": "Stan Lee & Don Heck"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Signature weapon", "value": "Compound bow and trick arrows"},
            {"label": "Allies", "value": "Avengers, Kate Bishop, Mockingbird"},
            {"label": "Notable foes", "value": "Tracksuit Mafia, Crossfire, Trick Shot"},
            {"label": "Powers", "value": "Peak human archery, martial arts"},
        ],
    },
    "screen": [
        {"group": "MCU", "items": [
            _screen("hawkeye-2021", "Hawkeye", "Jeremy Renner & Hailee Steinfeld", "https://en.wikipedia.org/wiki/Hawkeye_(miniseries)", "https://www.imdb.com/title/tt10160804/", year="2021"),
            _screen("avengers-clint", "The Avengers", "Jeremy Renner", "https://en.wikipedia.org/wiki/The_Avengers_(2012_film)", "https://www.imdb.com/title/tt0848228/", year="2012"),
            _screen("endgame-clint", "Avengers: Endgame", "Jeremy Renner · Ronin", "https://en.wikipedia.org/wiki/Avengers:_Endgame", "https://www.imdb.com/title/tt4154796/", year="2019"),
        ]},
        {"group": "Animated", "items": [
            _screen("hawkeye-animated", "The Avengers: Earth's Mightiest Heroes", "Clint Barton", "https://en.wikipedia.org/wiki/The_Avengers:_Earth%27s_Mightiest_Heroes", "https://www.imdb.com/title/tt1626038/", years="2010–2012"),
        ]},
    ],
    "themes": {
        "clint-barton": (123, 31, 162), "kate-bishop": (156, 39, 176), "ronin-clint": (40, 40, 50),
        "ultimate-hawkeye": (80, 20, 100), "fraction-hawkeye": (180, 60, 40),
    },
    "issues": {},
}


BLACK_PANTHER = {
    "id": "black-panther",
    "brand": "Black Panther",
    "title": "Black Panther — Wakanda Across the Multiverse",
    "nav_who": "Who is Black Panther",
    "nav_verses": "Verses",
    "who_id": "who-is-black-panther",
    "header_img": "black-panther-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #1a237e, #0d1642 45%, #020208)",
    "verses_h2": "Black Panther Across the Multiverse",
    "verses_p": "versions across Marvel's Wakandan throne — T'Challa, Shuri, Killmonger, Ultimate BP, 2099, and the Storm royal era.",
    "comics_p": "Essential Black Panther stories — from Christopher Priest and Ta-Nehisi Coates to Shuri's reign and World of Wakanda.",
    "screen_p": "Live-action and animated appearances — from Ryan Coogler's MCU films to the 1960s Fantastic Four animated guest spots.",
    "types": MARVEL_TYPES,
    "versions": [
        _ver("tchalla", "T'Challa", "Earth-616 / Prime Marvel", "main", "Fantastic Four #52 (1966)", "King of the dead", "T'Challa is king of Wakanda and the Black Panther — a genius strategist who opened his nation to the world.", "https://en.wikipedia.org/wiki/Black_Panther_(character)", ["bp-priest-vol1", "bp-coates-vol1", "bp-jungle-action"]),
        _ver("shuri", "Shuri", "Earth-616 / Prime Marvel", "main", "Black Panther Vol. 4 #2 (2005)", "The queen of science", "T'Challa's sister Shuri became Black Panther during her brother's incapacitation — a tech genius and warrior queen.", "https://en.wikipedia.org/wiki/Shuri_(character)", ["shuri-black-panther", "shuri-solo"]),
        _ver("killmonger", "Killmonger", "Earth-616", "alternate", "Jungle Action #6 (1973)", "The usurper", "Erik Killmonger is the exiled claimant to Wakanda's throne — T'Challa's greatest rival for the mantle.", "https://en.wikipedia.org/wiki/Killmonger", ["bp-killmonger-saga", "bp-jungle-action"]),
        _ver("ultimate-bp", "Ultimate Black Panther", "Earth-1610", "ultimate", "Ultimates Vol. 2 #9 (2005)", "Ultimate Wakanda", "The Ultimate Universe's T'Challa — a mute king with a very different Wakandan history.", "https://en.wikipedia.org/wiki/Ultimate_Black_Panther", ["ultimate-bp-vol1"]),
        _ver("bp-2099", "Black Panther 2099", "Earth-928 / 2099", "future", "2099: World of Tomorrow #1 (1999)", "Future king", "In the 2099 timeline, a new Black Panther protects a Wakanda transformed by the future.", "https://en.wikipedia.org/wiki/Black_Panther_2099", ["2099-bp-world"]),
        _ver("storm-tchalla", "Storm & T'Challa", "Earth-616", "main", "Black Panther Vol. 4 #18 (2006)", "Royal power couple", "When Storm of the X-Men married T'Challa, Wakanda gained a queen — and Marvel gained a royal epic.", "https://en.wikipedia.org/wiki/Storm_(Marvel_Comics)", ["bp-storm-wedding", "bp-doomwar"]),
    ],
    "runs": {
        "bp-jungle-action": {**_run("bp-jungle-action", "tchalla", "Black Panther: Jungle Action", "Don McGregor & Rich Buckler", "1973–76", "Jungle Action #6–24", "Bronze Age", "None — classic entry", "Don McGregor's literary run — the first great Black Panther stories.", "Black Panther: Jungle Action", "0785116865"), "isbn": "9780785116865"},
        "bp-priest-vol1": {**_run("bp-priest-vol1", "tchalla", "Black Panther by Christopher Priest Vol. 1", "Christopher Priest & Mark Texeira", "1998–99", "Black Panther Vol. 3 #1–7", "Modern Age", "None", "Christopher Priest's genre-defining run — espionage, humor, and Wakandan politics.", "Black Panther by Christopher Priest Vol. 1", "1302901901"), "isbn": "9781302901901"},
        "bp-coates-vol1": {**_run("bp-coates-vol1", "tchalla", "Black Panther: A Nation Under Our Feet", "Ta-Nehisi Coates & Brian Stelfreeze", "2016", "Black Panther Vol. 6 #1–4", "Modern Age", "None", "Ta-Nehisi Coates explores revolution, monarchy, and Wakanda's soul.", "Black Panther: A Nation Under Our Feet Book 1", "1302900530"), "isbn": "9781302900530"},
        "shuri-black-panther": {**_run("shuri-black-panther", "shuri", "Black Panther: Shuri", "Reginald Hudlin & various", "2009", "Black Panther Vol. 5 #7–12", "Modern Age", "None", "Shuri takes the Black Panther mantle when T'Challa falls.", "Black Panther: Shuri", "0785133420"), "isbn": "9780785133420"},
        "shuri-solo": {**_run("shuri-solo", "shuri", "Shuri", "Nnedi Okorafor & Leonardo Romero", "2018–19", "Shuri #1–5", "Modern Age", "None", "Shuri's solo series as Wakanda's princess-scientist.", "Shuri Vol. 1", "1302915103"), "isbn": "9781302915103"},
        "bp-killmonger-saga": {**_run("bp-killmonger-saga", "killmonger", "Killmonger", "Bryan Edward Hill & Juan Ferreyra", "2018–19", "Killmonger #1–5", "Modern Age", "None", "The origin of Erik Killmonger — exile, rage, and the throne denied.", "Killmonger", "1302912554"), "isbn": "9781302912554"},
        "ultimate-bp-vol1": {**_run("ultimate-bp-vol1", "ultimate-bp", "Ultimate Black Panther", "Mark Millar & Bryan Hitch", "2005", "Ultimates Vol. 2 #9–13", "Ultimate", "None", "Ultimate T'Challa joins the Ultimates under very different circumstances.", "Ultimates Vol. 2", "0785116784"), "isbn": "9780785116784"},
        "2099-bp-world": {**_run("2099-bp-world", "bp-2099", "2099: World of Wakanda", "Various", "1999", "2099: World of Tomorrow", "2099", "None", "The 2099 line's vision of a future Wakanda.", "2099: World of Tomorrow", "0785107120"), "isbn": "9780785107120"},
        "bp-storm-wedding": {**_run("bp-storm-wedding", "storm-tchalla", "Black Panther: The Wedding", "Reginald Hudlin & various", "2006", "Black Panther Vol. 4 #17–18", "Modern Age", "None", "The wedding of T'Challa and Storm — a royal Marvel event.", "Black Panther: The Bride", "0785126578"), "isbn": "9780785126578"},
        "bp-doomwar": {**_run("bp-doomwar", "storm-tchalla", "Doomwar", "Jonathan Hickman & various", "2010", "Doomwar #1–6", "Modern Age", "Black Panther wedding arc", "Doctor Doom invades Wakanda — T'Challa and Storm defend their nation.", "Doomwar", "0785146920"), "isbn": "9780785146920"},
    },
    "home_runs": ["bp-priest-vol1", "bp-coates-vol1", "bp-jungle-action", "shuri-black-panther", "shuri-solo", "bp-killmonger-saga", "ultimate-bp-vol1", "bp-storm-wedding", "bp-doomwar", "2099-bp-world"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Black_Panther_(character)",
        "lead": "Wakanda forever — a king, a nation, and a legacy that outlasts any single ruler.",
        "summary": "Black Panther is the ceremonial title of the ruler and protector of Wakanda, a technologically advanced African nation. T'Challa, created by Stan Lee and Jack Kirby, debuted in Fantastic Four #52 (1966) — the first Black superhero in mainstream American comics. Shuri, Killmonger, and alternate-timeline variants have all claimed or challenged the mantle.",
        "facts": [
            {"label": "Notable bearers", "value": "T'Challa, Shuri"},
            {"label": "First appearance", "value": "Fantastic Four #52 (1966)"},
            {"label": "Created by", "value": "Stan Lee & Jack Kirby"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Nation", "value": "Wakanda"},
            {"label": "Allies", "value": "Avengers, Dora Milaje, Storm"},
            {"label": "Notable foes", "value": "Killmonger, Klaw, Man-Ape"},
            {"label": "Powers", "value": "Heart-shaped herb enhancement, vibranium suit"},
        ],
    },
    "screen": [
        {"group": "MCU films", "items": [
            _screen("bp-2018", "Black Panther", "Chadwick Boseman · Ryan Coogler", "https://en.wikipedia.org/wiki/Black_Panther_(film)", "https://www.imdb.com/title/tt1825683/", year="2018"),
            _screen("bp-wf", "Black Panther: Wakanda Forever", "Ryan Coogler · Shuri", "https://en.wikipedia.org/wiki/Black_Panther:_Wakanda_Forever", "https://www.imdb.com/title/tt9114286/", year="2022"),
            _screen("bp-cw", "Captain America: Civil War", "Chadwick Boseman · Introduction", "https://en.wikipedia.org/wiki/Captain_America:_Civil_War", "https://www.imdb.com/title/tt3498820/", year="2016"),
        ]},
        {"group": "Animated", "items": [
            _screen("bp-animated", "Black Panther (2009)", "Animated miniseries", "https://en.wikipedia.org/wiki/Black_Panther_(TV_series)", "https://www.imdb.com/title/tt1439621/", year="2009"),
        ]},
    ],
    "themes": {
        "tchalla": (26, 35, 126), "shuri": (100, 50, 180), "killmonger": (140, 30, 40),
        "ultimate-bp": (20, 30, 90), "bp-2099": (10, 60, 100), "storm-tchalla": (60, 40, 120),
    },
    "issues": {},
}


BLACK_WIDOW = {
    "id": "black-widow",
    "brand": "Black Widow",
    "title": "Black Widow — Shadows Across the Multiverse",
    "nav_who": "Who is Black Widow",
    "nav_verses": "Verses",
    "who_id": "who-is-black-widow",
    "header_img": "black-widow-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #b71c1c, #4a0e0e 45%, #0a0202)",
    "verses_h2": "Black Widow Across the Multiverse",
    "verses_p": "versions across Marvel's espionage underworld — Natasha Romanoff, Yelena Belova, Contessa Valentina, Ultimate Natasha, and White Widow.",
    "comics_p": "Essential Black Widow stories — from the 1970s solo tales and Waid/Samnee to Yelena Belova and the White Widow era.",
    "screen_p": "Live-action and animated appearances — from the MCU Black Widow film and Avengers to animated spy adventures.",
    "types": MARVEL_TYPES,
    "versions": [
        _ver("natasha-romanoff", "Natasha Romanoff", "Earth-616 / Prime Marvel", "main", "Tales of Suspense #52 (1964)", "The spy who came in from the cold", "Trained in the Red Room, Natasha Romanoff defected to become the world's most dangerous spy and Avenger.", "https://en.wikipedia.org/wiki/Black_Widow_(Natasha_Romanoff)", ["bw-waid-samnee", "bw-1970s-solo", "bw-death"]),
        _ver("yelena-belova", "Yelena Belova", "Earth-616 / Prime Marvel", "main", "Inhumans #5 (1999)", "The other Widow", "A fellow Red Room graduate who challenged Natasha for the Black Widow name — ally, rival, and successor.", "https://en.wikipedia.org/wiki/Yelena_Belova", ["yelena-against-world", "yelena-white-widow"]),
        _ver("contessa-valentina", "Contessa Valentina Allegra de Fontaine", "Earth-616", "main", "Strange Tales #159 (1967)", "The spy mistress", "Valentina Allegra de Fontaine is a S.H.I.E.L.D. operative whose allegiances and eras shift across Marvel's espionage landscape.", "https://en.wikipedia.org/wiki/Contessa_Valletta", ["contessa-strange-tales", "contessa-valkyrie"]),
        _ver("ultimate-natasha", "Ultimate Black Widow", "Earth-1610", "ultimate", "Ultimates #7 (2002)", "The traitor", "Ultimate Natasha Romanoff was a double agent who betrayed the Ultimates in one of the line's biggest twists.", "https://en.wikipedia.org/wiki/Ultimate_Black_Widow", ["ultimate-bw-betrayal"]),
        _ver("white-widow-yelena", "White Widow (Yelena)", "Earth-616", "main", "Black Widow Vol. 8 #1 (2020)", "White suit, new mission", "Yelena Belova reclaims the spotlight as the White Widow — operating in Natasha's shadow after her death.", "https://en.wikipedia.org/wiki/Yelena_Belova", ["white-widow-vol1", "yelena-white-widow"]),
    ],
    "runs": {
        "bw-1970s-solo": {**_run("bw-1970s-solo", "natasha-romanoff", "Black Widow: The Sting of the Widow", "Various", "1970", "Amazing Spider-Man #86, Amazing Adventures #1–8", "Bronze Age", "None", "Natasha's earliest solo adventures — spy noir in the Marvel style.", "Black Widow: The Sting of the Widow", "0785115702"), "isbn": "9780785115702"},
        "bw-waid-samnee": {**_run("bw-waid-samnee", "natasha-romanoff", "Black Widow: The Name of the Rose", "Mark Waid & Chris Samnee", "2016", "Black Widow Vol. 5 #1–6", "Modern Age", "None", "Waid and Samnee's stylish spy thriller — one of the best Widow runs ever.", "Black Widow: The Name of the Rose", "0785195125"), "isbn": "9780785195125"},
        "bw-death": {**_run("bw-death", "natasha-romanoff", "Black Widow: No Restraints Play", "Jen & Sylvia Soska", "2019", "Black Widow Vol. 7 #1–5", "Modern Age", "None", "Natasha's final solo arc before Secret Empire's aftermath.", "Black Widow Vol. 1: The Ties That Bind", "1302912554"), "isbn": "9781302912554"},
        "yelena-against-world": {**_run("yelena-against-world", "yelena-belova", "Black Widow: Pale Little Spider", "Greg Rucka & Igor Kordey", "2002", "Black Widow #1–3 (2002 miniseries)", "Modern Age", "None", "Yelena Belova's origin and rivalry with Natasha.", "Black Widow: Pale Little Spider", "0785108907"), "isbn": "9780785108907"},
        "yelena-white-widow": {**_run("yelena-white-widow", "yelena-belova", "Black Widow: Widow's Sting", "Margaret Stohl & various", "2020", "Black Widow Vol. 8 #1–5", "Modern Age", "None", "Yelena steps up as the new Black Widow after Natasha's fall.", "Black Widow: Widow's Sting", "1302921376"), "isbn": "9781302921371"},
        "contessa-strange-tales": {**_run("contessa-strange-tales", "contessa-valentina", "Strange Tales: Contessa", "Jim Steranko & various", "1967", "Strange Tales #159–168", "Silver Age", "None", "Contessa Valentina's S.H.I.E.L.D. debut alongside Nick Fury.", "Nick Fury/Agent of S.H.I.E.L.D. Masterworks", "0785159560"), "isbn": "9780785159560"},
        "contessa-valkyrie": {**_run("contessa-valkyrie", "contessa-valentina", "The New Avengers: The Collective", "Brian Michael Bendis & David Finch", "2005–06", "New Avengers #16–20", "Modern Age", "None", "Contessa Valentina in modern espionage storylines.", "New Avengers Vol. 3", "0785117720"), "isbn": "9780785117720"},
        "ultimate-bw-betrayal": {**_run("ultimate-bw-betrayal", "ultimate-natasha", "Ultimates: Black Widow Betrayal", "Mark Millar & Bryan Hitch", "2004", "Ultimates Vol. 2 #9–13", "Ultimate", "None", "Ultimate Natasha's betrayal of the Ultimates — one of the line's biggest twists.", "Ultimates Vol. 2", "0785116784"), "isbn": "9780785116784"},
        "white-widow-vol1": {**_run("white-widow-vol1", "white-widow-yelena", "White Widow", "Kelly Thompson & Elena Casagrande", "2022", "Black Widow Vol. 8 #6–10", "Modern Age", "Widow's Sting", "Yelena as White Widow — espionage with a new visual identity.", "White Widow", "1302933846"), "isbn": "9781302933846"},
    },
    "home_runs": ["bw-waid-samnee", "yelena-against-world", "white-widow-vol1", "ultimate-bw-betrayal", "bw-1970s-solo", "yelena-white-widow", "contessa-strange-tales", "bw-death", "contessa-valkyrie"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Black_Widow_(Natasha_Romanoff)",
        "lead": "Red Room trained. Avenger forged. The world's deadliest spy wears no armor — only precision.",
        "summary": "Black Widow is Natasha Romanoff, a Russian spy trained in the Red Room who defected to S.H.I.E.L.D. and the Avengers. Created by Stan Lee, Don Rico, and Don Heck, she debuted in Tales of Suspense #52 (1964). Yelena Belova, Contessa Valentina, and Ultimate Natasha represent the wider espionage world orbiting the Widow mantle.",
        "facts": [
            {"label": "Notable bearers", "value": "Natasha Romanoff, Yelena Belova"},
            {"label": "First appearance", "value": "Tales of Suspense #52 (1964)"},
            {"label": "Created by", "value": "Stan Lee, Don Rico, Don Heck"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Training", "value": "Red Room Academy"},
            {"label": "Allies", "value": "Avengers, Hawkeye, Bucky Barnes"},
            {"label": "Notable foes", "value": "Taskmaster, Red Room, Madame Hydra"},
            {"label": "Powers", "value": "Peak human agility, espionage, martial arts"},
        ],
    },
    "screen": [
        {"group": "MCU films", "items": [
            _screen("bw-2021", "Black Widow", "Scarlett Johansson · Origin", "https://en.wikipedia.org/wiki/Black_Widow_(2021_film)", "https://www.imdb.com/title/tt3480822/", year="2021"),
            _screen("bw-avengers", "The Avengers", "Scarlett Johansson", "https://en.wikipedia.org/wiki/The_Avengers_(2012_film)", "https://www.imdb.com/title/tt0848228/", year="2012"),
            _screen("bw-winter-soldier", "Captain America: The Winter Soldier", "Scarlett Johansson", "https://en.wikipedia.org/wiki/Captain_America:_The_Winter_Soldier", "https://www.imdb.com/title/tt1843866/", year="2014"),
        ]},
        {"group": "Animated", "items": [
            _screen("bw-animated", "Avengers: Earth's Mightiest Heroes", "Natasha Romanoff", "https://en.wikipedia.org/wiki/The_Avengers:_Earth%27s_Mightiest_Heroes", "https://www.imdb.com/title/tt1626038/", years="2010–2012"),
        ]},
    ],
    "themes": {
        "natasha-romanoff": (183, 28, 28), "yelena-belova": (200, 60, 80), "contessa-valentina": (80, 40, 100),
        "ultimate-natasha": (120, 20, 30), "white-widow-yelena": (220, 220, 230),
    },
    "issues": {},
}


MARVEL_PACKS = [
    CAPTAIN_AMERICA,
    IRON_MAN,
    INCREDIBLE_HULK,
    HAWKEYE,
    BLACK_PANTHER,
    BLACK_WIDOW,
]
