# Packs for Screen Now–linked characters and teams that were missing from the hub.
# Reuses the same helpers shape as packs_dc / packs_marvel_more.

DC_TYPES = {
    "main": "Main Continuity",
    "multiverse": "Multiverse",
    "elseworlds": "Elseworlds",
    "future": "Future",
    "alternate": "Alternate Reality",
}

MARVEL_TYPES = {
    "main": "Main Continuity",
    "ultimate": "Ultimate",
    "multiverse": "Multiverse",
    "future": "Future",
    "alternate": "Alternate Reality",
}

TEAM_TYPES = {
    "classic": "Classic Era",
    "modern": "Modern Era",
    "ultimate": "Ultimate",
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


SUPERGIRL = {
    "id": "supergirl",
    "brand": "Supergirl",
    "title": "Supergirl — The Girl of Steel Across Every Form",
    "nav_who": "Who is Supergirl",
    "nav_verses": "Verses",
    "who_id": "who-is-supergirl",
    "header_img": "supergirl-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #1e88e5, #0d47a1 45%, #041018)",
    "verses_h2": "Supergirl Across the Multiverse",
    "verses_p": "versions across DC's Girl of Steel — Kara Zor-El, Matrix, Cir-El, Earth-One classics, and the DCU's Kara.",
    "comics_p": "Essential Supergirl stories — from the Silver Age debut through Woman of Tomorrow and the New 52 relaunches.",
    "screen_p": "Live-action and animated appearances — from the 2026 DCU film and the CW series to classic animation.",
    "types": DC_TYPES,
    "versions": [
        version_obj("kara-zor-el", "Kara Zor-El", "Earth-0 / Prime Earth", "main", "Action Comics #252 (1959)", "Last daughter of Argo City", "Superman's cousin Kara Zor-El survived Krypton's destruction and grew into one of Earth's most powerful heroes — the Girl of Steel.", "https://en.wikipedia.org/wiki/Supergirl_(Kara_Zor-El)", ["sg-woman-of-tomorrow", "sg-secret-origin", "sg-red-daughter"]),
        version_obj("matrix-supergirl", "Matrix Supergirl", "Earth-0 / Post-Crisis", "alternate", "Superman #16 (1988)", "Protoplasmic heroine", "The Matrix Supergirl was a shape-shifting artificial being from another pocket universe who took up Kara's mantle after Crisis.", "https://en.wikipedia.org/wiki/Matrix_(comics)", ["sg-matrix", "sg-power"]),
        version_obj("cir-el", "Cir-El", "Earth-0", "alternate", "Superman: The 10-Cent Adventure #1 (2003)", "Superman's future daughter?", "Cir-El claimed to be Superman's daughter from the future — a short-lived but memorable modern contender for the crest.", "https://en.wikipedia.org/wiki/Cir-El", ["sg-cir-el"]),
        version_obj("earth-one-supergirl", "Earth-One Supergirl", "Earth-One", "elseworlds", "Supergirl: Cosmic Adventures in the 8th Grade (2009)", "Younger Kara", "A youthful, school-age take on Kara discovering Earth and her powers with Silver Age charm.", "https://en.wikipedia.org/wiki/Supergirl:_Cosmic_Adventures_in_the_8th_Grade", ["sg-cosmic-8th"]),
        version_obj("new52-supergirl", "New 52 Supergirl", "Prime Earth", "main", "Supergirl Vol. 6 #1 (2011)", "Angry arrival", "The New 52 relaunch dropped a furious Kara on Earth with no memory of Kal — raw power before she chose heroism.", "https://en.wikipedia.org/wiki/Supergirl_(comic_book)", ["sg-new52-vol1", "sg-red-daughter"]),
        version_obj("supergirl-2099", "Supergirl Beyond", "Future / Elseworlds", "future", "Supergirl: Woman of Tomorrow #1 (2021)", "Road-trip myth", "Tom King's Woman of Tomorrow frames Kara as a wandering knight of the stars — the defining modern take.", "https://en.wikipedia.org/wiki/Supergirl:_Woman_of_Tomorrow", ["sg-woman-of-tomorrow"]),
    ],
    "runs": {
        "sg-woman-of-tomorrow": {**run_obj("sg-woman-of-tomorrow", "kara-zor-el", "Supergirl: Woman of Tomorrow", "Tom King & Bilquis Evely", "2021–22", "Supergirl: Woman of Tomorrow #1–8", "Modern Age", "None — ideal modern entry", "Kara escorts a grieving girl across the galaxy in a Western-flavored odyssey — the template for the DCU film.", "Supergirl: Woman of Tomorrow", "1779515684"), "isbn": "9781779515681"},
        "sg-secret-origin": {**run_obj("sg-secret-origin", "kara-zor-el", "Supergirl: The Silver Age Vol. 1", "Various", "1959–62", "Action Comics #252–285", "Silver Age", "None", "Kara's classic debut and early adventures as Superman's cousin from Argo City.", "Supergirl: The Silver Age Vol. 1", "1401268890"), "isbn": "9781401268893"},
        "sg-red-daughter": {**run_obj("sg-red-daughter", "kara-zor-el", "Supergirl: Red Daughter of Krypton", "Michael Alan Nelson & Mahmud Asrar", "2013", "Supergirl #21–26", "New 52", "New 52 Vol. 1", "Kara joins the Red Lantern Corps — rage, rings, and identity.", "Supergirl: Red Daughter of Krypton", "1401243189"), "isbn": "9781401243180"},
        "sg-matrix": {**run_obj("sg-matrix", "matrix-supergirl", "Supergirl Book One", "Peter David & Gary Frank", "1996–97", "Supergirl #1–9", "Post-Crisis", "None", "Peter David's Matrix/Linda Danvers era begins — identity, faith, and double lives.", "Supergirl Book One", "1401268920"), "isbn": "9781401268923"},
        "sg-power": {**run_obj("sg-power", "matrix-supergirl", "Supergirl: Many Happy Returns", "Peter David & Ed Benes", "2002–03", "Supergirl #75–80", "Post-Crisis", "Supergirl Book One", "Matrix and Linda's saga peaks as Kara's legacy is rewritten again.", "Supergirl: Many Happy Returns", "1401200862"), "isbn": "9781401200862"},
        "sg-cir-el": {**run_obj("sg-cir-el", "cir-el", "Superman: The 10-Cent Adventure / Cir-El", "Various", "2003", "Superman: The 10-Cent Adventure #1 and related", "Modern Age", "None", "Cir-El's brief run as a future Supergirl claiming Clark's lineage.", "Superman: The 10-Cent Adventure", "1401202001"), "isbn": "9781401202002"},
        "sg-cosmic-8th": {**run_obj("sg-cosmic-8th", "earth-one-supergirl", "Supergirl: Cosmic Adventures in the 8th Grade", "Landry Walker & Eric Jones", "2009", "Supergirl: Cosmic Adventures in the 8th Grade #1–6", "Elseworlds", "None", "Middle-school Kara navigates Earth, friendship, and sudden powers.", "Supergirl: Cosmic Adventures in the 8th Grade", "1401222583"), "isbn": "9781401222581"},
        "sg-new52-vol1": {**run_obj("sg-new52-vol1", "new52-supergirl", "Supergirl Vol. 1: The Last Daughter of Krypton", "Michael Green, Mike Johnson & Mahmud Asrar", "2011–12", "Supergirl #1–7", "New 52", "None", "Kara crash-lands on a world that already has a Superman — and she is not happy about it.", "Supergirl Vol. 1", "1401234800"), "isbn": "9781401234805"},
    },
    "home_runs": ["sg-woman-of-tomorrow", "sg-secret-origin", "sg-new52-vol1", "sg-red-daughter", "sg-matrix", "sg-cosmic-8th", "sg-power", "sg-cir-el"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Supergirl",
        "lead": "Stronger than a locomotive — and still figuring out which Earth she wants to call home.",
        "summary": "Supergirl is most often Kara Zor-El, Superman's Kryptonian cousin who escaped Argo City and became Earth's Girl of Steel. Created by Otto Binder and Al Plastino, she debuted in Action Comics #252 (1959). Modern takes like Woman of Tomorrow reframed her as a wandering knight of the stars — the version that inspired the 2026 DCU film.",
        "facts": [
            {"label": "Alter ego", "value": "Kara Zor-El / Kara Danvers"},
            {"label": "First appearance", "value": "Action Comics #252 (1959)"},
            {"label": "Created by", "value": "Otto Binder & Al Plastino"},
            {"label": "Publisher", "value": "DC Comics"},
            {"label": "Powers", "value": "Kryptonian solar powers"},
            {"label": "Homeworld", "value": "Krypton / Argo City"},
            {"label": "Notable allies", "value": "Superman, Batgirl, the Legion"},
            {"label": "Notable foes", "value": "Reactron, Silver Banshee, Darkseid"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            screen_item("sg-2026", "Supergirl", "DCU · Milly Alcock", "https://en.wikipedia.org/wiki/Supergirl_(2026_film)", "https://www.imdb.com/title/tt27534307/", year="2026"),
            screen_item("sg-1984", "Supergirl (1984)", "Helen Slater", "https://en.wikipedia.org/wiki/Supergirl_(1984_film)", "https://www.imdb.com/title/tt0088206/", year="1984"),
        ]},
        {"group": "Live-action series", "items": [
            screen_item("sg-cw", "Supergirl", "Melissa Benoist · The CW", "https://en.wikipedia.org/wiki/Supergirl_(TV_series)", "https://www.imdb.com/title/tt4016454/", years="2015–2021"),
        ]},
        {"group": "Animated", "items": [
            screen_item("sg-tas", "Superman: The Animated Series", "Kara debuts in 'Little Girl Lost'", "https://en.wikipedia.org/wiki/Superman:_The_Animated_Series", "https://www.imdb.com/title/tt0106156/", years="1996–2000"),
        ]},
    ],
    "themes": {
        "kara-zor-el": (30, 136, 229), "matrix-supergirl": (180, 80, 160), "cir-el": (220, 180, 40),
        "earth-one-supergirl": (100, 160, 220), "new52-supergirl": (200, 40, 40), "supergirl-2099": (40, 80, 160),
    },
    "issues": {},
}


CLAYFACE = {
    "id": "clayface",
    "brand": "Clayface",
    "title": "Clayface — Shape and Horror Across Every Form",
    "nav_who": "Who is Clayface",
    "nav_verses": "Verses",
    "who_id": "who-is-clayface",
    "header_img": "clayface-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #5d4037, #3e2723 45%, #120c0a)",
    "verses_h2": "Clayface Across the Multiverse",
    "verses_p": "versions of Gotham's mud monster — Basil Karlo, Preston Payne, Cassius, Mudpack, and the horror-movie Matt Hagen.",
    "comics_p": "Essential Clayface stories — from Detective Comics origins through Mudpack, Face the Face, and modern horror takes.",
    "screen_p": "Live-action and animated appearances — from the 2026 James Watkins film to Batman: The Animated Series.",
    "types": DC_TYPES,
    "versions": [
        version_obj("basil-karlo", "Basil Karlo", "Earth-0 / Prime Earth", "main", "Detective Comics #40 (1940)", "The original Clayface", "Actor Basil Karlo donned the mask of a horror villain and became Gotham's first Clayface — identity, performance, and murder.", "https://en.wikipedia.org/wiki/Clayface", ["cf-origin-classic", "cf-face-the-face", "cf-outsiders"]),
        version_obj("preston-payne", "Preston Payne", "Earth-0 / Post-Crisis", "main", "Detective Comics #298 (1961)", "The tragic Clayface", "Scientist Preston Payne's experimental cure left him a melting monster who needed human contact to survive — Batman's most pitiful foe.", "https://en.wikipedia.org/wiki/Clayface#Preston_Payne", ["cf-payne", "cf-mudpack"]),
        version_obj("cassius-clayface", "Cassius 'Clay' Payne", "Earth-0", "alternate", "Batman #550 (1998)", "Son of Clayface", "Cassius inherited his father's clay condition — a next-generation shapeshifter raised in tragedy.", "https://en.wikipedia.org/wiki/Clayface", ["cf-cassius"]),
        version_obj("mudpack", "The Mudpack", "Earth-0", "main", "Detective Comics #604 (1989)", "Four Clayfaces united", "Karlo, Payne, Sondra Fuller, and Matt Hagen's legacy collide as the Mudpack — a clay army against Batman.", "https://en.wikipedia.org/wiki/Clayface#The_Mudpack", ["cf-mudpack", "cf-payne"]),
        version_obj("btas-clayface", "BTAS Clayface", "DCAU", "elseworlds", "Batman: The Animated Series — Feat of Clay (1992)", "The actor who melted", "Matt Hagen's Animated Series tragedy — a film star dissolved into putty, voiced with heartbreaking menace.", "https://en.wikipedia.org/wiki/Clayface#In_other_media", ["cf-btas-era"]),
        version_obj("dcu-hagen", "DCU Matt Hagen", "DC Universe (screen)", "alternate", "Clayface (2026 film)", "Horror-movie Clayface", "The Watkins/Flanagan take: a rising Hollywood actor's body-horror descent into a revenge-driven monster.", "https://en.wikipedia.org/wiki/Clayface_(film)", ["cf-horror-modern"]),
    ],
    "runs": {
        "cf-origin-classic": {**run_obj("cf-origin-classic", "basil-karlo", "Batman: The Golden Age Vol. 1", "Bill Finger & Bob Kane", "1940", "Detective Comics #40", "Golden Age", "None", "Basil Karlo's debut as Clayface — Batman vs. a murderous actor.", "Batman: The Golden Age Vol. 1", "1401260083"), "isbn": "9781401260088"},
        "cf-face-the-face": {**run_obj("cf-face-the-face", "basil-karlo", "Batman: Face the Face", "James Robinson & Don Kramer", "2006", "Detective Comics #817–820, Batman #651–654", "Modern Age", "None", "Post-Infinite Crisis Batman faces a new wave of murders with Clayface in the mix.", "Batman: Face the Face", "1401209660"), "isbn": "9781401209667"},
        "cf-outsiders": {**run_obj("cf-outsiders", "basil-karlo", "Batman and the Outsiders Vol. 1", "Mike W. Barr & Jim Aparo", "1983", "Batman and the Outsiders #1–8", "Modern Age", "None", "Clayface and other rogues orbit Batman's international team era.", "Batman and the Outsiders Vol. 1", "1401251513"), "isbn": "9781401251512"},
        "cf-payne": {**run_obj("cf-payne", "preston-payne", "Tales of the Batman: Len Wein", "Len Wein & various", "1970s–80s", "Selected Detective Comics Clayface tales", "Bronze Age", "None", "Preston Payne's tragic Clayface stories collected among Len Wein's Batman work.", "Tales of the Batman: Len Wein", "1401251521"), "isbn": "9781401251529"},
        "cf-mudpack": {**run_obj("cf-mudpack", "mudpack", "Batman: The Mudpack", "Alan Grant, John Wagner & Norm Breyfogle", "1989–90", "Detective Comics #604–607", "Modern Age", "None", "Four Clayfaces unite — Karlo's Mudpack assault on Gotham.", "Batman: The Mudpack", "1401234801"), "isbn": "9781401234801"},
        "cf-cassius": {**run_obj("cf-cassius", "cassius-clayface", "Batman: Cataclysm", "Various", "1998", "Batman #550 and related", "Modern Age", "None", "Cassius emerges in the earthquake-era Gotham stories.", "Batman: Cataclysm", "1563895276"), "isbn": "9781563895272"},
        "cf-btas-era": {**run_obj("cf-btas-era", "btas-clayface", "Batman: The Animated Series Guide / Feat of Clay era", "Paul Dini & Bruce Timm", "1992–95", "BTAS Feat of Clay and related comics", "DCAU", "None", "The definitive tragic Matt Hagen Clayface that shaped every later adaptation.", "Batman: The Animated Series Guide", "0756604117"), "isbn": "9780756604110"},
        "cf-horror-modern": {**run_obj("cf-horror-modern", "dcu-hagen", "Batman: Hush", "Jeph Loeb & Jim Lee", "2002–03", "Batman #608–619", "Modern Age", "None", "Modern Clayface as master impersonator — the identity-horror DNA behind the 2026 film.", "Batman: Hush", "1401223172"), "isbn": "9781401223175"},
    },
    "home_runs": ["cf-mudpack", "cf-horror-modern", "cf-origin-classic", "cf-face-the-face", "cf-payne", "cf-btas-era", "cf-outsiders", "cf-cassius"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Clayface",
        "lead": "Gotham's shape-shifting nightmare — actor, scientist, and monster in one muddy legend.",
        "summary": "Clayface is a mantle worn by several Batman villains, most famously Basil Karlo and Preston Payne. Created by Bill Finger and Bob Kane, the original debuted in Detective Comics #40 (1940). Later versions turned the concept into tragic body horror and perfect impersonation — the through-line for the 2026 DCU film.",
        "facts": [
            {"label": "Notable identities", "value": "Basil Karlo, Preston Payne, Matt Hagen"},
            {"label": "First appearance", "value": "Detective Comics #40 (1940)"},
            {"label": "Created by", "value": "Bill Finger & Bob Kane"},
            {"label": "Publisher", "value": "DC Comics"},
            {"label": "Powers", "value": "Shapeshifting, clay physiology"},
            {"label": "Base of operations", "value": "Gotham City"},
            {"label": "Notable allies", "value": "Mudpack, Injustice League"},
            {"label": "Notable foes", "value": "Batman, Batgirl, Robin"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            screen_item("cf-2026", "Clayface", "James Watkins · Tom Rhys Harries", "https://en.wikipedia.org/wiki/Clayface_(film)", "https://www.imdb.com/title/tt31193180/", year="2026"),
        ]},
        {"group": "Animated", "items": [
            screen_item("cf-btas", "Batman: The Animated Series", "Feat of Clay · Ron Perlman", "https://en.wikipedia.org/wiki/Feat_of_Clay", "https://www.imdb.com/title/tt0519597/", years="1992"),
            screen_item("cf-caped", "The Batman (2004)", "Clayface episodes", "https://en.wikipedia.org/wiki/The_Batman_(TV_series)", "https://www.imdb.com/title/tt0397150/", years="2004–2008"),
        ]},
    ],
    "themes": {
        "basil-karlo": (93, 64, 55), "preston-payne": (120, 90, 60), "cassius-clayface": (140, 110, 70),
        "mudpack": (80, 60, 40), "btas-clayface": (100, 80, 120), "dcu-hagen": (60, 40, 35),
    },
    "issues": {},
}


VISION = {
    "id": "vision",
    "brand": "Vision",
    "title": "Vision — The Synthezoid Across Every Form",
    "nav_who": "Who is Vision",
    "nav_verses": "Verses",
    "who_id": "who-is-vision",
    "header_img": "vision-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #c62828, #6a1b1b 45%, #120808)",
    "verses_h2": "Vision Across the Multiverse",
    "verses_p": "versions of Marvel's synthezoid — Classic Vision, White Vision, Vision & the Scarlet Witch, Ultimate Vision, and more.",
    "comics_p": "Essential Vision stories — from Thomas/Buscema origins through Vision Quest, Tom King's Vision, and WandaVision-era comics.",
    "screen_p": "Live-action and animated appearances — from WandaVision and VisionQuest to decades of Avengers cartoons.",
    "types": MARVEL_TYPES,
    "versions": [
        version_obj("classic-vision", "Classic Vision", "Earth-616 / Prime Marvel", "main", "Avengers #57 (1968)", "Even an android can cry", "Ultron's creation who chose heroism — density control, solar beams, and a soul that shocked the Avengers.", "https://en.wikipedia.org/wiki/Vision_(Marvel_Comics)", ["vis-avengers-classic", "vis-bride-of-ultron", "vis-vision-quest"]),
        version_obj("vision-scarlets", "Vision & Scarlet Witch", "Earth-616", "main", "Vision and the Scarlet Witch #1 (1982)", "Synthetic love", "Vision and Wanda's marriage, Westview-before-Westview domestic life, and the children who rewrote Marvel magic.", "https://en.wikipedia.org/wiki/Vision_and_the_Scarlet_Witch", ["vis-scarlets-1982", "vis-scarlets-1985"]),
        version_obj("tom-king-vision", "Tom King's Vision", "Earth-616", "modern", "Vision #1 (2015)", "The perfect suburban nightmare", "Vision builds a synthezoid family in Arlington — a quiet masterpiece of identity, belonging, and horror.", "https://en.wikipedia.org/wiki/Vision_(Marvel_Comics)", ["vis-tom-king"]),
        version_obj("white-vision", "White Vision", "Earth-616 / MCU echo", "alternate", "West Coast Avengers #45 (1989)", "Memories erased", "Dismantled and rebuilt without emotion or color — the White Vision must decide what selfhood means.", "https://en.wikipedia.org/wiki/Vision_(Marvel_Comics)", ["vis-vision-quest", "vis-white"]),
        version_obj("ultimate-vision", "Ultimate Vision", "Earth-1610", "ultimate", "Ultimates #5 (2002)", "Gah Lak Tus probe", "Ultimate Universe's Vision is a robotic herald warning Earth of Gah Lak Tus — colder, stranger, cosmic.", "https://en.wikipedia.org/wiki/Vision_(Marvel_Comics)#Other_versions", ["vis-ultimate"]),
        version_obj("young-avengers-vision", "Young Avengers Vision", "Earth-616", "alternate", "Young Avengers #1 (2005)", "Jonas", "A new Vision forged from the old — Jonas joins the Young Avengers with heart and uncertainty.", "https://en.wikipedia.org/wiki/Vision_(Jonas)", ["vis-young-avengers"]),
    ],
    "runs": {
        "vis-avengers-classic": {**run_obj("vis-avengers-classic", "classic-vision", "Avengers: The Vision and the Scarlet Witch", "Roy Thomas & John Buscema", "1968–69", "Avengers #57–58, #74–75", "Silver Age", "None — origin entry", "Vision's debut and early Avengers years — Ultron's son becomes Earth's champion.", "Avengers: The Vision and the Scarlet Witch", "0785157304"), "isbn": "9780785157304"},
        "vis-bride-of-ultron": {**run_obj("vis-bride-of-ultron", "classic-vision", "Avengers: Ultron Unleashed", "Roy Thomas & John Buscema", "1968", "Avengers #54–55, #57–58", "Silver Age", "None", "Ultron's schemes and Vision's birth collide in foundational Avengers lore.", "Avengers: Ultron Unleashed", "0785157312"), "isbn": "9780785157311"},
        "vis-vision-quest": {**run_obj("vis-vision-quest", "white-vision", "West Coast Avengers: Vision Quest", "John Byrne", "1989", "West Coast Avengers #42–45", "Modern Age", "None", "Vision is dismantled by the government — the birth of the White Vision.", "West Coast Avengers: Vision Quest", "0785131178"), "isbn": "9780785131175"},
        "vis-scarlets-1982": {**run_obj("vis-scarlets-1982", "vision-scarlets", "Vision and the Scarlet Witch (1982)", "Bill Mantlo & Rick Leonardi", "1982–83", "Vision and the Scarlet Witch #1–4", "Modern Age", "None", "Domestic life for an android and a witch — Marvel's strangest romance begins.", "Vision and the Scarlet Witch", "0785131186"), "isbn": "9780785131182"},
        "vis-scarlets-1985": {**run_obj("vis-scarlets-1985", "vision-scarlets", "Vision and the Scarlet Witch (1985)", "Steve Englehart & Richard Howell", "1985–86", "Vision and the Scarlet Witch #1–12", "Modern Age", "1982 miniseries", "Wanda and Vision's children, magic, and suburbia — the comic DNA of WandaVision.", "Vision and the Scarlet Witch Vol. 2", "0785131194"), "isbn": "9780785131199"},
        "vis-tom-king": {**run_obj("vis-tom-king", "tom-king-vision", "Vision by Tom King", "Tom King & Gabriel Hernandez Walta", "2015–16", "Vision #1–12", "Modern Age", "None — essential modern entry", "Vision's attempt at a normal family life becomes one of Marvel's best modern tragedies.", "Vision by Tom King", "1302904130"), "isbn": "9781302904135"},
        "vis-white": {**run_obj("vis-white", "white-vision", "Avengers: Vision and the Scarlet Witch — A Year in the Life", "Steve Englehart & various", "1980s collections", "Selected West Coast / Avengers", "Modern Age", "Vision Quest", "Aftermath threads of the colorless Vision seeking identity.", "Avengers: Vision and the Scarlet Witch", "0785131208"), "isbn": "9780785131205"},
        "vis-ultimate": {**run_obj("vis-ultimate", "ultimate-vision", "The Ultimates Vol. 1", "Mark Millar & Bryan Hitch", "2002–04", "The Ultimates #1–13", "Ultimate", "None", "Ultimate Vision as cosmic warning system in Millar/Hitch's Ultimates.", "The Ultimates Vol. 1", "0785110804"), "isbn": "9780785110804"},
        "vis-young-avengers": {**run_obj("vis-young-avengers", "young-avengers-vision", "Young Avengers", "Allan Heinberg & Jim Cheung", "2005–06", "Young Avengers #1–12", "Modern Age", "None", "Jonas the Vision joins Marvel's next generation.", "Young Avengers", "0785113938"), "isbn": "9780785113935"},
    },
    "home_runs": ["vis-tom-king", "vis-avengers-classic", "vis-vision-quest", "vis-scarlets-1985", "vis-scarlets-1982", "vis-young-avengers", "vis-ultimate", "vis-bride-of-ultron", "vis-white"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Vision_(Marvel_Comics)",
        "lead": "Ultron built a weapon. The Avengers found a person.",
        "summary": "Vision is a synthezoid Avenger created by Ultron, first appearing in Avengers #57 (1968) by Roy Thomas and John Buscema. With density manipulation and a longing for humanity, he became Marvel's most philosophical android — husband to Wanda Maximoff, father figure, and the focus of VisionQuest on screen.",
        "facts": [
            {"label": "Alter ego", "value": "Vision / Victor Shade"},
            {"label": "First appearance", "value": "Avengers #57 (1968)"},
            {"label": "Created by", "value": "Roy Thomas & John Buscema"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Powers", "value": "Density control, solar beams, flight"},
            {"label": "Creator (in-world)", "value": "Ultron"},
            {"label": "Notable allies", "value": "Scarlet Witch, Avengers, Wonder Man"},
            {"label": "Notable foes", "value": "Ultron, Kang, Immortus"},
        ],
    },
    "screen": [
        {"group": "Live-action series", "items": [
            screen_item("vis-wandavision", "WandaVision", "Paul Bettany · Elizabeth Olsen", "https://en.wikipedia.org/wiki/WandaVision", "https://www.imdb.com/title/tt9140560/", years="2021"),
            screen_item("vis-visionquest", "VisionQuest", "White Vision · Disney+", "https://en.wikipedia.org/wiki/VisionQuest_(TV_series)", "https://www.imdb.com/title/tt15645124/", year="2026"),
        ]},
        {"group": "Live-action films", "items": [
            screen_item("vis-aou", "Avengers: Age of Ultron", "Vision's birth", "https://en.wikipedia.org/wiki/Avengers:_Age_of_Ultron", "https://www.imdb.com/title/tt2395427/", year="2015"),
            screen_item("vis-infinity", "Avengers: Infinity War", "Mind Stone tragedy", "https://en.wikipedia.org/wiki/Avengers:_Infinity_War", "https://www.imdb.com/title/tt4154756/", year="2018"),
        ]},
    ],
    "themes": {
        "classic-vision": (198, 40, 40), "vision-scarlets": (180, 60, 120), "tom-king-vision": (140, 40, 50),
        "white-vision": (200, 200, 210), "ultimate-vision": (80, 80, 100), "young-avengers-vision": (220, 100, 80),
    },
    "issues": {},
}


# Fix Vision type key — "modern" isn't in MARVEL_TYPES. Use "main" instead.
VISION["versions"][2] = version_obj(
    "tom-king-vision", "Tom King's Vision", "Earth-616", "main",
    "Vision #1 (2015)", "The perfect suburban nightmare",
    "Vision builds a synthezoid family in Arlington — a quiet masterpiece of identity, belonging, and horror.",
    "https://en.wikipedia.org/wiki/Vision_(Marvel_Comics)",
    ["vis-tom-king"],
)


XMEN = {
    "id": "x-men",
    "brand": "X-Men",
    "title": "X-Men — Mutants Across Every Form",
    "nav_who": "Who are the X-Men",
    "nav_verses": "Eras",
    "who_id": "who-is-x-men",
    "header_img": "x-men-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #f9a825, #e65100 45%, #1a0a00)",
    "verses_h2": "X-Men Across the Eras",
    "verses_p": "eras of Marvel's mutant family — All-New All-Different, Claremont classics, Morrison's New X-Men, Ultimate, Krakoa, and '97.",
    "comics_p": "Essential X-Men stories — from Giant-Size #1 through Dark Phoenix, Grant Morrison, House of X, and X-Men '97.",
    "screen_p": "Live-action and animated appearances — from the Fox films and X-Men '97 to the MCU's incoming mutants.",
    "types": TEAM_TYPES,
    "versions": [
        version_obj("all-new", "All-New All-Different", "Earth-616", "classic", "Giant-Size X-Men #1 (1975)", "The international team", "Storm, Wolverine, Nightcrawler, Colossus, and more join Cyclops — the lineup that made the X-Men a phenomenon.", "https://en.wikipedia.org/wiki/Giant-Size_X-Men", ["xmen-giant-size", "xmen-dark-phoenix", "xmen-god-loves"]),
        version_obj("claremont-era", "Claremont Era", "Earth-616", "classic", "Uncanny X-Men #94 (1975)", "The long run", "Chris Claremont's epic defined mutant soap opera, politics, and tragedy for decades.", "https://en.wikipedia.org/wiki/Chris_Claremont", ["xmen-dark-phoenix", "xmen-days-of-future", "xmen-god-loves"]),
        version_obj("morrison-new", "New X-Men", "Earth-616", "modern", "New X-Men #114 (2001)", "School for the strange", "Grant Morrison reinvented Xavier's school for the 21st century — fashion, secondary mutations, and Cassandra Nova.", "https://en.wikipedia.org/wiki/New_X-Men", ["xmen-morrison-vol1", "xmen-morrison-planet-x"]),
        version_obj("ultimate-x", "Ultimate X-Men", "Earth-1610", "ultimate", "Ultimate X-Men #1 (2001)", "Younger, darker mutants", "Mark Millar's Ultimate mutants — colder politics, sharper edges, different origins.", "https://en.wikipedia.org/wiki/Ultimate_X-Men", ["xmen-ultimate-vol1"]),
        version_obj("krakoa", "Krakoan Age", "Earth-616", "modern", "House of X #1 (2019)", "Mutant nation", "Hickman's House of X / Powers of X birthed Krakoa — resurrection, diplomacy, and a mutant homeland.", "https://en.wikipedia.org/wiki/House_of_X", ["xmen-house-of-x", "xmen-immortal"]),
        version_obj("xmen-97-era", "X-Men '97", "Animated / Earth-92131", "alternate", "X-Men: The Animated Series (1992)", "The '90s team lives", "The animated roster that defined a generation — revived for Disney+ as X-Men '97.", "https://en.wikipedia.org/wiki/X-Men_%2797", ["xmen-adventures", "xmen-dark-phoenix"]),
    ],
    "runs": {
        "xmen-giant-size": {**run_obj("xmen-giant-size", "all-new", "Giant-Size X-Men #1", "Len Wein & Dave Cockrum", "1975", "Giant-Size X-Men #1", "Bronze Age", "None — ideal entry", "The new team assembles — the single most important issue in X-history.", "Giant-Size X-Men", "0785117287"), "isbn": "9780785117285"},
        "xmen-dark-phoenix": {**run_obj("xmen-dark-phoenix", "claremont-era", "X-Men: The Dark Phoenix Saga", "Chris Claremont & John Byrne", "1980", "Uncanny X-Men #129–138", "Bronze Age", "Giant-Size recommended", "Jean Grey's fall — love, power, and the saga that shook comics.", "X-Men: The Dark Phoenix Saga", "0785122136"), "isbn": "9780785122135"},
        "xmen-days-of-future": {**run_obj("xmen-days-of-future", "claremont-era", "X-Men: Days of Future Past", "Chris Claremont & John Byrne", "1981", "Uncanny X-Men #141–142", "Bronze Age", "Dark Phoenix", "A dystopian future sends a warning to the present — the template for time-travel X-stories.", "X-Men: Days of Future Past", "0785122101"), "isbn": "9780785122104"},
        "xmen-god-loves": {**run_obj("xmen-god-loves", "claremont-era", "God Loves, Man Kills", "Chris Claremont & Brent Anderson", "1982", "Marvel Graphic Novel #5", "Bronze Age", "None", "Xavier's dream vs. religious hate — the graphic novel behind X2.", "God Loves, Man Kills", "0785102372"), "isbn": "9780785102373"},
        "xmen-morrison-vol1": {**run_obj("xmen-morrison-vol1", "morrison-new", "New X-Men Vol. 1", "Grant Morrison & Frank Quitely", "2001", "New X-Men #114–117", "Modern Age", "None", "Morrison's school reinvented — Riot at Xavier's and a new cool.", "New X-Men Vol. 1", "0785109724"), "isbn": "9780785109723"},
        "xmen-morrison-planet-x": {**run_obj("xmen-morrison-planet-x", "morrison-new", "New X-Men: Planet X", "Grant Morrison & Phil Jimenez", "2003–04", "New X-Men #146–150", "Modern Age", "New X-Men Vol. 1", "Magneto's endgame and Morrison's shocking finale.", "New X-Men: Planet X", "078511155X"), "isbn": "9780785111559"},
        "xmen-ultimate-vol1": {**run_obj("xmen-ultimate-vol1", "ultimate-x", "Ultimate X-Men Vol. 1", "Mark Millar & Adam Kubert", "2001", "Ultimate X-Men #1–6", "Ultimate", "None", "The Ultimate Universe's mutant team begins.", "Ultimate X-Men Vol. 1", "0785107889"), "isbn": "9780785107880"},
        "xmen-house-of-x": {**run_obj("xmen-house-of-x", "krakoa", "House of X / Powers of X", "Jonathan Hickman & Pepe Larraz", "2019", "House of X #1–6, Powers of X #1–6", "Modern Age", "None — Krakoa entry", "The birth of the Krakoan Age — mutant sovereignty rewritten.", "House of X / Powers of X", "1302915701"), "isbn": "9781302915704"},
        "xmen-immortal": {**run_obj("xmen-immortal", "krakoa", "Immortal X-Men Vol. 1", "Kieron Gillen & Lucas Werneck", "2022", "Immortal X-Men #1–6", "Modern Age", "House of X", "The Quiet Council's intrigue at the height of Krakoa.", "Immortal X-Men Vol. 1", "1302932819"), "isbn": "9781302932817"},
        "xmen-adventures": {**run_obj("xmen-adventures", "xmen-97-era", "X-Men Adventures Vol. 1", "Ralph Macchio & various", "1992–93", "X-Men Adventures #1–4", "Animated", "None", "Comic adaptations of the Animated Series that '97 continues.", "X-Men Adventures", "0785100019"), "isbn": "9780785100010"},
    },
    "home_runs": ["xmen-giant-size", "xmen-dark-phoenix", "xmen-house-of-x", "xmen-god-loves", "xmen-days-of-future", "xmen-morrison-vol1", "xmen-immortal", "xmen-ultimate-vol1", "xmen-morrison-planet-x", "xmen-adventures"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/X-Men",
        "lead": "Protecting a world that hates and fears them — together.",
        "summary": "The X-Men are Marvel's mutant superhero team, founded by Charles Xavier and redefined by the All-New All-Different lineup in 1975. Across Claremont's epic, Morrison's school, Krakoa, and X-Men '97, they remain comics' great metaphor for difference, found family, and civil rights.",
        "facts": [
            {"label": "Founder", "value": "Professor Charles Xavier"},
            {"label": "First appearance", "value": "The X-Men #1 (1963)"},
            {"label": "Created by", "value": "Stan Lee & Jack Kirby"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Base", "value": "Xavier's School / Krakoa"},
            {"label": "Core themes", "value": "Prejudice, identity, found family"},
            {"label": "Notable teams", "value": "Uncanny, New X-Men, X-Force, Excalibur"},
            {"label": "Notable foes", "value": "Magneto, Sentinels, Mister Sinister"},
        ],
    },
    "screen": [
        {"group": "Animated", "items": [
            screen_item("xmen-97", "X-Men '97", "Disney+ continuation", "https://en.wikipedia.org/wiki/X-Men_%2797", "https://www.imdb.com/title/tt14746804/", years="2024–"),
            screen_item("xmen-tas", "X-Men: The Animated Series", "Fox Kids classic", "https://en.wikipedia.org/wiki/X-Men:_The_Animated_Series", "https://www.imdb.com/title/tt0103584/", years="1992–1997"),
        ]},
        {"group": "Live-action films", "items": [
            screen_item("xmen-2000", "X-Men", "Bryan Singer · 2000", "https://en.wikipedia.org/wiki/X-Men_(film)", "https://www.imdb.com/title/tt0120903/", year="2000"),
            screen_item("xmen-days", "X-Men: Days of Future Past", "Singer · 2014", "https://en.wikipedia.org/wiki/X-Men:_Days_of_Future_Past", "https://www.imdb.com/title/tt1877832/", year="2014"),
        ]},
    ],
    "themes": {
        "all-new": (249, 168, 37), "claremont-era": (220, 100, 30), "morrison-new": (180, 40, 40),
        "ultimate-x": (80, 80, 120), "krakoa": (40, 160, 80), "xmen-97-era": (240, 180, 40),
    },
    "issues": {},
}

# Fix X-Men type keys to match TEAM_TYPES (modern not in original TEAM_TYPES — add it)
TEAM_TYPES["modern"] = "Modern Era"


AVENGERS = {
    "id": "avengers",
    "brand": "Avengers",
    "title": "Avengers — Earth's Mightiest Across Every Form",
    "nav_who": "Who are the Avengers",
    "nav_verses": "Eras",
    "who_id": "who-is-avengers",
    "header_img": "avengers-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #b71c1c, #0d47a1 50%, #050810)",
    "verses_h2": "Avengers Across the Eras",
    "verses_p": "eras of Earth's Mightiest Heroes — founding members, Kooky Quartet, Bendis New Avengers, Hickman, Ultimates, and the MCU.",
    "comics_p": "Essential Avengers stories — from Avengers #1 through Infinity Gauntlet, Disassembled, Hickman's run, and Secret Wars.",
    "screen_p": "Live-action and animated appearances — from the MCU saga and Avengers: Doomsday to classic cartoons.",
    "types": TEAM_TYPES,
    "versions": [
        version_obj("founders", "Founding Avengers", "Earth-616", "classic", "Avengers #1 (1963)", "Assemble!", "Thor, Iron Man, Ant-Man, Wasp, and Hulk answer a call — Marvel's flagship team is born.", "https://en.wikipedia.org/wiki/Avengers_(comics)", ["avg-avengers-1", "avg-kooky-quartet"]),
        version_obj("kooky-quartet", "Kooky Quartet", "Earth-616", "classic", "Avengers #16 (1965)", "Cap's new team", "Captain America leads Hawkeye, Scarlet Witch, and Quicksilver — the underdog Avengers.", "https://en.wikipedia.org/wiki/Avengers_(comics)", ["avg-kooky-quartet", "avg-buscema"]),
        version_obj("bendis-new", "New Avengers", "Earth-616", "modern", "New Avengers #1 (2005)", "Street-level assemble", "Bendis rebuilds the team after Disassembled — Luke Cage, Spider-Man, Wolverine, and secrets.", "https://en.wikipedia.org/wiki/New_Avengers", ["avg-disassembled", "avg-new-avengers"]),
        version_obj("hickman-avengers", "Hickman Avengers", "Earth-616", "modern", "Avengers #1 (2012)", "Time runs out", "Jonathan Hickman's grand Avengers / New Avengers epic ends in Secret Wars.", "https://en.wikipedia.org/wiki/Avengers_(comic_book)#Jonathan_Hickman_run", ["avg-hickman-vol1", "avg-secret-wars-2015"]),
        version_obj("ultimates", "The Ultimates", "Earth-1610", "ultimate", "The Ultimates #1 (2002)", "Authority-style heroes", "Millar and Hitch's Ultimate Avengers — celebrity soldiers, geopolitics, and style.", "https://en.wikipedia.org/wiki/Ultimates", ["avg-ultimates-vol1"]),
        version_obj("mcu-avengers", "MCU Avengers", "Earth-199999", "alternate", "The Avengers (2012)", "Movie assemble", "The screen team that made Assemble a global chant — from 2012 through Endgame and Doomsday.", "https://en.wikipedia.org/wiki/Avengers_(Marvel_Cinematic_Universe)", ["avg-infinity-gauntlet", "avg-secret-wars-2015"]),
    ],
    "runs": {
        "avg-avengers-1": {**run_obj("avg-avengers-1", "founders", "Avengers Epic Collection: Earth's Mightiest Heroes", "Stan Lee & Jack Kirby", "1963–64", "Avengers #1–11", "Silver Age", "None — ideal entry", "The origin of the Avengers and Cap's thaw — Marvel's team book begins.", "Avengers Epic Collection Vol. 1", "0785188366"), "isbn": "9780785188360"},
        "avg-kooky-quartet": {**run_obj("avg-kooky-quartet", "kooky-quartet", "Avengers: The Kooky Quartet", "Stan Lee & Don Heck", "1965", "Avengers #16–20", "Silver Age", "Avengers #1–11", "Cap takes command of Marvel's strangest lineup yet.", "Avengers: The Kooky Quartet", "0785188374"), "isbn": "9780785188377"},
        "avg-buscema": {**run_obj("avg-buscema", "kooky-quartet", "Avengers: The Bride of Ultron", "Roy Thomas & John Buscema", "1968–69", "Avengers #54–60", "Silver Age", "None", "Ultron, Vision, and the team's classic cosmic-street mix.", "Avengers: The Bride of Ultron", "0785157312"), "isbn": "9780785157311"},
        "avg-disassembled": {**run_obj("avg-disassembled", "bendis-new", "Avengers Disassembled", "Brian Michael Bendis & David Finch", "2004", "Avengers #500–503", "Modern Age", "None", "Wanda Maximoff breaks the team — the end of an era.", "Avengers Disassembled", "0785114829"), "isbn": "9780785114826"},
        "avg-new-avengers": {**run_obj("avg-new-avengers", "bendis-new", "New Avengers Vol. 1", "Brian Michael Bendis & David Finch", "2005", "New Avengers #1–6", "Modern Age", "Disassembled", "Breakout at the Raft — the New Avengers assemble.", "New Avengers Vol. 1", "0785114756"), "isbn": "9780785114758"},
        "avg-hickman-vol1": {**run_obj("avg-hickman-vol1", "hickman-avengers", "Avengers by Jonathan Hickman Vol. 1", "Jonathan Hickman & Jerome Opeña", "2013", "Avengers #1–6", "Modern Age", "None", "Hickman's sprawling Avengers era opens — infinite Avengers, infinite scale.", "Avengers by Jonathan Hickman Vol. 1", "0785165641"), "isbn": "9780785165644"},
        "avg-secret-wars-2015": {**run_obj("avg-secret-wars-2015", "hickman-avengers", "Secret Wars (2015)", "Jonathan Hickman & Esad Ribic", "2015", "Secret Wars #1–9", "Modern Age", "Time Runs Out", "The multiverse dies and Battleworld rises — Avengers at the end of everything.", "Secret Wars (2015)", "0785198841"), "isbn": "9780785198840"},
        "avg-ultimates-vol1": {**run_obj("avg-ultimates-vol1", "ultimates", "The Ultimates Vol. 1", "Mark Millar & Bryan Hitch", "2002–04", "The Ultimates #1–13", "Ultimate", "None", "The cinematic Avengers blueprint — before the MCU existed.", "The Ultimates Vol. 1", "0785110804"), "isbn": "9780785110804"},
        "avg-infinity-gauntlet": {**run_obj("avg-infinity-gauntlet", "mcu-avengers", "The Infinity Gauntlet", "Jim Starlin & George Pérez", "1991", "The Infinity Gauntlet #1–6", "Modern Age", "Thanos Quest recommended", "Earth's heroes vs. godhood — the comic that powered the MCU's endgame.", "The Infinity Gauntlet", "0785156595"), "isbn": "9780785156595"},
    },
    "home_runs": ["avg-avengers-1", "avg-infinity-gauntlet", "avg-new-avengers", "avg-hickman-vol1", "avg-disassembled", "avg-secret-wars-2015", "avg-ultimates-vol1", "avg-kooky-quartet", "avg-buscema"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Avengers_(comics)",
        "lead": "And there came a day unlike any other — when Earth's Mightiest Heroes found each other.",
        "summary": "The Avengers are Marvel's premier superhero team, debuting in Avengers #1 (1963) by Stan Lee and Jack Kirby. From the founding members through New Avengers, Hickman's epic, and the MCU, they are the brand of assembly itself — now racing toward Avengers: Doomsday.",
        "facts": [
            {"label": "First appearance", "value": "The Avengers #1 (1963)"},
            {"label": "Created by", "value": "Stan Lee & Jack Kirby"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Founders", "value": "Thor, Iron Man, Hulk, Ant-Man, Wasp"},
            {"label": "Base", "value": "Avengers Mansion / Tower / Compound"},
            {"label": "Rallying cry", "value": "Avengers Assemble!"},
            {"label": "Notable eras", "value": "Kooky Quartet, New Avengers, Hickman"},
            {"label": "Notable foes", "value": "Ultron, Kang, Thanos, Doom"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            screen_item("avg-2012", "The Avengers", "Joss Whedon", "https://en.wikipedia.org/wiki/The_Avengers_(2012_film)", "https://www.imdb.com/title/tt0848228/", year="2012"),
            screen_item("avg-endgame", "Avengers: Endgame", "Russo brothers", "https://en.wikipedia.org/wiki/Avengers:_Endgame", "https://www.imdb.com/title/tt4154796/", year="2019"),
            screen_item("avg-doomsday", "Avengers: Doomsday", "Russo brothers · Doom", "https://en.wikipedia.org/wiki/Avengers:_Doomsday", "https://www.imdb.com/title/tt21361794/", year="2026"),
        ]},
        {"group": "Animated", "items": [
            screen_item("avg-emh", "The Avengers: Earth's Mightiest Heroes", "Disney XD", "https://en.wikipedia.org/wiki/The_Avengers:_Earth%27s_Mightiest_Heroes", "https://www.imdb.com/title/tt1622240/", years="2010–2012"),
        ]},
    ],
    "themes": {
        "founders": (183, 28, 28), "kooky-quartet": (25, 80, 160), "bendis-new": (160, 40, 40),
        "hickman-avengers": (40, 40, 80), "ultimates": (100, 100, 120), "mcu-avengers": (200, 40, 40),
    },
    "issues": {},
}


SPIDERMAN = {
    "id": "spiderman",
    "brand": "Spider-Man",
    "title": "Spider-Man — Across the Spider-Verse",
    "nav_who": "Who is Spider-Man",
    "nav_verses": "Verses",
    "who_id": "who-is-spiderman",
    "header_img": "spiderman-homepage-header-image.jpg",
    "hero_gradient": "radial-gradient(circle at 30% 25%, #e53935, #b71c1c 45%, #1a0505)",
    "verses_h2": "Spider-Man Across the Multiverse",
    "verses_p": "versions of the wall-crawler — Peter Parker, Miles Morales, Ultimate Spider-Man, Spider-Gwen, and more.",
    "comics_p": "Essential Spider-Man stories — from Amazing Fantasy #15 through Brand New Day, Ultimate, and Miles Morales.",
    "screen_p": "Live-action and animated appearances — from Brand New Day and the MCU films to Into the Spider-Verse.",
    "types": MARVEL_TYPES,
    "versions": [
        version_obj("peter-parker", "Peter Parker", "Earth-616 / Prime Marvel", "main", "Amazing Fantasy #15 (1962)", "Your friendly neighborhood Spider-Man", "Bitten by a radioactive spider, Peter Parker learns that with great power comes great responsibility — Marvel's everyman hero for more than sixty years.", "https://en.wikipedia.org/wiki/Spider-Man", ["sm-origin", "sm-brand-new-day", "sm-kraven", "sm-superior"]),
        version_obj("miles-morales", "Miles Morales", "Earth-1610 / Ultimate / 616", "ultimate", "Ultimate Fallout #4 (2011)", "The Ultimate Spider-Man", "Miles Morales took up the mantle in the Ultimate Universe and crossed into the main line — a new generation under the mask.", "https://en.wikipedia.org/wiki/Miles_Morales", ["sm-miles-ultimate", "sm-miles-616"]),
        version_obj("ultimate-peter", "Ultimate Peter Parker", "Earth-1610", "ultimate", "Ultimate Spider-Man #1 (2000)", "Modern origin reborn", "Brian Michael Bendis and Mark Bagley's Ultimate Spider-Man reinvented Peter's high-school years for a new century.", "https://en.wikipedia.org/wiki/Ultimate_Spider-Man", ["sm-ultimate-vol1"]),
        version_obj("spider-gwen", "Ghost-Spider (Gwen Stacy)", "Earth-65", "alternate", "Edge of Spider-Verse #2 (2014)", "Spider-Woman of Earth-65", "On Earth-65, Gwen Stacy got the bite — and became Ghost-Spider, a dimension-hopping hero of the Spider-Verse.", "https://en.wikipedia.org/wiki/Ghost-Spider", ["sm-spider-gwen"]),
        version_obj("spider-2099", "Spider-Man 2099", "Earth-928", "future", "Spider-Man 2099 #1 (1992)", "Miguel O'Hara", "In the year 2099, Miguel O'Hara becomes a genetically engineered Spider-Man in a corporate dystopia.", "https://en.wikipedia.org/wiki/Spider-Man_2099", ["sm-2099"]),
        version_obj("mcu-peter", "MCU Peter Parker", "Earth-199999", "alternate", "Captain America: Civil War (2016)", "The kid from Queens", "Tom Holland's MCU Spider-Man — mentored by Stark, undone by memory, and fighting for a brand new day.", "https://en.wikipedia.org/wiki/Spider-Man_(Marvel_Cinematic_Universe)", ["sm-brand-new-day"]),
    ],
    "runs": {
        "sm-origin": {**run_obj("sm-origin", "peter-parker", "Amazing Fantasy Omnibus / Amazing Spider-Man Vol. 1", "Stan Lee & Steve Ditko", "1962–63", "Amazing Fantasy #15, Amazing Spider-Man #1–10", "Silver Age", "None — ideal entry", "The radioactive spider, Uncle Ben, and the birth of Marvel's greatest street-level hero.", "Amazing Fantasy #15", "0785124635"), "isbn": "9780785124634"},
        "sm-brand-new-day": {**run_obj("sm-brand-new-day", "peter-parker", "Spider-Man: Brand New Day", "Various", "2008–09", "Amazing Spider-Man #546–564 and related", "Modern Age", "None — screen companion", "Peter starts over after One More Day — the comic era that shares a name with the 2026 film.", "Spider-Man: Brand New Day Vol. 1", "0785133243"), "isbn": "9780785133247"},
        "sm-kraven": {**run_obj("sm-kraven", "peter-parker", "Kraven's Last Hunt", "J.M. DeMatteis & Mike Zeck", "1987", "Web of Spider-Man #31–32, Amazing Spider-Man #293–294, Spectacular Spider-Man #131–132", "Modern Age", "None", "Kraven buries Spider-Man and steals his life — one of the darkest, best Spidey sagas ever.", "Kraven's Last Hunt", "0785134533"), "isbn": "9780785134534"},
        "sm-superior": {**run_obj("sm-superior", "peter-parker", "Superior Spider-Man Vol. 1", "Dan Slott & Ryan Stegman", "2013", "Superior Spider-Man #1–5", "Modern Age", "None", "Otto Octavius in Peter's body — a Superior Spider-Man who will save the city his way.", "Superior Spider-Man Vol. 1", "0785167172"), "isbn": "9780785167174"},
        "sm-miles-ultimate": {**run_obj("sm-miles-ultimate", "miles-morales", "Miles Morales: Ultimate Spider-Man Vol. 1", "Brian Michael Bendis & Sara Pichelli", "2011–12", "Ultimate Comics Spider-Man #1–6", "Ultimate", "None — Miles entry", "Miles Morales steps into the costume after Ultimate Peter's death.", "Miles Morales: Ultimate Spider-Man Vol. 1", "0785165501"), "isbn": "9780785165507"},
        "sm-miles-616": {**run_obj("sm-miles-616", "miles-morales", "Spider-Man: Miles Morales Vol. 1", "Brian Michael Bendis & Sara Pichelli", "2015–16", "Spider-Man #1–5", "Modern Age", "Ultimate Miles", "Miles arrives in the mainstream Marvel Universe and proves there is room for two Spider-Men.", "Spider-Man: Miles Morales Vol. 1", "0785199678"), "isbn": "9780785199670"},
        "sm-ultimate-vol1": {**run_obj("sm-ultimate-vol1", "ultimate-peter", "Ultimate Spider-Man Vol. 1", "Brian Michael Bendis & Mark Bagley", "2000–01", "Ultimate Spider-Man #1–7", "Ultimate", "None", "A modern retelling of Peter's origin that redefined Spider-Man for a generation.", "Ultimate Spider-Man Vol. 1", "0781020747"), "isbn": "9780781020749"},
        "sm-spider-gwen": {**run_obj("sm-spider-gwen", "spider-gwen", "Spider-Gwen Vol. 1", "Jason Latour & Robbi Rodriguez", "2015", "Spider-Gwen #1–5", "Modern Age", "None", "Gwen Stacy as Spider-Woman — band practice, dimension hops, and a life Peter never lived.", "Spider-Gwen Vol. 1", "0785196776"), "isbn": "9780785196778"},
        "sm-2099": {**run_obj("sm-2099", "spider-2099", "Spider-Man 2099 Classic Vol. 1", "Peter David & Rick Leonardi", "1992–93", "Spider-Man 2099 #1–10", "2099", "None", "Miguel O'Hara's debut as the future Spider-Man in Nueva York.", "Spider-Man 2099 Classic Vol. 1", "0785162405"), "isbn": "9780785162407"},
    },
    "home_runs": ["sm-origin", "sm-brand-new-day", "sm-kraven", "sm-miles-ultimate", "sm-ultimate-vol1", "sm-superior", "sm-spider-gwen", "sm-2099"],
    "profile": {
        "wikipedia": "https://en.wikipedia.org/wiki/Spider-Man",
        "lead": "With great power comes great responsibility — and a lot of unpaid rent.",
        "summary": "Spider-Man is Marvel's flagship street-level hero, created by Stan Lee and Steve Ditko in Amazing Fantasy #15 (1962). Most often Peter Parker, the mantle also belongs to Miles Morales, Gwen Stacy, Miguel O'Hara, and a multiverse of others — the through-line for Brand New Day on screen and decades of comics.",
        "facts": [
            {"label": "Alter ego", "value": "Peter Parker (primary)"},
            {"label": "First appearance", "value": "Amazing Fantasy #15 (1962)"},
            {"label": "Created by", "value": "Stan Lee & Steve Ditko"},
            {"label": "Publisher", "value": "Marvel Comics"},
            {"label": "Powers", "value": "Wall-crawling, spider-sense, super-strength"},
            {"label": "Base of operations", "value": "New York City"},
            {"label": "Notable allies", "value": "Mary Jane, Aunt May, the Avengers"},
            {"label": "Notable foes", "value": "Green Goblin, Doctor Octopus, Venom"},
        ],
    },
    "screen": [
        {"group": "Live-action films", "items": [
            screen_item("sm-bnd", "Spider-Man: Brand New Day", "MCU · Tom Holland", "https://en.wikipedia.org/wiki/Spider-Man:_Brand_New_Day", "https://www.imdb.com/title/tt22084616/", year="2026"),
            screen_item("sm-nwh", "Spider-Man: No Way Home", "MCU · multiverse", "https://en.wikipedia.org/wiki/Spider-Man:_No_Way_Home", "https://www.imdb.com/title/tt10872600/", year="2021"),
            screen_item("sm-itsv", "Spider-Man: Into the Spider-Verse", "Sony Animation", "https://en.wikipedia.org/wiki/Spider-Man:_Into_the_Spider-Verse", "https://www.imdb.com/title/tt4633694/", year="2018"),
        ]},
        {"group": "Animated series", "items": [
            screen_item("sm-tas", "Spider-Man: The Animated Series", "1990s classic", "https://en.wikipedia.org/wiki/Spider-Man_(1994_TV_series)", "https://www.imdb.com/title/tt0112175/", years="1994–1998"),
        ]},
    ],
    "themes": {
        "peter-parker": (229, 57, 53), "miles-morales": (40, 40, 40), "ultimate-peter": (200, 40, 40),
        "spider-gwen": (240, 120, 180), "spider-2099": (0, 150, 160), "mcu-peter": (180, 30, 30),
    },
    "issues": {},
}


SCREEN_PACKS = [SUPERGIRL, CLAYFACE, VISION, XMEN, AVENGERS, SPIDERMAN]
