"""Guides, part 2: planning, travel, health and practical. Facts as of November 2026."""
from guides_a import callout, checks, table

GUIDES_B = [
    # ------------------------------------------------------------------ VISA
    dict(
        slug="guide-umrah-visa", cat="planning", image="safa-marwa",
        eyebrow="Visas · 2026–27 season",
        title="Umrah Visa from the UK and Pakistan (2026–27): eVisa & Nusuk",
        h1="Umrah visas, <em>explained.</em>",
        desc="Which visa to use for Umrah from the UK or Pakistan in 2026–27: the Saudi eVisa, Umrah visa, free Nusuk permit, ACWY certificate and season dates.",
        intro="Getting into Saudi Arabia and being allowed into the Haram for Umrah are two separate things. You need a visa that permits Umrah, and a free Umrah permit from the Nusuk app.",
        og="eVisa or Umrah visa, plus your free Nusuk permit",
        minutes=6,
        tldr=["<strong>British passport</strong>: the Saudi tourist eVisa allows Umrah outside the Hajj season. It is usually issued online within a few days.",
              "<strong>Pakistani passport</strong>: you normally need an Umrah visa through an approved Umrah company, unless you hold a valid UK, US or Schengen visa.",
              "Every pilgrim also needs a <strong>Nusuk Umrah permit</strong> with a time slot. It is free.",
              "Tourist and Umrah visas cannot be used to perform Hajj."],
        scrolly=None,
        sections=[
            ("routes", "Which visa do I need?", f"""
{table(["Your passport", "Usual route", "Notes"], [
    ["British (and most EU, US, Canadian)", "Saudi tourist eVisa, or Umrah visa via a provider", "Eligibility depends on your passport, not where you live. The eVisa is typically one-year, multiple-entry, with stays of up to 90 days."],
    ["Pakistani, living in Pakistan", "Umrah visa through a licensed Umrah company", "Your operator applies through the Saudi system and includes accommodation and transport."],
    ["Pakistani, living in the UK", "Umrah visa via a provider; eVisa may be possible", "Holders of a valid UK, US or Schengen visa or residence have been eligible for the Saudi eVisa. Check visa.visitsaudi.com with your exact documents."],
])}
{callout("Rules change each season", "Saudi Arabia updates visa products often. In July 2026 it announced a 90-day, multiple-entry Umrah visa valid for a year, linked to buying a service package from an approved Nusuk provider. Always check the official portal before you book flights.", warn=True)}
"""),
            ("nusuk", "The Nusuk permit", """
<p>Nusuk is the official Saudi platform for Hajj and Umrah. Once you have a visa, download the app, register with your passport and visa details, and book a date and time for your Umrah. The permit is free. Show it when asked at the entrances to the Mataf. You also use Nusuk to book the Rawdah in Madinah (see our <a href="guide-madinah.html">Madinah guide</a>).</p>
"""),
            ("season", "Umrah season dates", """
<p>Umrah visas are not issued for travel during Hajj. For the 1448 AH season, visa issuance reportedly resumed on 31 May 2026, with 9 March 2027 reported as the last date for issuing an Umrah visa before Hajj 2027. Plan to complete Umrah and leave well before the Hajj period begins.</p>
"""),
            ("docs", "What you will need", checks([
                "Passport valid for at least six months from arrival",
                "A recent passport-style photo (digital)",
                "Meningitis ACWY certificate, issued at least 10 days before arrival",
                "Confirmed accommodation and return or onward ticket",
                "Health insurance (included in the eVisa and Umrah visa fee)",
                "Polio vaccination evidence if you are travelling from Pakistan",
            ])),
        ],
        faqs=[
            ("Can I do Umrah on a tourist visa?", "Yes. Holders of the Saudi tourist eVisa can perform Umrah outside the Hajj season, as long as they book a permit on Nusuk."),
            ("How long does an Umrah visa take?", "The eVisa is often issued within 24–72 hours. Umrah visas through providers usually take a few working days; allow longer before Ramadan."),
            ("Can women get an Umrah visa without a mahram?", "Yes. Saudi Arabia no longer requires women to travel with a mahram for Umrah. See our guide for women."),
        ],
        sources=[("Visit Saudi eVisa portal", "https://visa.visitsaudi.com/"),
                 ("Nusuk", "https://www.nusuk.sa/"),
                 ("UK FCDO: Saudi Arabia pilgrimage advice", "https://www.gov.uk/foreign-travel-advice/saudi-arabia/pilgrimage")],
        related=["guide-documents", "guide-best-time-umrah", "guide-women"],
    ),

    # ------------------------------------------------------------------ HAJJ UK
    dict(
        slug="guide-hajj-uk", cat="hajj", image="holy-kaaba",
        eyebrow="Hajj from the UK",
        title="How to Go to Hajj from the UK: Nusuk Hajj Booking Explained",
        h1="Hajj from the UK, <em>the official way.</em>",
        desc="How UK residents book Hajj through the official Nusuk Hajj platform: registration, choosing a package from an approved provider, payment, vaccines, ATOL protection and avoiding Hajj scams.",
        intro="Since 2023, pilgrims living in the UK, Europe, the Americas and Australia book Hajj through one official platform: Nusuk Hajj. The UK government is clear that it is the only way to book a Hajj place.",
        og="One official route: register, choose, pay on Nusuk Hajj",
        minutes=6,
        tldr=["UK residents can <strong>only</strong> book Hajj through Nusuk Hajj (hajj.nusuk.sa).",
              "Places are limited and packages sell out quickly. Register as soon as registration opens.",
              "Anyone offering a Hajj visa outside Nusuk is breaking the rules. Performing Hajj without a permit brings fines and deportation.",
              "You need a meningitis ACWY certificate, issued at least 10 days before arrival."],
        scrolly=[
            ("Step 1", "Register", "Create your Nusuk Hajj account",
             "Sign up at hajj.nusuk.sa with your email and passport details. Add everyone who will travel with you, including your mahram if required.",
             ("img", "holy-kaaba"), ["hajj.nusuk.sa", "One account per pilgrim"]),
            ("Step 2", "Verify", "Complete your profile and eligibility",
             "Upload your passport, photo and proof of residence. Nusuk checks eligibility. Priority is generally given to people who have not performed Hajj before.",
             ("img", "maqam-ibrahim"), ["Passport", "Residence proof"]),
            ("Step 3", "Choose", "Pick a package from an approved provider",
             "When packages open, compare camps (Mina categories), hotels, durations and prices from licensed service providers. Popular packages can sell out within hours.",
             ("img", "mina-tents"), ["Compare Mina category", "Check hotels and dates"]),
            ("Step 4", "Pay", "Pay and receive your Hajj visa",
             "Pay within the time limit shown. Your visa and Hajj permit are issued through the platform once payment is confirmed and your vaccinations are recorded.",
             ("img", "kaaba-tawaf"), ["Pay on Nusuk only", "Visa issued digitally"]),
            ("Step 5", "Prepare", "Book flights and get ready",
             "Check whether flights are included. If you book flights separately, make sure they match your package dates. Start walking practice and read up on the rites.",
             ("img", "arafat"), ["Flights", "Vaccines", "Learn the rites"]),
        ],
        sections=[
            ("who", "Who uses Nusuk Hajj?", """
<p>Nusuk Hajj serves Muslims resident in countries without a national Hajj mission, including the UK, Europe, the United States, Canada and Australia. Pilgrims living in Pakistan go through Pakistan's own scheme instead (see <a href="guide-hajj-pakistan.html">Hajj from Pakistan</a>).</p>
"""),
            ("protect", "Protect yourself", f"""
{checks(["Pay only through the Nusuk Hajj platform", "Be wary of anyone promising a guaranteed Hajj visa or a 'VIP' route", "Never travel for Hajj on a tourist or visit visa", "Keep copies of every confirmation and receipt", "Report suspected fraud to Action Fraud (0300 123 2040)"])}
{callout("The FCDO warning", "The UK government warns that organised crime groups target people planning Hajj and Umrah, and that you can only book a Hajj place on Nusuk Hajj.", warn=True)}
"""),
            ("help", "How we can help", """
<p>Even when you book through Nusuk, you still need to prepare: vaccines, documents, the rites, packing and what to expect in Mina. Our team in Feltham can talk you through it, and can arrange Umrah and Madinah stays around your Hajj dates. <a href="contact.html">Get in touch</a>.</p>
"""),
        ],
        faqs=[
            ("Can I book Hajj through a UK travel agent?", "Not directly. UK residents book Hajj places on Nusuk Hajj. A UK agent can help you prepare and can arrange travel around it, but the Hajj place and package must be booked on the platform."),
            ("When does Nusuk Hajj registration open?", "It usually opens several months before Hajj. For Hajj 2027 (mid-May 2027), watch hajj.nusuk.sa and the FCDO pilgrimage page for announcements."),
            ("What happens if I perform Hajj without a permit?", "Saudi authorities enforce Hajj permits strictly. People found performing Hajj without one face heavy fines, deportation and a ban on re-entry."),
        ],
        sources=[("Nusuk Hajj", "https://hajj.nusuk.sa/"),
                 ("UK FCDO: Saudi Arabia pilgrimage advice", "https://www.gov.uk/foreign-travel-advice/saudi-arabia/pilgrimage"),
                 ("Action Fraud", "https://www.actionfraud.police.uk/")],
        related=["guide-hajj-step-by-step", "guide-safety", "guide-health"],
    ),

    # ------------------------------------------------------------------ HAJJ PK
    dict(
        slug="guide-hajj-pakistan", cat="hajj", image="mina-tents",
        eyebrow="Hajj from Pakistan · 2027",
        title="Hajj 2027 from Pakistan: Government vs Private Scheme Explained",
        h1="Hajj 2027 <em>from Pakistan.</em>",
        desc="Hajj 2027 from Pakistan: the 179,210 quota, government vs private scheme, mandatory registration, passport validity and paying only through official channels.",
        intro="Pakistan's first multi-year Hajj policy covers 2027 to 2030. For Hajj 2027, Saudi Arabia has allocated Pakistan 179,210 places, split between the government scheme and authorised private Hajj organisers.",
        og="179,210 places · government or private scheme",
        minutes=6,
        tldr=["Quota for Hajj 2027: <strong>179,210</strong>: 107,526 government and 71,684 private.",
              "Registration with the Ministry of Religious Affairs was <strong>mandatory</strong>; it opened on 22 June 2026.",
              "Your passport must be valid until at least <strong>16 November 2027</strong>.",
              "Pay for private packages only through the official Hajj portal or app."],
        scrolly=None,
        sections=[
            ("schemes", "Government or private scheme?", f"""
{table(["", "Government scheme", "Private scheme"], [
    ["Places for 2027", "107,526", "71,684"],
    ["Organised by", "Ministry of Religious Affairs", "Authorised Hajj Group Organisers (HGOs)"],
    ["Selection", "Balloting if over-subscribed", "First come, first served within each organiser's quota"],
    ["Packages", "Set by the ministry", "Choice of packages, e.g. Maktab category, hotels, length"],
    ["Price range", "Announced by the ministry", "Approximately Rs 1.4 million to Rs 3.75 million (basic packages)"],
])}
<p>Private packages give you more choice: Maktab A tents in Zone 1, closer hotels, shorter or longer stays and Madinah before or after Hajj. Our <a href="packages.html">Hajj 2027 collections</a> are built on Maktab A.</p>
"""),
            ("dates", "Key dates and rules", f"""
{checks(["Registration opened 22 June 2026 and was required before applying", "Passports must be valid until 16 November 2027", "The ministry set 20 November 2026 as the deadline to select and pay for a private package", "Unused private quota can be reallocated by the ministry", "Payments for private packages go through the official Hajj portal or app"])}
{callout("Check before you pay", "Deadlines can be extended or changed. Confirm every date on the Ministry of Religious Affairs website or the official Pak Hajj app before you make a payment.", warn=True)}
"""),
            ("choose", "Choosing a private package", """
<p>Compare packages on the things that change your experience most: the <strong>Maktab category and zone</strong> in Mina (closer to the Jamarat means less walking), whether you stay in <strong>Aziziya or a Makkah hotel</strong> before Hajj, the <strong>hotels by name</strong>, the meal plan, room sharing, whether <strong>Madinah is before or after</strong> Hajj, and what is excluded (often airfare and Qurbani). Our <a href="guide-choosing.html">package comparison guide</a> has a full checklist.</p>
"""),
        ],
        faqs=[
            ("What is the Hajj quota for Pakistan in 2027?", "179,210 places: 107,526 for the government scheme and 71,684 for private Hajj organisers."),
            ("Is airfare included in private Hajj packages?", "It depends on the package. Many private packages, including ours, are priced without airfare, so you can choose your flights."),
            ("Can I go for Hajj 2027 without registering?", "No. The Ministry of Religious Affairs made registration mandatory for Hajj 2027 applications."),
        ],
        sources=[("Ministry of Religious Affairs and Interfaith Harmony, Pakistan", "https://www.mora.gov.pk/"),
                 ("Arab News Pakistan: Hajj 2027 private package deadline", "https://www.arabnews.pk/pakistan/pakistan-sets-nov-20-deadline-to-select-and-pay-for-private-hajj-packages-3000305")],
        related=["guide-choosing", "guide-hajj-step-by-step", "guide-types-of-hajj"],
    ),

    # ------------------------------------------------------------------ WOMEN
    dict(
        slug="guide-women", cat="umrah", image="madinah",
        eyebrow="For women pilgrims",
        title="Umrah and Hajj for Women: Mahram Rules, Ihram and Periods",
        h1="Umrah and Hajj <em>for women.</em>",
        desc="A practical guide for women performing Umrah or Hajj: current mahram rules, what to wear in Ihram, what to do if your period starts, prayer areas, the Rawdah, and tips for staying comfortable.",
        intro="Women make up almost half of all pilgrims. The rites are the same, with a few differences in dress and practice, and some practical planning makes a real difference.",
        og="Mahram rules, Ihram, periods and comfort, answered",
        minutes=6,
        tldr=["Saudi Arabia <strong>no longer requires a mahram</strong> for women performing Umrah. Hajj routes may still set conditions.",
              "Women's Ihram is ordinary modest clothing. No niqab or gloves.",
              "A woman on her period can do every rite <strong>except Tawaf</strong>, and is excused from the farewell Tawaf.",
              "Women do not jog in Tawaf or Sa'i, and trim a fingertip's length of hair."],
        scrolly=None,
        sections=[
            ("mahram", "Do I need a mahram?", """
<p>Saudi Arabia removed the mahram requirement for women travelling for Umrah, and women can now apply for visas independently. For Hajj, rules depend on your route: national Hajj authorities and Nusuk Hajj may require women without a mahram to travel in an organised group. Separately, many scholars hold that a mahram is still required religiously, while others permit travel in a safe, trusted group. Discuss it with a scholar you trust.</p>
"""),
            ("ihram", "Ihram for women", """
<ul><li>Wear loose, modest clothing in any colour. Comfortable abayas with deep pockets are popular.</li><li>Keep the face and hands uncovered in Ihram. Many scholars allow lowering a cloth over the face, without a fitted niqab, when near non-mahram men.</li><li>Normal shoes, socks and underwear are fine.</li><li>Avoid scented products after making the intention.</li></ul>
"""),
            ("periods", "If your period starts", """
<p>Menstruation does not stop you from entering Ihram or doing most rites. The Prophet ﷺ told Aisha (may Allah be pleased with her), when her period began during Hajj: <em>“Do everything the pilgrim does, except Tawaf around the House until you are pure.”</em> (Ṣaḥīḥ al-Bukhārī)</p>
<ul><li>You can enter Ihram, stay at Arafat and Muzdalifah, stone the Jamarat and make duʿā' and dhikr.</li><li>Wait to perform Tawaf (and, for Umrah, the Sa'i that follows it) until your period ends and you have bathed.</li><li>The farewell Tawaf is waived for a woman on her period.</li><li>Some women take medication to delay their period; speak to your GP well in advance.</li></ul>
<div class="callout"><b>Short trips and Tawaf al-Ifadah</b><p>If your flight home is fixed and your period continues past it, this is a matter to discuss with a scholar before you travel. Arranging a little flexibility in your return date helps.</p></div>
"""),
            ("practical", "Practical tips", """
<ul class="checks"><li>Women's prayer areas are separate. Agree a meeting point with your group by gate number.</li><li>Rawdah visits for women have their own time slots, booked on Nusuk.</li><li>Carry a small bag that fits under an abaya for your phone, permit and water.</li><li>Pack sanitary products and pain relief in your hand luggage.</li><li>Upper floors of the Haram are often calmer for Tawaf, though the circuit is longer.</li></ul>
"""),
        ],
        faqs=[
            ("Can a woman go for Umrah alone?", "Under current Saudi rules, yes. Women can obtain an Umrah visa without a mahram. Many choose to travel with a trusted group, and scholars differ on the religious ruling."),
            ("Can a woman perform Sa'i during her period?", "Most scholars say Sa'i does not require purity, but the Sa'i of Umrah must follow a valid Tawaf, so in practice she waits until she can perform Tawaf."),
        ],
        sources=[("Ṣaḥīḥ al-Bukhārī, Book of Menstruation", "https://sunnah.com/bukhari:305"),
                 ("Nusuk", "https://www.nusuk.sa/")],
        related=["guide-ihram", "guide-first-umrah", "guide-madinah"],
    ),

    # ------------------------------------------------------------------ MADINAH
    dict(
        slug="guide-madinah", cat="umrah", image="madinah",
        eyebrow="Madinah",
        title="Visiting Madinah: Rawdah Permit, Etiquette and Ziyarat Places",
        h1="Madinah, <em>the city of the Prophet ﷺ.</em>",
        desc="How to visit Masjid an-Nabawi: booking the Rawdah on Nusuk, greeting the Prophet ﷺ, women's visiting times, and the Ziyarat places of Madinah, from Masjid Quba to Uhud and al-Baqi.",
        intro="Visiting Madinah is not part of Umrah or Hajj, but most pilgrims would not travel without it. Here is how to plan your time, book the Rawdah and visit the places of the Prophet's ﷺ life.",
        og="Book the Rawdah on Nusuk · Quba · Uhud · al-Baqi",
        minutes=6,
        tldr=["You need a free <strong>Rawdah permit</strong> from the Nusuk app. Slots open in advance and go quickly.",
              "Men and women have separate Rawdah times.",
              "Praying two rak'ahs in <strong>Masjid Quba</strong> carries the reward of an Umrah (Sunan Ibn Mājah).",
              "There is no Ihram for Madinah; it is outside the Miqat."],
        scrolly=[
            ("Masjid an-Nabawi", "01", "The Prophet's Mosque ﷺ",
             "A prayer in Masjid an-Nabawi is worth more than a thousand prayers elsewhere, except Masjid al-Haram (Bukhari and Muslim). Enter with the right foot and the duʿā' for entering a mosque.",
             ("img", "madinah"), ["1,000× reward", "Open 24 hours"]),
            ("Riyāḍ al-Jannah", "02", "The Rawdah",
             "The area between the Prophet's ﷺ house and his minbar is “a garden from the gardens of Paradise.” Book a slot on Nusuk, arrive early at the gate shown, and pray two rak'ahs calmly.",
             ("type", "رَوْضَةٌ مِنْ رِيَاضِ الْجَنَّةِ", "A garden of Paradise"), ["Nusuk permit", "Separate times for women"]),
            ("Masjid Quba", "03", "The first mosque in Islam",
             "About 3.5 km south of the Prophet's Mosque. The Prophet ﷺ visited it every Saturday. Making wudu at your hotel and praying two rak'ahs in Quba carries the reward of an Umrah.",
             ("type", "قُبَاء", "Masjid Quba"), ["Reward of Umrah", "Go on a Saturday morning"]),
            ("Uhud", "04", "The mountain that loves us",
             "Site of the Battle of Uhud. Visit the graves of the martyrs, including Hamza (may Allah be pleased with him), and the archers' hill (Jabal al-Rumāt).",
             ("type", "أُحُد", "Jabal Uhud"), ["Martyrs of Uhud", "Archers' hill"]),
            ("Jannat al-Baqi", "05", "The cemetery of Madinah",
             "Next to the Prophet's Mosque, where many of his family and Companions are buried. Usually open to men after Fajr and Asr. Greet the people of the graves and pray for them.",
             ("type", "الْبَقِيع", "Jannat al-Baqi"), ["After Fajr and Asr", "Greet and pray for them"]),
        ],
        sections=[
            ("rawdah", "Booking the Rawdah on Nusuk", """
<ol class="steps-list"><li>Open the Nusuk app and log in with the account linked to your visa.</li><li>Choose the Rawdah permit (men or women).</li><li>Pick a date and time. Slots are released in advance and fill quickly; check regularly, and use the waitlist if offered.</li><li>Save the permit and arrive at the stated gate 20–30 minutes early.</li></ol>
<p>Permits are free. Children usually need their own permit, and very young children may not be admitted. Rules on how often you can book have changed in the past, so check the app for current limits.</p>
"""),
            ("salam", "Greeting the Prophet ﷺ", """
<p>After praying, walk calmly along the front of the mosque past the Prophet's ﷺ grave. Say <em>As-salāmu ʿalayka yā Rasūla-llāh</em>, then step right and greet Abu Bakr, then Umar (may Allah be pleased with them). Keep your voice low, keep moving, and face the Qibla when you make duʿā'.</p>
"""),
            ("more", "More places in Madinah", """
<ul><li><strong>Masjid al-Qiblatain</strong>, where the Qibla changed from Jerusalem to Makkah.</li><li><strong>The Seven Mosques (al-Masājid as-Sab'ah)</strong>, near the site of the Battle of the Trench.</li><li><strong>The date market</strong>, for Ajwa and other Madinah dates.</li><li><strong>The Dar al-Madinah Museum</strong>, on the history of the city.</li></ul>
"""),
        ],
        faqs=[
            ("Do I need a permit for the Rawdah?", "Yes. A free permit with a time slot is booked through the Nusuk app."),
            ("How many days should I spend in Madinah?", "Three to five days is common. It gives time for the Rawdah, Quba, Uhud and plenty of prayers in the mosque. Our Hajj 2027 journeys include two to four nights."),
            ("Do I need Ihram in Madinah?", "No. Madinah is outside the Miqat. You enter Ihram when you leave Madinah for Makkah, at Dhul Hulayfah."),
        ],
        sources=[("Nusuk", "https://www.nusuk.sa/"),
                 ("Ministry of Hajj and Umrah: Rawdah permit service", "https://haj.gov.sa/en/E-Services/Permit-to-Visit-Al-Rawdah-Al-Sharifiyah-for-Men?sc_lang=en")],
        related=["guide-ziyarat-makkah", "guide-miqat", "guide-duas"],
    ),

    # ------------------------------------------------------------------ ZIYARAT MAKKAH
    dict(
        slug="guide-ziyarat-makkah", cat="umrah", image="jamarat",
        eyebrow="Ziyarat in Makkah",
        title="Ziyarat in Makkah: Historic Places to Visit Around the Haram",
        h1="Ziyarat <em>in Makkah.</em>",
        desc="Historic places to visit in Makkah: the Cave of Hira, Jabal Thawr, Jannat al-Mu'alla, Masjid Aisha at Tan'eem, Arafat, Mina and the Kiswa museum.",
        intro="A Ziyarat tour is a chance to stand where the story of Islam began. None of these visits is part of the rites, so plan them around your prayers in the Haram, not instead of them.",
        og="Hira · Thawr · al-Mu'alla · Tan'eem · Arafat",
        minutes=5,
        tldr=["Most tours take <strong>three to four hours</strong> by coach, early morning.",
              "The climb to the Cave of Hira takes about an hour each way and is steep.",
              "Masjid Aisha (Tan'eem) is where pilgrims in Makkah enter Ihram for another Umrah."],
        scrolly=None,
        sections=[
            ("places", "Places to visit", f"""
{table(["Place", "Why it matters", "Tips"], [
    ["Jabal al-Nour & Cave of Hira", "Where the first revelation came to the Prophet ﷺ", "≈ 640 m high; climb before sunrise; take water"],
    ["Jabal Thawr", "The cave where the Prophet ﷺ and Abu Bakr hid during the Hijrah", "Harder climb than Hira; most view it from below"],
    ["Jannat al-Mu'alla", "Cemetery where Khadijah (may Allah be pleased with her) is buried", "Close to the Haram"],
    ["Masjid Aisha, Tan'eem", "Nearest point outside the Haram boundary", "The Miqat for a second Umrah from Makkah"],
    ["Arafat & Jabal al-Rahmah", "Site of the Prophet's ﷺ farewell sermon", "Visit outside Hajj to understand the layout"],
    ["Muzdalifah & Mina", "The sites of Hajj", "Mina's tents are empty most of the year"],
    ["Kiswa factory & Two Holy Mosques museum", "How the Kaaba's cover is made; history of the mosques", "Check opening times before you go"],
])}
"""),
            ("etiquette", "Etiquette", """
<p>Scholars caution against rituals at these sites that have no basis in the Sunnah, such as rubbing walls, tying cloth or praying towards the caves. Visit to learn and reflect, send salam on the Prophet ﷺ and pray for the believers.</p>
"""),
        ],
        faqs=[
            ("Is Ziyarat part of Umrah?", "No. Umrah is Ihram, Tawaf, Sa'i and cutting the hair. Ziyarat visits are optional."),
            ("Can I do another Umrah from Makkah?", "Yes. Go to Masjid Aisha at Tan'eem (or another point outside the Haram boundary), enter Ihram there and book a new permit on Nusuk."),
        ],
        sources=[("Ministry of Hajj and Umrah, Saudi Arabia", "https://www.haj.gov.sa/en")],
        related=["guide-madinah", "guide-first-umrah", "guide-best-time-umrah"],
    ),

    # ------------------------------------------------------------------ BEST TIME
    dict(
        slug="guide-best-time-umrah", cat="planning", image="zamzam",
        eyebrow="When to go",
        title="Best Time for Umrah in 2026–27: Weather, Crowds, Ramadan and Prices",
        h1="The best time <em>for Umrah.</em>",
        desc="When to perform Umrah from the UK or Pakistan: month-by-month weather in Makkah, Ramadan 2027 dates, school holidays, crowds, prices and the Hajj-season cut-off for the 2026–27 season.",
        intro="Umrah has no wrong month, but the experience changes a lot with the season. Here's how weather, crowds and price shift through the year, and the dates that matter for 2026–27.",
        og="Weather, crowds, Ramadan 2027 and price, month by month",
        minutes=5,
        tldr=["<strong>Coolest and calmest</strong>: late November to early February, outside school holidays.",
              "<strong>Ramadan 2027</strong> is expected to begin around <strong>8 February 2027</strong>, with Eid al-Fitr around 9–10 March. Umrah in Ramadan carries great reward, and the highest prices.",
              "Umrah visas stop being issued before Hajj; 9 March 2027 was reported as the last issue date this season.",
              "Summer (June–September) is very hot, but often cheapest."],
        scrolly=None,
        sections=[
            ("months", "Month by month", f"""
{table(["When", "Makkah weather", "Crowds", "Price"], [
    ["Jun – Sep 2026", "Very hot, 40–45°C", "Lower, rising in school holidays", "£ – ££"],
    ["Oct – Nov", "Hot, easing to low 30s°C", "Moderate", "££"],
    ["Dec – Jan", "Pleasant, 25–31°C by day", "High at Christmas and New Year", "££ – £££"],
    ["Early Feb 2027", "Pleasant", "Building before Ramadan", "££"],
    ["Ramadan, ≈ 8 Feb – 9 Mar 2027", "Mild", "Very high, peak in the last ten nights", "£££ – ££££"],
    ["After 9 Mar 2027", "Warming", "Umrah visas close for Hajj season", "—"],
])}
"""),
            ("ramadan", "Umrah in Ramadan", """
<p>The Prophet ﷺ said that Umrah in Ramadan is equal to Hajj in reward (Bukhari and Muslim). It is also the busiest time of the year: book hotels and Nusuk permits early, expect Tawaf to take far longer, and plan around Taraweeh and Qiyam. In 2027, Ramadan overlaps the UK February half-term, which pushes prices up further.</p>
"""),
            ("tips", "Getting the timing right", """
<ul class="checks"><li>Avoid Fridays and the first and last days of school holidays if you want quieter Tawaf</li><li>Perform Tawaf after Isha or between Fajr and sunrise for lighter crowds</li><li>Leave room for Madinah: three days or more</li><li>Book your Nusuk permit as soon as your visa is issued</li></ul>
"""),
        ],
        faqs=[
            ("When is the cheapest time for Umrah?", "Usually the hot summer months, outside UK school holidays, and the weeks just after the Umrah season reopens after Hajj."),
            ("When is Ramadan 2027?", "Ramadan 1448 is expected to begin around 8 February 2027, with Eid al-Fitr on about 9 or 10 March 2027, depending on moon sighting."),
        ],
        sources=[("Gulf News: Ramadan 2027 expected dates", "https://gulfnews.com/uae/ramadan/when-is-ramadan-2027-the-expected-date-moon-sighting-and-eid-explained-1.500630523"),
                 ("Wego: Umrah 1448 season dates", "https://blog.wego.com/umrah-application/")],
        related=["guide-umrah-visa", "guide-packing", "guide-first-umrah"],
    ),

    # ------------------------------------------------------------------ PACKING
    dict(
        slug="guide-packing", cat="planning", image="mina-tents",
        eyebrow="Packing checklist",
        title="Umrah and Hajj Packing List: The Complete Checklist",
        h1="What to pack <em>for Umrah and Hajj.</em>",
        desc="A complete Umrah and Hajj packing checklist: documents, Ihram, clothing, footwear, medicines, toiletries, and the extra items you need for Mina, Arafat and Muzdalifah.",
        intro="Pack light, pack for heat and crowds, and keep the essentials on you. Here's everything, grouped so you can tick it off.",
        og="The complete checklist, plus the Mina day bag",
        minutes=5,
        tldr=["Carry documents, medicines and one set of Ihram in your <strong>hand luggage</strong>.",
              "Everything for Ihram must be <strong>unscented</strong>.",
              "For Hajj, pack a separate <strong>small backpack</strong> for the five days in Mina and Arafat."],
        scrolly=None,
        sections=[
            ("docs", "Documents and money", checks(["Passport, plus photocopies and phone photos", "Visa or Hajj permit, Nusuk app logged in", "ACWY vaccine certificate", "Booking confirmations and emergency contacts", "Travel insurance details", "Bank card and some Saudi riyals in cash", "Pen for immigration and luggage tags"])),
            ("clothes", "Clothing and Ihram", checks(["Men: 2 sets of Ihram, Ihram belt, safety pins", "Women: 3–4 loose abayas, comfortable hijabs, socks", "Light cotton clothes for after Ihram", "A light jumper for air-conditioned hotels and coaches (and Madinah nights in winter)", "Prayer mat (small, foldable)"])),
            ("feet", "Footwear", checks(["Sandals for Ihram that leave the ankles bare, worn in at home", "Comfortable trainers for after Ihram", "Shoe bag (you'll carry shoes in the Haram)", "Blister plasters"])),
            ("health", "Health and toiletries", checks(["Regular medicines in original packaging, with prescription copy", "Paracetamol, antihistamine, rehydration salts, throat lozenges", "Unscented soap, shampoo, deodorant, wet wipes", "Vaseline or anti-chafe balm", "SPF sunscreen (unscented if in Ihram), lip balm", "Face masks for crowds", "Small hand sanitiser"])),
            ("hajj", "Extra for the days of Hajj", checks(["Small backpack or crossbody bag", "Light umbrella for shade", "Refillable water bottle and a spray bottle for cooling", "Pebble pouch for the Jamarat", "Phone power bank and short cable", "Earplugs and an eye mask for Mina", "Thin sleeping mat if not provided (our Muzdalifah kit includes mats and sleeping bags)"])),
            ("leave", "Leave at home", """
<ul><li>Large suitcases you can't lift alone, as lifts are crowded</li><li>Valuable jewellery</li><li>Drones and professional camera gear</li><li>Anything you'd be upset to lose in a crowd</li></ul>
"""),
        ],
        faqs=[
            ("Can I take Zamzam water home?", "Yes. Most airlines allow one 5-litre sealed Zamzam bottle per passenger, bought at the airport or approved outlets. Check your airline's rules."),
            ("Should I take a suitcase or a backpack?", "One medium suitcase plus a small backpack works best. You'll use the backpack every day in the Haram and during the days of Hajj."),
        ],
        sources=[],
        related=["guide-health", "guide-ihram", "guide-documents"],
    ),

    # ------------------------------------------------------------------ HEALTH
    dict(
        slug="guide-health", cat="health", image="zamzam",
        eyebrow="Health & vaccinations",
        title="Hajj & Umrah Vaccinations and Health: ACWY, Heat, Medicines",
        h1="Health, heat <em>and vaccinations.</em>",
        desc="Hajj and Umrah health guide: the meningitis ACWY certificate, polio for travellers from Pakistan, heat illness, medicines and symptoms to watch after you return.",
        intro="Millions of people, intense heat and long days on foot make pilgrimage physically demanding. A few weeks of preparation prevents most of the problems pilgrims run into.",
        og="ACWY certificate · heat · medicines · after you return",
        minutes=6,
        tldr=["Saudi Arabia requires a <strong>meningitis ACWY</strong> certificate issued at least <strong>10 days</strong> before arrival.",
              "Travellers from Pakistan should also carry proof of <strong>polio vaccination</strong>.",
              "Heat is the biggest danger. Drink before you're thirsty and rest in the shade.",
              "If you feel unwell with meningitis symptoms within two weeks of returning, call your GP or NHS 111 straight away."],
        scrolly=None,
        sections=[
            ("vaccines", "Vaccinations", f"""
{table(["Vaccine", "Status", "Notes"], [
    ["Meningitis ACWY", "Required", "At least 10 days before arrival. Conjugate vaccines are valid for 5 years, polysaccharide for 3. Required for everyone over one year old."],
    ["Polio", "Required for travellers from polio-affected countries, including Pakistan", "Proof of a recent dose. Check current Saudi Ministry of Health guidance."],
    ["Seasonal flu", "Recommended", "Especially for over-65s and anyone with a long-term condition."],
    ["COVID-19", "Check current guidance", "Saudi requirements have changed season to season."],
    ["Routine (MMR, tetanus)", "Recommended", "Make sure you're up to date."],
])}
<p>In the UK, the ACWY vaccine for travel is usually given at a private travel clinic or pharmacy, not free on the NHS. Book six to eight weeks before you travel.</p>
"""),
            ("heat", "Heat and hydration", """
<ul class="checks"><li>Drink water and Zamzam regularly, add oral rehydration salts on long days</li><li>Use an umbrella; men in Ihram cannot cover their heads, but shade is allowed</li><li>Walk in the early morning and at night where possible</li><li>Know the warning signs: headache, dizziness, confusion, no sweating, fainting. Get to shade and medical help</li><li>Saudi first-aid points and hospitals in Mina and Arafat treat pilgrims free of charge</li></ul>
"""),
            ("meds", "Medicines and long-term conditions", """
<p>Bring enough medicine for the whole trip plus a week, in original packaging, with a copy of your prescription. Some medicines are controlled in Saudi Arabia, including some strong painkillers and ADHD medicines, so check with the Saudi embassy before travelling. If you have diabetes, heart or kidney disease, see your GP before booking; fasting, heat and walking all affect your condition.</p>
"""),
            ("fitness", "Get fit before you go", """
<p>Expect to walk 10–15 km on many days and more during Hajj. Start walking daily six to eight weeks before you travel, in the footwear you'll wear.</p>
"""),
            ("return", "After you return", """
<div class="callout warn"><b>Watch for meningitis symptoms</b><p>UKHSA advises anyone who becomes unwell with symptoms of meningitis (fever, severe headache, stiff neck, rash, confusion) within two weeks of returning from Saudi Arabia to contact their GP or NHS 111 immediately, and say where they have travelled.</p></div>
<p>A cough that lasts weeks after Hajj is common. See a doctor if it gets worse or you have a fever.</p>
"""),
        ],
        faqs=[
            ("Is the meningitis vaccine compulsory for Umrah?", "Yes. Saudi Arabia requires a valid meningitis ACWY certificate for Hajj and Umrah, issued at least 10 days before arrival."),
            ("How long is the ACWY vaccine valid for?", "Conjugate ACWY vaccines are accepted for five years and polysaccharide vaccines for three, provided the dose was given at least 10 days before arrival."),
            ("Is the meningitis vaccine free on the NHS for Hajj?", "Generally not. Travel ACWY vaccination is usually provided privately by travel clinics and pharmacies."),
        ],
        sources=[("TravelHealthPro (NaTHNaC): Hajj and Umrah", "https://travelhealthpro.org.uk/factsheet/19/hajj-and-umrah"),
                 ("UKHSA: meningitis vaccination for pilgrims", "https://www.gov.uk/government/news/ukhsa-urges-hajj-and-umrah-pilgrims-to-get-meningitis-vaccination"),
                 ("UK FCDO: Saudi Arabia pilgrimage advice", "https://www.gov.uk/foreign-travel-advice/saudi-arabia/pilgrimage")],
        related=["guide-packing", "guide-hajj-step-by-step", "guide-women"],
    ),

    # ------------------------------------------------------------------ DOCUMENTS
    dict(
        slug="guide-documents", cat="planning", image="safa-marwa",
        eyebrow="Documents checklist",
        title="Hajj and Umrah Documents Checklist: Passport, Visa, Nusuk and More",
        h1="Your documents, <em>in order.</em>",
        desc="Every document you need for Umrah or Hajj from the UK or Pakistan: passport validity, visa, Nusuk permit, vaccine certificates, insurance, booking confirmations, and how to keep them safe.",
        intro="Most travel problems on pilgrimage start with paperwork. Gather everything early, check names match exactly, and keep copies separate from the originals.",
        og="Passport · visa · Nusuk · ACWY · insurance",
        minutes=4,
        tldr=["Passport valid for <strong>6+ months</strong> (for Pakistan's Hajj 2027 scheme: valid until 16 Nov 2027).",
              "The name on your visa, tickets and bookings must match your passport <strong>exactly</strong>.",
              "Keep digital copies in your email and paper copies apart from the originals."],
        scrolly=None,
        sections=[
            ("list", "The checklist", checks(["Passport with 6+ months validity and two blank pages", "Visa (eVisa, Umrah visa or Hajj visa)", "Nusuk account, Umrah or Hajj permit, and Rawdah permit", "Meningitis ACWY certificate (and polio if travelling from Pakistan)", "Flight tickets and hotel confirmations", "Travel insurance documents", "Emergency contact card in English and Arabic", "Your operator's 24/7 contact in Saudi Arabia", "For women under 18 or children: any guardian consent your route requires"])),
            ("children", "Travelling with children", """
<p>Each child needs their own passport, visa, vaccine certificate and Nusuk permit. Children under one are exempt from the ACWY requirement. Carry birth certificates if surnames differ from a parent's.</p>
"""),
            ("safe", "Keeping documents safe", """
<ul><li>Use a neck pouch or Ihram belt for your passport and permit on travel days.</li><li>Leave your passport in the hotel safe in Makkah and Madinah unless you need it; carry a copy and your hotel card.</li><li>Only send passport scans to your operator through a channel they've told you to use.</li></ul>
"""),
        ],
        faqs=[
            ("How much passport validity do I need for Umrah?", "At least six months from your date of arrival in Saudi Arabia."),
            ("Do I need to print my Nusuk permit?", "No, it's shown in the app, but a screenshot helps when signal is weak."),
        ],
        sources=[("UK FCDO: Saudi Arabia entry requirements", "https://www.gov.uk/foreign-travel-advice/saudi-arabia/entry-requirements")],
        related=["guide-umrah-visa", "guide-packing", "guide-safety"],
    ),

    # ------------------------------------------------------------------ CHOOSING
    dict(
        slug="guide-choosing", cat="planning", image="maqam-ibrahim",
        eyebrow="Choosing a package",
        title="How to Compare Hajj and Umrah Packages: 12 Questions to Ask",
        h1="How to compare <em>Hajj packages.</em>",
        desc="What really differs between Hajj packages: Maktab category and zone, Aziziya vs Makkah hotels, room sharing, meals, exclusions, and 12 questions to ask before paying.",
        intro="Two packages at a similar price can feel completely different on the ground. These are the questions that reveal what you're actually buying.",
        og="Maktab, hotels, rooms, meals — read past the headline price",
        minutes=5,
        tldr=["The <strong>Maktab category and zone</strong> in Mina decides how far you walk during Hajj.",
              "Ask for <strong>hotel names</strong>, not “5-star or similar”.",
              "Check what's <strong>excluded</strong>: airfare and Qurbani are common exclusions."],
        scrolly=None,
        sections=[
            ("q", "12 questions to ask", """
<ol class="steps-list">
<li><strong>Which Maktab category and zone in Mina?</strong> Category A in Zone 1 is closest to the Jamarat.</li>
<li><strong>What kind of tents?</strong> Gypsum-walled, air-conditioned tents with sofa-beds are far more comfortable than basic tents.</li>
<li><strong>Where do I stay before Hajj?</strong> Aziziya (near Mina) or a hotel by the Haram, and for how many nights?</li>
<li><strong>Which hotels exactly?</strong> Names, distance to the Haram, and whether the hotel is confirmed.</li>
<li><strong>How many people per room?</strong> Quad, triple, double, and whether Aziziya rooms are shared.</li>
<li><strong>Which meals?</strong> Full board, half board or breakfast only, in each city.</li>
<li><strong>Madinah before or after Hajj?</strong> And how do you travel between cities: coach or Haramain train?</li>
<li><strong>What's excluded?</strong> Airfare, Qurbani, visa fees, Ziyarat, insurance.</li>
<li><strong>Who supports us on the ground?</strong> Named staff, phone numbers, scholar in the group.</li>
<li><strong>What are the dates in Gregorian and Hijri?</strong> And what happens if they move by a day?</li>
<li><strong>What are the payment and cancellation terms?</strong> In writing.</li>
<li><strong>Is the operator authorised?</strong> Nusuk-approved, ministry-licensed, or ATOL protected for UK flights.</li>
</ol>
"""),
            ("ours", "How our Hajj 2027 journeys answer these", """
<p>Every Sada-e-Rehmat Hajj 2027 journey is Maktab A in Zone 1, with gypsum-walled tents, A/C marquees in Arafat, buffet meals, private buses and the Haramain train, and each lists its hotels, board and dates by name. Prices are per person, excluding airfare and Qurbani. <a href="packages.html">Compare all twelve</a>.</p>
"""),
        ],
        faqs=[
            ("What does Maktab A mean?", "Maktabs are the service categories in Mina and Arafat. Category A is the highest standard and is located in the zones closest to the Jamarat."),
            ("Is Aziziya a good place to stay?", "Aziziya is a district between Makkah and Mina. It's convenient for the days of Hajj, but further from the Haram than hotels in the central area."),
        ],
        sources=[],
        related=["guide-hajj-pakistan", "guide-safety", "guide-types-of-hajj"],
    ),

    # ------------------------------------------------------------------ SAFETY
    dict(
        slug="guide-safety", cat="planning", image="muzdalifah",
        eyebrow="Avoiding scams",
        title="Avoiding Hajj and Umrah Scams: How to Check an Operator",
        h1="Avoiding Hajj <em>and Umrah scams.</em>",
        desc="How to spot Hajj and Umrah fraud: fake Hajj visas, unofficial payments, ATOL protection for UK pilgrims, Pakistan's official portal and where to report scams.",
        intro="Every year, pilgrims lose savings to fake Hajj places and vanishing operators. A few checks before you pay protect both your money and your Hajj.",
        og="Fake Hajj visas, unofficial payments and how to check",
        minutes=4,
        tldr=["UK residents: Hajj places are sold <strong>only</strong> on Nusuk Hajj.",
              "Pakistan: pay for private Hajj packages <strong>only</strong> through the official ministry portal or app.",
              "Never travel for Hajj on a tourist or visit visa.",
              "UK Umrah packages that include flights should be <strong>ATOL protected</strong>."],
        scrolly=None,
        sections=[
            ("signs", "Warning signs", checks(["A Hajj place offered outside Nusuk or your national scheme", "Prices far below everyone else's", "Pressure to pay today, in cash or to a personal account", "No written terms, hotel names or company details", "No physical office or registered company", "“Hajj on a visit visa” or “no permit needed”"])),
            ("check", "How to check an operator", """
<ul><li><strong>UK:</strong> look up the company on Companies House, check ATOL protection on the CAA website for flight packages, and look for ABTA membership.</li><li><strong>Pakistan:</strong> check the organiser is on the Ministry of Religious Affairs' list of authorised Hajj organisers.</li><li>Ask for everything in writing: hotels, dates, room sharing, inclusions, exclusions and refund terms.</li><li>Pay by card or bank transfer to a company account, never a personal one.</li></ul>
<p>Sada-e-Rehmat Ltd is registered in England and Wales (company no. 16043621), with offices in Feltham and Rawalpindi.</p>
"""),
            ("report", "Where to report fraud", """
<ul><li>UK: Action Fraud, 0300 123 2040 or actionfraud.police.uk</li><li>Pakistan: the Ministry of Religious Affairs complaint cell and the FIA Cyber Crime Wing</li></ul>
"""),
        ],
        faqs=[
            ("Can I perform Hajj on a visit visa?", "No. Saudi Arabia only allows Hajj with an official Hajj permit, and enforces it strictly with fines, deportation and entry bans."),
            ("What is ATOL protection?", "ATOL is a UK scheme run by the Civil Aviation Authority that protects you if a travel company selling a flight-inclusive package fails."),
        ],
        sources=[("UK FCDO: Saudi Arabia pilgrimage advice", "https://www.gov.uk/foreign-travel-advice/saudi-arabia/pilgrimage"),
                 ("Action Fraud", "https://www.actionfraud.police.uk/"),
                 ("Civil Aviation Authority: ATOL", "https://www.caa.co.uk/atol-protection/")],
        related=["guide-hajj-uk", "guide-hajj-pakistan", "guide-choosing"],
    ),
]
