"""Additional Marvel character pack definitions for character reading guides."""

MARVEL_TYPES = {
    "main": "Main Continuity",
    "ultimate": "Ultimate Universe",
    "multiverse": "Multiverse",
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


DOCTOR_DOOM = {
    "id": "doctor-doom",
    "brand": "Doctor Doom",
    "title": "Doctor Doom — Latveria Across the Multiverse",
    "nav_who": "Who is Doctor Doom",
    "nav_verses": "Verses",
    "who_id": "who-is-doctor-doom",
    "header_img": "doctor-doom-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #006633, #003319 45%, #010805)",
    "verses_h2": "Doctor Doom Across the Multiverse",
    "verses_p": "versions across Marvel's iron throne — Victor von Doom, God Emperor Doom, Infamous Iron Man, Ultimate Doom, and alternate Latverias.",
    "comics_p": "Essential Doctor Doom stories — from Books of Doom and Unthinkable to Secret Wars 2015 and Infamous Iron Man.",
    "screen_p": "Live-action and animated appearances — from Fantastic Four films and Avengers: Doomsday to the 1967 Marvel Super Heroes shorts.",
    "types": MARVEL_TYPES,
    "versions": [
        version_obj("victor-von-doom", "Victor von Doom", "Earth-616 / Prime Marvel", "main", "Fantastic Four #5 (1962)", "Master of sorcery and science", "Victor von Doom is the iron-masked monarch of Latveria — Reed Richards' rival and Marvel's greatest villain who believes only he can save the world.", "https://en.wikipedia.org/wiki/Doctor_Doom", ["doom-books-of-doom", "doom-unthinkable", "doom-triumph-torment"]),
        version_obj("god-emperor-doom", "God Emperor Doom", "Battleworld / Secret Wars", "multiverse", "Secret Wars #3 (2015)", "He became a god", "During Secret Wars, Doom seized the Beyonder's power and rebuilt reality as Battleworld's absolute ruler — wearing the Infinity Gauntlet and Molecule Man's might.", "https://en.wikipedia.org/wiki/Secret_Wars_(2015_comic_book)", ["doom-secret-wars-2015", "doom-time-runs-out"]),
        version_obj("infamous-iron-man", "Infamous Iron Man", "Earth-616", "alternate", "Infamous Iron Man #1 (2016)", "The Superior Iron Doom", "After Civil War II, Doctor Doom sought redemption by donning Tony Stark's armor — a fallen tyrant playing hero.", "https://en.wikipedia.org/wiki/Infamous_Iron_Man", ["doom-infamous-iron-man", "doom-unthinkable"]),
        version_obj("ultimate-doom", "Ultimate Doctor Doom", "Earth-1610", "ultimate", "Ultimate Fantastic Four #7 (2004)", "Victor Van Damme", "The Ultimate Universe's Victor Van Damme — a metal-skinned sorcerer-scientist with a very different origin and grudge against Reed Richards.", "https://en.wikipedia.org/wiki/Ultimate_Doctor_Doom", ["doom-ultimate-vol1", "doom-ultimate-cataclysm"]),
        version_obj("doom-2099", "Doom 2099", "Earth-928 / 2099", "future", "Doom 2099 #1 (1993)", "Future monarch", "In the cyberpunk 2099 timeline, a new Victor von Doom rises to reclaim Latveria and challenge a corporate dystopia.", "https://en.wikipedia.org/wiki/Doom_2099", ["doom-2099-vol1"]),
        version_obj("doomwar-doom", "Doomwar Doctor Doom", "Earth-616", "main", "Doomwar #1 (2010)", "The Wakanda invasion", "Doctor Doom at his most ruthless — invading Wakanda to steal its vibranium in a war against T'Challa and the Black Panther.", "https://en.wikipedia.org/wiki/Doomwar", ["doom-doomwar", "doom-triumph-torment"]),
    ],
    "runs": {
        "doom-books-of-doom": {**run_obj("doom-books-of-doom", "victor-von-doom", "Books of Doom", "Ed Brubaker & Pablo Raimondi", "2006–07", "Books of Doom #1–6", "Modern Age", "None — ideal origin entry", "The definitive origin of Victor von Doom from gypsy child to iron-faced monarch.", "Books of Doom", "0785121229"), "isbn": "9780785121229"},
        "doom-unthinkable": {**run_obj("doom-unthinkable", "victor-von-doom", "Fantastic Four: Unthinkable", "Mark Waid & Mike Wieringo", "2003–04", "Fantastic Four #67–70", "Modern Age", "None", "Doctor Doom unleashes hell itself against the Fantastic Four in Waid's terrifying arc.", "Fantastic Four: Unthinkable", "0785115140"), "isbn": "9780785115140"},
        "doom-triumph-torment": {**run_obj("doom-triumph-torment", "victor-von-doom", "Doctor Strange and Doctor Doom: Triumph and Torment", "Roger Stern & Mike Mignola", "1989", "Doctor Strange and Doctor Doom: Triumph and Torment", "Modern Age", "None", "Doom bargains with Mephisto to save his mother's soul — Marvel's finest villain spotlight.", "Doctor Strange and Doctor Doom: Triumph and Torment", "0785107370"), "isbn": "9780785107370"},
        "doom-secret-wars-2015": {**run_obj("doom-secret-wars-2015", "god-emperor-doom", "Secret Wars (2015)", "Jonathan Hickman & Esad Ribic", "2015", "Secret Wars #1–9", "Modern Age", "Time Runs Out / New Avengers", "God Emperor Doom rules Battleworld as the multiverse collapses — Hickman's Marvel culmination.", "Secret Wars (2015)", "0785198841"), "isbn": "9780785198841"},
        "doom-time-runs-out": {**run_obj("doom-time-runs-out", "god-emperor-doom", "Time Runs Out", "Jonathan Hickman & various", "2014–15", "Avengers #35–44, New Avengers #24–33", "Modern Age", "New Avengers / Avengers", "The road to Secret Wars — incursions, the Illuminati, and Doom's ascension.", "Avengers: Time Runs Out", "0785192274"), "isbn": "9780785192274"},
        "doom-infamous-iron-man": {**run_obj("doom-infamous-iron-man", "infamous-iron-man", "Infamous Iron Man", "Brian Michael Bendis & Alex Maleev", "2016–17", "Infamous Iron Man #1–12", "Modern Age", "Civil War II", "Doctor Doom wears the Iron Man armor and tries to prove he can be a hero.", "Infamous Iron Man Vol. 1", "1302902995"), "isbn": "9781302902995"},
        "doom-ultimate-vol1": {**run_obj("doom-ultimate-vol1", "ultimate-doom", "Ultimate Fantastic Four Vol. 3", "Mark Millar & Bryan Hitch", "2004–05", "Ultimate Fantastic Four #7–12", "Ultimate", "Ultimate FF Vol. 1–2", "Ultimate Doom's origin and first strike against the Ultimate Fantastic Four.", "Ultimate Fantastic Four Vol. 3", "0785116806"), "isbn": "9780785116806"},
        "doom-ultimate-cataclysm": {**run_obj("doom-ultimate-cataclysm", "ultimate-doom", "Cataclysm: The Ultimates' Last Stand", "Joshua Hale Fialkov & various", "2013–14", "Cataclysm #0.1–4", "Ultimate", "Ultimate FF", "Ultimate Doom faces the end of the Ultimate Universe.", "Cataclysm: The Ultimates' Last Stand", "0785184677"), "isbn": "9780785184677"},
        "doom-2099-vol1": {**run_obj("doom-2099-vol1", "doom-2099", "Doom 2099 Vol. 1", "Willie F. Brooker & various", "1993–94", "Doom 2099 #1–6", "2099", "None", "Victor von Doom awakens in the future to reclaim his throne in the 2099 line.", "Doom 2099 Vol. 1", "0785100150"), "isbn": "9780785100157"},
        "doom-doomwar": {**run_obj("doom-doomwar", "doomwar-doom", "Doomwar", "Jonathan Hickman & various", "2010", "Doomwar #1–6", "Modern Age", "None", "Doctor Doom invades Wakanda — vibranium, espionage, and total war.", "Doomwar", "0785146920"), "isbn": "9780785146920"},
    },
    "home_runs": ["doom-books-of-doom", "doom-unthinkable", "doom-triumph-torment", "doom-secret-wars-2015", "doom-infamous-iron-man", "doom-doomwar", "doom-ultimate-vol1", "doom-time-runs-out", "doom-2099-vol1", "doom-ultimate-cataclysm"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Doctor_Doom",
        "lead": "Victor von Doom does not make mistakes — only victories delayed by fools and Richards.",
        "summary": "Doctor Doom is Victor von Doom, the iron-masked monarch of Latveria and arch-enemy of the Fantastic Four. Created by Stan Lee and Jack Kirby, he debuted in Fantastic Four #5 (1962). A master of science and sorcery, Doom has threatened Earth, stolen godhood during Secret Wars, and even briefly wore the Iron Man armor in a bid for redemption.",
        "facts": [
            {"label": "Alter ego", "value": "Victor von Doom"},
            {"label": "First appearance", "value": "Fantastic Four #5 (1962)"},
            {"label": "Created by", "value": "Stan Lee & Jack Kirby"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Nation", "value": "Latveria"},
            {"label": "Allies", "value": "Latverian army, Kristoff Vernard"},
            {"label": "Notable foes", "value": "Mr. Fantastic, Black Panther, Iron Man"},
            {"label": "Powers", "value": "Genius intellect, sorcery, powered armor"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            screen_item("doom-2005", "Fantastic Four", "Julian McMahon · Victor von Doom", "https://en.wikipedia.org/wiki/Fantastic_Four_(2005_film)", "https://www.imdb.com/title/tt0120667/", year="2005"),
            screen_item("doom-2015", "Fantastic Four", "Toby Kebbell · Victor von Doom", "https://en.wikipedia.org/wiki/Fantastic_Four_(2015_film)", "https://www.imdb.com/title/tt1502712/", year="2015"),
            screen_item("doom-2026", "Avengers: Doomsday", "Robert Downey Jr. · Victor von Doom", "https://en.wikipedia.org/wiki/Avengers:_Doomsday", "https://www.imdb.com/title/tt21357150/", year="2026"),
        ]},
        {"group": "Animated", "items": [
            screen_item("doom-1967", "The Marvel Super Heroes", "1966 Doctor Doom shorts", "https://en.wikipedia.org/wiki/The_Marvel_Super_Heroes", "https://www.imdb.com/title/tt0060004/", years="1966"),
            screen_item("doom-1994", "Fantastic Four (1994)", "Animated series", "https://en.wikipedia.org/wiki/Fantastic_Four_(1994_TV_series)", "https://www.imdb.com/title/tt0108850/", years="1994–1996"),
        ]},
    ],
    "themes": {
        "victor-von-doom": (0, 102, 51), "god-emperor-doom": (80, 40, 120), "infamous-iron-man": (180, 140, 40),
        "ultimate-doom": (60, 80, 60), "doom-2099": (20, 100, 80), "doomwar-doom": (0, 60, 30),
    },
    "issues": {},
}


THANOS = {
    "id": "thanos",
    "brand": "Thanos",
    "title": "Thanos — Death Across the Multiverse",
    "nav_who": "Who is Thanos",
    "nav_verses": "Verses",
    "who_id": "who-is-thanos",
    "header_img": "thanos-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #6a1b9a, #38006b 45%, #120020)",
    "verses_h2": "Thanos Across the Multiverse",
    "verses_p": "versions across Marvel's cosmic hunger — Classic Starlin Thanos, Infinity Gauntlet, Hickman's Infinity, Annihilation, and MCU framing.",
    "comics_p": "Essential Thanos stories — from Jim Starlin's cosmic tragedies and Thanos Quest to Infinity Gauntlet and Jonathan Hickman's Infinity.",
    "screen_p": "Live-action and animated appearances — from the MCU Infinity Saga and Avengers films to the 1990s Silver Surfer animated series.",
    "types": MARVEL_TYPES,
    "versions": [
        version_obj("classic-thanos", "Classic Thanos", "Earth-616 / Prime Marvel", "main", "Iron Man #55 (1973)", "The Mad Titan", "Jim Starlin's Thanos is a nihilist in love with Death — the cosmic tyrant whose schemes reshaped the Marvel Universe.", "https://en.wikipedia.org/wiki/Thanos", ["thanos-starlin-omnibus", "thanos-death", "thanos-cosmic"]),
        version_obj("infinity-gauntlet-thanos", "Infinity Gauntlet Thanos", "Earth-616", "main", "The Thanos Quest #1 (1990)", "With the Gauntlet, godhood", "After assembling the Infinity Gems, Thanos erased half the universe with a snap — Marvel's defining cosmic event.", "https://en.wikipedia.org/wiki/The_Infinity_Gauntlet", ["thanos-quest", "infinity-gauntlet", "infinity-gauntlet-aftermath"]),
        version_obj("hickman-infinity-thanos", "Infinity Thanos", "Earth-616", "main", "Infinity #1 (2013)", "The Builder War", "Jonathan Hickman's Thanos leads an invasion of Earth while the Avengers face the Builders — a darker, grander cosmic war.", "https://en.wikipedia.org/wiki/Infinity_(comic_book)", ["thanos-infinity-hickman", "thanos-new-avengers", "thanos-annihilation"]),
        version_obj("thanos-rising-era", "Thanos Rising", "Earth-616", "main", "Thanos Rising #1 (2013)", "Born to destroy", "Jason Aaron and Simone Bianchi explore Thanos' childhood on Titan — the making of the Mad Titan.", "https://en.wikipedia.org/wiki/Thanos_Rising", ["thanos-rising", "thanos-starlin-omnibus"]),
        version_obj("annihilation-thanos", "Annihilation Thanos", "Earth-616", "main", "Annihilation #1 (2006)", "Cosmic survivor", "Thanos manipulates Annihilus' wave of destruction from the shadows in Marvel's modern cosmic revival.", "https://en.wikipedia.org/wiki/Annihilation_(comic_book)", ["thanos-annihilation", "thanos-silver-surfer"]),
        version_obj("king-thanos", "King Thanos", "Earth-TRN666", "future", "Thanos #13 (2018)", "The last Titan standing", "An older Thanos from a future where he killed every hero and now seeks the one worthy opponent left — himself.", "https://en.wikipedia.org/wiki/Thanos", ["thanos-king-thanos", "thanos-death"]),
    ],
    "runs": {
        "thanos-starlin-omnibus": {**run_obj("thanos-starlin-omnibus", "classic-thanos", "Thanos by Jim Starlin: The Complete Collection", "Jim Starlin & various", "1973–76", "Iron Man #55, Captain Marvel #25–33, Warlock #9–11", "Bronze Age", "None — classic entry", "The foundational Starlin Thanos stories — Death, the Infinity Gems, and Adam Warlock.", "Thanos by Jim Starlin: The Complete Collection", "0785190026"), "isbn": "9780785190026"},
        "thanos-death": {**run_obj("thanos-death", "classic-thanos", "The Death of Captain Marvel", "Jim Starlin & Steve Oliffe", "1982", "The Death of Captain Marvel", "Bronze Age", "Starlin Thanos stories", "Thanos' relationship with Death crystallized in Marvel's first graphic novel.", "The Death of Captain Marvel", "0785136840"), "isbn": "9780785136840"},
        "thanos-cosmic": {**run_obj("thanos-cosmic", "classic-thanos", "Warlock: The Complete Saga", "Jim Starlin & various", "1974–76", "Strange Tales #178–181, Warlock #1–12", "Bronze Age", "None", "Adam Warlock, the Magus, and Thanos in Starlin's cosmic masterpiece.", "Warlock: The Complete Saga", "0785190034"), "isbn": "9780785190034"},
        "thanos-quest": {**run_obj("thanos-quest", "infinity-gauntlet-thanos", "Thanos Quest", "Jim Starlin & Ron Lim", "1990", "Thanos Quest #1–2", "Modern Age", "Silver Surfer / Thanos collections", "Thanos outwits the Elders of the Universe to claim every Infinity Gem.", "Thanos Quest", "0785108974"), "isbn": "9780785108974"},
        "infinity-gauntlet": {**run_obj("infinity-gauntlet", "infinity-gauntlet-thanos", "The Infinity Gauntlet", "Jim Starlin & George Pérez", "1991", "The Infinity Gauntlet #1–6", "Modern Age", "Thanos Quest", "Thanos wields ultimate power and the heroes of Earth fight back against godhood.", "The Infinity Gauntlet", "0785156595"), "isbn": "9780785156595"},
        "infinity-gauntlet-aftermath": {**run_obj("infinity-gauntlet-aftermath", "infinity-gauntlet-thanos", "Infinity War", "Jim Starlin & Ron Lim", "1992", "Infinity War #1–6", "Modern Age", "Infinity Gauntlet", "The aftermath of the Gauntlet — Magus, Warlock, and cosmic fallout.", "Infinity War", "0785156609"), "isbn": "9780785156609"},
        "thanos-infinity-hickman": {**run_obj("thanos-infinity-hickman", "hickman-infinity-thanos", "Infinity", "Jonathan Hickman & Jim Cheung", "2013", "Infinity #1–6", "Modern Age", "New Avengers / Avengers", "Thanos invades Earth during the Builder War — Hickman's cosmic event.", "Infinity", "0785184227"), "isbn": "9780785184227"},
        "thanos-new-avengers": {**run_obj("thanos-new-avengers", "hickman-infinity-thanos", "New Avengers Vol. 2", "Jonathan Hickman & Steve Epting", "2013", "New Avengers #1–6", "Modern Age", "None", "The Illuminati and incursions set the stage for Thanos' return.", "New Avengers Vol. 2", "0785164520"), "isbn": "9780785164520"},
        "thanos-annihilation": {**run_obj("thanos-annihilation", "annihilation-thanos", "Annihilation", "Keith Giffen & various", "2006", "Annihilation #1–6", "Modern Age", "None", "Marvel's cosmic revival — Thanos manipulates the Annihilation Wave.", "Annihilation Book 1", "0785118345"), "isbn": "9780785118345"},
        "thanos-silver-surfer": {**run_obj("thanos-silver-surfer", "annihilation-thanos", "Silver Surfer: Requiem", "J. Michael Straczynski & Esad Ribic", "2007–08", "Silver Surfer Vol. 5 #1–5", "Modern Age", "Annihilation", "The Silver Surfer faces mortality as Thanos' shadow looms.", "Silver Surfer: Requiem", "0785127470"), "isbn": "9780785127470"},
        "thanos-rising": {**run_obj("thanos-rising", "thanos-rising-era", "Thanos Rising", "Jason Aaron & Simone Bianchi", "2013", "Thanos Rising #1–5", "Modern Age", "None", "The origin of the Mad Titan on Titan — tragedy, cruelty, and Death.", "Thanos Rising", "0785184870"), "isbn": "9780785184870"},
        "thanos-king-thanos": {**run_obj("thanos-king-thanos", "king-thanos", "Thanos: King Thanos", "Donny Cates & Geoff Shaw", "2018", "Thanos #13–18", "Modern Age", "None", "King Thanos from the future recruits younger Thanos to finish the universe.", "Thanos: King Thanos", "1302910110"), "isbn": "9781302910110"},
    },
    "home_runs": ["infinity-gauntlet", "thanos-quest", "thanos-starlin-omnibus", "thanos-infinity-hickman", "thanos-rising", "thanos-annihilation", "thanos-king-thanos", "thanos-death", "infinity-gauntlet-aftermath", "thanos-new-avengers"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Thanos",
        "lead": "Perfectly balanced, as all things should be — the Mad Titan who loved Death and reshaped the cosmos.",
        "summary": "Thanos is the Mad Titan of Titan, a cosmic warlord obsessed with proving his devotion to the entity Death. Created by Jim Starlin, he debuted in Iron Man #55 (1973). From Starlin's cosmic epics through Infinity Gauntlet to Jonathan Hickman's Infinity and the MCU, Thanos remains Marvel's greatest cosmic antagonist.",
        "facts": [
            {"label": "Homeworld", "value": "Titan (moon of Saturn)"},
            {"label": "First appearance", "value": "Iron Man #55 (1973)"},
            {"label": "Created by", "value": "Jim Starlin & Mike Friedrich"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Signature weapon", "value": "Infinity Gauntlet"},
            {"label": "Allies", "value": "Black Order, Chitauri (MCU)"},
            {"label": "Notable foes", "value": "Avengers, Adam Warlock, Silver Surfer"},
            {"label": "Powers", "value": "Superhuman strength, genius, cosmic energy"},
        ],
    },
    "screen": [
        {"group": "MCU films", "items": [
            screen_item("thanos-avengers", "The Avengers", "Mystery villain · Mid-credits", "https://en.wikipedia.org/wiki/The_Avengers_(2012_film)", "https://www.imdb.com/title/tt0848228/", year="2012"),
            screen_item("thanos-guardians", "Guardians of the Galaxy", "Josh Brolin · First full appearance", "https://en.wikipedia.org/wiki/Guardians_of_the_Galaxy_(film)", "https://www.imdb.com/title/tt2015381/", year="2014"),
            screen_item("thanos-infinity-war", "Avengers: Infinity War", "Josh Brolin · The Snap", "https://en.wikipedia.org/wiki/Avengers:_Infinity_War", "https://www.imdb.com/title/tt4154756/", year="2018"),
            screen_item("thanos-endgame", "Avengers: Endgame", "Josh Brolin · Final battle", "https://en.wikipedia.org/wiki/Avengers:_Endgame", "https://www.imdb.com/title/tt4154796/", year="2019"),
        ]},
        {"group": "Animated", "items": [
            screen_item("thanos-surfer-90s", "Silver Surfer (1998)", "Animated Mad Titan", "https://en.wikipedia.org/wiki/Silver_Surfer_(TV_series)", "https://www.imdb.com/title/tt0120370/", years="1998–2000"),
            screen_item("thanos-super-hero-squad", "The Super Hero Squad Show", "Comedic Thanos", "https://en.wikipedia.org/wiki/The_Super_Hero_Squad_Show", "https://www.imdb.com/title/tt1388589/", years="2009–2011"),
        ]},
    ],
    "themes": {
        "classic-thanos": (106, 27, 154), "infinity-gauntlet-thanos": (156, 39, 176), "hickman-infinity-thanos": (80, 20, 100),
        "thanos-rising-era": (60, 40, 80), "annihilation-thanos": (100, 50, 140), "king-thanos": (40, 20, 60),
    },
    "issues": {},
}


SILVER_SURFER = {
    "id": "silver-surfer",
    "brand": "Silver Surfer",
    "title": "Silver Surfer — Herald Across the Multiverse",
    "nav_who": "Who is the Silver Surfer",
    "nav_verses": "Verses",
    "who_id": "who-is-silver-surfer",
    "header_img": "silver-surfer-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #b0bec5, #546e7a 45%, #1a2328)",
    "verses_h2": "Silver Surfer Across the Multiverse",
    "verses_p": "versions across Marvel's cosmic herald — Norrin Radd, Annihilation era, Silver Surfer Black, Parable, and Ultimate Surfer.",
    "comics_p": "Essential Silver Surfer stories — from Lee/Buscema's cosmic origin and Parable to Requiem, Annihilation, and Silver Surfer Black.",
    "screen_p": "Live-action and animated appearances — from Fantastic Four: Rise of the Silver Surfer to the 1990s animated series and MCU cameos.",
    "types": MARVEL_TYPES,
    "versions": [
        version_obj("norrin-radd", "Norrin Radd", "Earth-616 / Prime Marvel", "main", "Fantastic Four #48 (1966)", "The herald of Galactus", "Norrin Radd of Zenn-La sacrificed himself to become the Silver Surfer — a cosmic wanderer seeking humanity among the stars.", "https://en.wikipedia.org/wiki/Silver_Surfer", ["surfer-origins", "surfer-parable", "surfer-requiem"]),
        version_obj("annihilation-surfer", "Annihilation Silver Surfer", "Earth-616", "main", "Annihilation: Silver Surfer #1 (2006)", "Reborn in the void", "The Silver Surfer is stripped of the Power Cosmic and must survive Annihilus' cosmic war.", "https://en.wikipedia.org/wiki/Annihilation_(comic_book)", ["surfer-annihilation", "surfer-annihilation-conquest"]),
        version_obj("silver-surfer-black", "Silver Surfer Black", "Earth-616", "main", "Silver Surfer: Black #1 (2019)", "Into the black", "Donny Cates and Tradd Moore send the Surfer through a black hole — a psychedelic horror odyssey at the edge of creation.", "https://en.wikipedia.org/wiki/Silver_Surfer", ["surfer-black", "surfer-black-complete"]),
        version_obj("surfer-parable", "Silver Surfer: Parable", "Earth-616", "main", "Silver Surfer Vol. 3 #1 (1987)", "Stan Lee's gospel", "Stan Lee and Jean Giraud (Moebius) reimagine Galactus and the Surfer as a philosophical fable.", "https://en.wikipedia.org/wiki/Silver_Surfer", ["surfer-parable", "surfer-origins"]),
        version_obj("ultimate-surfer", "Ultimate Silver Surfer", "Earth-1610", "ultimate", "Ultimate Fantastic Four #43 (2007)", "Ultimate herald", "The Ultimate Universe's Silver Surfer is a cosmic probe with a very different relationship to Galactus.", "https://en.wikipedia.org/wiki/Ultimate_Silver_Surfer", ["surfer-ultimate-vol1"]),
        version_obj("surfer-2099", "Silver Surfer 2099", "Earth-928 / 2099", "future", "2099: World of Tomorrow #3 (1999)", "Future herald", "In the 2099 timeline, a new herald carries the Power Cosmic through a corporate dystopia.", "https://en.wikipedia.org/wiki/Silver_Surfer", ["surfer-2099-vol1"]),
    ],
    "runs": {
        "surfer-origins": {**run_obj("surfer-origins", "norrin-radd", "Silver Surfer Epic Collection: When Calls Galactus", "Stan Lee & John Buscema", "1966–68", "Fantastic Four #48–50, Silver Surfer #1–3", "Silver Age", "None — classic entry", "The coming of Galactus and the Silver Surfer's debut — Marvel's first cosmic epic.", "Silver Surfer Epic Collection: When Calls Galactus", "1302901901"), "isbn": "9781302901901"},
        "surfer-parable": {**run_obj("surfer-parable", "norrin-radd", "Silver Surfer: Parable", "Stan Lee & Jean Giraud", "1988–89", "Silver Surfer Vol. 3 #1–2", "Modern Age", "None", "Stan Lee and Moebius craft a philosophical masterpiece about faith and freedom.", "Silver Surfer: Parable", "0871354918"), "isbn": "9780871354915"},
        "surfer-requiem": {**run_obj("surfer-requiem", "norrin-radd", "Silver Surfer: Requiem", "J. Michael Straczynski & Esad Ribic", "2007–08", "Silver Surfer Vol. 5 #1–5", "Modern Age", "None", "The Silver Surfer faces mortality in a haunting, elegiac miniseries.", "Silver Surfer: Requiem", "0785127470"), "isbn": "9780785127470"},
        "surfer-annihilation": {**run_obj("surfer-annihilation", "annihilation-surfer", "Annihilation: Silver Surfer", "Christos Gage & Gabriele Dell'Otto", "2006", "Annihilation: Silver Surfer #1–4", "Modern Age", "None", "The Surfer is stripped of the Power Cosmic and reborn during Annihilation.", "Annihilation: Silver Surfer", "0785118345"), "isbn": "9780785118345"},
        "surfer-annihilation-conquest": {**run_obj("surfer-annihilation-conquest", "annihilation-surfer", "Annihilation: Conquest", "Dan Abnett & Andy Lanning", "2007", "Annihilation: Conquest #1–6", "Modern Age", "Annihilation", "The Surfer joins the fight against the Phalanx in Annihilation's sequel.", "Annihilation: Conquest", "0785129031"), "isbn": "9780785129031"},
        "surfer-black": {**run_obj("surfer-black", "silver-surfer-black", "Silver Surfer: Black", "Donny Cates & Tradd Moore", "2019", "Silver Surfer: Black #1–5", "Modern Age", "None", "The Surfer falls through a black hole into a psychedelic cosmic horror.", "Silver Surfer: Black", "1302916470"), "isbn": "9781302916470"},
        "surfer-black-complete": {**run_obj("surfer-black-complete", "silver-surfer-black", "Silver Surfer: Black Complete", "Donny Cates & Tradd Moore", "2019–20", "Silver Surfer: Black #1–5 + Annual", "Modern Age", "Silver Surfer: Black", "The complete Silver Surfer Black saga with annual.", "Silver Surfer: Black Complete", "1302921376"), "isbn": "9781302921371"},
        "surfer-ultimate-vol1": {**run_obj("surfer-ultimate-vol1", "ultimate-surfer", "Ultimate Fantastic Four: The Silver Surfer", "Mark Millar & Bryan Hitch", "2007", "Ultimate Fantastic Four #43–46", "Ultimate", "Ultimate FF Vol. 1", "The Ultimate Silver Surfer arrives as a cosmic probe in the Ultimate Universe.", "Ultimate Fantastic Four Vol. 7", "0785126578"), "isbn": "9780785126578"},
        "surfer-2099-vol1": {**run_obj("surfer-2099-vol1", "surfer-2099", "2099: World of Tomorrow", "Various", "1999", "2099: World of Tomorrow #1–3", "2099", "None", "The 2099 line's vision of a future Silver Surfer.", "2099: World of Tomorrow", "0785107120"), "isbn": "9780785107120"},
    },
    "home_runs": ["surfer-origins", "surfer-parable", "surfer-requiem", "surfer-annihilation", "surfer-black", "surfer-ultimate-vol1", "surfer-annihilation-conquest", "surfer-black-complete", "surfer-2099-vol1"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Silver_Surfer",
        "lead": "He who travels fastest travels alone — the herald who defied Galactus and searched the stars for meaning.",
        "summary": "The Silver Surfer is Norrin Radd, a Zenn-Lavian who became the herald of Galactus to save his homeworld. Created by Stan Lee and Jack Kirby, he debuted in Fantastic Four #48 (1966). From cosmic parables and Requiem to Annihilation and Silver Surfer Black, the Surfer embodies Marvel's most philosophical space opera.",
        "facts": [
            {"label": "Alter ego", "value": "Norrin Radd"},
            {"label": "First appearance", "value": "Fantastic Four #48 (1966)"},
            {"label": "Created by", "value": "Stan Lee & Jack Kirby"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Homeworld", "value": "Zenn-La"},
            {"label": "Allies", "value": "Fantastic Four, Adam Warlock, Dawn Greenwood"},
            {"label": "Notable foes", "value": "Galactus, Thanos, Mephisto"},
            {"label": "Powers", "value": "Power Cosmic, faster-than-light travel"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            screen_item("surfer-2007", "Fantastic Four: Rise of the Silver Surfer", "Doug Jones / Laurence Fishburne · Voice", "https://en.wikipedia.org/wiki/Fantastic_Four:_Rise_of_the_Silver_Surfer", "https://www.imdb.com/title/tt0486576/", year="2007"),
        ]},
        {"group": "Animated", "items": [
            screen_item("surfer-1998", "Silver Surfer", "1998 animated series", "https://en.wikipedia.org/wiki/Silver_Surfer_(TV_series)", "https://www.imdb.com/title/tt0120370/", years="1998–2000"),
            screen_item("surfer-1967", "The Marvel Super Heroes", "1966 Silver Surfer segments", "https://en.wikipedia.org/wiki/The_Marvel_Super_Heroes", "https://www.imdb.com/title/tt0060004/", years="1966"),
        ]},
    ],
    "themes": {
        "norrin-radd": (176, 190, 197), "annihilation-surfer": (84, 110, 122), "silver-surfer-black": (20, 20, 30),
        "surfer-parable": (200, 180, 120), "ultimate-surfer": (160, 160, 180), "surfer-2099": (100, 120, 140),
    },
    "issues": {},
}


FANTASTIC_FOUR = {
    "id": "fantastic-four",
    "brand": "Fantastic Four",
    "title": "Fantastic Four — First Family Across the Multiverse",
    "nav_who": "Who are the Fantastic Four",
    "nav_verses": "Verses",
    "who_id": "who-is-fantastic-four",
    "header_img": "fantastic-four-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #1565c0, #0d47a1 45%, #021020)",
    "verses_h2": "Fantastic Four Across the Multiverse",
    "verses_p": "versions across Marvel's first family — Reed, Sue, Johnny, Ben, Ultimate FF, Future Foundation, and FF 2099.",
    "comics_p": "Essential Fantastic Four stories — from Lee/Kirby's origin through Byrne, Waid/Wieringo, Hickman, and the Future Foundation era.",
    "screen_p": "Live-action and animated appearances — from Fantastic Four films and The Marvels to decades of animated series.",
    "types": MARVEL_TYPES,
    "versions": [
        version_obj("mr-fantastic", "Mr. Fantastic", "Earth-616 / Prime Marvel", "main", "Fantastic Four #1 (1961)", "Stretching genius", "Reed Richards is the elastic genius who leads the Fantastic Four — scientist, explorer, and father of the Marvel Universe's first family.", "https://en.wikipedia.org/wiki/Mister_Fantastic", ["ff-lee-kirby-vol1", "ff-hickman-vol1", "ff-byrne"]),
        version_obj("invisible-woman", "Invisible Woman", "Earth-616 / Prime Marvel", "main", "Fantastic Four #1 (1961)", "The heart of the team", "Sue Storm is the Invisible Woman — force-field master, diplomat, and the emotional center of Marvel's first family.", "https://en.wikipedia.org/wiki/Invisible_Woman", ["ff-lee-kirby-vol1", "ff-waid-wieringo", "ff-invisible-woman"]),
        version_obj("human-torch", "Human Torch", "Earth-616 / Prime Marvel", "main", "Fantastic Four #1 (1961)", "Flame on!", "Johnny Storm is the Human Torch — hotheaded, heroic, and the youngest member of the Fantastic Four.", "https://en.wikipedia.org/wiki/Human_Torch", ["ff-lee-kirby-vol1", "ff-strange-tales", "ff-waid-wieringo"]),
        version_obj("the-thing", "The Thing", "Earth-616 / Prime Marvel", "main", "Fantastic Four #1 (1961)", "It's clobberin' time!", "Ben Grimm is the Thing — a pilot transformed into a rock-skinned monster who became Marvel's most lovable blue-eyed brawler.", "https://en.wikipedia.org/wiki/Thing_(comics)", ["ff-lee-kirby-vol1", "ff-thing-solo", "ff-byrne"]),
        version_obj("ultimate-ff", "Ultimate Fantastic Four", "Earth-1610", "ultimate", "Ultimate Fantastic Four #1 (2004)", "Younger, darker origins", "Mark Millar and Bryan Hitch reimagined the first family for the Ultimate Universe — younger, sharper, and more volatile.", "https://en.wikipedia.org/wiki/Ultimate_Fantastic_Four", ["ff-ultimate-vol1", "ff-ultimate-vol2"]),
        version_obj("future-foundation", "Future Foundation", "Earth-616", "main", "FF #1 (2011)", "Beyond the four", "After the death of Johnny Storm, Reed Richards formed the Future Foundation — a team of geniuses rebuilding the future.", "https://en.wikipedia.org/wiki/Future_Foundation", ["ff-future-foundation", "ff-hickman-vol1"]),
        version_obj("ff-2099", "Fantastic Four 2099", "Earth-928 / 2099", "future", "2099: World of Tomorrow #1 (1999)", "Tomorrow's first family", "In the 2099 timeline, new versions of the Fantastic Four protect a corporate dystopian future.", "https://en.wikipedia.org/wiki/Fantastic_Four_2099", ["ff-2099-vol1"]),
    ],
    "runs": {
        "ff-lee-kirby-vol1": {**run_obj("ff-lee-kirby-vol1", "mr-fantastic", "Fantastic Four Epic Collection: The World's Greatest Comic Magazine", "Stan Lee & Jack Kirby", "1961–63", "Fantastic Four #1–20", "Silver Age", "None — ideal entry", "Lee and Kirby invent the Marvel Universe — the origin of the Fantastic Four.", "Fantastic Four Epic Collection Vol. 1", "1302901901"), "isbn": "9781302901901"},
        "ff-hickman-vol1": {**run_obj("ff-hickman-vol1", "mr-fantastic", "Fantastic Four by Jonathan Hickman Vol. 1", "Jonathan Hickman & Dale Eaglesham", "2009–10", "Fantastic Four #570–574", "Modern Age", "None", "Hickman's grand reimagining — the Future Foundation, Reed's inventions, and cosmic scope.", "Fantastic Four by Jonathan Hickman Vol. 1", "0785146720"), "isbn": "9780785146720"},
        "ff-waid-wieringo": {**run_obj("ff-waid-wieringo", "invisible-woman", "Fantastic Four by Waid & Wieringo Vol. 1", "Mark Waid & Mike Wieringo", "2003–04", "Fantastic Four #60–66", "Modern Age", "None", "Waid and Wieringo's joyful run restores the wonder and family spirit of the FF.", "Fantastic Four by Waid & Wieringo Vol. 1", "0785115140"), "isbn": "9780785115140"},
        "ff-byrne": {**run_obj("ff-byrne", "mr-fantastic", "Fantastic Four by John Byrne Omnibus Vol. 1", "John Byrne & various", "1981–83", "Fantastic Four #232–260", "Modern Age", "Lee/Kirby recommended", "John Byrne's definitive run — Franklin Richards, the Beyonder, and classic FF storytelling.", "Fantastic Four by John Byrne Omnibus Vol. 1", "1302912554"), "isbn": "9781302912554"},
        "ff-invisible-woman": {**run_obj("ff-invisible-woman", "invisible-woman", "Invisible Woman", "Mark Russell & Ramon Perez", "2019", "Invisible Woman #1–5", "Modern Age", "None", "Sue Storm's solo espionage miniseries — the Invisible Woman as secret agent.", "Invisible Woman", "1302916470"), "isbn": "9781302916470"},
        "ff-strange-tales": {**run_obj("ff-strange-tales", "human-torch", "Strange Tales: Human Torch", "Stan Lee & Jack Kirby", "1962–65", "Strange Tales #101–134", "Silver Age", "FF Vol. 1", "Johnny Storm's early solo adventures in Strange Tales.", "Strange Tales: Human Torch", "0785108907"), "isbn": "9780785108907"},
        "ff-thing-solo": {**run_obj("ff-thing-solo", "the-thing", "The Thing", "John Byrne & Ron Wilson", "1983", "The Thing #1–4", "Modern Age", "None", "Ben Grimm's solo miniseries — the Thing on his own in New York.", "The Thing", "0785107370"), "isbn": "9780785107370"},
        "ff-ultimate-vol1": {**run_obj("ff-ultimate-vol1", "ultimate-ff", "Ultimate Fantastic Four Vol. 1", "Mark Millar & Bryan Hitch", "2004", "Ultimate Fantastic Four #1–6", "Ultimate", "None", "The Ultimate Universe's Fantastic Four — younger, sharper, and reimagined.", "Ultimate Fantastic Four Vol. 1", "0785116806"), "isbn": "9780785116806"},
        "ff-ultimate-vol2": {**run_obj("ff-ultimate-vol2", "ultimate-ff", "Ultimate Fantastic Four Vol. 2", "Mark Millar & Bryan Hitch", "2004–05", "Ultimate Fantastic Four #7–12", "Ultimate", "Ultimate FF Vol. 1", "Ultimate Doom, the N-Zone, and the darkening of the Ultimate FF.", "Ultimate Fantastic Four Vol. 2", "0785116865"), "isbn": "9780785116865"},
        "ff-future-foundation": {**run_obj("ff-future-foundation", "future-foundation", "FF Vol. 1", "Jonathan Hickman & Steve Epting", "2011", "FF #1–6", "Modern Age", "Fantastic Four Hickman", "The Future Foundation era — Reed's school of genius and Johnny's return.", "FF Vol. 1", "0785157370"), "isbn": "9780785157370"},
        "ff-civil-war": {**run_obj("ff-civil-war", "mr-fantastic", "Civil War: Fantastic Four", "Mark Millar & Steve McNiven", "2006–07", "Civil War #1–7, Fantastic Four #536–543", "Modern Age", "None", "Reed Richards sides with Iron Man as the Fantastic Four fracture during Civil War.", "Civil War", "0785121789"), "isbn": "9780785121787"},
        "ff-2099-vol1": {**run_obj("ff-2099-vol1", "ff-2099", "2099: World of Tomorrow", "Various", "1999", "2099: World of Tomorrow #1–3", "2099", "None", "The 2099 line's vision of a future Fantastic Four.", "2099: World of Tomorrow", "0785107120"), "isbn": "9780785107120"},
    },
    "home_runs": ["ff-lee-kirby-vol1", "ff-hickman-vol1", "ff-waid-wieringo", "ff-byrne", "ff-ultimate-vol1", "ff-future-foundation", "ff-invisible-woman", "ff-thing-solo", "ff-civil-war", "ff-ultimate-vol2"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Fantastic_Four",
        "lead": "It's clobberin' time — Marvel's first family of explorers, inventors, and heroes.",
        "summary": "The Fantastic Four are Reed Richards, Sue Storm, Johnny Storm, and Ben Grimm — astronauts transformed by cosmic rays into Marvel's first superhero team. Created by Stan Lee and Jack Kirby, they debuted in Fantastic Four #1 (1961). Their family dynamic, cosmic exploration, and rogues gallery — especially Doctor Doom — defined the Marvel Universe.",
        "facts": [
            {"label": "Members", "value": "Mr. Fantastic, Invisible Woman, Human Torch, The Thing"},
            {"label": "First appearance", "value": "Fantastic Four #1 (1961)"},
            {"label": "Created by", "value": "Stan Lee & Jack Kirby"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Headquarters", "value": "Baxter Building, Four Freedoms Plaza"},
            {"label": "Allies", "value": "Future Foundation, Black Panther, Silver Surfer"},
            {"label": "Notable foes", "value": "Doctor Doom, Galactus, Mole Man"},
            {"label": "Powers", "value": "Elasticity, invisibility, fire, super-strength"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            screen_item("ff-2005", "Fantastic Four", "Ioan Gruffudd · Tim Story", "https://en.wikipedia.org/wiki/Fantastic_Four_(2005_film)", "https://www.imdb.com/title/tt0120667/", year="2005"),
            screen_item("ff-2015", "Fantastic Four", "Miles Teller · Josh Trank", "https://en.wikipedia.org/wiki/Fantastic_Four_(2015_film)", "https://www.imdb.com/title/tt1502712/", year="2015"),
            screen_item("ff-marvels", "The Marvels", "Post-credits FF tease", "https://en.wikipedia.org/wiki/The_Marvels", "https://www.imdb.com/title/tt6320628/", year="2023"),
        ]},
        {"group": "Animated", "items": [
            screen_item("ff-1967", "Fantastic Four (1967)", "Hanna-Barbera animated", "https://en.wikipedia.org/wiki/Fantastic_Four_(1967_TV_series)", "https://www.imdb.com/title/tt0061260/", years="1967–1970"),
            screen_item("ff-1994", "Fantastic Four (1994)", "Fox Kids animated", "https://en.wikipedia.org/wiki/Fantastic_Four_(1994_TV_series)", "https://www.imdb.com/title/tt0108850/", years="1994–1996"),
        ]},
    ],
    "themes": {
        "mr-fantastic": (21, 101, 192), "invisible-woman": (100, 180, 220), "human-torch": (255, 100, 30),
        "the-thing": (120, 80, 50), "ultimate-ff": (40, 80, 160), "future-foundation": (200, 200, 60),
        "ff-2099": (60, 100, 140),
    },
    "issues": {},
}


PUNISHER = {
    "id": "punisher",
    "brand": "The Punisher",
    "title": "The Punisher — War Across the Multiverse",
    "nav_who": "Who is the Punisher",
    "nav_verses": "Verses",
    "who_id": "who-is-punisher",
    "header_img": "punisher-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #37474f, #1a2327 45%, #050808)",
    "verses_h2": "The Punisher Across the Multiverse",
    "verses_p": "versions across Marvel's one-man war — Frank Castle, MAX Punisher, Ultimate Punisher, War Journal, and alternate skulls.",
    "comics_p": "Essential Punisher stories — from Year One and Welcome Back, Frank to Garth Ennis' MAX run and War Journal.",
    "screen_p": "Live-action and animated appearances — from the 1989, 2004, and 2008 Punisher films to the Netflix Daredevil and Punisher series.",
    "types": MARVEL_TYPES,
    "versions": [
        version_obj("frank-castle", "Frank Castle", "Earth-616 / Prime Marvel", "main", "The Amazing Spider-Man #129 (1974)", "One man war on crime", "Frank Castle is the Punisher — a Marine veteran who wages eternal war on criminals after his family was murdered.", "https://en.wikipedia.org/wiki/Punisher", ["punisher-year-one", "punisher-welcome-back-frank", "punisher-circle-of-blood"]),
        version_obj("max-punisher", "MAX Punisher", "Earth-200111 / MAX", "alternate", "Punisher Vol. 6 #1 (2004)", "No heroes, no mercy", "Garth Ennis' MAX Punisher exists in a brutal, realistic world — no superheroes, just Frank Castle's one-man war.", "https://en.wikipedia.org/wiki/Punisher", ["punisher-max-vol1", "punisher-max-vol2", "punisher-max-kitchen"]),
        version_obj("ultimate-punisher", "Ultimate Punisher", "Earth-1610", "ultimate", "Ultimate Marvel Team-Up #1 (2001)", "Ultimate vigilante", "The Ultimate Universe's Frank Castle — a former soldier turned anti-hero in a grittier Marvel world.", "https://en.wikipedia.org/wiki/Ultimate_Punisher", ["punisher-ultimate-vol1", "punisher-ultimate-avengers"]),
        version_obj("war-journal-punisher", "Punisher War Journal", "Earth-616", "main", "Punisher War Journal Vol. 2 #1 (2006)", "Journal of vengeance", "Matt Fraction and Ariel Olivetti's Punisher War Journal — Frank Castle's war journal during Civil War and beyond.", "https://en.wikipedia.org/wiki/Punisher", ["punisher-war-journal-vol1", "punisher-war-journal-vol2"]),
        version_obj("punisher-2099", "Punisher 2099", "Earth-928 / 2099", "future", "Punisher 2099 #1 (1995)", "Future skull", "In the 2099 timeline, Jake Gallows carries the Punisher mantle in a cyberpunk dystopia.", "https://en.wikipedia.org/wiki/Punisher_2099", ["punisher-2099-vol1"]),
        version_obj("cosmic-ghost-rider-punisher", "Cosmic Ghost Rider Frank Castle", "Earth-TRN666", "multiverse", "Thanos #13 (2018)", "The last Punisher", "Frank Castle bonded with a Spirit of Vengeance and the Power Cosmic — the Cosmic Ghost Rider from King Thanos' future.", "https://en.wikipedia.org/wiki/Cosmic_Ghost_Rider", ["punisher-cosmic-gr", "punisher-max-vol1"]),
    ],
    "runs": {
        "punisher-year-one": {**run_obj("punisher-year-one", "frank-castle", "Punisher: Year One", "Dan Abnett & Andy Lanning", "1994–95", "Punisher: Year One #1–4", "Modern Age", "None — origin entry", "Frank Castle's first year as the Punisher — the making of the skull.", "Punisher: Year One", "0785108907"), "isbn": "9780785108907"},
        "punisher-welcome-back-frank": {**run_obj("punisher-welcome-back-frank", "frank-castle", "Welcome Back, Frank", "Garth Ennis & Steve Dillon", "2000–01", "Punisher Vol. 5 #1–6", "Modern Age", "None", "Garth Ennis and Steve Dillon relaunch the Punisher — darkly comic, brutally violent.", "Punisher: Welcome Back, Frank", "0785108907"), "isbn": "9780785108907"},
        "punisher-circle-of-blood": {**run_obj("punisher-circle-of-blood", "frank-castle", "Punisher: Circle of Blood", "Chuck Dixon & various", "1992", "Punisher Vol. 2 #1–6", "Modern Age", "None", "Chuck Dixon's Punisher run establishes Frank Castle's war on organized crime.", "Punisher: Circle of Blood", "0785100150"), "isbn": "9780785100157"},
        "punisher-max-vol1": {**run_obj("punisher-max-vol1", "max-punisher", "Punisher MAX Vol. 1", "Garth Ennis & Darick Robertson", "2004", "Punisher Vol. 6 #1–6", "MAX", "None", "Garth Ennis' MAX Punisher — realistic, brutal, and without superheroes.", "Punisher MAX Vol. 1", "0785116806"), "isbn": "9780785116806"},
        "punisher-max-vol2": {**run_obj("punisher-max-vol2", "max-punisher", "Punisher MAX Vol. 2", "Garth Ennis & Darick Robertson", "2004–05", "Punisher Vol. 6 #7–12", "MAX", "Punisher MAX Vol. 1", "The MAX Punisher continues his war — Barracuda, Nikolai, and Ennis at his peak.", "Punisher MAX Vol. 2", "0785116865"), "isbn": "9780785116865"},
        "punisher-max-kitchen": {**run_obj("punisher-max-kitchen", "max-punisher", "Punisher MAX: Kitchen Irish", "Garth Ennis & Leandro Fernandez", "2005", "Punisher Vol. 6 #7–12", "MAX", "Punisher MAX Vol. 1", "Frank Castle vs. the Kitchen Irish — one of Ennis' finest MAX arcs.", "Punisher MAX: Kitchen Irish", "0785126578"), "isbn": "9780785126578"},
        "punisher-ultimate-vol1": {**run_obj("punisher-ultimate-vol1", "ultimate-punisher", "Ultimate Punisher", "Garth Ennis & various", "2001", "Ultimate Marvel Team-Up #1–8", "Ultimate", "None", "The Ultimate Punisher debuts in a grittier Marvel Universe.", "Ultimate Punisher", "0785107880"), "isbn": "9780785107880"},
        "punisher-ultimate-avengers": {**run_obj("punisher-ultimate-avengers", "ultimate-punisher", "Ultimate Comics: Avengers", "Mark Millar & Leinil Yu", "2009–10", "Ultimate Comics: Avengers #1–6", "Ultimate", "Ultimate Punisher", "Ultimate Frank Castle joins Nick Fury's black-ops Avengers.", "Ultimate Comics: Avengers Vol. 1", "0785139789"), "isbn": "9780785139789"},
        "punisher-war-journal-vol1": {**run_obj("punisher-war-journal-vol1", "war-journal-punisher", "Punisher War Journal Vol. 1", "Matt Fraction & Ariel Olivetti", "2006–07", "Punisher War Journal Vol. 2 #1–6", "Modern Age", "None", "Matt Fraction's Punisher War Journal during Civil War.", "Punisher War Journal Vol. 1", "0785129923"), "isbn": "9780785129923"},
        "punisher-war-journal-vol2": {**run_obj("punisher-war-journal-vol2", "war-journal-punisher", "Punisher War Journal Vol. 2", "Matt Fraction & Ariel Olivetti", "2007–08", "Punisher War Journal Vol. 2 #7–12", "Modern Age", "War Journal Vol. 1", "The Punisher's war journal continues through World War Hulk and beyond.", "Punisher War Journal Vol. 2", "0785131645"), "isbn": "9780785131649"},
        "punisher-2099-vol1": {**run_obj("punisher-2099-vol1", "punisher-2099", "Punisher 2099 Vol. 1", "Pat Mills & various", "1995", "Punisher 2099 #1–6", "2099", "None", "Jake Gallows becomes the Punisher of 2099.", "Punisher 2099 Vol. 1", "0785107120"), "isbn": "9780785107120"},
        "punisher-cosmic-gr": {**run_obj("punisher-cosmic-gr", "cosmic-ghost-rider-punisher", "Cosmic Ghost Rider", "Donny Cates & Dylan Burnett", "2018", "Cosmic Ghost Rider #1–5", "Modern Age", "Thanos King Thanos", "Frank Castle as the Cosmic Ghost Rider — unhinged, violent, and cosmic.", "Cosmic Ghost Rider", "1302910110"), "isbn": "9781302910110"},
    },
    "home_runs": ["punisher-welcome-back-frank", "punisher-max-vol1", "punisher-max-vol2", "punisher-year-one", "punisher-war-journal-vol1", "punisher-ultimate-vol1", "punisher-max-kitchen", "punisher-circle-of-blood", "punisher-cosmic-gr", "punisher-2099-vol1"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Punisher",
        "lead": "If you're guilty, you're dead — one man's eternal war on crime.",
        "summary": "The Punisher is Frank Castle, a Marine veteran who became a vigilante after his family was murdered by the mob. Created by Gerry Conway, John Romita Sr., and Ross Andru, he debuted in The Amazing Spider-Man #129 (1974). Garth Ennis' MAX run and Welcome Back, Frank define the character's modern brutal mythology.",
        "facts": [
            {"label": "Alter ego", "value": "Frank Castle (Francis Castiglione)"},
            {"label": "First appearance", "value": "The Amazing Spider-Man #129 (1974)"},
            {"label": "Created by", "value": "Gerry Conway, John Romita Sr., Ross Andru"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Symbol", "value": "White skull on black"},
            {"label": "Allies", "value": "Microchip, Rachel Cole-Alves"},
            {"label": "Notable foes", "value": "Kingpin, Jigsaw, Barracuda"},
            {"label": "Powers", "value": "Peak human combat, weapons mastery"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            screen_item("punisher-1989", "The Punisher", "Dolph Lundgren", "https://en.wikipedia.org/wiki/The_Punisher_(1989_film)", "https://www.imdb.com/title/tt0098141/", year="1989"),
            screen_item("punisher-2004", "The Punisher", "Thomas Jane", "https://en.wikipedia.org/wiki/The_Punisher_(2004_film)", "https://www.imdb.com/title/tt0330793/", year="2004"),
            screen_item("punisher-2008", "Punisher: War Zone", "Ray Stevenson", "https://en.wikipedia.org/wiki/Punisher:_War_Zone", "https://www.imdb.com/title/tt0450315/", year="2008"),
        ]},
        {"group": "Netflix / TV", "items": [
            screen_item("punisher-dd", "Daredevil", "Jon Bernthal · Season 2 introduction", "https://en.wikipedia.org/wiki/Daredevil_(TV_series)", "https://www.imdb.com/title/tt3322312/", year="2016"),
            screen_item("punisher-netflix", "The Punisher", "Jon Bernthal · Solo series", "https://en.wikipedia.org/wiki/The_Punisher_(TV_series)", "https://www.imdb.com/title/tt5675620/", years="2017–2019"),
        ]},
    ],
    "themes": {
        "frank-castle": (55, 71, 79), "max-punisher": (30, 30, 35), "ultimate-punisher": (80, 80, 90),
        "war-journal-punisher": (50, 60, 70), "punisher-2099": (100, 40, 40), "cosmic-ghost-rider-punisher": (255, 120, 40),
    },
    "issues": {},
}


DAREDEVIL = {
    "id": "daredevil",
    "brand": "Daredevil",
    "title": "Daredevil — Devil Across the Multiverse",
    "nav_who": "Who is Daredevil",
    "nav_verses": "Verses",
    "who_id": "who-is-daredevil",
    "header_img": "daredevil-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #b71c1c, #4a0e0e 45%, #0a0202)",
    "verses_h2": "Daredevil Across the Multiverse",
    "verses_p": "versions across Marvel's Man Without Fear — Matt Murdock, Miller era, Shadowland, Ultimate DD, Elektra framing, and modern runs.",
    "comics_p": "Essential Daredevil stories — from Frank Miller's Born Again and Man Without Fear to Bendis, Waid, Zdarsky, and Shadowland.",
    "screen_p": "Live-action and animated appearances — from the Netflix Daredevil series and Ben Affleck film to Spider-Man animated guest spots.",
    "types": MARVEL_TYPES,
    "versions": [
        version_obj("matt-murdock", "Matt Murdock", "Earth-616 / Prime Marvel", "main", "Daredevil #1 (1964)", "The Man Without Fear", "Blinded as a child, Matt Murdock gained radar senses and became Daredevil — Hell's Kitchen's devil-advocate by day, vigilante by night.", "https://en.wikipedia.org/wiki/Daredevil_(Marvel_Comics_character)", ["dd-born-again", "dd-bendis-vol1", "dd-waid-vol1"]),
        version_obj("miller-daredevil", "Daredevil (Miller Era)", "Earth-616", "main", "Daredevil #158 (1979)", "The Man Without Fear reborn", "Frank Miller reinvented Daredevil — ninja tragedy, Kingpin's cruelty, and Elektra's death defined the character forever.", "https://en.wikipedia.org/wiki/Daredevil_(Marvel_Comics_character)", ["dd-miller-vol1", "dd-born-again", "dd-man-without-fear"]),
        version_obj("shadowland-daredevil", "Shadowland Daredevil", "Earth-616", "main", "Shadowland #1 (2010)", "The devil takes Hell's Kitchen", "Possessed by the Hand, Matt Murdock becomes Shadowland's dark lord — Daredevil at his most corrupted.", "https://en.wikipedia.org/wiki/Shadowland_(comics)", ["dd-shadowland", "dd-shadowland-saga"]),
        version_obj("ultimate-daredevil", "Ultimate Daredevil", "Earth-1610", "ultimate", "Ultimate Marvel Team-Up #1 (2001)", "Ultimate Man Without Fear", "The Ultimate Universe's Matt Murdock — a younger, grittier Daredevil in a reimagined Hell's Kitchen.", "https://en.wikipedia.org/wiki/Ultimate_Daredevil", ["dd-ultimate-vol1"]),
        version_obj("elektra-era-dd", "Elektra Era Daredevil", "Earth-616", "main", "Daredevil #168 (1981)", "Love and death", "Frank Miller's Elektra saga — Daredevil's doomed romance with the assassin Elektra Natchios.", "https://en.wikipedia.org/wiki/Elektra_(character)", ["dd-elektra-saga", "dd-miller-vol1"]),
        version_obj("zdarsky-daredevil", "Daredevil (Zdarsky Era)", "Earth-616", "main", "Daredevil Vol. 6 #1 (2019)", "Modern devil", "Chip Zdarsky and Marco Checchetto's acclaimed run — Matt Murdock's faith, fall, and fight for Hell's Kitchen.", "https://en.wikipedia.org/wiki/Daredevil_(Marvel_Comics_character)", ["dd-zdarsky-vol1", "dd-zdarsky-vol2"]),
    ],
    "runs": {
        "dd-born-again": {**run_obj("dd-born-again", "matt-murdock", "Daredevil: Born Again", "Frank Miller & David Mazzucchelli", "1986", "Daredevil #227–233", "Modern Age", "None — essential entry", "Kingpin destroys Matt Murdock's life piece by piece — the greatest Daredevil story ever told.", "Daredevil: Born Again", "0785106146"), "isbn": "9780785106146"},
        "dd-miller-vol1": {**run_obj("dd-miller-vol1", "miller-daredevil", "Daredevil by Frank Miller Vol. 1", "Frank Miller & Klaus Janson", "1979–81", "Daredevil #158–168", "Modern Age", "None", "Frank Miller's run introduces Elektra, Bullseye, and the Hand — Daredevil reinvented.", "Daredevil by Frank Miller Vol. 1", "0785108907"), "isbn": "9780785108907"},
        "dd-man-without-fear": {**run_obj("dd-man-without-fear", "miller-daredevil", "Daredevil: The Man Without Fear", "Frank Miller & John Romita Jr.", "1993–94", "Daredevil: The Man Without Fear #1–5", "Modern Age", "None", "Frank Miller and John Romita Jr. retell Matt Murdock's origin — from blind child to devil.", "Daredevil: The Man Without Fear", "0785108907"), "isbn": "9780785108907"},
        "dd-bendis-vol1": {**run_obj("dd-bendis-vol1", "matt-murdock", "Daredevil by Brian Michael Bendis Vol. 1", "Brian Michael Bendis & Alex Maleev", "2001–03", "Daredevil Vol. 2 #16–19, 26–30", "Modern Age", "Born Again recommended", "Bendis and Maleev's noir masterpiece — Daredevil unmasked and on trial.", "Daredevil by Brian Michael Bendis Vol. 1", "0785115702"), "isbn": "9780785115702"},
        "dd-waid-vol1": {**run_obj("dd-waid-vol1", "matt-murdock", "Daredevil by Mark Waid Vol. 1", "Mark Waid & Paolo Rivera", "2011", "Daredevil Vol. 3 #1–6", "Modern Age", "None", "Mark Waid's joyful run restores the swashbuckling spirit of Daredevil.", "Daredevil by Mark Waid Vol. 1", "0785157370"), "isbn": "9780785157370"},
        "dd-shadowland": {**run_obj("dd-shadowland", "shadowland-daredevil", "Shadowland", "Andy Diggle & various", "2010", "Shadowland #1–5", "Modern Age", "Daredevil by Ed Brubaker", "Matt Murdock possessed by the Hand rules Shadowland — heroes unite against him.", "Shadowland", "0785146920"), "isbn": "9780785146920"},
        "dd-shadowland-saga": {**run_obj("dd-shadowland-saga", "shadowland-daredevil", "Shadowland Saga", "Andy Diggle & various", "2010", "Shadowland #1–5 + tie-ins", "Modern Age", "Shadowland", "The complete Shadowland event with all tie-in issues.", "Shadowland Saga", "0785146742"), "isbn": "9780785146743"},
        "dd-ultimate-vol1": {**run_obj("dd-ultimate-vol1", "ultimate-daredevil", "Ultimate Daredevil", "Brian Michael Bendis & Alex Maleev", "2003", "Ultimate Marvel Team-Up #1–8", "Ultimate", "None", "The Ultimate Universe's Matt Murdock — a grittier Man Without Fear.", "Ultimate Daredevil", "0785107880"), "isbn": "9780785107880"},
        "dd-elektra-saga": {**run_obj("dd-elektra-saga", "elektra-era-dd", "Daredevil: Elektra Saga", "Frank Miller & Klaus Janson", "1981–82", "Daredevil #168–182", "Modern Age", "Miller Vol. 1", "Elektra's introduction, romance, and death — Frank Miller's tragic masterpiece.", "Daredevil: Elektra Saga", "0785108907"), "isbn": "9780785108907"},
        "dd-zdarsky-vol1": {**run_obj("dd-zdarsky-vol1", "zdarsky-daredevil", "Daredevil by Chip Zdarsky Vol. 1", "Chip Zdarsky & Marco Checchetto", "2019", "Daredevil Vol. 6 #1–5", "Modern Age", "None", "Chip Zdarsky's acclaimed run begins — Matt Murdock's faith and fall.", "Daredevil by Chip Zdarsky Vol. 1", "1302916470"), "isbn": "9781302916470"},
        "dd-zdarsky-vol2": {**run_obj("dd-zdarsky-vol2", "zdarsky-daredevil", "Daredevil by Chip Zdarsky Vol. 2", "Chip Zdarsky & Marco Checchetto", "2019–20", "Daredevil Vol. 6 #6–10", "Modern Age", "Zdarsky Vol. 1", "Zdarsky's Daredevil deepens — Kingpin, Stromwyn, and Hell's Kitchen.", "Daredevil by Chip Zdarsky Vol. 2", "1302921376"), "isbn": "9781302921371"},
    },
    "home_runs": ["dd-born-again", "dd-miller-vol1", "dd-bendis-vol1", "dd-waid-vol1", "dd-zdarsky-vol1", "dd-shadowland", "dd-elektra-saga", "dd-man-without-fear", "dd-ultimate-vol1", "dd-zdarsky-vol2"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Daredevil_(Marvel_Comics_character)",
        "lead": "The Man Without Fear — blind lawyer by day, devil of Hell's Kitchen by night.",
        "summary": "Daredevil is Matt Murdock, a blind lawyer with radar senses who protects Hell's Kitchen as a vigilante. Created by Stan Lee, Bill Everett, and Jack Kirby, he debuted in Daredevil #1 (1964). Frank Miller's Born Again and Man Without Fear, plus runs by Bendis, Waid, and Zdarsky, define the character's street-level noir legacy.",
        "facts": [
            {"label": "Alter ego", "value": "Matthew Michael Murdock"},
            {"label": "First appearance", "value": "Daredevil #1 (1964)"},
            {"label": "Created by", "value": "Stan Lee, Bill Everett, Jack Kirby"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Neighborhood", "value": "Hell's Kitchen, New York"},
            {"label": "Allies", "value": "Foggy Nelson, Karen Page, Elektra"},
            {"label": "Notable foes", "value": "Kingpin, Bullseye, The Hand"},
            {"label": "Powers", "value": "Radar sense, acrobatics, martial arts"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            screen_item("dd-2003", "Daredevil", "Ben Affleck · Origin", "https://en.wikipedia.org/wiki/Daredevil_(film)", "https://www.imdb.com/title/tt0287978/", year="2003"),
            screen_item("dd-elektra-film", "Elektra", "Jennifer Garner · Spin-off", "https://en.wikipedia.org/wiki/Elektra_(2005_film)", "https://www.imdb.com/title/tt0359013/", year="2005"),
        ]},
        {"group": "Netflix / TV", "items": [
            screen_item("dd-netflix", "Daredevil", "Charlie Cox · Netflix series", "https://en.wikipedia.org/wiki/Daredevil_(TV_series)", "https://www.imdb.com/title/tt3322312/", years="2015–2018"),
            screen_item("dd-born-again", "Daredevil: Born Again", "Charlie Cox · Disney+", "https://en.wikipedia.org/wiki/Daredevil:_Born_Again", "https://www.imdb.com/title/tt18923754/", years="2025–"),
        ]},
    ],
    "themes": {
        "matt-murdock": (183, 28, 28), "miller-daredevil": (120, 20, 20), "shadowland-daredevil": (40, 10, 10),
        "ultimate-daredevil": (140, 30, 30), "elektra-era-dd": (160, 40, 60), "zdarsky-daredevil": (100, 20, 30),
    },
    "issues": {},
}


GHOST_RIDER = {
    "id": "ghost-rider",
    "brand": "Ghost Rider",
    "title": "Ghost Rider — Vengeance Across the Multiverse",
    "nav_who": "Who is Ghost Rider",
    "nav_verses": "Verses",
    "who_id": "who-is-ghost-rider",
    "header_img": "ghost-rider-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #ff6f00, #bf360c 45%, #1a0800)",
    "verses_h2": "Ghost Rider Across the Multiverse",
    "verses_p": "versions across Marvel's Spirits of Vengeance — Johnny Blaze, Danny Ketch, Robbie Reyes, Jason Aaron's run, and alternate riders.",
    "comics_p": "Essential Ghost Rider stories — from Johnny Blaze's 1970s origin through Danny Ketch, Jason Aaron, and All-New Ghost Rider.",
    "screen_p": "Live-action and animated appearances — from Ghost Rider (2007) and Agents of S.H.I.E.L.D. to the 1990s animated series.",
    "types": MARVEL_TYPES,
    "versions": [
        version_obj("johnny-blaze", "Johnny Blaze", "Earth-616 / Prime Marvel", "main", "Marvel Spotlight #5 (1972)", "The original Spirit of Vengeance", "Stunt rider Johnny Blaze sold his soul to save his father and became the first Ghost Rider — Marvel's demonic anti-hero.", "https://en.wikipedia.org/wiki/Ghost_Rider", ["gr-johnny-classic", "gr-jason-aaron", "gr-spirits-of-vengeance"]),
        version_obj("danny-ketch", "Danny Ketch", "Earth-616 / Prime Marvel", "main", "Ghost Rider Vol. 3 #1 (1990)", "The 90s Ghost Rider", "Danny Ketch found a mystical motorcycle and became the Ghost Rider of the 1990s — chains, flames, and hellfire.", "https://en.wikipedia.org/wiki/Ghost_Rider_(Danny_Ketch)", ["gr-danny-ketch-vol1", "gr-danny-ketch-vol2"]),
        version_obj("robbie-reyes", "Robbie Reyes", "Earth-616 / Prime Marvel", "main", "All-New Ghost Rider #1 (2014)", "The All-New Ghost Rider", "Robbie Reyes bonded with a demonic spirit in a muscle car — a street-level Ghost Rider for a new generation.", "https://en.wikipedia.org/wiki/Robbie_Reyes", ["gr-all-new-vol1", "gr-all-new-vol2"]),
        version_obj("aaron-ghost-rider", "Ghost Rider (Jason Aaron Era)", "Earth-616", "main", "Ghost Rider Vol. 6 #1 (2006)", "Heaven's on fire", "Jason Aaron's Ghost Rider run — Johnny Blaze vs. angels, demons, and the Ghost Rider legacy.", "https://en.wikipedia.org/wiki/Ghost_Rider", ["gr-jason-aaron", "gr-heaven-on-fire"]),
        version_obj("cosmic-ghost-rider", "Cosmic Ghost Rider", "Earth-TRN666", "multiverse", "Thanos #13 (2018)", "Frank Castle rides again", "Frank Castle bonded with a Spirit of Vengeance and the Power Cosmic — the unhinged Cosmic Ghost Rider.", "https://en.wikipedia.org/wiki/Cosmic_Ghost_Rider", ["gr-cosmic-rider", "gr-jason-aaron"]),
        version_obj("ghost-rider-2099", "Ghost Rider 2099", "Earth-928 / 2099", "future", "Ghost Rider 2099 #1 (1994)", "Future rider", "Kenshiro Cochrane's consciousness uploaded into a cyborg body — the Ghost Rider of 2099.", "https://en.wikipedia.org/wiki/Ghost_Rider_2099", ["gr-2099-vol1"]),
    ],
    "runs": {
        "gr-johnny-classic": {**run_obj("gr-johnny-classic", "johnny-blaze", "Ghost Rider Epic Collection: Original Sin", "Gary Friedrich & Mike Ploog", "1972–75", "Marvel Spotlight #5–12, Ghost Rider #1–10", "Bronze Age", "None — classic entry", "Johnny Blaze's origin and early adventures — the birth of the Ghost Rider.", "Ghost Rider Epic Collection: Original Sin", "1302901901"), "isbn": "9781302901901"},
        "gr-jason-aaron": {**run_obj("gr-jason-aaron", "johnny-blaze", "Ghost Rider by Jason Aaron", "Jason Aaron & Roland Boschi", "2006–09", "Ghost Rider Vol. 6 #1–20", "Modern Age", "None", "Jason Aaron's acclaimed run — Johnny Blaze vs. heaven, hell, and the Ghost Rider legacy.", "Ghost Rider by Jason Aaron Omnibus", "1302912554"), "isbn": "9781302912554"},
        "gr-spirits-of-vengeance": {**run_obj("gr-spirits-of-vengeance", "johnny-blaze", "Spirits of Vengeance", "Howard Mackie & various", "1992–93", "Spirits of Vengeance #1–6", "Modern Age", "None", "Johnny Blaze and Danny Ketch team up as the Spirits of Vengeance.", "Spirits of Vengeance", "0785108907"), "isbn": "9780785108907"},
        "gr-danny-ketch-vol1": {**run_obj("gr-danny-ketch-vol1", "danny-ketch", "Ghost Rider Vol. 3", "Howard Mackie & Javier Saltares", "1990–91", "Ghost Rider Vol. 3 #1–6", "Modern Age", "None", "Danny Ketch's debut as the 1990s Ghost Rider — chains and hellfire.", "Ghost Rider Vol. 3", "0785100150"), "isbn": "9780785100157"},
        "gr-danny-ketch-vol2": {**run_obj("gr-danny-ketch-vol2", "danny-ketch", "Ghost Rider: Danny Ketch Classic Vol. 2", "Howard Mackie & Javier Saltares", "1991–92", "Ghost Rider Vol. 3 #7–12", "Modern Age", "Ghost Rider Vol. 3", "Danny Ketch's Ghost Rider run continues — Morbius, Blackout, and hell.", "Ghost Rider: Danny Ketch Classic Vol. 2", "0785107370"), "isbn": "9780785107370"},
        "gr-all-new-vol1": {**run_obj("gr-all-new-vol1", "robbie-reyes", "All-New Ghost Rider Vol. 1", "Felipe Smith & Tradd Moore", "2014", "All-New Ghost Rider #1–5", "Modern Age", "None", "Robbie Reyes debuts as the All-New Ghost Rider — muscle car and vengeance.", "All-New Ghost Rider Vol. 1", "0785192987"), "isbn": "9780785192981"},
        "gr-all-new-vol2": {**run_obj("gr-all-new-vol2", "robbie-reyes", "All-New Ghost Rider Vol. 2", "Felipe Smith & Tradd Moore", "2014–15", "All-New Ghost Rider #6–12", "Modern Age", "All-New Vol. 1", "Robbie Reyes' Ghost Rider run continues — street racing and demonic power.", "All-New Ghost Rider Vol. 2", "0785197067"), "isbn": "9780785197061"},
        "gr-heaven-on-fire": {**run_obj("gr-heaven-on-fire", "aaron-ghost-rider", "Ghost Riders: Heaven's on Fire", "Jason Aaron & Roland Boski", "2009", "Ghost Riders: Heaven's on Fire #1–6", "Modern Age", "Jason Aaron Ghost Rider", "Johnny Blaze and Danny Ketch unite as Ghost Riders against heaven itself.", "Ghost Riders: Heaven's on Fire", "0785146920"), "isbn": "9780785146920"},
        "gr-cosmic-rider": {**run_obj("gr-cosmic-rider", "cosmic-ghost-rider", "Cosmic Ghost Rider", "Donny Cates & Dylan Burnett", "2018", "Cosmic Ghost Rider #1–5", "Modern Age", "Thanos King Thanos", "Frank Castle as the Cosmic Ghost Rider — unhinged cosmic vengeance.", "Cosmic Ghost Rider", "1302910110"), "isbn": "9781302910110"},
        "gr-2099-vol1": {**run_obj("gr-2099-vol1", "ghost-rider-2099", "Ghost Rider 2099 Vol. 1", "Len Kaminski & Chris Bachalo", "1994–95", "Ghost Rider 2099 #1–6", "2099", "None", "Kenshiro Cochrane becomes the cyborg Ghost Rider of 2099.", "Ghost Rider 2099 Vol. 1", "0785107120"), "isbn": "9780785107120"},
    },
    "home_runs": ["gr-johnny-classic", "gr-jason-aaron", "gr-all-new-vol1", "gr-danny-ketch-vol1", "gr-heaven-on-fire", "gr-cosmic-rider", "gr-spirits-of-vengeance", "gr-all-new-vol2", "gr-danny-ketch-vol2", "gr-2099-vol1"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Ghost_Rider",
        "lead": "Vengeance rides a motorcycle — the Spirit of Vengeance punishes the guilty.",
        "summary": "Ghost Rider is the mantle of the Spirit of Vengeance — a demonic anti-hero who punishes the wicked. Johnny Blaze, created by Gary Friedrich, Mike Ploog, and Roy Thomas, debuted in Marvel Spotlight #5 (1972). Danny Ketch, Robbie Reyes, and others have carried the flaming skull across decades of horror-tinged superhero comics.",
        "facts": [
            {"label": "Notable riders", "value": "Johnny Blaze, Danny Ketch, Robbie Reyes"},
            {"label": "First appearance", "value": "Marvel Spotlight #5 (1972)"},
            {"label": "Created by", "value": "Gary Friedrich, Mike Ploog, Roy Thomas"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Signature weapon", "value": "Hellfire chain"},
            {"label": "Allies", "value": "Blade, Morbius, Spirits of Vengeance"},
            {"label": "Notable foes", "value": "Mephisto, Blackheart, Zarathos"},
            {"label": "Powers", "value": "Hellfire, Penance Stare, supernatural motorcycle"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            screen_item("gr-2007", "Ghost Rider", "Nicolas Cage · Johnny Blaze", "https://en.wikipedia.org/wiki/Ghost_Rider_(2007_film)", "https://www.imdb.com/title/tt0259324/", year="2007"),
            screen_item("gr-spirit", "Ghost Rider: Spirit of Vengeance", "Nicolas Cage · Sequel", "https://en.wikipedia.org/wiki/Ghost_Rider:_Spirit_of_Vengeance", "https://www.imdb.com/title/tt1071875/", year="2011"),
        ]},
        {"group": "TV / Animated", "items": [
            screen_item("gr-aos", "Agents of S.H.I.E.L.D.", "Gabriel Luna · Robbie Reyes", "https://en.wikipedia.org/wiki/Agents_of_S.H.I.E.L.D.", "https://www.imdb.com/title/tt2364582/", years="2013–2020"),
            screen_item("gr-1994", "Ghost Rider (1994)", "Animated series", "https://en.wikipedia.org/wiki/Ghost_Rider_(TV_series)", "https://www.imdb.com/title/tt0110333/", years="1994–1995"),
        ]},
    ],
    "themes": {
        "johnny-blaze": (255, 111, 0), "danny-ketch": (200, 50, 0), "robbie-reyes": (180, 40, 20),
        "aaron-ghost-rider": (255, 80, 0), "cosmic-ghost-rider": (255, 140, 40), "ghost-rider-2099": (100, 60, 80),
    },
    "issues": {},
}


MARVEL_MORE_PACKS = [
    DOCTOR_DOOM,
    THANOS,
    SILVER_SURFER,
    FANTASTIC_FOUR,
    PUNISHER,
    DAREDEVIL,
    GHOST_RIDER,
]
