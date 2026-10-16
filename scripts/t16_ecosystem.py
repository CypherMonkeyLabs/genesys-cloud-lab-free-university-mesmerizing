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

add(lesson(
    "z-cpaas", "The telephony door this lab can cite is BYOC, not a word the page did not use", "Foundation", 12,
    "CPaaS is the classroom name for a communications API you bring. The opened page is About BYOC Cloud.",
    [
        "About BYOC Cloud says the solution lets you define SIP trunks between the Genesys Cloud AWS-based Edge and Media Tier and a third-party carrier over the public internet. That is the door this lab will teach when someone asks for a communications-platform bridge: your carrier, Genesys media, and the articles for trunks, number plans, ports, and emergency calling. The page does not use the word CPaaS. This lesson will not add it to the product.",
        "BYOC Premises is the other door, with a customer Edge, and it has its own track. Genesys Cloud Voice is the Genesys carrier offer and stays on the voice-region article. AppFoundry lists a Telco and Devices category among others. A listing there is not a configuration this lab performed. The Developer Center is where a client would be written, and this lab’s API explorer still does not send one.",
    ],
    cites("byoc", "edges", "appfoundry", "dev"),
    fig("The cited door is a SIP trunk to the Genesys media tier. The classroom may call that a CPaaS-style bridge.", [
        ("car", "Carrier", "trunk", 14, 40),
        ("sip", "SIP trunk", "phone", 46, 40),
        ("med", "Media tier", "region", 78, 40),
    ], [("car", "sip"), ("sip", "med")]),
    "Name the page before the category",
    [
        ("Ask", "CPaaS", "Classroom word", "Do not paste it onto the article.", "The article says SIP trunks"),
        ("Cloud", "BYOC Cloud", "Public internet", "No customer Edge on that path.", "Ports stay on the ports article"),
        ("Premises", "Edge", "A different track", "Do not merge the pictures.", "Emergency is still yours to test"),
        ("Market", "AppFoundry", "Telco and Devices is a category", "Not an install.", "Developer Center for a client"),
    ],
    [
        q("About BYOC Cloud describes:", "SIP trunks between the Genesys media tier and a third-party carrier over the public internet", ["A forecast", "An evaluation form", "A certification exam"], "That is the sentence this lesson uses."),
        q("The word CPaaS on that page is:", "Not used. This lab will not add it", ["The product name", "A routing method", "A required license field"], "Use it only as the classroom’s question, then answer with the article’s words."),
        q("BYOC Premises differs because:", "A customer Edge is in the path", ["It is the same picture as BYOC Cloud", "It is a speech program", "It is Virtual Agent"], "The Edge track is the place to study it."),
        q("AppFoundry in this lesson is:", "A marketplace category list, not a trunk you configured", ["The BYOC quick start", "A queue", "An RFC"], "Telco and Devices is one category on the home page that was opened."),
        q("A client that would place calls belongs on:", "The Developer Center, and this lab will not send the request", ["The forecast editor", "The glossary as a second source", "A Wikipedia distribution method"], "The API track explains why the explorer stays quiet."),
        q("Emergency calling on a BYOC trunk is:", "Still a separate article and a test", ["Included as a Genesys PSAP by this lesson", "A topic phrase", "A forecast checkbox"], "Do not let the bridge skip it."),
    ],
    [("Door", "SIP trunks to the Genesys media tier."), ("Word", "CPaaS is the classroom’s, not the article’s."), ("Premises", "A different Edge path."), ("Market", "AppFoundry lists categories. It does not configure them.")],
    "Answer a CPaaS question",
    ["The word the person used.", "The article you will open.", "Whether an Edge is involved.", "The emergency article you will not skip."],
    "The answer names BYOC Cloud or Premises and does not invent a CPaaS feature.",
    ("Renamed product", "A diagram labels the carrier trunk “Genesys CPaaS” and drops the emergency test.", "The opened page says SIP trunks. It does not say CPaaS.", "The classroom word was written on the box.", "Relabel the box BYOC Cloud and put the emergency article back on the diagram."),
))

add(lesson(
    "z-crm", "Salesforce and Zendesk are the embeds this lab opened", "Core", 13,
    "Salesforce Open CTI is in maintenance and has a later retirement date. Zendesk’s page does not say that.",
    [
        "About Genesys Cloud for Salesforce describes the embed inside Salesforce and says that, effective 23 March 2026, the integration is deprecated, in maintenance, and will not receive new features. The deprecation article opened beside it is a different sentence: announced 23 March 2026, planned effective date 28 February 2028, when Salesforce retires Open CTI and this integration retires with it. That announcement says there is no immediate impact, and it names two paths: CX Cloud from Genesys and Salesforce, or the Genesys Cloud user interface with no Salesforce CTI. It also says the two can run side by side, and that a migration’s length varies.",
        "About Genesys Cloud for Zendesk describes the embed inside Zendesk, with nothing to install on each computer, and lists support for call, callback, outbound dialing, email, message, and ACD voicemail. Both articles say not to run different embedded clients, including Salesforce and Zendesk, at the same time. Both mention Agent Copilot in the interaction window. Other CRMs stay on AppFoundry until you open a listing. This lab did not install either embed.",
    ],
    cites("salesforce", "sf-retire", "zendesk", "appfoundry"),
    fig("Two documented embeds. One of them has a retirement table. The other page does not.", [
        ("sf", "Salesforce", "crm", 22, 28),
        ("zd", "Zendesk", "crm", 22, 72),
        ("date", "2028-02-28", "region", 70, 28),
    ], [("sf", "date")]),
    "Read the date that matches the page",
    [
        ("About", "Salesforce", "Maintenance from the March 2026 sentence", "No new features, on that page.", "Do not paste the date onto Zendesk"),
        ("Table", "Retirement", "28 February 2028", "Announced 23 March 2026.", "No immediate impact, on the announcement"),
        ("Path", "Two choices", "CX Cloud, or Genesys Cloud itself", "They can run together.", "Length varies. Do not promise one"),
        ("Other", "Zendesk", "Its own article", "Do not run both clients.", "Anything else is AppFoundry"),
    ],
    [
        q("The Salesforce about page says the integration, from 23 March 2026, is:", "Deprecated and in maintenance, with no new features", ["Retired on that day", "Unchanged", "A speech program"], "The retirement table is a different page."),
        q("The Open CTI deprecation table’s planned effective date is:", "28 February 2028", ["29 June 2026", "23 March 2026", "31 December 2026"], "23 March 2026 is the announced-on date. 29 June 2026 is Journey Outcomes. 31 December 2026 is the webcam note."),
        q("That announcement says the current service:", "Has no immediate impact", ["Stops the day you read it", "Deletes queues", "Disables BYOC"], "Genesys Cloud core features are described as independent of Open CTI."),
        q("Paths named on the announcement are:", "CX Cloud from Genesys and Salesforce, or the Genesys Cloud user interface", ["Zendesk and a forecast", "Bullseye and direct routing", "Two Wikipedia methods"], "The announcement says they can exist side by side."),
        q("Zendesk’s about page, as opened for this lesson, lists:", "Call, callback, outbound dialing, email, message, and ACD voicemail", ["A 2028 retirement date", "Six bullseye rings", "A forecast import"], "Do not copy the Salesforce dates onto it."),
        q("Running the Salesforce client and the Zendesk client together is:", "Warned against on both articles", ["Required", "How CX Cloud is installed", "A forecast method"], "The note includes other embedded clients as well."),
    ],
    [("Maintenance", "The Salesforce about page, from 23 March 2026."), ("Retirement", "28 February 2028, on the deprecation table."), ("Paths", "CX Cloud, or Genesys Cloud without that CTI."), ("Zendesk", "A separate article. No date copied across.")],
    "Correct a migration slide",
    ["Separate the maintenance sentence from the 2028 date.", "Name the two paths.", "Remove any Zendesk date you cannot point at.", "Say this lab did not install the packages."],
    "The slide has two Salesforce sentences and no invented Zendesk date.",
    ("One date", "A plan retires Zendesk on 28 February 2028 because Salesforce’s table used that day.", "The Zendesk page opened here does not say that.", "The embeds were treated as one product.", "Delete the Zendesk date. Keep the Salesforce table on the Salesforce row."),
    "Read in 2026-10. The about page says maintenance effective 23 March 2026. The deprecation table says planned retirement 28 February 2028. The announcement says migration length varies and does not give one duration for every customer.",
))

add(lesson(
    "z-agents", "A bot, a Virtual Agent, and Copilot are three assists", "Core", 12,
    "Dialog Engine builds the bot. Virtual Agent adds Genesys AI. Copilot sits with the person.",
    [
        "About Genesys Dialog Engine Bot Flows says you build bots in Architect and use them in call, chat, and message flows. The page says the feature is PCI DSS-compliant and can be used in secure call flows. It also points at Genesys Virtual Agent: an advanced conversational bot for voice and digital bot flows that can generate intents and utterances, search knowledge-base content on digital interactions, and summarize the bot conversation with a wrap-up code. Token metering has its own article. This lesson does not copy a price.",
        "Agent Copilot, on its overview, assists a person during and after the interaction: knowledge articles, a transcript, scripts, next best action, a form, and notes that can include the reason, the resolution, and a possible wrap-up code. The overview says the benefit continues when an agent blind-transfers a call or a digital interaction. Copilot is not the bot that answered first, and Virtual Agent is not the panel on the human agent’s screen. The Salesforce and Zendesk articles both say Copilot can be placed in the embedded interaction window.",
    ],
    cites("dialog", "virtual", "copilot", "salesforce"),
    fig("The bot can answer before the queue. Copilot sits beside the person who received the interaction.", [
        ("bot", "Bot", "bot", 18, 40),
        ("q", "Queue", "queue", 48, 40),
        ("co", "Copilot", "agent", 80, 40),
    ], [("bot", "q"), ("q", "co")]),
    "Place each assist",
    [
        ("Build", "Dialog Engine", "Architect bot flow", "Call, chat, and message.", "Secure flows are allowed, on that page"),
        ("AI bot", "Virtual Agent", "Voice and digital", "Knowledge search is described for digital.", "Summary and wrap-up after the bot"),
        ("Person", "Copilot", "During and after", "Knowledge, transcript, script, form, notes.", "Blind transfer keeps the benefit"),
        ("Price", "Tokens", "Open the metering article", "Do not type a rate here.", "CX package order stays on the overview"),
    ],
    [
        q("Dialog Engine Bot Flows are used in:", "Call, chat, and message flows", ["Forecasts", "Number plans", "Edge groups"], "The article says you integrate them into those Architect flows."),
        q("Virtual Agent, on its article, can search knowledge:", "On digital interactions", ["On every trunk", "Inside a forecast", "As a SIP header"], "The during-contact section says the knowledge highlight is only digital."),
        q("Copilot’s overview includes notes for:", "The reason, the resolution, and a possible wrap-up code", ["The carrier ACL", "The OAuth secret", "A bullseye ring"], "The person still handles the interaction."),
        q("A blind transfer, on the Copilot overview:", "Keeps the Copilot benefit for the next agent", ["Ends the transcript", "Converts the call to email", "Publishes a program"], "The sentence covers a call or a digital interaction."),
        q("Virtual Agent and Copilot differ because:", "One is the bot, and the other assists the person", ["They are the same screen", "Both are queue routing methods", "Both are BYOC trunks"], "Do not draw one box for both."),
        q("A token price in this lesson is:", "Not copied. The metering article is the place to read it", ["100 per interaction", "Included in the Wikipedia ACD page", "The same as a forecast week"], "The Virtual Agent page points at that article."),
    ],
    [("Dialog Engine", "The Architect bot."), ("Virtual Agent", "Genesys AI on voice and digital bot flows."), ("Copilot", "The person’s panel."), ("Tokens", "Read the metering article. Do not invent a rate.")],
    "Draw the handoff",
    ["Where the bot is allowed to fail.", "What Virtual Agent may summarize.", "What Copilot shows the person.", "The article you will open before anyone types a token price."],
    "The failure still has a queue, and the price is a link.",
    ("One robot", "A design says Copilot will deflect the call before it queues, because it is “the AI.”", "Copilot’s overview assists the agent. Virtual Agent is the bot.", "The names were swapped.", "Put Virtual Agent in the flow, give it a failure path to the queue, and leave Copilot on the agent’s window."),
))

add(lesson(
    "z-hooks", "Future hooks are dates on announcements, not a roadmap this lab invented", "Advanced", 12,
    "Journey Outcomes, Salesforce Open CTI, and Customer Outcomes are three different sentences.",
    [
        "The Journey Outcomes announcement lists announced-on 18 May 2026 and planned effective date 29 June 2026. After that date the page says outcomes cannot be created, existing outcomes are not processed, action maps are not triggered by them, and reporting for them is not available. Customer Outcomes is described there as under development, and Outcome Scoring is not part of it. Architect flows that call getJourneyOutcome skip that branch. This lab did not sign in to see whether a given org still has the feature.",
        "The Salesforce Open CTI announcement is the other dated hook: announced 23 March 2026, planned effective 28 February 2028, with no immediate impact stated on that page. The predictive-routing custom-KPI announcement is a third page, and the predictive track is where this lab keeps it. A future hook in a design should name the announcement, the date printed on it, and the sentence “re-open before you rely.” A hook without that page is a guess.",
    ],
    cites("pe-deprecate", "sf-retire", "pe-kpi", "virtual"),
    fig("Each hook is an announcement with a date. Customer Outcomes is still described as under development.", [
        ("jo", "2026-06-29", "bot", 20, 30),
        ("sf", "2028-02-28", "crm", 52, 30),
        ("co", "Customer Outcomes", "architect", 80, 68),
    ], [("jo", "co")]),
    "Attach a page to every date",
    [
        ("Outcomes", "29 June 2026", "Journey Outcomes", "Announced 18 May 2026.", "getJourneyOutcome skips"),
        ("Replace", "Customer Outcomes", "Under development on that page", "Outcome Scoring is not included.", "No shipment date copied from elsewhere"),
        ("CTI", "28 February 2028", "Salesforce Open CTI", "Maintenance is the other Salesforce sentence.", "No immediate impact, on the announcement"),
        ("KPI", "Predictive routing", "Its own announcement", "Not Journey Outcomes.", "The predictive track holds it"),
    ],
    [
        q("The Journey Outcomes planned effective date on the announcement is:", "29 June 2026", ["28 February 2028", "23 March 2026", "31 December 2026"], "28 February 2028 is Salesforce Open CTI. 31 December 2026 is the webcam note."),
        q("After that Journey Outcomes date, the announcement says:", "Existing outcomes are not processed and do not trigger action maps", ["They keep running until Customer Outcomes ships", "Queues stop", "BYOC trunks close"], "Flows that call getJourneyOutcome skip that branch."),
        q("Customer Outcomes, on that same announcement, is:", "Under development, and Outcome Scoring is not part of it", ["Generally available on 29 June 2026", "A queue routing method", "The Zendesk embed"], "The page says you can follow it on the Aha! portal. This lesson does not invent a release date."),
        q("The Salesforce Open CTI planned effective date is:", "28 February 2028", ["29 June 2026", "The same day as Journey Outcomes", "Unstated"], "The about page’s maintenance sentence is 23 March 2026. Keep them apart."),
        q("A future hook this lab will accept in a design is:", "An announcement, the date printed on it, and a note to re-open it", ["A feature someone expects next quarter", "A price", "A GCX- code"], "No page, no hook."),
        q("The predictive-routing custom-KPI note belongs:", "On its own announcement and in the predictive track", ["Inside Journey Outcomes", "On the forecast editor", "On the bullseye ring"], "The names are easy to swap. The pages are not."),
    ],
    [("Journey Outcomes", "Planned 29 June 2026."), ("Customer Outcomes", "Described as under development. No date added here."), ("Salesforce CTI", "Planned 28 February 2028."), ("Hook", "A page, a printed date, and a re-open note.")],
    "Strike the undated items",
    ["Journey Outcomes on 29 June 2026.", "A Customer Outcomes release week you made up.", "Salesforce retirement on 28 February 2028.", "A Zendesk retirement you cannot cite."],
    "The made-up week and the Zendesk date are gone.",
    ("Helpful calendar", "A roadmap adds Customer Outcomes in July 2026 because Journey Outcomes ends in June.", "The announcement says Customer Outcomes is under development and does not give that month.", "The empty box was filled.", "Leave the month off. Link the announcement and write “re-open.”"),
    "Checked in 2026-10. This lab did not sign in to an organization, so it cannot say whether Journey Outcomes is still present in any given org.",
))
