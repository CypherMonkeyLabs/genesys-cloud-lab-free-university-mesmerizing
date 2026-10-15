from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "ecosystem",
    "title": "Ecosystem",
    "kicker": "The map",
    "accent": 4,
    "summary": "How the tracks fit, how to read certifications, and what this lab refuses to invent.",
    "lessons": [],
}


def add(item):
    TRACK["lessons"].append(item)


add(lesson(
    "z-map", "The conversation crosses a short list of systems", "Foundation", 12,
    "Carrier, trunk or Edge, Architect, queue, agent, then the systems beside the agent.",
    [
        "A voice conversation enters through Genesys Cloud Voice or BYOC, optionally through a premises Edge, and reaches Architect. Architect transfers to a queue. ACD offers an agent who is On Queue and under utilization. Recording, quality, workforce management, speech analytics, Copilot, and a CRM sit beside that path. They can fail alone. The topology studio is the picture, with failure toggles that drop one link at a time.",
        "Digital conversations skip the trunk and still use Architect, queues, and the same beside-the-agent systems when those products are in the package. CX 1 is voice. Digital and quality arrive at CX 2. WEM and transcription minutes arrive at CX 3. Copilot arrives at CX 4. The overview is the stack.",
    ],
    cites("overview", "architect", "routing", "byoc"),
    fig("One path for the conversation. Several optional neighbors.", [
        ("car", "Carrier", "trunk", 8, 40),
        ("arch", "Architect", "architect", 36, 40),
        ("q", "Queue", "queue", 62, 40),
        ("ag", "Agent", "agent", 86, 28),
        ("nb", "Neighbors", "wem", 86, 68),
    ], [("car", "arch"), ("arch", "q"), ("q", "ag"), ("ag", "nb")]),
    "Walk one call across the map",
    [
        ("Enter", "Trunk or Edge", "BYOC or premises", "Or Genesys Cloud Voice.", "Emergency is not implied"),
        ("Decide", "Architect", "Published flow", "Bot optional, with a failure queue.", "In-queue also published"),
        ("Offer", "ACD", "Method and evaluation", "On Queue, utilization.", "Preferred and bullseye if you configured them"),
        ("Beside", "WEM, CRM, AI", "Only if the package and the install exist", "They are not the path.", "Name the one you actually bought"),
    ],
    [
        q("The required voice path is:", "Entry, Architect, queue, agent", ["CRM, then maybe a queue", "A bot with no queue", "An exam, then a trunk"], "Neighbors are optional."),
        q("Digital calls skip:", "The SIP trunk", ["Architect", "Queues", "Agents"], "They still need a flow and a queue."),
        q("CX package order on the overview is:", "Voice, then digital and quality, then WEM, then Copilot", ["Copilot, then voice", "WEM on CX 1", "Quality only on CX 4"], "Read the stack."),
        q("A CRM outage with a healthy queue means:", "The neighbor failed", ["ACD is down", "The region moved", "The cert expired"], "Say which system."),
        q("The topology toggles are:", "Teaching failures, one link at a time", ["Live controls of your org", "Cisco scripts", "Token meters"], "They do not call an API."),
        q("An unpublished flow on this map:", "Is a break in the path", ["Still runs", "Is a neighbor", "Is fair use"], "Publish."),
    ],
    [("Path", "Entry, flow, queue, agent."), ("Neighbors", "WEM, CRM, AI."), ("Packages", "CX 1 through CX 4."), ("Toggles", "A picture, not a switch on your org.")],
    "Draw your org on the map",
    ["Your entry door.", "Your published flow.", "Your queue method.", "The neighbors you do not have."],
    "The missing neighbors are listed, not implied.",
    ("Everything box", "The diagram is one box labeled Genesys. Nobody can say what fails.", "No trunk, no flow, no queue.", "The map was skipped.", "Redraw the four hops before the workshop ends."),
))

add(lesson(
    "z-sisters", "WFM, QM, E911, analytics, CRM, and bots are sisters", "Core", 12,
    "Each sister has a track and a page. None of them is a setting on the queue tab alone.",
    [
        "Workforce management is business units, schedules, and adherence, inside WEM, on CX 3. Quality is forms, policies, and coaching, from CX 2. Emergency calling is a classification, a route, and a location, with BYOC leaving you responsible for the provider. STA is transcription and topics. Bots and Copilot are the AI track. CRM is AppFoundry plus the Salesforce and Zendesk articles.",
        "The glossary in this lab is a short restatement of those pages, each with a link. If the glossary and the page disagree, the page wins. The glossary is not a second source of truth.",
    ],
    cites("wem", "qm", "emergency", "sta", "salesforce"),
    fig("Sisters hang off the conversation. They are not the queue.", [
        ("q", "Queue", "queue", 50, 18),
        ("w", "WFM", "wem", 18, 55),
        ("m", "QM", "wem", 40, 70),
        ("e", "E911", "phone", 62, 70),
        ("c", "CRM", "crm", 84, 55),
    ], [("q", "w"), ("q", "m"), ("q", "e"), ("q", "c")]),
    "Point each sister at its page",
    [
        ("WFM", "Schedules", "WEM article", "Not QM.", "CX 3"),
        ("QM", "Forms", "Quality article", "Recording policy beside it.", "CX 2"),
        ("E911", "Route", "BYOC emergency article", "Test it.", "No invented backup PSAP"),
        ("CRM", "Embed", "Salesforce or Zendesk", "Or AppFoundry.", "No invented Dynamics list"),
    ],
    [
        q("WFM and QM differ because:", "Scheduling and evaluating are different articles and different package rows", ["They are the same screen", "Both are trunks", "Both are grants"], "CX 3 versus CX 2."),
        q("Emergency on BYOC is:", "Your provider, your route, your test", ["Included as a Genesys PSAP", "A topic", "A bot"], "The emergency article."),
        q("The glossary wins an argument with the product page when:", "It does not. Re-open the page.", ["Always", "On Fridays", "If the term is long"], "Links are there so you can check."),
        q("STA’s sister job is:", "Transcripts, topics, sentiment, search", ["SIP trunks", "OAuth", "Number plans"], "Its own track."),
        q("A bot is a sister, which means:", "It can fail while ACD is healthy, and it needs a path back", ["It replaces the queue", "It is WFM", "It is a region"], "Draw the failure."),
        q("Dynamics in the sister list is:", "Unconfirmed here. Use AppFoundry.", ["Fully specified", "The same as Zendesk", "An RFC"], "The CRM track says so."),
    ],
    [("WFM", "Schedules."), ("QM", "Forms and recordings."), ("E911", "A tested route."), ("Glossary", "A pointer, not the law.")],
    "Match six sisters",
    ["WFM.", "QM.", "Emergency.", "STA.", "CRM.", "Bots.", "The page for each."],
    "Each sister has a different URL.",
    ("QM sold as WFM", "The customer asks why there is no schedule. They own quality.", "CX 2. No business units.", "The sisters were merged in the proposal.", "Show the overview’s package rows."),
))

add(lesson(
    "z-bridge", "The Cisco bridge is a translation, with both citations showing", "Core", 11,
    "UCCE, UCCX, CUCM, and Webex are named so a Cisco engineer can find the door.",
    [
        "The migration track is the bridge: UCCE skill groups and precision queues, UCCX scripts and CSQs, CUCM trunks, and a deliberate blank where a Webex article was not confirmed. Each row should show a Cisco URL for the old system and a Genesys URL for the new one. A row with only one vendor is a guess about the other.",
        "CUCM is the closest “sister technology” outside Genesys that voice engineers already know. It remains their PBX until a separate project removes it. Genesys number plans do not edit calling search spaces.",
    ],
    cites("ucce", "uccx", "byoc", "numbers"),
    fig("Two citations on every bridge row.", [
        ("c", "Cisco", "phone", 18, 40),
        ("row", "Row", "architect", 50, 40),
        ("g", "Genesys", "queue", 82, 40),
    ], [("c", "row"), ("row", "g")]),
    "Audit a mapping table",
    [
        ("Row", "Old", "Cisco document", "Series page or the page you attached.", "Webex may be abstain"),
        ("Row", "New", "Genesys article", "Architect, queue, or BYOC.", "Not a forum"),
        ("Limit", "Numbers", "Do not copy caps across", "Five bullseye rings are Genesys.", "Cisco’s caps stay on Cisco’s page"),
        ("PBX", "CUCM", "Still theirs", "Trunk or Edge is the door.", "Emergency tested"),
    ],
    [
        q("A bridge row needs:", "A citation for each side", ["Only a Genesys link", "Only a memory", "A token price"], "Otherwise one side is fiction."),
        q("Bullseye limits belong on:", "The Genesys bullseye article", ["The UCCE page", "Both, as if they matched", "The OAuth article"], "Do not merge the numbers."),
        q("Webex in this lab is:", "Abstain until you attach a document", ["Fully specified", "The same as UCCX", "A Genesys product"], "The migration lesson says why."),
        q("CUCM calling search spaces are:", "Still CUCM configuration", ["Edited by number plans", "OAuth scopes", "Topics"], "Genesys classifies what it receives."),
        q("UCCX CSQs map as a teaching step to:", "Genesys queues", ["Login hosts", "AI tokens", "Satellite regions"], "Skills are extra."),
        q("The studio table:", "Does not change either product", ["Pushes scripts", "Is an API client", "Burns tokens"], "It is a reader."),
    ],
    [("Two links", "Cisco and Genesys."), ("Caps", "Stay on their own page."), ("Webex", "Attach or abstain."), ("CUCM", "Still the PBX.")],
    "Fix one row",
    ["Add the missing vendor link.", "Remove a limit that was copied across.", "Say whether CUCM remains.", "Say whether Webex is abstain."],
    "The row has two real URLs or an explicit abstain.",
    ("Single citation", "A mapping says precision queues support 50 rings, linking only the UCCE page.", "The 50 was the Genesys skill-removal cap.", "The vendors were blended.", "Split the sentence and cite bullseye for the Genesys number."),
))

add(lesson(
    "z-certs", "Read the catalog by name, then the announcement", "Core", 11,
    "GC-GCP and GC-GCD are catalog codes. Specialist rows are names. AI rows are two exams.",
    [
        "On the Genesys Cloud exams page, as read on 14 October 2026, Genesys Cloud Professional Certification is GC-GCP, one exam, with prep courses Implementation (135), Contact Center Administration (140), and Reporting and Analytics (143), and the cert course 17089. Genesys Cloud Developer Certification is GC-GCD, prep API course 11874, cert course 17173. Specialists are listed by name: Architect, Workforce Management, Scripting, Quality Management, Outbound, and Speech and Text Analytics. The catalog links those to cert courses 11975, 12173, 12174, 12175, 16125, and 18415. AI – GPE & GPR and Digital Bots & Knowledge are one exam each, courses 17671 and 18174.",
        "This lab does not promote older GCX- community prefixes to current codes. Engage on-premises exams are a different section of the catalog. The announcement page is where the webcam relaxation through 31 December 2026 and the free practice exams are described. Re-open both pages before you pay.",
    ],
    cites("certs", "cert-note"),
    fig("Catalog name, then announcement, then a seat.", [
        ("cat", "Catalog", "region", 18, 40),
        ("ann", "Announcement", "architect", 52, 40),
        ("seat", "Seat", "agent", 84, 40),
    ], [("cat", "ann"), ("ann", "seat")]),
    "Book from the row that matches the job",
    [
        ("Implement", "GC-GCP", "Courses 135, 140, 143", "Cert course 17089.", "One exam"),
        ("API", "GC-GCD", "Prep 11874", "Cert course 17173.", "One exam"),
        ("Specialist", "By name", "Architect through STA", "No GCX- code from this lab.", "Prep courses are on the catalog"),
        ("Rules", "Announcement", "Webcam and practice", "Through the date the page states.", "Practice exams are not vouchers"),
    ],
    [
        q("GC-GCP is:", "Genesys Cloud Professional Certification, one exam", ["A specialist code this lab invented", "The STA exam", "A Cisco cert"], "Use the catalog name."),
        q("GC-GCD prep on the catalog is:", "The API course 11874", ["Architect course 660 only", "A practice dump", "WFM only"], "The cert course is 17173."),
        q("Specialist exam codes in this lab are:", "Not stated. The catalog row is the name.", ["GCX- for each", "The same as GC-GCP", "RFC numbers"], "Older posts are not the catalog."),
        q("STA’s specialist cert is:", "Its own row, catalog course 18415", ["The same as Digital Bots", "Included in GC-GCP", "Retired here"], "Do not swap AI and STA."),
        q("The announcement’s webcam note, as read for this lab, runs through:", "31 December 2026", ["31 December 2024", "Forever", "The next Edge upgrade"], "Re-open the announcement. The date is the page’s."),
        q("Free practice exams on that announcement are:", "Not a voucher", ["The same as passing", "GCX- dumps", "Required to be paid"], "Webassessor’s practice catalog is the mechanism the page describes."),
    ],
    [("GC-GCP", "Professional. One exam."), ("GC-GCD", "Developer. One exam."), ("Specialists", "Names, not invented codes."), ("Announcement", "Webcam and practice. Re-read.")],
    "Choose a row",
    ["The job.", "The catalog name.", "The prep course numbers you will confirm.", "The announcement sentence you will re-read."],
    "No GCX- code appears in the answer.",
    ("Dump site", "A candidate memorizes a GCX- question bank.", "The catalog does not use that prefix for these rows.", "The source was not Genesys.", "Close it. Use the catalog and the official practice exam."),
    "Catalog details were read on 14 October 2026. Course numbers and the webcam date must be re-checked before you enroll or book.",
))

add(lesson(
    "z-interview", "Interview answers cite a page, not a vibe", "Core", 11,
    "The drill in this lab is a set of questions with a model answer and a link.",
    [
        "A hiring panel for this platform asks about regions, queues, routing methods, Architect publish, OAuth grants, and the difference between a bot and Copilot. The interview view gives a short model answer and the article it came from. Practice saying the limit: five bullseye rings, users/me forbidden on client credentials, implicit grant deprecated after 25 May 2026, CX packages in order.",
        "If you cannot point at a page, say you would look it up. That is a better answer than a precise fiction. The drill is not an exam dump and not a voucher.",
    ],
    cites("routing", "oauth", "overview", "certs"),
    fig("Question, model answer, article.", [
        ("q", "Question", "agent", 16, 40),
        ("a", "Answer", "architect", 50, 40),
        ("u", "URL", "region", 82, 40),
    ], [("q", "a"), ("a", "u")]),
    "Answer one question the long way",
    [
        ("Hear", "The ask", "Restate the object", "Queue, grant, or package.", "Do not answer a neighbor"),
        ("Limit", "The number", "Only if you know the page", "Otherwise say you will open it.", "Rings, timeouts, tokens"),
        ("Cite", "The URL", "From the drill or the track", "Not a dump site.", "Offer to re-read"),
        ("Stop", "Scope", "What you will not claim", "Webex article, Dynamics features, PureConnect EOL.", "Uncertainty is professional"),
    ],
    [
        q("A strong routing answer includes:", "The method, the evaluation, and the article", ["Only “it depends”", "A GCX- code", "A token price"], "Limits if you know them."),
        q("users/me on a client-credentials token is:", "The wrong call", ["The health check", "Required", "A queue"], "The guide says there is no user."),
        q("If you do not know a limit:", "Say you will open the page", ["Invent a round number", "Cite a forum", "Change the subject to Cisco"], "Looking it up is the skill."),
        q("The interview drill is:", "Practice with citations", ["An exam dump", "A voucher", "A live API"], "It stays in the browser."),
        q("Package questions are answered from:", "The overview", ["A 2023 memory if it conflicts", "AppFoundry", "RFC 5737"], "CX 1 through CX 4."),
        q("PureConnect end-of-life in an interview:", "“I would confirm the Genesys notice”", ["A date from a blog", "Never", "31 December 2026"], "That webcam date is a different page."),
    ],
    [("Object", "Name it."), ("Limit", "Or look it up."), ("Cite", "A real article."), ("Abstain", "EOL, unconfirmed CRMs, Webex.")],
    "Practice three",
    ["One routing limit.", "One OAuth limit.", "One thing you will refuse to invent.", "The URL for the first two."],
    "The refusal is specific.",
    ("Confident fiction", "The candidate says bullseye supports 12 rings because a blog did.", "The article says 5.", "The number was borrowed.", "Answer 5 and offer the bullseye overview."),
))

add(lesson(
    "z-refuse", "What this lab will not invent", "Foundation", 10,
    "Prices, unconfirmed hosts, exam codes, lifecycle dates, and CRM feature lists stay off the page.",
    [
        "The rules that built the lessons: cite a page that was actually opened, prefer Genesys articles and the RFCs for SIP, RTP, SRTP, and DTMF, use documentation addresses from RFC 5737 in synthetic logs, and mark uncertainty when a number can move. Fair-use dollar figures, DCVP IP lists, dialect lists, and country-by-country voice coverage are links, not copies.",
        "Specialist exams are names. Implicit grant’s date is the OAuth article’s date. PureConnect and Engage dates wait for a Genesys notice. Dynamics and ServiceNow wait for a listing. Webex waits for a document you attach. If a later page disagrees with a lesson, the page wins, and the lesson should be read as the way to find that page.",
    ],
    cites("fair", "dcvp", "certs", "rfc5737"),
    fig("If it is not on a page you can open, it is not in the design.", [
        ("page", "Page", "region", 22, 40),
        ("lab", "Lesson", "architect", 55, 40),
        ("no", "Not invented", "crm", 84, 40),
    ], [("page", "lab"), ("lab", "no")]),
    "Run the refusal checklist",
    [
        ("Money", "Fair use", "Link, do not copy rates", "The policy page.", "Allowances are named, prices are not"),
        ("IPs", "DCVP", "Link, do not paste the allowlist", "It changes.", "Stale ACLs are an outage"),
        ("Codes", "Catalog", "GC-GCP and GC-GCD only", "Specialists by name.", "No GCX-"),
        ("Dates", "Notices", "EOL unconfirmed", "Webcam date only from the announcement.", "Re-read"),
    ],
    [
        q("Fair-use prices in this lab are:", "Not copied. The policy page is the source.", ["A rate card", "A quiz answer you should memorize as dollars", "An RFC"], "Name the allowance family if you must."),
        q("DCVP ingress addresses should be:", "Read from the current article when you configure a trunk", ["Pasted from a lesson", "RFC 5737 addresses", "Guessed"], "5737 is for documentation examples, not for your ACL."),
        q("Synthetic logs use RFC 5737 because:", "Those ranges are reserved for documentation", ["They are Genesys", "They are your carrier", "They are the PSAP"], "192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24."),
        q("A specialist GCX- code in a lesson would be:", "A defect in this lab", ["Required", "The catalog", "A grant"], "Names only."),
        q("When a lesson and a live article disagree:", "The article wins", ["The lesson wins", "The older PDF wins", "The forum wins"], "These pages are how you find the article."),
        q("An unconfirmed CRM feature list should be:", "Removed or replaced with a listing you opened", ["Filled in from Salesforce", "Marked CX 4", "Given a price"], "The refusal is the point."),
    ],
    [("Prices", "Link only."), ("IPs", "Current article only."), ("Codes", "Catalog only."), ("Conflict", "The live page wins.")],
    "Strike three claims",
    ["A dollar figure.", "A pasted IP.", "A GCX- code or an EOL date.", "The URL you would use instead."],
    "The design is shorter and sourced.",
    ("Helpful invention", "A proposal adds a backup PSAP number, a Dynamics field map, and a PureConnect end date.", "None of the three has a page.", "The author was being helpful.", "Delete all three. Link the emergency article, AppFoundry, and the lifecycle notice once you have it."),
    "If you find a lesson that states a price, a DCVP prefix, a GCX- code, or a PureConnect end date, treat that sentence as a bug.",
))
