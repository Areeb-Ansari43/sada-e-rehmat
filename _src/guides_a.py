"""Guides, part 1: the rites. Facts checked November 2026; dates are projections
until the moon is sighted. Keep the religious content to widely agreed practice
and point readers to a scholar for madhab-specific rulings."""


def dua(when, ar, tr, en, src=""):
    s = f'<span class="src">{src}</span>' if src else ""
    return (f'<div class="dua"><span class="when">{when}</span><div class="ar" lang="ar">{ar}</div>'
            f'<div class="tr">{tr}</div><div class="en">{en}</div>{s}</div>')


def callout(title, text, warn=False):
    return f'<div class="callout{" warn" if warn else ""}"><b>{title}</b><p>{text}</p></div>'


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def table(head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


TALBIYAH = dua(
    "The Talbiyah · from the moment you enter Ihram",
    "لَبَّيْكَ اللَّهُمَّ لَبَّيْكَ، لَبَّيْكَ لَا شَرِيكَ لَكَ لَبَّيْكَ، إِنَّ الْحَمْدَ وَالنِّعْمَةَ لَكَ وَالْمُلْكَ، لَا شَرِيكَ لَكَ",
    "Labbayk Allāhumma labbayk, labbayka lā sharīka laka labbayk, inna l-ḥamda wa n-niʿmata laka wa l-mulk, lā sharīka lak.",
    "Here I am, O Allah, here I am. Here I am, You have no partner, here I am. All praise and blessings are Yours, and all sovereignty. You have no partner.",
    "Ṣaḥīḥ al-Bukhārī and Ṣaḥīḥ Muslim")

RABBANA = dua(
    "Between the Yemeni Corner and the Black Stone",
    "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ",
    "Rabbanā ātinā fi d-dunyā ḥasanatan wa fi l-ākhirati ḥasanatan wa qinā ʿadhāba n-nār.",
    "Our Lord, give us good in this world and good in the Hereafter, and protect us from the punishment of the Fire.",
    "Qur'an 2:201 · Sunan Abī Dāwūd")

SAFA = dua(
    "On Safa and on Marwa, facing the Kaaba",
    "اللَّهُ أَكْبَرُ، اللَّهُ أَكْبَرُ، اللَّهُ أَكْبَرُ. لَا إِلَٰهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ، لَا إِلَٰهَ إِلَّا اللَّهُ وَحْدَهُ، أَنْجَزَ وَعْدَهُ، وَنَصَرَ عَبْدَهُ، وَهَزَمَ الْأَحْزَابَ وَحْدَهُ",
    "Allāhu akbar (×3). Lā ilāha illa-llāhu waḥdahū lā sharīka lah, lahu l-mulku wa lahu l-ḥamdu wa huwa ʿalā kulli shay'in qadīr. Lā ilāha illa-llāhu waḥdah, anjaza waʿdah, wa naṣara ʿabdah, wa hazama l-aḥzāba waḥdah.",
    "Allah is the Greatest. There is no god but Allah alone, without partner. His is the dominion and His is the praise, and He has power over all things. There is no god but Allah alone. He fulfilled His promise, helped His servant and defeated the confederates alone.",
    "Ṣaḥīḥ Muslim (the Prophet's ﷺ Hajj, narrated by Jābir). Repeat three times, making your own duʿā' in between.")

ARAFAH = dua(
    "The best duʿā' · the Day of Arafah",
    "لَا إِلَٰهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ، وَهُوَ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ",
    "Lā ilāha illa-llāhu waḥdahū lā sharīka lah, lahu l-mulku wa lahu l-ḥamd, wa huwa ʿalā kulli shay'in qadīr.",
    "There is no god but Allah alone, without partner. His is the dominion and His is the praise, and He has power over all things.",
    "Jāmiʿ at-Tirmidhī: “The best duʿā' is the duʿā' of the Day of Arafah.”")

MASJID = dua(
    "Entering the mosque · right foot first",
    "بِسْمِ اللَّهِ، وَالصَّلَاةُ وَالسَّلَامُ عَلَىٰ رَسُولِ اللَّهِ، اللَّهُمَّ افْتَحْ لِي أَبْوَابَ رَحْمَتِكَ",
    "Bismillāh, wa ṣ-ṣalātu wa s-salāmu ʿalā rasūli-llāh. Allāhumma-ftaḥ lī abwāba raḥmatik.",
    "In the name of Allah, and peace and blessings upon the Messenger of Allah. O Allah, open for me the doors of Your mercy.",
    "Ṣaḥīḥ Muslim · Sunan Ibn Mājah")

GUIDES_A = [
    # ------------------------------------------------------------------ UMRAH
    dict(
        slug="guide-first-umrah", cat="umrah", image="kaaba-tawaf",
        eyebrow="Umrah · step by step",
        title="How to Perform Umrah: Step-by-Step Guide for First-Timers (2026–27)",
        h1="How to perform Umrah, <em>step by step.</em>",
        desc="A clear step-by-step Umrah guide: Ihram and intention at the Miqat, Tawaf, two rak'ahs at Maqam Ibrahim, Zamzam, Sa'i and cutting the hair, with duas and common mistakes.",
        intro="Umrah has four essential acts: Ihram, Tawaf, Sa'i and cutting the hair. Most pilgrims complete it in three to five hours. Here is the whole thing, in order, with the duas and the mistakes to avoid.",
        og="Ihram · Tawaf · Sa'i · Halq — in order, with duas",
        minutes=9,
        tldr=["Umrah = <strong>Ihram → Tawaf → Sa'i → shave or trim</strong>. That's it.",
              "Make your intention <strong>before</strong> you pass the Miqat, which on most flights happens in the air.",
              "Book your Umrah time slot on the <strong>Nusuk</strong> app before you go to the Haram.",
              "Allow 3–5 hours, more in Ramadan. Go after Isha or before Fajr for lighter crowds."],
        scrolly=[
            ("Before the Miqat", "Step 1", "Prepare and enter Ihram",
             "Take a bath (ghusl), trim nails and remove unwanted hair. Men may put fragrance on the body, not the Ihram cloth. Men wear two unstitched white sheets; women wear normal modest clothing. Then, before the Miqat, make the intention: <em>Labbayk Allāhumma ʿumrah.</em>",
             ("type", "لَبَّيْكَ", "Intention · Niyyah"), ["Ghusl", "Two white sheets for men", "Intention before the Miqat"]),
            ("On the way", "Step 2", "Recite the Talbiyah",
             "From the moment you are in Ihram, repeat the Talbiyah often: men aloud, women quietly. Stop when you begin Tawaf. Keep the Ihram rules: no perfume, no cutting hair or nails, no arguments.",
             ("img", "holy-kaaba"), ["Men aloud, women softly", "Stop at the start of Tawaf"]),
            ("Masjid al-Haram", "Step 3", "Seven circuits of Tawaf",
             "Enter with your right foot. Start at the line facing the Black Stone, raise your right hand and say <em>Allāhu akbar</em>. Walk seven circuits anticlockwise, keeping the Kaaba on your left. Men uncover the right shoulder (idṭibāʿ) for this Tawaf and walk briskly in the first three circuits if space allows.",
             ("img", "kaaba-tawaf"), ["7 circuits", "Anticlockwise", "Start and end at the Black Stone"]),
            ("Behind the Maqam", "Step 4", "Pray two rak'ahs",
             "Cover the right shoulder again. Pray two short rak'ahs behind Maqam Ibrahim if you can, or anywhere in the mosque if it is crowded. It is sunnah to recite Surah al-Kāfirūn in the first and al-Ikhlāṣ in the second.",
             ("img", "maqam-ibrahim"), ["2 rak'ahs", "Anywhere if crowded"]),
            ("Zamzam", "Step 5", "Drink Zamzam water",
             "Drink your fill of Zamzam, facing the Qibla if you can, and make duʿā'. The Prophet ﷺ said Zamzam is for whatever it is drunk for. Coolers are placed throughout the mosque.",
             ("img", "zamzam"), ["Any cooler in the Haram", "Make duʿā'"]),
            ("Safa to Marwa", "Step 6", "Seven laps of Sa'i",
             "Climb Safa, face the Kaaba and praise Allah. Walk to Marwa: that is one lap. Marwa back to Safa is the second. You finish on Marwa after the seventh. Men jog lightly between the green lights. Wudu is recommended but not required for Sa'i.",
             ("img", "safa-marwa"), ["7 laps", "Start Safa, end Marwa", "About 3.2 km"]),
            ("Umrah complete", "Step 7", "Shave or trim the hair",
             "Men shave the head (best) or trim evenly all over. Women gather their hair and cut a fingertip's length from the ends. Your Umrah is complete and the Ihram restrictions are lifted.",
             ("type", "تَقَبَّلَ اللَّهُ", "May Allah accept it"), ["Men: shave or trim", "Women: a fingertip's length"]),
        ],
        sections=[
            ("before", "Before you travel", f"""
<p>Umrah can be performed at any time of year except the days of Hajj. Before you fly, you need a visa that allows Umrah (the Saudi tourist eVisa or an Umrah visa), a valid <strong>meningitis ACWY</strong> certificate issued at least 10 days before arrival, and an Umrah permit booked through the official <strong>Nusuk</strong> app. Read our <a href="guide-umrah-visa.html">Umrah visa guide</a> and <a href="guide-health.html">health guide</a> for the details.</p>
{checks(["Passport valid for at least six months", "Visa that permits Umrah", "ACWY certificate (10+ days before arrival)", "Nusuk account and Umrah permit", "Ihram clothing in your hand luggage", "Unscented soap, deodorant and lip balm"])}
"""),
            ("miqat", "Ihram and the Miqat", f"""
<p>The Miqat is the boundary you must not cross without being in Ihram. If you are flying straight to Jeddah from the UK or Pakistan, you will cross it in the air, usually 20 to 40 minutes before landing. Jeddah itself is inside the boundary, so you cannot wait to change at the airport.</p>
<p>The simplest approach: shower and change into Ihram at home or the departure airport, then make the intention when the crew announce the Miqat, or a little before. Our <a href="guide-miqat.html">Miqat guide</a> explains each route, including what to do if you are going to Madinah first.</p>
{TALBIYAH}
"""),
            ("tawaf", "Tawaf, done properly", f"""
{MASJID}
<p>Tawaf starts and ends in line with the Black Stone, marked by a green light on the wall opposite. Point your right hand towards it and say <em>Allāhu akbar</em> at the start of each circuit; do not push to kiss it. There is no fixed duʿā' for each circuit, so pray in any language from the heart. Between the Yemeni Corner and the Black Stone, it is sunnah to recite:</p>
{RABBANA}
<p>If you lose count, go with the lower number. If the prayer starts during Tawaf, join the congregation and continue from where you stopped. You need wudu for Tawaf.</p>
"""),
            ("sai", "Sa'i between Safa and Marwa", f"""
<p>As you approach Safa, recite <em>Inna ṣ-ṣafā wa l-marwata min shaʿā'iri-llāh</em> (Qur'an 2:158) and say, <em>“I begin with what Allah began with.”</em> Then face the Kaaba and say:</p>
{SAFA}
<p>The full Sa'i is about 3.2 km on smooth marble. The upper floors and the roof are usually less crowded, and electric carts and wheelchairs are available for elderly pilgrims.</p>
"""),
            ("mistakes", "Common mistakes to avoid", f"""
{checks(["Crossing the Miqat without Ihram, then changing in Jeddah", "Starting Tawaf away from the Black Stone line", "Keeping the right shoulder uncovered outside Tawaf, including in prayer", "Counting Safa → Marwa → Safa as one lap (it's two)", "Cutting only a few strands of hair", "Taking selfies or blocking the flow in the Mataf"])}
{callout("A note on differences of opinion", "The schools of Islamic law differ on some details, such as how much hair must be trimmed or the penalty for a missed act. If you follow a particular madhab, check these points with a scholar you trust before travelling.")}
"""),
        ],
        faqs=[
            ("How long does Umrah take?", "Tawaf usually takes 45–90 minutes and Sa'i 45–75 minutes, depending on crowds and your pace. Allow three to five hours in total, longer in Ramadan and on Fridays."),
            ("Can I perform Umrah more than once on a trip?", "Yes. Pilgrims staying in Makkah exit to the nearest boundary, usually Masjid Aisha at Tan'eem, enter Ihram there and perform another Umrah. Each needs its own Nusuk permit."),
            ("Do I need wudu for Sa'i?", "It is recommended but not required according to most scholars. Wudu is required for Tawaf."),
            ("Do I need a Nusuk permit for Umrah?", "Yes. Since 2022 every pilgrim needs an Umrah permit with a time slot from the Nusuk app. The permit is free."),
        ],
        sources=[("Nusuk — official Hajj and Umrah platform", "https://www.nusuk.sa/"),
                 ("Ministry of Hajj and Umrah, Saudi Arabia", "https://www.haj.gov.sa/en")],
        related=["guide-ihram", "guide-duas", "guide-miqat"],
    ),

    # ------------------------------------------------------------------ HAJJ
    dict(
        slug="guide-hajj-step-by-step", cat="hajj", image="arafat",
        eyebrow="Hajj · day by day",
        title="How to Perform Hajj: Day-by-Day Guide with Hajj 2027 Dates",
        h1="Hajj, <em>day by day.</em>",
        desc="A day-by-day guide to Hajj al-Tamattu' with projected Hajj 2027 dates: Umrah, the Day of Tarwiyah in Mina, Arafat on 15 May 2027, Muzdalifah, the Jamarat, Tawaf al-Ifadah and the farewell Tawaf.",
        intro="Most pilgrims from the UK and Pakistan perform Hajj al-Tamattu': an Umrah first, then the rites of Hajj from the 8th to the 12th or 13th of Dhul Hijjah. Projected dates for 1448 AH are below. They can move by a day once the moon is sighted.",
        og="8–13 Dhul Hijjah · Arafat on Saturday 15 May 2027",
        minutes=11,
        tldr=["Projected Hajj 2027: <strong>8 Dhul Hijjah = Friday 14 May</strong>, <strong>Arafat = Saturday 15 May</strong>, Eid al-Adha = Sunday 16 May.",
              "The pillars of Hajj are Ihram, standing at Arafat, Tawaf al-Ifadah and Sa'i. Missing Arafat means missing Hajj.",
              "Pilgrims on Tamattu' must offer a sacrifice (hady). Qurbani is <strong>not</strong> included in most package prices, including ours.",
              "Expect 15–20 km of walking across the five days, in heat of around 40°C in May."],
        scrolly=[
            ("Before 8 Dhul Hijjah", "Arrival", "Perform your Umrah",
             "On Tamattu', you arrive in Makkah in Ihram, perform Umrah, then come out of Ihram and wait for the days of Hajj. If you travel to Madinah first, you put on Ihram before leaving Madinah for Makkah.",
             ("img", "kaaba-tawaf"), ["Umrah first", "Exit Ihram until the 8th"]),
            ("Friday 14 May 2027 · 8 Dhul Hijjah", "Day 1", "Tarwiyah: Ihram again, then Mina",
             "Bathe, put on Ihram from your hotel or Aziziya and make the intention for Hajj: <em>Labbayk Allāhumma ḥajjan.</em> Travel to Mina and pray Dhuhr, Asr, Maghrib, Isha and the next Fajr there, shortening the four-unit prayers without combining them.",
             ("img", "mina-tents"), ["Ihram for Hajj", "Five prayers in Mina", "Talbiyah throughout"]),
            ("Saturday 15 May 2027 · 9 Dhul Hijjah", "Day 2", "Arafat: the heart of Hajj",
             "After sunrise, move to Arafat. Pray Dhuhr and Asr shortened and combined at the time of Dhuhr, then spend the afternoon in duʿā', facing the Qibla. Make sure you are within the boundaries of Arafat. Stay until sunset; this day is Hajj.",
             ("img", "arafat"), ["Dhuhr + Asr combined", "Stay until sunset", "Make duʿā'"]),
            ("Night of 9–10 Dhul Hijjah", "Night", "Muzdalifah under the open sky",
             "After sunset, travel to Muzdalifah. Pray Maghrib and Isha combined on arrival, rest, and collect pebbles (49 or 70, the size of a chickpea). Pray Fajr there and make duʿā' until it is light. The elderly, women and those caring for them may leave after midnight.",
             ("img", "muzdalifah"), ["Maghrib + Isha combined", "Collect pebbles", "Fajr in Muzdalifah"]),
            ("Sunday 16 May 2027 · Eid al-Adha", "Day 3", "The busiest day of Hajj",
             "Stone Jamarat al-Aqabah with seven pebbles, saying <em>Allāhu akbar</em> with each, and stop the Talbiyah. Then the sacrifice, shaving or trimming, and Tawaf al-Ifadah with Sa'i. After shaving you may leave Ihram clothing. The order can vary if needed.",
             ("img", "jamarat"), ["7 pebbles at Aqabah", "Sacrifice", "Shave or trim", "Tawaf al-Ifadah + Sa'i"]),
            ("17–18 May 2027 · 11–12 Dhul Hijjah", "Days 4–5", "The days of Tashreeq",
             "Spend the nights in Mina. Each day after midday, stone all three Jamarat in order, small, middle and large, with seven pebbles each. If you leave on the 12th, you must leave Mina before sunset; otherwise stay and stone again on the 13th.",
             ("img", "mina-tents"), ["21 pebbles a day", "After midday", "Leave Mina before sunset on the 12th"]),
            ("Before you leave Makkah", "Farewell", "Tawaf al-Wada'",
             "The last thing you do in Makkah is the farewell Tawaf: seven circuits, no Sa'i. Women who are menstruating are excused from it. Then your Hajj is complete.",
             ("type", "حَجٌّ مَبْرُورٌ", "Ḥajj mabrūr · an accepted Hajj"), ["Last act in Makkah", "No Sa'i"]),
        ],
        sections=[
            ("dates", "Hajj 2027 at a glance", f"""
<p>Hajj 1448 AH falls in mid-May 2027. Saudi Arabia follows the Umm al-Qura calendar and confirms Dhul Hijjah by moon sighting, so treat these as projections that may move by one day.</p>
{table(["Date (projected)", "Hijri", "Where", "What happens"], [
    ["Fri 7 May 2027", "1 Dhul Hijjah", "—", "First of the ten best days"],
    ["Fri 14 May 2027", "8 Dhul Hijjah", "Mina", "Ihram for Hajj, Day of Tarwiyah"],
    ["Sat 15 May 2027", "9 Dhul Hijjah", "Arafat → Muzdalifah", "Day of Arafah; night in Muzdalifah"],
    ["Sun 16 May 2027", "10 Dhul Hijjah", "Mina, Makkah", "Eid al-Adha; Aqabah, sacrifice, shave, Ifadah"],
    ["Mon 17 May 2027", "11 Dhul Hijjah", "Mina", "Stone all three Jamarat"],
    ["Tue 18 May 2027", "12 Dhul Hijjah", "Mina", "Stone all three; early departure before sunset"],
    ["Wed 19 May 2027", "13 Dhul Hijjah", "Mina", "Optional third day of stoning"],
])}
<p>All of our <a href="packages.html">Hajj 2027 journeys</a> follow this timetable, with the five days of Hajj on 14–18 May.</p>
"""),
            ("pillars", "Pillars, obligations and sunnahs", f"""
<p>It helps to know what is essential and what is recommended, because on a crowded day you may need to prioritise.</p>
<div class="two-col">
<div><h3>Pillars (arkān)</h3><ul><li>Ihram with intention</li><li>Standing at Arafat</li><li>Tawaf al-Ifadah</li><li>Sa'i</li></ul><p style="font-size:15px;margin:10px 0 0">Missing a pillar invalidates Hajj or must be made up.</p></div>
<div><h3>Obligations (wājibāt)</h3><ul><li>Ihram from the Miqat</li><li>Staying at Arafat until sunset</li><li>The night in Muzdalifah</li><li>Nights in Mina on the 11th and 12th</li><li>Stoning the Jamarat</li><li>Shaving or trimming</li><li>Farewell Tawaf</li></ul></div>
</div>
{callout("Different schools, different lists", "The four schools of Islamic law classify a few acts differently, and the penalty for missing an obligation is usually a sacrifice. Ask your group's scholar before Hajj so you know what applies to you.")}
"""),
            ("arafah", "Making the most of Arafat", f"""
<p>The afternoon of Arafat is the most important time of your Hajj. Rest in the morning so you have energy for the hours after Dhuhr. Write a list of the people and the things you want to pray for before you leave home.</p>
{ARAFAH}
{checks(["Check you are inside the Arafat boundary signs", "Keep a small umbrella and a water bottle with you", "Stay in your tent or shade at the hottest time", "Avoid climbing Jabal al-Rahmah in the heat; it is not required", "Do not leave before sunset"])}
"""),
            ("jamarat", "Stoning the Jamarat safely", """
<p>The Jamarat Bridge has several levels and one-way flows, which has made stoning far safer than it used to be. Your Maktab will usually be given set times; follow them. Pebbles should hit the basin around the pillar, not necessarily the pillar itself.</p>
<ul><li>Stone after midday on the 11th, 12th and 13th, in the order: small, middle, large.</li><li>After the small and middle Jamarat, step aside, face the Qibla and make a long duʿā'.</li><li>The elderly or unwell may appoint someone to stone on their behalf, after that person has stoned for themselves.</li></ul>
"""),
            ("health", "Staying well during Hajj", """
<p>May temperatures in Makkah regularly reach 40–45°C. Heat illness is the biggest risk to pilgrims. Drink before you feel thirsty, use oral rehydration salts, walk at night where you can, and rest whenever you are told to. Break in your sandals well before the trip. See our <a href="guide-health.html">health guide</a>.</p>
"""),
        ],
        faqs=[
            ("When is Hajj 2027?", "Hajj 1448 AH is projected for 14–19 May 2027, with the Day of Arafah on Saturday 15 May and Eid al-Adha on Sunday 16 May. Dates are confirmed by moon sighting and can move by one day."),
            ("What is the difference between Hajj and Umrah?", "Hajj is obligatory once in a lifetime for those able, happens only on 8–13 Dhul Hijjah and includes Arafat, Muzdalifah, Mina and the Jamarat. Umrah is shorter, can be performed almost any time of year and consists of Ihram, Tawaf, Sa'i and cutting the hair."),
            ("How many pebbles do I need?", "49 if you leave Mina on the 12th (7 on the 10th, 21 on the 11th, 21 on the 12th), or 70 if you stay for the 13th. Many pilgrims collect a few spare."),
            ("Is Qurbani included in Hajj packages?", "Usually not. Pilgrims on Hajj al-Tamattu' must offer a sacrifice. You can buy an official Adahi voucher in advance, and your group will arrange it on the 10th. Qurbani is not included in Sada-e-Rehmat's Hajj 2027 prices."),
        ],
        sources=[("Ministry of Hajj and Umrah, Saudi Arabia", "https://www.haj.gov.sa/en"),
                 ("Umm al-Qura calendar (Makkah Live)", "https://makkahlive.net/en/tools/islamic-calendar")],
        related=["guide-types-of-hajj", "guide-ihram", "guide-hajj-pakistan"],
    ),

    # ------------------------------------------------------------------ IHRAM
    dict(
        slug="guide-ihram", cat="umrah", image="holy-kaaba",
        eyebrow="Rules of Ihram",
        title="Ihram Rules for Men and Women: What Is Allowed and What Is Not",
        h1="Ihram rules, <em>made simple.</em>",
        desc="What Ihram is, how men and women dress for it, the actions that are forbidden in Ihram, what is allowed (showers, belts, umbrellas, unscented soap) and what to do if you make a mistake.",
        intro="Ihram is both what you wear and the sacred state you enter with your intention. Once you say the Talbiyah, a few everyday things become forbidden until your Umrah or Hajj is complete.",
        og="What men and women wear, and what changes once you say Labbayk",
        minutes=7,
        tldr=["Ihram begins with the <strong>intention and Talbiyah</strong>, not with putting on the clothes.",
              "Men: two unstitched white sheets, head uncovered, sandals that leave the ankles bare.",
              "Women: ordinary modest clothing of any colour; face and hands uncovered (no niqab or gloves).",
              "Forbidden for all: perfume, cutting hair or nails, intimacy, hunting, arguing."],
        scrolly=None,
        sections=[
            ("what", "What Ihram is", """
<p>Ihram is the state a pilgrim enters before Umrah or Hajj. It starts with a sincere intention (niyyah) and the Talbiyah, made before crossing the Miqat. The white sheets men wear are also called Ihram, but wearing them without the intention does not put you in Ihram, so you can change at home and make the intention later on the plane.</p>
<p>It is sunnah to bathe beforehand, trim nails and remove unwanted hair, and for men to apply fragrance to the body (not the clothing). Many pilgrims pray two rak'ahs before making the intention if it is not a disliked time.</p>
"""),
            ("dress", "What men and women wear", """
<div class="two-col">
<div><h3>Men</h3><ul><li>Two seamless white sheets: the izar around the waist, the rida' over the shoulders</li><li>Head and face uncovered</li><li>Sandals or flip-flops that leave the ankles and top of the foot bare</li><li>No underwear, socks or stitched, fitted clothes</li></ul></div>
<div><h3>Women</h3><ul><li>Any loose, modest clothing, in any colour (white is common, not required)</li><li>Hijab as usual</li><li>Face and hands uncovered: no niqab or gloves</li><li>Normal shoes and socks are fine</li></ul></div>
</div>
"""),
            ("rules", "Forbidden and allowed in Ihram", """
<div class="two-col">
<div class="dont"><h3>Not allowed</h3><ul><li>Perfume or scented products on body or clothes</li><li>Cutting or removing hair or nails</li><li>Marital relations, intimacy, or a marriage contract</li><li>Hunting land animals</li><li>Men: covering the head, fitted clothing</li><li>Women: niqab and gloves</li><li>Arguing, swearing or obscene talk</li></ul></div>
<div class="do"><h3>Allowed</h3><ul><li>Showering, with unscented soap and shampoo</li><li>A belt or money pouch around the waist</li><li>Watch, glasses, ring, hearing aid</li><li>Umbrella or shade (just not a cap on the head for men)</li><li>Changing into a clean set of Ihram</li><li>Medicines, plasters and unscented creams</li><li>Washing and scratching gently, even if a hair falls by accident</li></ul></div>
</div>
"""),
            ("mistakes", "If you make a mistake", """
<p>Anything done through genuine forgetfulness or ignorance is generally forgiven; stop as soon as you remember. Deliberately doing a forbidden act usually requires a compensation (fidyah): fasting three days, feeding six poor people, or sacrificing a sheep. Intimacy before the end of the pillars is the most serious breach.</p>
<div class="callout"><b>Ask before you act</b><p>Penalties depend on the act and the school of law you follow. Ask your group scholar rather than guessing, especially for anything involving hair, intimacy or leaving the Miqat without Ihram.</p></div>
"""),
            ("kit", "Ihram packing list", """
<ul class="checks"><li>Two sets of Ihram (men), so one can dry</li><li>Ihram belt with pockets</li><li>Unscented soap, shampoo, deodorant and wet wipes</li><li>Vaseline or anti-chafe balm for the thighs</li><li>Comfortable sandals, already worn in</li><li>Safety pins (to fasten, not to stitch)</li></ul>
"""),
        ],
        faqs=[
            ("Can I wear a belt in Ihram?", "Yes. Men can wear a belt or money pouch to hold the izar and keep valuables, and women can wear whatever they normally wear."),
            ("Can I use soap while in Ihram?", "Yes, as long as it is unscented. The same applies to shampoo, deodorant and moisturiser."),
            ("Can men wear underwear under Ihram?", "No. Men should not wear any stitched, fitted garment, including underwear and vests. An anti-chafe balm helps."),
            ("Can women wear any colour?", "Yes. Women's Ihram is ordinary modest clothing and does not have to be white."),
        ],
        sources=[("Ministry of Hajj and Umrah, Saudi Arabia", "https://www.haj.gov.sa/en")],
        related=["guide-miqat", "guide-first-umrah", "guide-women"],
    ),

    # ------------------------------------------------------------------ MIQAT
    dict(
        slug="guide-miqat", cat="umrah", image="muzdalifah",
        eyebrow="Ihram on a flight",
        title="Miqat on a Flight: When to Wear Ihram from the UK or Pakistan",
        h1="Where is the Miqat <em>on my flight?</em>",
        desc="The five Miqat points, why you can't enter Ihram in Jeddah, and when to put on Ihram flying from the UK or Pakistan, or when travelling to Madinah first.",
        intro="Jeddah is inside the Miqat boundary, so pilgrims flying straight there must be in Ihram before landing. Here is how to get it right from the UK or Pakistan, and what changes if you go to Madinah first.",
        og="Jeddah is inside the boundary — be ready before you land",
        minutes=6,
        tldr=["You must be in Ihram <strong>before</strong> you cross the Miqat. Jeddah is inside it.",
              "Flying to Jeddah: change at home or the airport, make the intention when the crew announce the Miqat, or a little before.",
              "Flying to Madinah first: no Ihram on the flight. Enter Ihram at Dhul Hulayfah before travelling to Makkah.",
              "On the Haramain train from Madinah, be in Ihram <strong>before boarding</strong>."],
        scrolly=None,
        sections=[
            ("five", "The five Miqat points", f"""
<p>The Prophet ﷺ set five boundaries around the Haram. Anyone intending Umrah or Hajj must enter Ihram at, or before, the one they pass or come level with.</p>
{table(["Miqat", "Today", "Distance to Makkah", "Who uses it"], [
    ["Dhul Hulayfah", "Abyar Ali, Madinah", "≈ 450 km", "Pilgrims leaving Madinah for Makkah"],
    ["Al-Juhfah", "Near Rabigh", "≈ 185 km", "From the north-west: Syria, Egypt, North Africa, many European routes"],
    ["Qarn al-Manazil", "As-Sayl al-Kabir", "≈ 80 km", "From the east: Najd, Riyadh, the Gulf, many routes from South Asia"],
    ["Yalamlam", "As-Sa'diyyah", "≈ 100 km", "From the south: Yemen and some routes from South Asia"],
    ["Dhat 'Irq", "Al-Dariba", "≈ 95 km", "From the north-east: Iraq"],
])}
"""),
            ("uk", "Flying from the UK", f"""
<p>Flights from London, Manchester or Birmingham to Jeddah usually approach from the north or north-west and pass the Miqat line roughly 20–40 minutes before landing. Your exact path depends on the airline and the day, so:</p>
<ol class="steps-list"><li>Bathe and change into Ihram at home, at the airport, or on a connecting stop.</li><li>Board in Ihram, or carry it in your hand luggage and change on board before the Miqat (aircraft toilets are small, so changing earlier is easier).</li><li>Listen for the crew's Miqat announcement, which Saudia and many other airlines make. If yours doesn't, make the intention about an hour before landing to be safe.</li><li>Make the intention and begin the Talbiyah.</li></ol>
{callout("Connecting via Riyadh, Dubai or Doha?", "Your route into Jeddah changes. You will usually cross Qarn al-Manazil or Yalamlam from the east. The rule is the same: be in Ihram before you come level with it.")}
"""),
            ("pk", "Flying from Pakistan", """
<p>Flights from Islamabad, Lahore, Karachi or Peshawar to Jeddah cross the Arabian Peninsula from the east and pass a Miqat (commonly Qarn al-Manazil or Yalamlam, depending on route) shortly before landing. Most pilgrims from Pakistan put on Ihram at home or at the airport before departure, and make the intention on the plane when announced.</p>
"""),
            ("madinah", "Going to Madinah first", """
<p>If your journey starts in Madinah, for example one of our <a href="packages.html">Madinah-first Hajj 2027 journeys</a>, you do not enter Ihram on the flight. Madinah is outside the Miqat.</p>
<p>When you leave Madinah for Makkah, you pass Dhul Hulayfah. Many groups stop at Masjid Dhul Hulayfah (Abyar Ali) on the way. If you are taking the Haramain high-speed train, the line passes the Miqat soon after leaving, so bathe, change into Ihram at your hotel, and make the intention before or as the train departs.</p>
"""),
            ("missed", "If you pass the Miqat without Ihram", """
<p>If you realise you have crossed it, the safest option is to go back to a Miqat and enter Ihram there. If you enter Ihram after passing it, most scholars say a sacrifice (dam) is due. Ask your group scholar as soon as you land.</p>
"""),
        ],
        faqs=[
            ("Can I put on Ihram in Jeddah?", "Not if you are flying in from abroad for Umrah or Hajj. Jeddah lies inside the Miqat boundary, so you must enter Ihram before landing. Residents of Jeddah enter Ihram from home."),
            ("Can I wear Ihram for the whole flight?", "Yes. You can wear the clothing from departure and only make the intention near the Miqat. The rules of Ihram begin with the intention."),
            ("Where is the Miqat on the Haramain train from Madinah?", "The train passes Dhul Hulayfah shortly after leaving Madinah, so be in Ihram before you board and make the intention as it departs."),
        ],
        sources=[("Islamic Fiqh Academy and fatwa summaries on Ihram on aircraft (IslamQA 4635)", "https://islamqa.info/en/answers/4635")],
        related=["guide-ihram", "guide-first-umrah", "guide-madinah"],
    ),

    # ------------------------------------------------------------------ DUAS
    dict(
        slug="guide-duas", cat="umrah", image="maqam-ibrahim",
        eyebrow="Duas & dhikr",
        title="Duas for Umrah and Hajj: Arabic, Transliteration and Meaning",
        h1="Duas for Umrah <em>and Hajj.</em>",
        desc="The authentic duas for Umrah and Hajj in Arabic with transliteration and English: the Talbiyah, entering the Haram, Tawaf, Safa and Marwa, Zamzam, Arafat, the Jamarat and visiting the Prophet ﷺ.",
        intro="There are only a handful of fixed words in Umrah and Hajj. Everything else is your own duʿā', in any language. Here are the ones that come from the Sunnah, in the order you will need them.",
        og="Talbiyah · Tawaf · Safa · Arafat — Arabic, transliteration, meaning",
        minutes=6,
        tldr=["There is <strong>no fixed duʿā' for each circuit</strong> of Tawaf. Booklets that assign one are not from the Sunnah.",
              "Learn the Talbiyah and the Safa dhikr by heart before you travel.",
              "Write your personal duʿā' list at home, for Arafat, Multazam and Zamzam."],
        scrolly=None,
        sections=[
            ("ihram", "Entering Ihram", TALBIYAH + dua("Intention for Umrah", "لَبَّيْكَ اللَّهُمَّ عُمْرَةً", "Labbayk Allāhumma ʿumrah.", "Here I am, O Allah, for Umrah.") + dua("Intention for Hajj (on 8 Dhul Hijjah for Tamattu')", "لَبَّيْكَ اللَّهُمَّ حَجًّا", "Labbayk Allāhumma ḥajjan.", "Here I am, O Allah, for Hajj.")),
            ("haram", "At the Haram and in Tawaf", MASJID + dua("Facing the Black Stone at the start of each circuit", "اللَّهُ أَكْبَرُ", "Allāhu akbar.", "Allah is the Greatest.", "Ṣaḥīḥ al-Bukhārī. Many add “Bismillāh” before it, as Ibn ʿUmar did.") + RABBANA + dua("Approaching Maqam Ibrahim", "وَاتَّخِذُوا مِن مَّقَامِ إِبْرَاهِيمَ مُصَلًّى", "Wa-ttakhidhū min maqāmi Ibrāhīma muṣallā.", "And take the station of Ibrahim as a place of prayer.", "Qur'an 2:125 · Ṣaḥīḥ Muslim")),
            ("zamzam", "Drinking Zamzam", """
<p>The Prophet ﷺ said: <em>“The water of Zamzam is for whatever it is drunk for.”</em> (Sunan Ibn Mājah). Drink it facing the Qibla, in three sips, and ask Allah for whatever you need. A duʿā' reported from Ibn ʿAbbās is:</p>
""" + dua("Drinking Zamzam (reported from Ibn ʿAbbās)", "اللَّهُمَّ إِنِّي أَسْأَلُكَ عِلْمًا نَافِعًا، وَرِزْقًا وَاسِعًا، وَشِفَاءً مِنْ كُلِّ دَاءٍ", "Allāhumma innī as'aluka ʿilman nāfiʿā, wa rizqan wāsiʿā, wa shifā'an min kulli dā'.", "O Allah, I ask You for beneficial knowledge, abundant provision and healing from every illness.", "Sunan ad-Dāraquṭnī")),
            ("sai", "On Safa and Marwa", dua("Approaching Safa", "إِنَّ الصَّفَا وَالْمَرْوَةَ مِن شَعَائِرِ اللَّهِ · أَبْدَأُ بِمَا بَدَأَ اللَّهُ بِهِ", "Inna ṣ-ṣafā wa l-marwata min shaʿā'iri-llāh. Abda'u bimā bada'a-llāhu bih.", "Indeed Safa and Marwa are among the symbols of Allah. I begin with what Allah began with.", "Qur'an 2:158 · Ṣaḥīḥ Muslim") + SAFA),
            ("hajj", "During Hajj", ARAFAH + dua("At Mash'ar al-Haram, Muzdalifah, after Fajr", "اللَّهُ أَكْبَرُ، لَا إِلَٰهَ إِلَّا اللَّهُ", "Allāhu akbar, lā ilāha illa-llāh.", "Allah is the Greatest; there is no god but Allah. The Prophet ﷺ faced the Qibla and made duʿā', takbīr and tahlīl until it was very light.", "Ṣaḥīḥ Muslim") + dua("With each pebble at the Jamarat", "اللَّهُ أَكْبَرُ", "Allāhu akbar.", "Allah is the Greatest.", "Ṣaḥīḥ al-Bukhārī")),
            ("madinah", "Visiting the Prophet ﷺ", dua("At the grave of the Prophet ﷺ, then Abu Bakr and Umar", "السَّلَامُ عَلَيْكَ يَا رَسُولَ اللَّهِ · السَّلَامُ عَلَيْكَ يَا أَبَا بَكْرٍ · السَّلَامُ عَلَيْكَ يَا عُمَرُ", "As-salāmu ʿalayka yā Rasūla-llāh. As-salāmu ʿalayka yā Abā Bakr. As-salāmu ʿalayka yā ʿUmar.", "Peace be upon you, O Messenger of Allah. Peace be upon you, O Abu Bakr. Peace be upon you, O Umar.", "Reported from Ibn ʿUmar") + "<p>Then step away, face the Qibla and make your own duʿā'. See our <a href=\"guide-madinah.html\">Madinah guide</a> for the Rawdah permit.</p>"),
        ],
        faqs=[
            ("Is there a special dua for each circuit of Tawaf?", "No. Apart from Allāhu akbar at the Black Stone and Rabbanā ātinā between the Yemeni Corner and the Black Stone, there is no fixed duʿā' for each circuit. Make your own duʿā' and dhikr, or recite Qur'an."),
            ("Can I make dua in English or Urdu?", "Yes. Personal duʿā' can be made in any language. Only the Qur'an recitation in prayer must be in Arabic."),
        ],
        sources=[("Sunnah.com — hadith collections", "https://sunnah.com/")],
        related=["guide-first-umrah", "guide-hajj-step-by-step", "guide-madinah"],
    ),

    # ------------------------------------------------------------------ TYPES
    dict(
        slug="guide-types-of-hajj", cat="hajj", image="jamarat",
        eyebrow="Tamattu', Qiran, Ifrad",
        title="Types of Hajj Explained: Tamattu', Qiran and Ifrad",
        h1="Three ways <em>to perform Hajj.</em>",
        desc="Tamattu', Qiran and Ifrad compared: when you enter Ihram, whether a sacrifice is required, and which type most pilgrims from the UK and Pakistan perform.",
        intro="Every Hajj includes the same rites from the 8th to the 13th of Dhul Hijjah. What differs is whether you also perform an Umrah, and whether you stay in Ihram in between.",
        og="Which one you'll perform, and why most pilgrims choose Tamattu'",
        minutes=4,
        tldr=["<strong>Tamattu'</strong>: Umrah, leave Ihram, Hajj Ihram on the 8th. Sacrifice required. Most common.",
              "<strong>Qiran</strong>: Umrah and Hajj together in one Ihram. Sacrifice required.",
              "<strong>Ifrad</strong>: Hajj only. No sacrifice required."],
        scrolly=None,
        sections=[
            ("compare", "The three types side by side", f"""
{table(["", "Tamattu'", "Qiran", "Ifrad"], [
    ["Intention at Miqat", "Umrah", "Umrah and Hajj", "Hajj"],
    ["Umrah performed?", "Yes, before Hajj", "Yes, combined", "No"],
    ["Leave Ihram between?", "Yes", "No", "No"],
    ["Sacrifice (hady)", "Required", "Required", "Not required"],
    ["Best for", "Most international pilgrims", "Those who bring their sacrifice", "Those arriving close to the 8th"],
])}
"""),
            ("tamattu", "Why most pilgrims perform Tamattu'", """
<p>Pilgrims from the UK and Pakistan usually arrive days or weeks before the 8th of Dhul Hijjah. Tamattu' lets them perform Umrah on arrival, then live normally, out of Ihram, until Hajj begins. The Prophet ﷺ encouraged his Companions who had not brought sacrificial animals to make their Hajj Tamattu'.</p>
<p>All of our <a href="packages.html">Hajj 2027 journeys</a> are planned for Tamattu'. Remember that the sacrifice is an obligation of Tamattu' and is not included in the package price.</p>
"""),
            ("hady", "The sacrifice, if you can't afford it", """
<p>A pilgrim on Tamattu' or Qiran who cannot afford the sacrifice fasts ten days instead: three during Hajj and seven after returning home (Qur'an 2:196).</p>
"""),
        ],
        faqs=[
            ("Which type of Hajj is best?", "Scholars differ. Many consider Tamattu' best for those who did not bring an animal, following the Prophet's ﷺ instruction to his Companions. All three are valid."),
            ("When are the months of Hajj?", "Shawwal, Dhul Qa'dah and the first ten days of Dhul Hijjah. For Tamattu', the Umrah must be performed within these months."),
        ],
        sources=[("Ministry of Hajj and Umrah, Saudi Arabia", "https://www.haj.gov.sa/en")],
        related=["guide-hajj-step-by-step", "guide-hajj-pakistan", "guide-hajj-uk"],
    ),
]
